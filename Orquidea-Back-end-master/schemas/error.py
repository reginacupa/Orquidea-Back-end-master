from pydantic import Basemodel


class ErrorSchema (Basemodel):
    """Define uma mensagem de erro"""

    mesage: str 