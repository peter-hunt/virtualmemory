__all__ = [
    'Bit',
    'Array',

    'true',
    'false',
]


class Bit:
    __slots__ = ['value']

    # ----- Initialization Methods ----- #
    def __init__(self, value=False, /):
        'Initialize self.  See help(type(self)) for accurate signature.'
        if isinstance(value, bool):
            self.value = value
        elif hasattr(value, '__bool__'):
            self.value = value.__bool__()
        elif hasattr(value, '__len__'):
            self.value = False if len(value) == 0 else True
        else:
            self.value = True

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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        return 1 if self.value else 0

    def __bool__(self, /):
        'Return bool(self).'
        return True if self.value else False

    # ----- Calculation Methods ----- #
    def __and__(self, other, /):
        'Return self&other.'
        if isinstance(other, (Boolean, bool)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __rand__(self, other, /):
        'Return other&self.'
        if isinstance(other, (Boolean, bool)):
            if self:
                if other:
                    return true
            return false
        else:
            return NotImplemented

    def __xor__(self, other, /):
        'Return self^other.'
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
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
        if isinstance(other, (Boolean, bool)):
            if self:
                return true
            elif other:
                return true
            else:
                return false
        else:
            return NotImplemented


true = Bit(True)
false = Bit(False)
