import re

class Vent:
    def __init__(self,vent_string = ''):
        x1 = x2 = y1 = y2 = 0
        max_x = max_y = 0
        min_x = min_y = 0
        is_ortogonal= False

        if(vent_string!='' and vent_string is not None):
            vent_list=re.split('\W+', vent_string)
            x1=int(vent_list[0])
            x2=int(vent_list[2])
            y1=int(vent_list[1])
            y2=int(vent_list[3])

            max_x=max(x1, x2)
            max_y=max(y1, y2)
            min_x=min(x1, x2)
            min_y=min(y1, y2)

        if(x1==x2 or y1==y2):
            is_ortogonal = True

        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        self._max_x = max_x
        self._max_y = max_y
        self._min_x = min_x
        self._min_y = min_y
        self._is_ortogonal = is_ortogonal
        

    def __str__(self) -> str:
        return (f'{self._x1}, {self._y1} -> {self._x2}, {self._y2} - max_x: {self._max_x} - max_y {self._max_y} - is ortogonal: {self._is_ortogonal} ')

    def __eq__(self, __o: object) -> bool:
        return_val = False

        if(self._x1 == __o._x1 and 
                self._x2 == __o._x2 and 
                self._y1 == __o._y1 and  
                self._y2 == __o._y2 and 
                self._max_x == __o._max_x and 
                self._max_y == __o._max_y and
                self._is_ortogonal == __o._is_ortogonal):
            return_val = True
            #print(return_val)

        return return_val
