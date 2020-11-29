from typing import Iterable, List

from bits import Bit, true, false
from obj import Immutable

__all__ = [
    'ByteUnit',
    'Bytes',
    'null',
]


class ByteUnit(Immutable):
    pass


class ByteUnit(Immutable):
    """
    ByteUnit(Bit, Bit, Bit, Bit,
             Bit, Bit, Bit, Bit) -> ByteUnit object initialized
                                    with given bits
    ByteUnit(iterable_of_bits) -> ByteUnit object initialized
                                    with given bits
    ByteUnit(byte_unit) -> mutable copy of byte_unit
    ByteUnit(int) -> ByteUnit object initialized with given value
    ByteUnit() -> empty ByteUnit object
    """
    bits: List[Bit]

    __slots__ = ('bits',)

    # ----- Initialization Methods ----- #
    def __init__(self, *args):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if not args:
            super(Immutable, self).__setattr__(
                'bits', [false for i in range(8)]
            )
        elif len(args) == 1:
            arg = args[0]

            if isinstance(arg, int):
                if not 0 <= arg < 256:
                    raise ValueError(f'a byte unit only accepts integer '
                                     f'from 0 to 255, not {arg}.')
                super(Immutable, self).__setattr__(
                    'bits', [Bit(int(bit)) for bit in f'{arg:0>8b}']
                )
            elif isinstance(arg, ByteUnit):
                super(Immutable, self).__setattr__(
                    'bits', [bit.copy() for bit in arg.bits]
                )
            elif isinstance(arg, Iterable):
                arg = [*arg]
                if len(arg) != 8:
                    raise ValueError(f'a byte unit must have exactly '
                                     f'8 digits, not {len(arg)}.')
                self._type_check(arg)
                super(Immutable, self).__setattr__(
                    'bits', [bit.copy() for bit in arg]
                )
            else:
                raise TypeError(f'cannot convert {type(arg).__name__} object '
                                f'to a byte unit.')
        elif len(args) == 8:
            self._type_check(args)
            super(Immutable, self).__setattr__('bits', [*args])
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

    # ----- Informal Methods ----- #
    def to_string(self, /):
        'Return a raw representation of the byte unit.'
        char = 0
        for i in range(8):
            char += 2 ** (7 - i) * self.bits[i].value
        return chr(char)

    def __repr__(self, /):
        'Return repr(self).'
        return f'ByteUnit({self.to_string()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'ByteUnit({self.to_string()!r})'

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
    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.bits)

    def __bool__(self, /):
        'Return bool(self).'
        return any(self.bits)

    # ----- Mutational Methods ----- #
    def copy(self, /):
        'Return a copy of the byte unit.'
        return ByteUnit((bit.copy() for bit in self.bits))


class Bytes(Immutable):
    pass


class Bytes(Immutable):
    """
    Bytes(iterable_of_byte_units) -> Bytes object initialized
                                     with given byte unit
                                     (accepts builtin bytes)
    Bytes(bytes) -> mutable copy of bytes
    Bytes(int) -> Bytes object of size given by the parameter
                  initialized with null bytes
    Bytes() -> empty Bytes object
    """
    bytes: List[ByteUnit]

    __slots__ = ('bytes',)

    # ----- Initialization Methods ----- #
    def __init__(self, value=0):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if isinstance(value, int):
            super(Immutable, self).__setattr__(
                'bytes', [ByteUnit() for i in range(value)]
            )
        elif isinstance(value, Bytes):
            super(Immutable, self).__setattr__(
                'bytes', [byte.copy() for byte in value.bytes]
            )
        elif isinstance(value, Iterable):
            super(Immutable, self).__setattr__(
                'bytes', [ByteUnit(item) for item in value]
            )
        else:
            raise TypeError(f'cannot convert {type(value).__name__} '
                            f'object to bytes.')

    # ----- Informal Methods ----- #
    def to_string(self, /):
        'Return a raw representation of the bytes.'
        return ''.join(byte.to_string() for byte in self.bytes)

    def __repr__(self, /):
        'Return repr(self).'
        return f'Bytes({self.to_string()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'Bytes({self.to_string()!r})'

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
            raise TypeError(f'byte indices must be integers or slices, '
                            f'not {type(key).__name__}')

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

    # ----- Calculation Methods ----- #
    def __add__(self, other, /):
        'Return self+other.'
        if isinstance(other, Bytes):
            return Bytes(self.bytes + other.bytes)
        elif isinstance(other, bytes):
            return Bytes(self.bytes + Bytes(other).bytes)
        else:
            raise TypeError(f"can't concat {type(other).__name__} to bytes")

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
        'Return a copy of the bytes.'
        return Bytes((byte.copy() for byte in self.bytes))


null = Bytes()
