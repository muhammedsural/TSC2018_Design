

class ValidationError(Exception):
     """General api comments error handler. First arg return api comment value, second arg error message"""
     def __init__(self, *args: object) -> None:
          super().__init__(*args)

     def __str__(self) -> str:
          return f"Unexpected value = {self.args}"