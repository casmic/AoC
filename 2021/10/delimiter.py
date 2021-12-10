_opening_chars = ["(","[","{","<"]

class Delimiter:

    def __init__(self, init_char) -> None:
        self._character = init_char
        self._completion_score = 0
        self._corruption_score = 0
        self._expected = ""

        if(init_char == "("):
            self._expected = ")"
            self._completion_score = 1
        elif (init_char == "["):
            self._expected = "]"
            self._completion_score = 2
        elif(init_char == "{"):
            self._expected = "}"
            self._completion_score = 3                        
        elif(init_char == "<"):
            self._expected = ">"
            self._completion_score = 4            
        elif (init_char == ")"):            
            self._corruption_score = 3
        elif (init_char == "]"):                        
            self._corruption_score = 57
        elif (init_char == "}"):                        
            self._corruption_score = 1197
        elif (init_char == ">"):
            self._corruption_score = 25137

    def __str__(self) -> str:
        return self._character

    def is_opening_char(self):
        if(self._character in _opening_chars):
            return True
        else:
            return False            