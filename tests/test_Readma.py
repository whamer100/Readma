import pytest
from readma import Readma
from math import isclose
from struct import pack, unpack


def test_Readma_buffer_string():
    assert Readma(b"test").readall() == b"test"


@pytest.mark.xfail
def test_Readma_buffer_string_invalidType():
    Readma(69)


def test_Readma_buffer_fulltest():
    r = Readma("./tests/test.bin")
    assert r.read(1) == 42
    assert r.read(2) == 2448
    assert r.read(4) == 694201337
    assert r.read(8) == 2396795999211369490
    e_f64 = 2.718281828459045
    e_f32 = unpack(">f", pack(">f", e_f64))[0]  # convert to float32
    assert isclose(r.float(), e_f32)
    assert isclose(r.float32(), e_f32)  # check if alias works
    assert isclose(r.float64(), e_f64)
    _strsize = r.read(1)
    assert _strsize == 13
    assert r.bytes(_strsize) == b"Hello, World!"


def test_Readma_buffer_string_endianness():
    r = Readma(b"\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78")
    assert r.read(4) == 2018915346
    r.set_endianness("big")
    assert r.read(4) == 305419896
    r.set_endianness("little")
    assert r.read(4) == 2018915346
