import string

from datatype.base import Base
from config.constant.const import IRIMG_SZ, IMG_ROW_IDX, IMG_COL_IDX

class IrImg(Base):

    def __init__(self):
        self._data : bytearray = bytearray(IRIMG_SZ[IMG_ROW_IDX]*IRIMG_SZ[IMG_COL_IDX])
    
    def m_getData(self) -> bytearray:
        return self._data 
        
    def m_setData(self,p_dNewVal:bytearray) -> None: 
        """[summary]

        Arguments:
            p_dNewVal {bytearray} -- [description]
        """        
        self._data = p_dNewVal



