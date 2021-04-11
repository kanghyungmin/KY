import zmq
import zlib
import pickle
import string
import sys


from zmq.backend import Socket
from zmq.sugar.constants import NOBLOCK, NULL, PULL, PUSH, SUBSCRIBE
from typing import List, Callable, Iterable
from msgWorker.socketinfo import socketInfo



class SerializingSocket(zmq.Socket):
    """
    A class with some extra serialization methods
    send_zipped_pickle is just like send_pyobj, but uses
    zlib to compress the stream before sending.
    send_array sends numpy arrays with metadata necessary
    for reconstructing the array on the other side (dtype,shape).
    """
    def __init__(self,*a, **kw):
        super().__init__(*a,**kw)
        
        # self.resutl : int = 0
        # self._ofunc : Callable = NULL
        
    # def __getattr__(self, key):
    #     if key in self.__dict__:
    #         return self.__dict__[key]
    #     # return super().__getattr__(key)

    # def __setattr__(self, key, value):
    #     print("Called __setattr__(%s, %r)" % (key, value))
    #     try:
    #          super().__setattr__(key, value)
    #     except Exception as e:
    #         print(e)

    def send_zipped_pickle_with_topic(self, obj, topic : str, flags=NOBLOCK, protocol=5):
        """pack and compress an object with pickle and zlib."""
        pobj = pickle.dumps(obj, protocol)
        zobj = zlib.compress(pobj)
        print(topic.encode())
        return self.send_multipart([topic.encode(),zobj], flags=flags)

    def send_zipped_pickle(self, obj, flags=NOBLOCK, protocol=5):
        """pack and compress an object with pickle and zlib."""
        pobj = pickle.dumps(obj, protocol)
        zobj = zlib.compress(pobj)

        return self.send_pyobj(zobj, flags=flags)

    def recv_zipped_pickle(self, flags=0):
        """reconstruct a Python object sent with zipped_pickle"""
        try: 
            zobj = self.recv_pyobj(flags)
        except Exception as e:
            print(e)

        pobj = zlib.decompress(zobj)
        # print('unzipped pickle is %i bytes' % len(zobj))
        # print(f'unzipped pickle is {sys.getsizeof(pobj)} bytes {type(pobj)}')
        return pickle.loads(pobj)

    def recv_zipped_pickle_with_topic(self, flags=0):
        """reconstruct a Python object sent with zipped_pickle"""
        try: 
            [topic, zobj] = self.recv_multipart(flags)
        except Exception as e:
            print(e)

        pobj = zlib.decompress(zobj)
        # print('unzipped pickle is %i bytes' % len(zobj))
        # print(f'unzipped pickle is {sys.getsizeof(pobj)} bytes {type(pobj)}')
        return pickle.loads(pobj)

    def m_bindOrConnect(self, p_sAddr: str, p_bBind: bool) -> None:
        if p_bBind: 
            self.bind(p_sAddr) 
        else: 
            self.connect(p_sAddr)

    def m_defincFunc(self, p_sActionName: string):
        self._ofunc = getattr(self,p_sActionName)

    def m_actionFunc(self, obj : object = "None", p_sActionName: string = "None", topic : List[str] = None) -> object:

        if  'send_zipped_pickle_with_topic' in p_sActionName:
            retParsing = p_sActionName.split(' ')
            return getattr(self,retParsing[0])(obj,retParsing[1])
        elif 'recv' in p_sActionName:
            return  getattr(self,p_sActionName)()
        else: 
            return getattr(self,p_sActionName)(obj)

    # def recvGenericFunc(List[str])

    # def send_array(self, A, flags=0, copy=True, track=False):
    #     """send a numpy array with metadata"""
    #     md = dict(
    #         dtype=str(A.dtype),
    #         shape=A.shape,
    #     )
    #     self.send_json(md, flags | zmq.SNDMORE)
    #     return self.send(A, flags, copy=copy, track=track)

    # def recv_array(self, flags=0, copy=True, track=False):
    #     """recv a numpy array"""
    #     md = self.recv_json(flags=flags)
    #     msg = self.recv(flags=flags, copy=copy, track=track)
    #     A = numpy.frombuffer(msg, dtype=md['dtype'])
    #     return A.reshape(md['shape'])


class SerializingContext(zmq.Context):
    _socket_class = SerializingSocket

    def m_doPreSetting(self, p_OSocketInfo : socketInfo) -> SerializingSocket:
        # print(p_OSocketInfo.m_getTopicList())
        retSocket  = self.socket(p_OSocketInfo.m_retType())

        retSocket.m_bindOrConnect(p_OSocketInfo.m_getAddr(),
                                  p_OSocketInfo.m_retIsBind())

        # Sub Socket
        for topic in p_OSocketInfo.m_getTopicList():
            if topic == 'None' or topic == ['None']:
                break
            retSocket.setsockopt_string(SUBSCRIBE, "")
            # print(f'topic:{topic}')

        return retSocket

            
