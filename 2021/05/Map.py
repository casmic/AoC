from Vent import Vent

class Map:
    def __init__(self, sizeX = 0, sizeY = 0):
        line=[]
        resulting_empty_map = []

        if (sizeX!=0 and sizeY != 0):
            line = [0 for x in range(sizeX)]
            for y in range(sizeY):
                resulting_empty_map.append(line.copy())
        
        self._map = resulting_empty_map
        self._intersections_count=0

    def __str__(self) -> str:
        to_string = "Map: \n"

        for line in self._map:
            to_string += str(line) + "\n"

        return to_string

    def DrawVent(self, vent, only_ortogonals = True):

        if(vent._is_ortogonal or only_ortogonals==False):
            print(vent)
            x = vent._x1
            y = vent._y1

            step_x = 1
            step_y = 1
            if(vent._x1 > vent._x2):
                step_x = -1

            if(vent._y1 > vent._y2):
                step_y = -1

            while (True):
                print(f'X: {x}  Y: {y}')
                self._map[y][x] += 1
                if(self._map[y][x] == 2):
                    self._intersections_count += 1
                
                if((x == vent._x2) and (y == vent._y2)):
                    break
                
                if(x != vent._x2):
                    x += 1 * step_x
                if(y != vent._y2):
                    y += 1 * step_y
                
                
