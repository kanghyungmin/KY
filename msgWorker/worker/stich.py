from typing import Callable, Iterable, List
from multiprocessing import Process
from typing import Iterable

from zmq.sugar.constants import NULL

from msgWorker.socketinfo import socketInfo
from msgWorker.serializeSocket import SerializingContext, SerializingSocket
from datatype.dataFactory import dataFactory
from config.constant.const import NUMBER

import zmq

class stichWorker(Process):

    def __init__(self, p_iterOSocket: Iterable[socketInfo]): 

        Process.__init__(self)

        self._iterOSocket = p_iterOSocket

        self._oContext : object = NULL
        self._oData : object = NULL
        self._iterOsockActionName = []

    def run(self):
        self._oContext = SerializingContext()
        self._oData = dataFactory.m_genData(self._iterOSocket[0].m_getDataName())

        self._iterOsockActionName = [(self._oContext.m_doPreSetting(info),
                                        info.m_getActionName()) 
                                        for info in self._iterOSocket]

        while True:
            for socketActionName in self._iterOsockActionName:
                self._oData  = socketActionName[0].m_actionFunc(obj = self._oData, p_sActionName= socketActionName[1])
                print(f'in worker {socketActionName[1]}')
                import time 
                time.sleep(4)
                print(f'4초마다 {time.time()}')
                