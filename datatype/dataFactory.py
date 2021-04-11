import string

from datatype.image.eoImg import EoImg
from datatype.image.irImg import IrImg
from datatype.image.stichImg import StichImg
from datatype.image.eoImgs import EoImgs
from datatype.base import Base



class dataFactory():

    @staticmethod
    def m_genData(p_name: string) -> object:
        """[summary]

        Arguments:
            p_name {string} -- [description]

        Returns:
            object -- [description]
        """        
        for cls in Base.__subclasses__():
            if cls.__name__ == p_name: return cls()



