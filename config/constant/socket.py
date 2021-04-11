
from pickle import TRUE
from config.constant.const import LOCALHOST, ALL, SERVER
from typing import List
from enum import Enum
import zmq

TCP : str ="tcp://"

PRODUCER_EO3_PORT : str = str(49152)
CONSUMER_EO3_PORT : str = str(49210)
WOKER_EO3_PORT_PULL : str = str(49153)
WOKER_EO3_PORT_PUB : str = str(49200) 

STREAMER_FRONTEND_PORT : str = str(49152)
STREAMER_BACKEND_PORT : str = str(49153)

FORWARDER_FRONTEND_PORT : str = WOKER_EO3_PORT_PUB
FORWARDER_BACKEND_PORT : str = CONSUMER_EO3_PORT

class PRODUCER_EO3(Enum):
    TYPE : int = zmq.PUSH
    IP : str =  LOCALHOST
    PORT : str = PRODUCER_EO3_PORT
    PROTOCOL : str = TCP
    ISBIND : bool = False
    FUNCNAME : str = "send_zipped_pickle"
    DATANAME : str = "EoImgs"

class CONSUMER_STICH(Enum):
    TYPE : int = zmq.SUB
    IP : str =  SERVER
    PORT : str = CONSUMER_EO3_PORT
    PROTOCOL : str = TCP
    ISBIND : bool = False
    FUNCNAME : str = "recv_zipped_pickle"
    # FUNCNAME : str = "recv_zipped_pickle_with_topic"
    DATANAME : str = "EoImgs"
    TOPIC: List[str] = [""]

class WORKER_EO3(Enum):
    TYPES : List[int] = [zmq.PULL, zmq.PUB]
    IPS : List[str] = [LOCALHOST, SERVER]
    PORT : List[str] = [ WOKER_EO3_PORT_PULL , WOKER_EO3_PORT_PUB ]
    PROTOCOLS : List[str] = [TCP, TCP]
    ISBINDS : List[bool] = [False, False]
    # FUNCNAME : List[str] = ["recv_zipped_pickle", "send_zipped_pickle_with_topic EoImgs"]
    FUNCNAME : List[str] = ["recv_zipped_pickle", "send_zipped_pickle"]
    DATANAME : List[str] = ["EoImgs", "EoImgs"]

class IMAGE_STREAMER(Enum):
    TYPES : List[int] = [zmq.PULL, zmq.PUSH]
    IPS : List[str] = [ALL, ALL]
    PORT : List[str] = [ STREAMER_FRONTEND_PORT , STREAMER_BACKEND_PORT ]
    PROTOCOLS : List[str] = [TCP, TCP]
    ISBINDS : List[bool] = [True, True]
    FUNCNAME : List[str] = ["None", "None"]
    DATANAME : List[str] = ["None", "None"]

class DATA_FORWARDER(Enum):
    TYPES : List[int] = [zmq.SUB, zmq.PUB]
    IPS : List[str] = [ALL, ALL]
    PORT : List[str] = [ FORWARDER_FRONTEND_PORT , FORWARDER_BACKEND_PORT]
    PROTOCOLS : List[str] = [TCP, TCP]
    ISBINDS : List[bool] = [True, True]
    FUNCNAME : List[str] = ["None", "None"]
    DATANAME : List[str] = ["None", "None"]
    TOPIC: List[str] = ["","None"]



