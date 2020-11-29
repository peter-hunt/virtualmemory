__all__ = [
    'Object',
    'Mutable',
    'Immutable',
    'Iterable',
    'MutableIterable',
    'ImmutableIterable',
]


class Object:
    """
    Object() -> Empty Object
    """

    # ----- Initialization Methods ----- #
    def __init__(self, /):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass

    def __repr__(self, /):
        'Return repr(self).'
        return f'{type(self).__name__}()'

    def __str__(self, /):
        'Return str(self).'
        return f'{type(self).__name__}()'

    # ----- Comparison Methods ----- #
    def __lt__(self, other, /):
        'Return self<other.'
        return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        return NotImplemented

    # ----- Transformation Methods ----- #
    def __hash__(self, /):
        'Return hash(self).'
        return NotImplemented

    def __bool__(self, /):
        'Return bool(self).'
        return True

    # ----- Calculation Methods ----- #
    def __add__(self, other, /):
        'Return self+other.'
        return NotImplemented

    def __radd__(self, other, /):
        'Return other+self.'
        return NotImplemented

    def __iadd__(self, other, /):
        'Implement self+=other.'
        return NotImplemented

    def __sub__(self, other, /):
        'Return self-other.'
        return NotImplemented

    def __rsub__(self, other, /):
        'Return other-self.'
        return NotImplemented

    def __isub__(self, other, /):
        'Implement self-=other.'
        return NotImplemented

    def __mul__(self, other, /):
        'Return self*other.'
        return NotImplemented

    def __rmul__(self, other, /):
        'Return other*self.'
        return NotImplemented

    def __imul__(self, other, /):
        'Implement self*=other.'
        return NotImplemented

    def __matmul__(self, other, /):
        'Return self@other.'
        return NotImplemented

    def __rmatmul__(self, other, /):
        'Return other@self.'
        return NotImplemented

    def __imatmul__(self, other, /):
        'Implement self@=other.'
        return NotImplemented

    def __div__(self, other, /):
        'Return self/other.'
        return NotImplemented

    def __rdiv__(self, other, /):
        'Return other/self.'
        return NotImplemented

    def __idiv__(self, other, /):
        'Implement self/=other.'
        return NotImplemented

    def __floordiv__(self, other, /):
        'Return self//other.'
        return NotImplemented

    def __rfloordiv__(self, other, /):
        'Return other//self.'
        return NotImplemented

    def __ifloordiv__(self, other, /):
        'Implement self//=other.'
        return NotImplemented

    def __mod__(self, other, /):
        'Return self%other.'
        return NotImplemented

    def __rmod__(self, other, /):
        'Return other%self.'
        return NotImplemented

    def __imod__(self, other, /):
        'Implement self%=other.'
        return NotImplemented

    def __divmod__(self, other, /):
        'Return divmod(self, other).'
        return self // other, self % other

    def __rdivmod__(self, other, /):
        'Return divmod(other, self).'
        return other // self, other % self

    def __pow__(self, other, modulo=None, /):
        'Return pow(self, other, modulo).'
        return NotImplemented

    def __rpow__(self, other, modulo=None, /):
        'Return pow(other, self, modulo).'
        return NotImplemented

    def __ipow__(self, other, modulo=None, /):
        'Implement self=self**other%modulo.'
        return NotImplemented

    def __lshift__(self, other, /):
        'Return self<<other.'
        return NotImplemented

    def __rlshift__(self, other, /):
        'Return other<<self.'
        return NotImplemented

    def __ilshift__(self, other, /):
        'Implement self<<=other.'
        return NotImplemented

    def __rshift__(self, other, /):
        'Return self>>other.'
        return NotImplemented

    def __rrshift__(self, other, /):
        'Return other>>self.'
        return NotImplemented

    def __irshift__(self, other, /):
        'Implement self>>=other.'
        return NotImplemented

    # ----- Bitwise Calculation Methods ----- #
    def __and__(self, other, /):
        'Return self&other.'
        return NotImplemented

    def __rand__(self, other, /):
        'Return other&self.'
        return NotImplemented

    def __iand__(self, other, /):
        'Implement self&=other.'
        return NotImplemented

    def __xor__(self, other, /):
        'Return self^other.'
        return NotImplemented

    def __rxor__(self, other, /):
        'Return other^self.'
        return NotImplemented

    def __ixor__(self, other, /):
        'Implement self^=other.'
        return NotImplemented

    def __or__(self, other, /):
        'Return self|other.'
        return NotImplemented

    def __ror__(self, other, /):
        'Return other|self.'
        return NotImplemented

    def __ior__(self, other, /):
        'Implement self|=other.'
        return NotImplemented


class Mutable(Object):
    """
    Mutable() -> Empty Mutable
    """

    # ----- Informal Methods ----- #
    def __repr__(self, /):
        'Return repr(self).'
        return f'{type(self).__name__}({self.to_string()})'

    def __str__(self, /):
        'Return str(self).'
        return f'{type(self).__name__}({self.to_string()})'

    # ----- Custom Informal Methods ----- #
    def to_string(self, /):
        'Return a raw representation of the object.'
        return ''

    # ----- Custom Mutable Methods ----- #
    def copy(self, /):
        'Return a copy of the object.'
        pass


class Immutable(Object):
    """
    Immutable() -> Empty Immutable
    """

    __slots__ = ()

    # ----- Attribute Methods ----- #
    def __getattr__(self, name):
        if name in self.__slots__:
            return super(Object, self).__getattr__(name)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has "
                                 f"no attribute '{name}'")

    def __setattr__(self, name, value):
        if name in self.__slots__:
            raise AttributeError(
                f"attribute '{name}' of '{type(self).__name__}' "
                f"objects is not writable"
            )
        else:
            raise AttributeError(f"'{type(self).__name__}' object has "
                                 f"no attribute '{name}'")

    def __delattr__(self, name):
        if name in self.__slots__:
            raise AttributeError(
                f"attribute '{name}' of '{type(self).__name__}' "
                f"objects is not writable"
            )
        else:
            raise AttributeError(f"'{type(self).__name__}' object has "
                                 f"no attribute '{name}'")


class Iterable(Object):
    """
    Iterable() -> Empty Iterable
    """

    # ----- Iterable Methods ----- #
    def __len__(self, /):
        'Return len(self).'
        pass

    def __getitem__(self, key, /):
        'Return self[key].'
        pass

    def __iter__(self, /):
        'Implement iter(self).'
        pass

    def __reversed__(self, /):
        'Return a reverse iterator over the object.'
        pass

    def __contains__(self, item, /):
        'Return item in self.'
        pass

    # ----- Custom Iterable Methods ----- #
    def count(self, value, /):
        'Return number of occurrences of value.'
        pass

    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        pass


class MutableIterable(Mutable, Iterable):
    """
    MutableIterable() -> Empty MutableIterable
    """

    # ----- Mutable Iterable Methods ----- #
    def __setitem__(self, key, value, /):
        'Return self[key].'
        pass

    def __delitem__(self, key, /):
        'Return self[key].'
        pass

    # ----- Custom Mutable Iterable Methods ----- #
    def clear(self, /):
        'Remove all items from mutable.'
        pass


class ImmutableIterable(Immutable, Iterable):
    """
    ImmutableIterable() -> Empty ImmutableIterable
    """

    pass
