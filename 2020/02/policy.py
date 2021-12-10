class Policy:

    def __init__(self, policy_string:str = "") -> None:

        if(policy_string != ""):
            interval, self._character = policy_string.split()
            split = interval.split("-")
            self._min, self._max = int(split[0]), int(split[1])    
        else:
            self._min = self._max = 0
            self._character = None

    def __eq__(self, __o: object) -> bool:
        if(self._max == __o._max and
            self._min == __o._min and
            self._character == __o._character):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"char:{self._character} - min:{self._min} - max:{self._max}"