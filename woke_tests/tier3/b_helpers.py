from woke_tests.common import *
from .a_init import *

class Helpers(Init):
    def random_user(s) -> Account:
        return random.choice(s.users)

    # def random_token(s) -> ERC20:
    #     return random.choice(s.tokens)
