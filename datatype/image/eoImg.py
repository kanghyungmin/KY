
from datatype.base import Base
from config.constant.const import EOIMG_SZ, IMG_ROW_IDX, IMG_COL_IDX

class EoImg(Base):
    """[summary]

    Arguments:
        Base {Object} -- Abstract Class
    """
    
    def __init__(self):
        """AI is creating summary for __init__
        """        
        self._data : bytearray = bytearray(EOIMG_SZ[IMG_ROW_IDX]*EOIMG_SZ[IMG_COL_IDX])
    
    def m_getData(self) -> bytearray:

        return self._data 


    
        