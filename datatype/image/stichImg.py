import string

from datatype.base import Base
from config.constant.const import STICHIMG_SZ, IMG_ROW_IDX, IMG_COL_IDX

    

class StichImg(Base):
    """[summary]

    Arguments:
        Base {[type]} -- [description]
    """    
    def __init__(self):
        self._data : bytearray = bytearray(STICHIMG_SZ[IMG_ROW_IDX]*STICHIMG_SZ[IMG_COL_IDX])
    
    def m_getData(self) -> bytearray:
        """[summary]

        Returns:
            bytearray -- [description]
        """        
        return self._data 
        
    def m_setData(self,p_dNewVal:bytearray) -> None: 
        """[summary]

        Arguments:
            p_dNewVal {bytearray} -- [description]
        """        
        self._data = p_dNewVal

