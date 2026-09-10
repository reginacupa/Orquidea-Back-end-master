from pydantic import BaseModel


class ErrorSchema (BaseModel):
    """Define uma mensagem de erro"""

    mesage: str
