<h1 align="center">Readma? What's Readma?</h1>

### Readma is a binary stream reading library I made for fun that I decided I would extend on and release

> Well, what does it do?

### Well I'm glad you asked!

Readma is a little library I started to help with parsing binary files.

> That's it?

Well yeah, what did you expect?
Some large module I've been writing my entire life that will change the world with its amazing binary reading ability?

## Cool Badge
![Tests](https://github.com/whamer100/Readma/actions/workflows/tests.yml/badge.svg)

## Usage

> Note, requires Python 3.9 or higher (For now at least)

### Installation

```sh
pip install readma
```

### Sample code

```py
from readma import Readma

# Let's say this file contains in order:
# - An integer
# - An unsigned integer
# - A float
# - A string prefixed by its length with a byte
# - An unknown amount of data you just really need read
r = Readma("some_file.bin") # note: defaults to Little Endian

integer = r.read(4) # size in bytes
unsigned_integer = r.uread(4)

a_float = r.float()

length = r.read(1)
string = r.bytes(length)

important_data = r.readall()
```

## Documentation

### [tba](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## License

Copyright (c) 2021 [whamer100](https://github.com/whamer100) <br />
This project is [MIT](https://github.com/whamer100/Readma/blob/master/LICENSE.md) licensed.

---
> hey is this project name just one big ligma joke
###### maybe
