
import zmq, string

from typing import Callable, Iterable, List



class socketInfo():

    def __init__(self, p_iType:int, p_sIp: str, p_sPort: str,p_sProtocol: str,
                 p_bBind:bool,p_sActionName : str, p_sDataName : str="None",
                 p_dTopic: List[str]=["None"]):
            self._iType: int = p_iType
            self._sIp : str = p_sIp
            self._sPort : str = p_sPort
            self._sProtocol : str = p_sProtocol
            self._bBind : bool = p_bBind
            self._sActionName  : str = p_sActionName
            self._dTopic : List[str] = p_dTopic
            self._sDataNAME : str = p_sDataName

    def m_retType(self) -> int:
        return self._iType

    def m_retIsBind(self) -> bool:
        return self._bBind

    def m_getAddr(self) -> str:
        return str(self._sProtocol) + str(self._sIp) + ":" + str(self._sPort)

    def m_getActionName(self) -> str:
        return self._sActionName

    def m_getTopicList(self) -> List[str]:
        return self._dTopic
        
    def m_getDataName(self) -> str:
        return self._sDataNAME    

    def m_getPort(self) -> int:
        return int(self._sPort)

    def m_setPort(self, p_iPort : int) -> None:
        self._sPort = str(p_iPort)