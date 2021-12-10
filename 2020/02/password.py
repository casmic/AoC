from policy import Policy

class Password:

    def __init__(self, policy_password:str = "") -> None:
        self._counts = {}
        if(policy_password != ""):
            policy_str, self._password = policy_password.split(":")
            self._password = self._password.strip()
            self._policy = Policy(policy_str)

            for c in self._password:
                if(c not in self._counts.keys()):
                    self._counts[c] = 1
                else:
                    self._counts[c] += 1

            self._validate_password_a()
            self._validate_password_b()
        else:
            self._policy = Policy()
            self._password = None
            self._is_valid_a = False
            self._is_valid_b = False

    def __eq__(self, __o: object) -> bool:
        if(self._password == __o._password and
                self._policy == __o._policy):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"password:{self._password} - policy: {str(self._policy)}"

    def _validate_password_a(self):
        self._is_valid_a = False
        if(self._policy._character in self._counts.keys()):
            count = self._counts[self._policy._character]
            if(count >= self._policy._min and
                    count <= self._policy._max):
                self._is_valid_a = True

    def _validate_password_b(self):
        self._is_valid_b = False
        passwd = self._password
        pol = self._policy

        if(len(passwd) >= pol._max):
            count = 0 
            if(passwd[pol._min-1] == pol._character):
                count += 1
            if(passwd[pol._max-1] == pol._character):
                count += 1
            if(count == 1):
                self._is_valid_b = True

    def IsValid(self):
        return self._is_valid_a, self._is_valid_b

