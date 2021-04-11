from abc import ABCMeta, abstractclassmethod, abstractmethod
import string 

class Base(metaclass = ABCMeta):

    def __init__(self):
        self._data : bytearray = bytearray()
    
    @abstractmethod
    def m_getData(self) -> None:

        pass

    @abstractmethod
    def m_setData(self,p_dNewVal:bytearray) -> None: 
        self._data = p_dNewVal
    
