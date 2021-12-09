class Point:
    def __init__(self, value:int) -> None:
        self._value = value
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self._risk = value+1
        self._visited = False

    def isLowPoint(self):
        if(self._up is not None):
            if(self._up._value <= self._value):
                return False
        
        if(self._down is not None):
            if(self._down._value <= self._value):
                return False

        if(self._left is not None):
            if(self._left._value <= self._value):
                return False

        if(self._right is not None):
            if(self._right._value <= self._value):
                return False

        return True

    def __str__(self) -> str:
        if(self._up is None):
            up_val = "None"
        else:
            up_val = self._up._value

        if(self._down is None):
            down_val = "None"
        else:
            down_val = self._down._value

        if(self._left is None):
            left_val = "None"
        else:
            left_val = self._left._value

        if(self._right is None):
            right_val = "None"
        else:
            right_val = self._right._value

        return f'value: {self._value} - up:{up_val} - right:{right_val} - down:{down_val} - left:{left_val}'
