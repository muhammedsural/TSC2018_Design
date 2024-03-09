
from dataclasses import dataclass

from MSCSI.Enums import eLoadPatternType
from MSCSI.ErrorHandler import ApiReturnError


@dataclass
class LoadPattern:
    RefApi : object # SapModel.LoadPatterns
    # AutoSeismic : cAutoSeismic 
    # AutoWind    : cAutoWind

    def Add(self,Name : str, MyType : eLoadPatternType, SelfWTMultiplier : float = 0, AddAnalysisCase : bool = True) -> None|ApiReturnError:
        """Adds a new load pattern.

        Args:
            Name (str): The name for the new load pattern.
            MyType (eLoadPatternType): This is one of the items in the eLoadPatternType enumeration. 
            SelfWTMultiplier (float, optional): The self weight multiplier for the new load pattern. . Defaults to 0.
            AddAnalysisCase (bool, optional): If this item is True, a linear static load case corresponding to the new load pattern is added.Defaults to True.

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None|ApiReturnError
        """
        result = self.RefApi.Add(Name,MyType,SelfWTMultiplier,AddAnalysisCase)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def ChangeName(self, Name : str, NewName : str) -> None|ApiReturnError:
        """Applies a new name to a load pattern.

        Args:
            Name (str): The name of a defined load pattern.
            NewName (str): The new name for the load pattern.

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None|ApiReturnError
        """
        result = self.RefApi.ChangeName(Name,NewName)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def Count(self) -> int:
        """Retrieves the number of defined load patterns."""
        result = self.RefApi.Count()
        return result

    def Delete(self,Name : str) -> None|ApiReturnError:
        """Deletes the specified load pattern.  

        Args:
            Name (str): The name of a defined load pattern.
        """
        result = self.RefApi.Delete(Name)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def GetAutoSeismicCode(self,Name : str):
        """Retrieves the code name used for auto seismic parameters in Quake-type load patterns."""  
        CodeName = str()
        result = self.RefApi.GetAutoSeismicCode(Name,CodeName)
        return result

    def GetAutoWindCode(self,Name : str):
        """Retrieves the code name used for auto wind parameters in Wind-type load patterns.  """
        CodeName = str()
        result = self.RefApi.GetAutoSeismicCode(Name,CodeName)
        return result
    
    def GetLoadType(self,Name : str) -> None|ApiReturnError:
        """Retrieves the load type for a specified load pattern.  """
        MyType = int()
        result = self.RefApi.GetLoadType(Name,MyType)
        return result

    def GetNameList(self) -> None|ApiReturnError:
        """Retrieves the names of all defined load cases.  """
        NumberNames = int()
        MyName = list([])
        retVal = 0
        result = [NumberNames,MyName,retVal]
        result = self.RefApi.GetNameList(NumberNames,MyName)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
            return result

    def GetSelfWTMultiplier(self,Name : str) -> None|ApiReturnError:
        """Retrieves the self weight multiplier for a specified load pattern."""
        SelfWTMultiplier = float()
        retVal = 0
        result = [SelfWTMultiplier,retVal]
        result = self.RefApi.GetSelfWTMultiplier(Name,SelfWTMultiplier)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
            return result

    def SetLoadType(self,Name : str,MyType : eLoadPatternType) -> None|ApiReturnError:
        """Assigns a load type to a load pattern."""
        result = self.RefApi.SetLoadType(Name,MyType)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
        
    def SetSelfWTMultiplier(self, Name : str, SelfWTMultiplier : float) -> None|ApiReturnError:
        """Assigns a self weight multiplier to a load case."""
        result = self.RefApi.SetLoadType(Name,SelfWTMultiplier)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
