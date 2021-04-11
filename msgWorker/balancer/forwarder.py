
from multiprocessing import Process

from zmq.sugar.constants import NULL
from msgWorker.serializeSocket import SerializingContext, SerializingSocket
from msgWorker.socketinfo import socketInfo

from config.constant.const import NUMBER
from typing import List, Iterable

import string,zmq

class Forwarder(Process):
    def __init__(self,  p_iterOSocket : Iterable[socketInfo]):

        Process.__init__(self)

        self._iterOSocketInfo = p_iterOSocket

        self._oContext : SerializingContext = NULL
        self._iterOData : Iterable[object] = []
        self._iterOSockActionName = []

    def run(self):
        try:
            self._oContext = SerializingContext()

            # Frontend , Backend
            socketList : Iterable[SerializingSocket] = [self._oContext.m_doPreSetting(info)
                                                        for info in self._iterOSocketInfo]

            zmq.device(zmq.FORWARDER, socketList[NUMBER.ZERO.value], socketList[NUMBER.ONE.value])
        except Exception as e:
            print(e)



        
        


