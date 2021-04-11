from typing import Iterable, List
from multiprocessing import Process

from zmq.sugar.constants import NULL
from msgWorker.serializeSocket import SerializingContext, SerializingSocket
from msgWorker.socketinfo import socketInfo
from datatype.dataFactory import dataFactory
from datatype.image.eoImgs import EoImgs

import string, zmq, time
import numpy as np


class StichImg(Process):

    def __init__(self, p_iterOSocket : Iterable[socketInfo]):

        Process.__init__(self)

        self._iterOSocket = p_iterOSocket

        self._oContext : object = NULL
        self._oData : object = NULL 
        self._iterOsockActionName = [] 

    def run(self):
        
        self._oContext = SerializingContext()
        self._oData = dataFactory.m_genData(self._iterOSocket[0].m_getDataName())

        self._iterOsockActionName = [(self._oContext.m_doPreSetting(info),
                                      info.m_getActionName()) for info in self._iterOSocket]

        while True:
            for socketActionName in self._iterOsockActionName:
                print(f'in consumer')
                self._oData = socketActionName[0].m_actionFunc(obj = self._oData, 
                                                               p_sActionName= socketActionName[1])
                
                import sys
                print(f'in consumer {type(self._oData)} {sys.getsizeof(self._oData)}, {self._oData._time}')
                time.sleep(1)
                print(f'3초마다 {time.time()}')
                
                # decoded_info = np.frombuffer(self._oData, dtype=np.uint8)
                # decoded_info2 = np.reshape(decoded_info, [1280, 720, 3])