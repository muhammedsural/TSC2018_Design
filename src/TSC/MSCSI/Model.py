
from dataclasses import dataclass
from TSC.MSCSI.Enums import eReturnCode, eUnits
from TSC.MSCSI.ErrorHandler import ApiReturnError


@dataclass
class SapModel:
    RefApi      : object

    def GetDatabaseUnits(self) -> None:
         val = self.RefApi.GetDatabaseUnits()
         for unitName,unitValue in zip(eUnits._member_map_.keys(),eUnits._member_map_.values()):
            if val == unitValue.value: 
                 print(unitName)
                 break
            
    def GetDatabaseUnits_2(self,forceUnits : int, lengthUnits : int, temperatureUnits : int) -> list:
         val = self.RefApi.GetDatabaseUnits_2(forceUnits,lengthUnits,temperatureUnits)
         return val
    
    def GetMergeTol(self, MergeTol : float) -> list:
         val = self.RefApi.GetMergeTol(MergeTol)
         return val

    def GetModelFilename(self,IncludePath  : bool) -> str:
        """Returns a string that represents the filename of the current model, with or without the full path. 
            Method testi yapılmadı sıkıntı çıkabilir...
        Args:
            IncludePath (bool): A boolean (True or False) value. When this item is True, the returned filename includes the full path where the file is located. 

        """
        Filename = self.RefApi.GetModelFilename(IncludePath)
        return Filename
    
    def GetModelFilename(self) -> str:
        """Returns a string that represents the filepath of the current model 

        Returns:
            str: Returns a string that represents the filepath of the current model 
        """
        Filepath = self.RefApi.GetModelFilepath()
        return Filepath
    
    def GetModelIsLocked(self) -> bool:
        return self.RefApi.GetModelIsLocked()
    
    def GetPresentCoordSystem(self) -> str:
        return self.RefApi.GetPresentCoordSystem()
    
    def GetPresentUnits(self) -> None:
        val = self.RefApi.GetPresentUnits()        
        for unitName,unitValue in zip(eUnits._member_map_.keys(),eUnits._member_map_.values()):
            if val == unitValue.value: 
                 print(unitName)
                 break
    
    def GetPresentUnits_2(self, forceUnits:int, lengthUnits:int, temperatureUnits:int) -> list:
         val = self.RefApi.GetPresentUnits_2(forceUnits,lengthUnits,temperatureUnits)
         return val
    
    def GetProgramInfo(self, ProgramName: str, ProgramVersion : str, ProgramLevel : str) -> int:
         val = self.RefApi.GetProgramInfo(ProgramName,ProgramVersion,ProgramLevel)
         return val
    
    def GetProjectInfo(self, NumberItems : int, Item : str, Data : str) -> int:
         val = self.RefApi.GetProjectInfo(NumberItems,Item,Data)
         return val
    
    def GetVersion(self, Version: str, MyVersionNumber : float) -> int:
         val = self.RefApi.GetVersion(Version,MyVersionNumber)
         return val
    
    def InitializeNewModel(self, Units : int = eUnits.kN_m_C.value):
         val = self.RefApi.InitializeNewModel(Units)
         if val != 0:
            raise ApiReturnError(val)
         
    def SetMergeTol(self, MergeTol: float) -> None | ApiReturnError:
         val = self.RefApi.SetMergeTol(MergeTol)
         if val != 0:
            raise ApiReturnError(val)
    
    def SetModelIsLocked(self, Lockit : bool) -> None | ApiReturnError:
         val = self.RefApi.SetModelIsLocked(Lockit)
         if val != 0:
            raise ApiReturnError(val)
    
    def SetPresentUnits(self,Units : int) -> None | ApiReturnError:
         val = self.RefApi.SetPresentUnits(Units)
         if val != 0:
            raise ApiReturnError(val)
    
    def SetPresentUnits_2(self, forceUnits:int, lengthUnits:int, temperatureUnits:int) -> None | ApiReturnError:
         val = self.RefApi.SetPresentUnits_2(forceUnits,lengthUnits,temperatureUnits)
         if val != 0:
            raise ApiReturnError(val)
    
    def SetProjectInfo(self,Item : str, Data : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Item (str): _description_
            Data (str): _description_

        Raises:
            CustomCommentError: _description_
            CustomCommentError: _description_

        Returns:
            int: _description_
        """

        val = self.RefApi.SetProjectInfo(Item,Data)
        if val != 0:
            raise ApiReturnError(val)
    
    def TreeIsUpdateSuspended(self,IsSuspended : bool):
         val = self.RefApi.TreeIsUpdateSuspended(IsSuspended)
         if val != 0:
            raise ApiReturnError(val)
         pass
    
    def TreeResumeUpdateData(self):
         val = self.RefApi.TreeResumeUpdateData()
         if val != 0:
            raise ApiReturnError(val)
         pass
    
    def TreeSuspendUpdateData(self,updateAtResume):
         val = self.RefApi.TreeSuspendUpdateData(updateAtResume)
         if val != 0:
            raise ApiReturnError(val)
         pass
