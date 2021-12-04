class Board:
    def __init__(self,index):
        self._rows=[]
        self._columns=[]
        self._sum=0
        self._board_won = False
        self._index = index
    
    def AddRow(self, values):
        return_value = -1

        if(values is None or len(values)==0):
            return return_value


        rows_count = len(self._rows)
        self._rows.append(values)
        self._sum += sum(values)

        if(rows_count==0):
            self._columns.append([])
        
        for value_index in range(len(values)):
            if(rows_count==0):
                self._columns.append([])            
            self._columns[value_index].append(values[value_index])

        return return_value

    def Draw(self, value):

        return_value = 0 

        for row_index in range(len(self._rows)):
            try:
                value_index = self._rows[row_index].index(value)
                self._rows[row_index][value_index] = -1
                self._sum -= value
                col_value_index = self._columns[value_index].index(value)
                self._columns[value_index][col_value_index] = -1
                if(sum(self._rows[row_index]) / len(self._rows[row_index]) == -1 or 
                    sum(self._columns[value_index]) / len(self._columns[value_index]) == -1):
                        return_value = self._sum
                        self._board_won = True
                        break
            except ValueError:
                #not found
                pass

        return return_value