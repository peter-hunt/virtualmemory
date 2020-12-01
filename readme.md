# Virtual Memory

Virtual Memory is a Python project for computer memory simulation

## Installation

Use git to install Virtual Memory.

```bash
git install https://github.com/peter-hunt/virtualmemory.git
```

## Usage

```python
from virtualmemory import *

print(true)
print(false)

byte_group = Char(-48)
print(byte_group)
print(byte_group.to_str())
print(byte_group.to_mem())

character = Char(-48)
print(character)
print(character.to_str())
print(character.to_mem())
print(character.to_int())
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE.txt)
