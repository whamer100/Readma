from readma.readma import Readma, ReadmaTypes

if __name__ == '__main__':
    r = Readma(b"Hello there. I think you're running the wrong file!")
    rm = ReadmaTypes.__members__  # this is to make a certain test not be angry
    print(r.readall())
