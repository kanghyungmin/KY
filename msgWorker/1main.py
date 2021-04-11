from config.constant.const import NUMBER, WORKER_NUM
from config.constant.socket import DATA_FORWARDER, PRODUCER_EO3, CONSUMER_STICH, WORKER_EO3, IMAGE_STREAMER,

from msgWorker.socketinfo import socketInfo
from msgWorker.producer.eo3 import Eo3 as producerEO3
from msgWorker.worker.stich import stichWorker as stichingWorker
from msgWorker.consumer.stichImg import StichImg as consumerStichImg
from msgWorker.balancer.balancer import Streamer as imageStreamer
from msgWorker.balancer.forwarder import Forwarder as DataForwarder

import multiprocessing
import copy


if __name__ == "__main__":

    #for windows    
    multiprocessing.freeze_support()
    
    #define socket
    eoPushSocket = socketInfo(PRODUCER_EO3.TYPE.value,PRODUCER_EO3.IP.value,PRODUCER_EO3.PORT.value,
                            PRODUCER_EO3.PROTOCOL.value, PRODUCER_EO3.ISBIND.value, 
                            PRODUCER_EO3.FUNCNAME.value, PRODUCER_EO3.DATANAME.value) # PRODUCER_EO3
        
    frontSocket = socketInfo(IMAGE_STREAMER.TYPES.value[NUMBER.ZERO.value], IMAGE_STREAMER.IPS.value[NUMBER.ZERO.value],
                             IMAGE_STREAMER.PORT.value[NUMBER.ZERO.value], IMAGE_STREAMER.PROTOCOLS.value[NUMBER.ZERO.value],
                             IMAGE_STREAMER.ISBINDS.value[NUMBER.ZERO.value], IMAGE_STREAMER.FUNCNAME.value[NUMBER.ZERO.value],
                             IMAGE_STREAMER.DATANAME.value[NUMBER.ZERO.value]
                              )

    BackSocket = socketInfo(IMAGE_STREAMER.TYPES.value[NUMBER.ONE.value], IMAGE_STREAMER.IPS.value[NUMBER.ONE.value],
                             IMAGE_STREAMER.PORT.value[NUMBER.ONE.value], IMAGE_STREAMER.PROTOCOLS.value[NUMBER.ONE.value],
                             IMAGE_STREAMER.ISBINDS.value[NUMBER.ONE.value], IMAGE_STREAMER.FUNCNAME.value[NUMBER.ONE.value],
                             IMAGE_STREAMER.DATANAME.value[NUMBER.ONE.value]
                              )
                              
    workerPullSocket = socketInfo(WORKER_EO3.TYPES.value[NUMBER.ZERO.value], WORKER_EO3.IPS.value[NUMBER.ZERO.value],
                             WORKER_EO3.PORT.value[NUMBER.ZERO.value], WORKER_EO3.PROTOCOLS.value[NUMBER.ZERO.value],
                             WORKER_EO3.ISBINDS.value[NUMBER.ZERO.value], WORKER_EO3.FUNCNAME.value[NUMBER.ZERO.value],
                             WORKER_EO3.DATANAME.value[NUMBER.ZERO.value]
                             )

    workerPubSocket = socketInfo(WORKER_EO3.TYPES.value[NUMBER.ONE.value], WORKER_EO3.IPS.value[NUMBER.ONE.value],
                                WORKER_EO3.PORT.value[NUMBER.ONE.value], WORKER_EO3.PROTOCOLS.value[NUMBER.ONE.value],
                                WORKER_EO3.ISBINDS.value[NUMBER.ONE.value], WORKER_EO3.FUNCNAME.value[NUMBER.ONE.value],
                                WORKER_EO3.DATANAME.value[NUMBER.ONE.value]
                                )

    consumerSubSocket = socketInfo(CONSUMER_STICH.TYPE.value, CONSUMER_STICH.IP.value,
                             CONSUMER_STICH.PORT.value, CONSUMER_STICH.PROTOCOL.value,
                             CONSUMER_STICH.ISBIND.value, CONSUMER_STICH.FUNCNAME.value,
                             CONSUMER_STICH.DATANAME.value, CONSUMER_STICH.TOPIC.value
                             )

    workerList = []
    

    proc = producerEO3([eoPushSocket])
    streamer = imageStreamer([frontSocket, BackSocket])

    for idx in range(WORKER_NUM):
        tempPubSocket = copy.deepcopy(workerPubSocket)
        
        
        tempPubSocket.m_setPort(tempPubSocket.m_getPort())
        

        workerList.append(stichingWorker([workerPullSocket, tempPubSocket]))
    
    ######################### MAIN SERVER

    forwarderFront = socketInfo(DATA_FORWARDER.TYPES.value[NUMBER.ZERO.value], DATA_FORWARDER.IPS.value[NUMBER.ZERO.value],
                             DATA_FORWARDER.PORT.value[NUMBER.ZERO.value], DATA_FORWARDER.PROTOCOLS.value[NUMBER.ZERO.value],
                             DATA_FORWARDER.ISBINDS.value[NUMBER.ZERO.value], DATA_FORWARDER.FUNCNAME.value[NUMBER.ZERO.value],
                             DATA_FORWARDER.DATANAME.value[NUMBER.ZERO.value])
    
    forwarderBackend = socketInfo(DATA_FORWARDER.TYPES.value[NUMBER.ONE.value], DATA_FORWARDER.IPS.value[NUMBER.ONE.value],
                             DATA_FORWARDER.PORT.value[NUMBER.ONE.value], DATA_FORWARDER.PROTOCOLS.value[NUMBER.ONE.value],
                             DATA_FORWARDER.ISBINDS.value[NUMBER.ONE.value], DATA_FORWARDER.FUNCNAME.value[NUMBER.ONE.value],
                             DATA_FORWARDER.DATANAME.value[NUMBER.ONE.value])

    forwarder = DataForwarder([forwarderFront, forwarderBackend])
        

    streamer.start()
    proc.start()

    for worker in workerList:
        worker.start()
        
    for worker in workerList:
        worker.join()
        

    proc.join()
    streamer.join()

    
    

    consumerList = []

    for idx in range(WORKER_NUM):
        tempConsumerSocket = copy.deepcopy(consumerSubSocket)
        tempConsumerSocket.m_setPort(tempConsumerSocket.m_getPort() + idx)
        consumerList.append(consumerStichImg([tempConsumerSocket]))
    
    for consumer in workerList:
        consumer.start()
    
    for consumer in consumerList:
        consumer.join()

    
