from obj import Mutable, MutableIterable
from bits import Bit, true, false
from bytes import Bytes

__all__ = [
    'Char',
    'UnsignedChar',
    'Short',
    'UnsignedShort',
    'Integer',
    'UnsignedInteger',
    'Long',
    'UnsignedLong',
    'LongLong',
    'UnsignedLongLong',
    'Float',
    'Double',
    'LongDouble',
    'null',

    'DATA_TYPES',
]

DATA_TYPES = (
    Char, UnsignedChar,
    Short, UnsignedShort,
    Integer, UnsignedInteger,
    Long, UnsignedLong,
    LongLong, UnsignedLongLong,
    Float, Double, LongDouble,
)


class Char(MutableIterable):
    """
    Mutable signed character.
    Same as signed 8-bit integer.
    The value can be from -128 to 127.

    Char(char) -> mutable copy of the signed character
    Char(int) -> signed character initialized with given value
    Char() -> Empty signed character

    Construct a mutable signed character from:
        - a signed character object
        - an integer from -128 to 127
        - nothing
    """

    # ----- Initialization Methods ----- #
    def __init__(self, value=0):
        if isinstance(value, Char):
            self.value = value.value.copy()
        elif isinstance(value, int):
            if not -128 <= value <= 127:
                raise ValueError(f'a signed character only accepts integer '
                                 f'from -128 to 127, not {value}.')
            self.value = Bytes(1)
            for i in range(7):
                if value & 2 ** i != 0:
                    self[7 - i] = true
        else:
            raise TypeError(f'cannot convert {type(value).__name__} '
                            f'object to a signed character.')

    # ----- Informal Methods ----- #
    def __repr__(self, /):
        'Return repr(self).'
        return f'{type(self).__name__}({self.to_str()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'{type(self).__name__}({self.to_str()!r})'

    def to_str(self, /):
        'Return a raw representation of the signed character.'
        return chr(self.to_int())

    def to_mem(self, /):
        'Return a hexadecimal representation of the signed character memory.'
        return f'{self.to_int():0>2x}'

    # ----- Comparison Methods ----- #

    # ----- Transformation Methods ----- #
    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.to_int())

    def __bool__(self, /):
        'Return bool(self).'
        return any(self.value)

    def to_int(self, /):
        'Return a python integer translation of the signed character.'
        return self.value[0].to_int()

    # ----- Iterable Methods ----- #
    def __len__(self, /):
        'Return len(self).'
        return 8

    def __getitem__(self, key, /):
        'Return self[key].'
        return self.value[0][key]

    def __setitem__(self, key, value, /):
        'Set self[key] to value.'
        self.value[0][key] = value

    def __delitem__(self, key, /):
        'Delete self[key].'
        if isinstance(key, (int, slice)):
            raise ValueError('signed character memory size is fixed')
        else:
            raise TypeError(f'signed character indices must be '
                            f'integers or slices, not {type(key).__name__}')

    def __iter__(self, /):
        'Implement iter(self).'
        return iter(self.value[0])

    def __reversed__(self, /):
        'Return a reverse iterator over the object.'
        return reversed(self.value[0])

    # ----- Calculation Methods ----- #
    def __add__(self, other, /):
        'Return self+other.'
        if isinstance(other, Char):
            carry = false
            result = Char()
            for i in range(8):
                last_carry = carry
                carry = false
                digit = false
                for value in (self[7 - i], other[7 - i], last_carry):
                    if value:
                        if digit:
                            carry = true
                            digit = false
                        else:
                            digit = true
                result.value[0][7 - i] = digit
            return result
        else:
            return NotImplemented

    def __iadd__(self, other, /):
        'Implement self+=other.'
        if isinstance(other, Char):
            self.value = (self + other).value
        else:
            return NotImplemented

    # ----- Custom Mutable Methods ----- #
    def copy(self, /):
        'Return a copy of the signed character.'
        return Char(self.value)


class UnsignedChar(Mutable):
    """
    Mutable unsigned character.
    Same as unsigned 8-bit integer.
    The value can be from 0 to 255.

    UnsignedChar(unsigned_char) -> mutable copy of the unsigned character
    UnsignedChar(int) -> unsigned character initialized with given value
    UnsignedChar() -> Empty unsigned character

    Construct a mutable short integer from:
        - an unsigned character object
        - an integer from 0 to 255
        - nothing
    """

    # ----- Initialization Methods ----- #
    def __init__(self, value=0):
        if isinstance(value, UnsignedChar):
            self.value = value.value.copy()
        elif isinstance(value, int):
            if not 0 <= value <= 255:
                raise ValueError(f'an unsigned character only accepts integer '
                                 f'from 0 to 255, not {value}.')
            self.value = Bytes(1)
            for i in range(7):
                if value & 2 ** i != 0:
                    self[7 - i] = true
        else:
            raise TypeError(f'cannot convert {type(value).__name__} '
                            f'object to an unsigned character.')

    # ----- Informal Methods ----- #
    def __repr__(self, /):
        'Return repr(self).'
        return f'{type(self).__name__}({self.to_str()!r})'

    def __str__(self, /):
        'Return str(self).'
        return f'{type(self).__name__}({self.to_str()!r})'

    def to_str(self, /):
        'Return a raw representation of the unsigned character.'
        return chr(self.to_int())

    def to_mem(self, /):
        'Return a hexadecimal representation of the unsigned character memory.'
        return f'{self.to_int():0>2x}'

    # ----- Comparison Methods ----- #

    # ----- Transformation Methods ----- #
    def __hash__(self, /):
        'Return hash(self).'
        return hash(self.to_int())

    def __bool__(self, /):
        'Return bool(self).'
        return any(self.value)

    def to_int(self, /):
        'Return a python integer translation of the unsigned character.'
        return self.value[0].to_int()

    # ----- Iterable Methods ----- #
    def __len__(self, /):
        'Return len(self).'
        return 8

    def __getitem__(self, key, /):
        'Return self[key].'
        return self.value[0][key]

    def __setitem__(self, key, value, /):
        'Set self[key] to value.'
        self.value[0][key] = value

    def __delitem__(self, key, /):
        'Delete self[key].'
        if isinstance(key, (int, slice)):
            raise ValueError('unsigned character memory size is fixed')
        else:
            raise TypeError(f'unsigned character indices must be '
                            f'integers or slices, not {type(key).__name__}')

    def __iter__(self, /):
        'Implement iter(self).'
        return iter(self.value[0])

    def __reversed__(self, /):
        'Return a reverse iterator over the object.'
        return reversed(self.value[0])

    # ----- Calculation Methods ----- #
    def __add__(self, other, /):
        'Return self+other.'
        if isinstance(other, UnsignedChar):
            carry = false
            result = Char()
            for i in range(8):
                last_carry = carry
                carry = false
                digit = false
                for value in (self[7 - i], other[7 - i], last_carry):
                    if value:
                        if digit:
                            carry = true
                            digit = false
                        else:
                            digit = true
                result.value[0][7 - i] = digit
            return result
        else:
            return NotImplemented

    def __iadd__(self, other, /):
        'Implement self+=other.'
        if isinstance(other, UnsignedChar):
            self.value = (self + other).value
        else:
            return NotImplemented

    # ----- Custom Mutable Methods ----- #
    def copy(self, /):
        'Return a copy of the unsigned character.'
        return UnsignedChar(self.value)


class Short(Mutable):
    """
    Mutable short integer.
    Same as 16-bit integer.
    The value can be from -32,768 to 32,767.

    Char(char) -> mutable copy of char
    Char(int) -> Char object initialized with given value
    Char() -> Empty Char object

    Construct a mutable short integer from:
        - a character object
        - an integer from 0 to 255
        - nothing
    """
    pass


class UnsignedShort(Mutable):
    pass


class Integer(Mutable):
    pass


class UnsignedInteger(Mutable):
    pass


class Long(Mutable):
    pass


class UnsignedLong(Mutable):
    pass


class LongLong(Mutable):
    pass


class UnsignedLongLong(Mutable):
    pass


class Float(Mutable):
    pass


class Double(Mutable):
    pass


class LongDouble(Mutable):
    pass


null = Char()
