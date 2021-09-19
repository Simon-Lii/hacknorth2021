import jwt
from typing import Tuple, Union

auth_secret = "my_secret"


def get_token(userid: str) -> str:  # should I use custom exceptions here?
    print(userid, "input_token")
    generated_token = jwt.encode(
        {"userid": str(userid)}, auth_secret, algorithm="HS256",
    )
    return generated_token


def verify_data(
    encoded_secret: str,
) -> Tuple[bool, Union[Tuple[str, int], str]]:  # TODO rename to verify session
    try:
        decoded = jwt.decode(encoded_secret, auth_secret, algorithms=["HS256"])
        print(decoded["userid"], "output token")
        return True, decoded["userid"]
    except jwt.ExpiredSignatureError:
        return False, ("Expired token", 401)
    except jwt.exceptions.InvalidSignatureError:
        return False, ("Invalid signature", 401)
    except jwt.InvalidTokenError:
        return False, ("Invalid Token", 401)
