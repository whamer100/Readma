import io
import struct
import os
from enum import Enum
from typing import Any, Union, Literal, Tuple

bytesType = bytes
floatType = float
intType = int


class ReadmaTypes(Enum):
    """Various Readma types to Readma files with"""
    byte = "b"
    short = "h"
    int = "i"
    long = "q"


sizeLiteral = Literal["byte", "short", "int", "long"]
sizeType = Union[int, sizeLiteral, ReadmaTypes]


def get_type(size: str) -> str:
    return ReadmaTypes[size].value  # python enums kinda suck


class Readma:
    """Readma? What's Readma? READMA FILE"""
    __type_shorthand = {
        1: "byte",
        2: "short",
        4: "int",
        8: "long"
    }

    __ts_rev = {
        "byte": 1,
        "short": 2,
        "int": 4,
        "long": 8
    }

    __endianness = {
        "little": False,
        "big": True
    }

    def __init__(self, buffer_or_path: Union[bytes, str]):
        buffer = Any
        if type(buffer_or_path) == bytes:
            buffer = buffer_or_path
        else:
            if os.path.isfile(buffer_or_path):
                with open(buffer_or_path, "rb") as b:
                    buffer = b.read()
            else:
                raise FileNotFoundError

        self.buffer = io.BytesIO(buffer)
        self.endianness = self.__endianness["little"]

    def __make_fmt(self, size: sizeType, signed: bool) -> Tuple[str, int]:
        _str = ">" if self.endianness else "<"
        _size = 0
        if type(size) == int:
            if size in self.__type_shorthand:
                _size = size
                _str += get_type(self.__type_shorthand[size])
            else:
                raise TypeError
        elif type(size) == str:
            if size in ReadmaTypes.__members__:
                _size = self.__ts_rev[size]
                _str += get_type(size)
            else:
                raise TypeError
        elif type(size) == ReadmaTypes:
            _size = self.__ts_rev[size.name]
            _str += size.value
        else:
            raise TypeError
        if not signed:
            _str = _str.upper()
        return _str, _size

    def set_endianness(self, endianness: Literal["little", "big"]) -> None:
        """ Sets endianness

        :param endianness: endianness to set [little | big]
        :return: None
        """
        self.endianness = self.__endianness[endianness]

    def bytes(self, num: int) -> bytesType:
        """ Readma bytes

        :param num: number of bytes to read
        :return: bytes
        """
        return self.buffer.read(num)

    def read(self, size: sizeType) -> intType:
        """ Readma integer

        :param size: size of int to read
        :return: int
        """
        rStr, rSize = self.__make_fmt(size, True)
        return struct.unpack(rStr, self.buffer.read(rSize))[0]

    def uread(self, size: sizeType) -> intType:
        """ Readma unsigned integer

        :param size: size of uint to read
        :return: int
        """
        rStr, rSize = self.__make_fmt(size, False)
        return struct.unpack(rStr, self.buffer.read(rSize))[0]

    def float(self) -> floatType:
        """ Readma float32

        :return: float
        """
        return struct.unpack("f", self.buffer.read(4))[0]

    float32 = float

    def float64(self) -> floatType:
        """ Readma float64 (also known as a double)

        :return: float
        """
        return struct.unpack("d", self.buffer.read(8))[0]

    def readall(self) -> bytesType:
        """ Readma all the bytes

        :return: bytes
        """
        # _pos = self.buffer.tell()
        _bytes = self.buffer.read()
        # self.buffer.seek(_pos)
        return _bytes

    def seek(self, loc) -> None:
        """ Change the current seek location

        :param loc: int to seek to
        :return:
        """
        self.buffer.seek(loc)
