
from enum import Enum

class ClientTypeEnum(Enum):
    USER_EMAIL = 100 #邮箱
    USER_MOBILE = 101 #手机号
    USER_MINA = 200 #微信小程序
    USER_WX = 201 #微信公众号
    pass