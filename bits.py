from obj import Immutable

__all__ = [
    'Bit',
    'true',
    'false',
]


class Bit(Immutable):
    """
    Bit(x) -> Bit

    Returns Bit(1) when the argument x is true, Bit(0) otherwise.
    The Bit(1) and Bit(0) are the only two instances of the class Bit.
    """
    value: bool

    __slots__ = ('value',)

    # ----- Initialization Methods ----- #
    def __init__(self, value=False, /):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if isinstance(value, bool):
            super(Immutable, self).__setattr__('value', value)
        elif hasattr(value, '__bool__'):
            super(Immutable, self).__setattr__('value', value.__bool__())
        elif hasattr(value, '__len__'):
            super(Immutable, self).__setattr__('value', len(value) != 0)
        else:
            super(Immutable, self).__setattr__('value', True)

    # ----- Informal Methods ----- #
    def __repr__(self, /):
        'Return repr(self).'
        return 'Bit(1)' if self else 'Bit(0)'

    def __str__(self, /):
        'Return str(self).'
        return 'Bit(1)' if self else 'Bit(0)'

    # ----- Comparison Methods ----- #
    def __lt__(self, other, /):
        'Return self<other.'
        if isinstance(other, (Bit, bool)):
            if self:
                return false
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __le__(self, other, /):
        'Return self<=other.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return true
                else:
                    return false
            else:
                return true
        else:
            return NotImplemented

    def __eq__(self, other, /):
        'Return self==other.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return true
                else:
                    return false
            else:
                if other:
                    return false
                else:
                    return true
        else:
            return NotImplemented

    def __ne__(self, other, /):
        'Return self!=other.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __gt__(self, other, /):
        'Return self>other.'
        if isinstance(other, (Bit, bool)):
            if other:
                return false
            elif self:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __ge__(self, other, /):
        'Return self>=other.'
        if isinstance(other, (Bit, bool)):
            if other:
                if self:
                    return true
                else:
                    return false
            else:
                return true
        else:
            return NotImplemented

    # ----- Transformation Methods ----- #
    def __hash__(self, /):
        'Return hash(self).'
        return 1 if self else 0

    def __bool__(self, /):
        'Return bool(self).'
        return True if self.value else False

    # ----- Calculation Methods ----- #
    def __and__(self, other, /):
        'Return self&other.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __rand__(self, other, /):
        'Return other&self.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __xor__(self, other, /):
        'Return self^other.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __rxor__(self, other, /):
        'Return other^self.'
        if isinstance(other, (Bit, bool)):
            if self:
                if other:
                    return false
                else:
                    return true
            else:
                if other:
                    return true
                else:
                    return false
        else:
            return NotImplemented

    def __or__(self, other, /):
        'Return self|other.'
        if isinstance(other, (Bit, bool)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    def __ror__(self, other, /):
        'Return other|self.'
        if isinstance(other, (Bit, bool)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented

    # ----- Custom Mutable Methods ----- #
    def copy(self, /):
        'Return a copy of the binary digit.'
        return Bit(self)


true = Bit(True)
false = Bit(False)
