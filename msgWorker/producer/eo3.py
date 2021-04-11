import string, zmq, time

from typing import List,Iterable
# from multiprocessing import Process
from multiprocessing import Process

from zmq.sugar.constants import NULL
from msgWorker.serializeSocket import SerializingContext, SerializingSocket
from msgWorker.socketinfo import socketInfo
from config.constant.const import NUMBER
from config.constant.socket import PRODUCER_EO3
from datatype.dataFactory import dataFactory

class  Eo3(Process):

    def __init__(self, p_iterOSocket : Iterable[socketInfo]): 

        
        Process.__init__(self)

        self._iterOScoket = p_iterOSocket

        self._oContext : object = NULL
        self._iterOData : Iterable[object] = []
        self._iterOsockActionName = []
    
    def run(self):
        self._oContext  = SerializingContext()
        self._iterOData = [ dataFactory.m_genData(info.m_getDataName())
                            for info in self._iterOScoket]

        self._iterOsockActionName = [(self._oContext.m_doPreSetting(info), 
                                     info.m_getActionName()) for info in self._iterOScoket]

                                             
        while True:
            for socketActionName, data in zip(self._iterOsockActionName, self._iterOData):
                #data maker
                import time 
                a = time.time()
                data.m_genData(p_bTest=True)
                print(f'gen Data: {time.time()-a}')                

                
                data.m_getData()
                
                
                import sys
                print(f'in producer {type(data)}, {sys.getsizeof(data)}, {data._time}, {time.time()}')
                
                socketActionName[0].m_actionFunc(obj = data,
                                                 p_sActionName= socketActionName[1])
