import sys,cv2

from datetime import datetime

from numpy.core.fromnumeric import shape

from datatype.base import Base
from config.constant.const import EOIMG_SZ, IMG_ROW_IDX, IMG_COL_IDX, NUMBER

class EoImgs(Base):

    def __init__(self):
        self._time : datetime = datetime.min
        self._data : bytearray = bytearray(EOIMG_SZ[IMG_ROW_IDX]*EOIMG_SZ[IMG_COL_IDX]*NUMBER.ONE.value)
    
    def m_getData(self) -> dict:

        return (self._time, self._data)

    def m_setData(self,p_dNewVal:bytearray) -> None: 
        self._data = p_dNewVal

    def m_genData(self, p_sPath : str = r'.\test\EO_1.mp4', 
                  p_bTest : bool = False ) -> None:

        if p_bTest==True:
            capture = cv2.VideoCapture(p_sPath)    
        else:
            capture = cv2.VideoCapture(p_sPath)    

        ret, frame = capture.read() 
        self.m_setData(frame.tobytes())

        # # ndarray 2 bytearray(Encode)
        # print(f'serialize 전: getsizeof: {sys.getsizeof(frame)} and dtype = {frame.dtype} ')
        # print(f'size: {frame.size} and ndim: {frame.ndim} and shape: {frame.shape}')
        # print(f'type: {type(frame)}')
        # print(f'----------------------------------------------------------------------------')
        # # ecoded information
        # print(f'serialize 후, self._data: {sys.getsizeof(self._data)} and type = {type(frame)} ')
        # print(f'----------------------------------------------------------------------------')

        # # bytearray 2 ndarray(Decode)
        # import numpy as np
        # decoded_info = np.frombuffer(self._data, dtype=np.uint8)
        # print(f'decode 후, decoded_info: {sys.getsizeof(decoded_info)} and dtype = {decoded_info.dtype}')
        # print(f'size: {decoded_info.size} and ndim: {decoded_info.ndim} and shape: {decoded_info.shape}')
        # print(f'type: {type(frame)}')
        # print(f'----------------------------------------------------------------------------')
        # decoded_info2 = np.reshape(decoded_info,frame.shape)
        # print(f'decode 후, decoded_info: {sys.getsizeof(decoded_info2)} and dtype = {decoded_info2.dtype}')
        # print(f'size: {decoded_info2.size} and ndim: {decoded_info2.ndim} and shape: {decoded_info2.shape}')
        # print(f'type: type(frame)')
        # print(f'type: {type(frame)}')
        # print(f'----------------------------------------------------------------------------')

    def __str__(self):
        print(f'{self._time} and {self._data}')

    def __sizeof__(self):
        return super().__sizeof__() + self._time.__sizeof__() + self._data.__sizeof__()

if __name__ == "__main__":
    import cv2,os

    capture = cv2.VideoCapture(r'.\test\EO_1.mp4')

    while cv2.waitKey(1):
        if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            print(f"{cv2.CAP_PROP_POS_FRAMES} and {cv2.CAP_PROP_FRAME_COUNT}")
            capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = capture.read()
        print(sys.getsizeof(frame))
        # print(type(frame))
        # print(dir(frame))
        # print(f"{cv2.CAP_PROP_POS_FRAMES} and {cv2.CAP_PROP_FRAME_COUNT}")
        # print(f"{cv2.CAP_PROP_FRAME_WIDTH} and {cv2.CAP_PROP_FRAME_HEIGHT}")
        # print(frame.shape)
        cv2.imshow("VideoFrame", frame)

    capture.release()
    cv2.destroyAllWindows()




        
