from enum import Enum

#NUMBER
class NUMBER(Enum):
    ZERO = 0
    ONE = 1 
    TWO = 2
    THREE = 3

#image Size
IMG_ROW_IDX = 0
IMG_COL_IDX = 1
EOIMG_SZ : tuple = (1280,720)
IRIMG_SZ : tuple = (1280,720)
STICHIMG_SZ : tuple = (2600, 720)

LOCALHOST : str = "127.0.0.1"
ALL : str = "*"
SERVER : str = "127.0.0.1"

WORKER_NUM  = 1