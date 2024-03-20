from TSC.MSCSI.Enums import eReturnCode

class CustomconnectionError(Exception):
    """Sap2000 or Etabs connection error"""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class CustomCommentError(Exception):
     """General api comments error handler. First arg return api comment value, second arg error message"""
     def __init__(self, *args: object) -> None:
          super().__init__(*args)

     def __str__(self) -> str:
          return f"Return api function succesfull value = {self.args[0]},\nError mesage : {self.args[1]}"
     
class ApiReturnError(Exception):
     """General api return error handler."""
     def __init__(self, ReturnCode) -> None:
          super().__init__()
          self.ReturnCode = ReturnCode

     def __str__(self) -> str:
          return f"Return api function succesfull value = {self.ReturnCode}, Error mesage : {self.Handle()}"
     
     def Handle(self)->None:
          for ErrorName,ErrorValue in zip(eReturnCode._member_map_.keys(),eReturnCode._member_map_.values()):
               if self.ReturnCode == ErrorValue.value:
                    return ErrorName