from typing import Iterable, List

from obj import MutableIterable
from bits import Bit, true, false

__all__ = [
    'ByteUnit',
    'Bytes',
]


class ByteUnit(MutableIterable):
    """
    Mmutable byte unit (containing data of one byte).
    Mostly used indirectly by byte groups.
    The value can be from 0 to 255.

    ByteUnit(Bit, Bit, Bit, Bit,
             Bit, Bit, Bit, Bit) -> ByteUnit object initialized
                                    with given bits
    ByteUnit(iterable_of_bits) -> ByteUnit object initialized
                                    with given bits
    ByteUnit(byte_unit) -> mutable copy of the byte unit
    ByteUnit(int) -> ByteUnit object initialized with given value
    ByteUnit() -> empty ByteUnit object

    Construct an mutable byte unit from:
        - eight binary digits
        - an iterable of eight binary digits
        - a byte unit
        - an integer
    """

    # ----- Initialization Methods ----- #
    def __init__(self, *args):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if not args:
            self.bits = [false for i in range(8)]
        elif len(args) == 1:
            arg = args[0]

            if isinstance(arg, int):
                if not 0 <= arg <= 255:
                    raise ValueError(f'a byte unit only accepts integer '
                                     f'from 0 to 255, not {arg}.')
                self.bits = [false for i in range(8)]
                for i in range(8):
                    if arg & 2 ** i != 0:
                        self.bits[7 - i] = true
            elif isinstance(arg, ByteUnit):
                self.bits = [bit.copy() for bit in arg.bits]
            elif isinstance(arg, Iterable):
                arg = [*arg]
                if len(arg) != 8:
                    raise ValueError(f'a byte unit must have exactly '
                                     f'8 digits, not {len(arg)}.')
                self._type_check(arg)
                self.bits = [bit.copy() for bit in arg]
            else:
                raise TypeError(f'cannot convert {type(arg).__name__} object '
                                f'to a byte unit.')
        elif len(args) == 8:
            self._type_check(args)
            self.bits = [*args]
        else:
            raise ValueError(f'ByteUnit only takes 1, 8 or no arguments, '
                             f'not {len(args)}.')

    # ----- Initialization Helper Methods ----- #
    @staticmethod
    def _type_check(iterable: Iterable):
        'Check the type for elements in iterable.  Used in initialization.'
        for bit in iterable:
            if not isinstance(bit, Bit):
                raise TypeError(f'digits of a bit unit must be bits, '
                                f'not {type(bit).__name__}.')

    # ----- Informal Methods ----- #s
    def __repr__(self, /):
        'Return repr(self).'
        return f'ByteUnit({self.to_str()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'ByteUnit({self.to_str()!r})'

    def to_str(self, /):
        'Return a raw representation of the byte unit.'
        return chr(self.to_int())

    def to_mem(self, /):
        'Return a hexadecimal representation of the byte unit memory.'
        return f'{self.to_int():0>2x}'

    # ----- Comparison Methods ----- #
    def __lt__(self, other, /):
        'Return self<other.'
        if isinstance(other, ByteUnit):
            return self.bits < other.bits
        else:
            return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        if isinstance(other, ByteUnit):
            return self.bits <= other.bits
        else:
            return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        if isinstance(other, ByteUnit):
            return self.bits == other.bits
        elif isinstance(other, int):
            char = 0
            for i in range(8):
                char += 2 ** (7 - i) * self.bits[i].value
            return char == other
        else:
            return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        if isinstance(other, ByteUnit):
            return self.bits != other.bits
        else:
            return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        if isinstance(other, ByteUnit):
            return self.bits > other.bits
        else:
            return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        if isinstance(other, ByteUnit):
            return self.bits >= other.bits
        else:
            return NotImplemented

    # ----- Transformation Methods ----- #
    def to_int(self, /):
        'Return a python integer translation of the byte unit.'
        num = 0
        for i in range(8):
            num += 2 ** (7 - i) * self.bits[i].value
        return num

    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.bits)

    def __bool__(self, /):
        'Return bool(self).'
        return any(self.bits)

    # ----- Iterable Methods ----- #
    def __len__(self, /):
        'Return len(self).'
        return 8

    def __getitem__(self, key, /):
        'Return self[key].'
        if isinstance(key, (int, slice)):
            return self.bits[key]
        else:
            raise TypeError(f'byte unit indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __setitem__(self, key, value, /):
        'Set self[key] to value.'
        if isinstance(key, int):
            self.bits[key] = Bit(value)
        elif isinstance(key, slice):
            if len(value) != len(self.bits[key]):
                raise ValueError('unmatched value length')
            self.bits[key] = [Bit(bit) for bit in value]
        else:
            raise TypeError(f'byte unit indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __delitem__(self, key, /):
        'Delete self[key].'
        if isinstance(key, (int, slice)):
            raise ValueError('byte unit memory size is fixed')
        else:
            raise TypeError(f'byte unit indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __iter__(self, /):
        'Implement iter(self).'
        return iter(self.bits)

    def __reversed__(self, /):
        'Return a reverse iterator over the object.'
        return reversed(self.bits)

    def count(self, value, /):
        'Return number of occurrences of value.'
        return self.bits.count(value)

    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        return self.bits.index(value, start, stop)

    # ----- Mutational Methods ----- #
    def copy(self, /):
        'Return a copy of the byte unit.'
        return ByteUnit((bit.copy() for bit in self.bits))


class Bytes(MutableIterable):
    """
    Mutable byte group (multiple bytes).

    Bytes(iterable_of_byte_units) -> Bytes object initialized
                                     with given byte-unit-convertibles
    Bytes(bytes) -> mutable copy of the byte group
    Bytes(int) -> byte group of size given by the parameter
                  initialized with empty byte units
    Bytes() -> empty byte group

    Construct an mutable byte group from:
        - an iterable of byte units
        - a byte group
        - an integer
    """
    bytes: List[ByteUnit]

    # ----- Initialization Methods ----- #
    def __init__(self, value=0):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if isinstance(value, int):
            self.bytes = [ByteUnit() for i in range(value)]
        elif isinstance(value, Bytes):
            self.bytes = [byte.copy() for byte in value.bytes]
        elif isinstance(value, Iterable):
            self.bytes = [ByteUnit(item) for item in value]
        else:
            raise TypeError(f'cannot convert {type(value).__name__} '
                            f'object to a byte group.')

    # ----- Informal Methods ----- #
    def __repr__(self, /):
        'Return repr(self).'
        return f'Bytes({self.to_str()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'Bytes({self.to_str()!r})'

    def to_str(self, /):
        'Return a raw representation of the byte group.'
        return ''.join(byte.to_str() for byte in self.bytes)

    def to_mem(self, /):
        'Return a hexadecimal representation of the byte group memory.'
        return ' '.join(byte.to_mem() for byte in self.bytes)

    # ----- Comparison Methods ----- #
    def __lt__(self, other, /):
        'Return self<other.'
        if isinstance(other, Bytes):
            return self.bytes < other.bytes
        else:
            return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        if isinstance(other, Bytes):
            return self.bytes <= other.bytes
        else:
            return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        if isinstance(other, Bytes):
            return self.bytes == other.bytes
        else:
            return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        if isinstance(other, Bytes):
            return self.bytes != other.bytes
        else:
            return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        if isinstance(other, Bytes):
            return self.bytes > other.bytes
        else:
            return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        if isinstance(other, Bytes):
            return self.bytes >= other.bytes
        else:
            return NotImplemented

    # ----- Transformation Methods ----- #
    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.bytes)

    def __bool__(self, /):
        'Return bool(self).'
        return len(self.bytes) != 0

    # ----- Iterable Methods ----- #
    def __len__(self, /):
        'Return len(self).'
        return len(self.bytes)

    def __getitem__(self, key, /):
        'Return self[key].'
        if isinstance(key, int):
            return self.bytes[key]
        elif isinstance(key, slice):
            return Bytes(self.bytes[key])
        else:
            raise TypeError(f'byte group indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __setitem__(self, key, value, /):
        'Set self[key] to value.'
        if isinstance(key, int):
            self.bytes[key] = ByteUnit(value)
        elif isinstance(key, slice):
            self.bytes[key] = Bytes(value).bytes
        else:
            raise TypeError(f'byte group indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __delitem__(self, key, /):
        'Delete self[key].'
        if isinstance(key, (int, slice)):
            del self.bytes[key]
        else:
            raise TypeError(f'byte group indices must be integers or slices, '
                            f'not {type(key).__name__}')

    def __iter__(self, /):
        'Implement iter(self).'
        return iter(self.bytes)

    def __reversed__(self, /):
        'Return a reverse iterator over the object.'
        return reversed(self.bytes)

    def __contains__(self, item, /):
        'Return item in self.'
        if isinstance(item, (ByteUnit, int)):
            return item in self.bytes
        elif isinstance(item, Bytes):
            if len(item) > len(self):
                return False
            item_len = len(item)
            for i in range(len(self) - item_len + 1):
                if item == self[i:i + item_len]:
                    return True
            else:
                return False
        else:
            return NotImplemented

    def clear(self, /):
        'Remove all items from mutable.'
        self.bytes.clear()

    def count(self, value, /):
        'Return number of occurrences of value.'
        return self.bytes.count(value)

    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        return self.bytes.index(value, start, stop)

    # ----- Calculation Methods ----- #
    def __add__(self, other, /):
        'Return self+other.'
        if isinstance(other, Bytes):
            return Bytes(self.bytes + other.bytes)
        elif isinstance(other, bytes):
            return Bytes(self.bytes + Bytes(other).bytes)
        else:
            raise TypeError(f"can't concat {type(other).__name__}"
                            f" to byte groups")

    def __mul__(self, other, /):
        'Return self*other.'
        if isinstance(other, int):
            return Bytes(self.bytes * other)
        else:
            raise TypeError(f"can't multiply sequence by non-int of "
                            f"type '{type(other).__name__}'")

    def __rmul__(self, other, /):
        'Return other*self.'
        if isinstance(other, int):
            return Bytes(self.bytes * other)
        else:
            raise TypeError(f"can't multiply sequence by non-int of "
                            f"type '{type(other).__name__}'")

    # ----- Mutational Methods ----- #
    def copy(self, /):
        'Return a copy of the byte group.'
        return Bytes((byte.copy() for byte in self.bytes))
