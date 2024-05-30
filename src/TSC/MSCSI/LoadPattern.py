
from dataclasses import dataclass

from TSC.MSCSI.Enums import eLoadPatternType
from TSC.MSCSI.ErrorHandler import ApiReturnError


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

    def SetAutoSeismicASCE716(self,Name : str, nDir : list[bool], Eccen : float, PeriodFlag : int, CtType : int, UserT : float, UserZ : bool, TopZ : float, BottomZ : float, R : float, Omega : float, Cd : float, I : float, Ss : float, S1 : float, TL : float, SiteClass : int, Fa : float, Fv : float)-> None|ApiReturnError:
        """Defines auto seismic loading parameters for the 2016 ASCE 7 code 

        Args:
            Name (str): The name of an existing Seismic-type load pattern 
            nDir (list[bool]): This is an array with 6 inputs that indicates the seismic load directions 
                                1- nDir(1) = True = X Dir
                                2- nDir(2) = True = Y Dir
                                3- nDir(3) = True = X Dir + Eccentricity
                                4- nDir(4) = True = Y Dir + Eccentricity
                                5- nDir(5) = True = X Dir - Eccentricity
                                6- nDir(6) = True = Y Dir - Eccentricity
            Eccen (float): The eccentricity ratio that applies to all diaphragms
            PeriodFlag (int): This is 1, 2 or 3, indicating the time period option 
                                1- Approximate
                                2- Program calculated
                                3- User defined
            CtType (int): This is one of the following values. This item is used only when PeriodFlag is 1 or 2 
                                1- 0 = Ct = 0.028 (ft), x = 0.8
                                2- 1 = Ct = 0.016 (ft), x = 0.9
                                3- 2 = Ct = 0.03 (ft), x = 0.75
                                4- 3 = Ct = 0.02 (ft), x = 0.75
            UserT (float): The user specified time period. This item is meaningful when the PeriodFlag item is 3. [s] 
            UserZ (bool): This item is not used in ETABS 
            TopZ (float): The global Z-coordinate at the highest level where auto seismic loads are applied. [L] 
            BottomZ (float): The global Z-coordinate at the lowest level where auto seismic loads are applied. [L]
            R (float): The response modification factor 
            Omega (float): The system overstrength factor 
            Cd (float): The deflection amplification factor 
            I (float): The occupancy importance factor
            Ss (float): The seismic coefficients Ss
            S1 (float): The seismic coefficients S1 
            TL (float): The long-period transition period. [s]
            SiteClass (int): This is 1, 2, 3, 4, 5 or 6, indicating the site class 
                               1- A
                               2- B
                               3- C
                               4- D
                               5- E
                               6- F
            Fa (float): The site coefficients Fa. This item is used only when the SiteClass item is 5 or 6
            Fv (float): The site coefficients Fv. This item is used only when the SiteClass item is 5 or 6 

        Returns:
            None|ApiReturnError: _description_
        """
        result = self.RefApi.AutoSeismic.SetASCE716(Name,nDir, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, Ss, S1, TL, SiteClass, Fa, Fv)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")