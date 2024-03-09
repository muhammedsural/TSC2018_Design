from dataclasses import dataclass
from pandas import DataFrame
from MSCSI.Enums import eLoadCaseType, eLoadPatternType
from MSCSI.ErrorHandler import ApiReturnError

@dataclass
class LoadCase:
    RefApi : object
    # Buckling              :  Buckling  
    # DirHistLinear         :  DirHistLinear  
    # DirHistNonlinear      :  DirHistNonlinear  
    # HyperStatic           :  HyperStatic  
    # ModalEigen            :  ModalEigen  
    # ModalRitz             :  ModalRitz  
    # ModHistLinear         :  ModHistLinear  
    # ModHistNonlinear      :  ModHistNonlinear  
    # ResponseSpectrum      :  ResponseSpectrum  
    # StaticLinear          :  StaticLinear  
    # StaticNonlinear       :  StaticNonlinear  
    # StaticNonlinearStaged :  StaticNonlinearStaged 

    def ChangeName(self,Name : str, NewName : str):
        result = self.RefApi.ChangeName(Name,NewName)   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def Count(self,CaseType : eLoadCaseType):
        result = self.RefApi.Count(CaseType)   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")   

    def Delete(self, Name : str):
        """Deletes the specified load case.
        """
        result = self.RefApi.Delete(Name)   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")        

    def GetNameList(self):
        """Retrieves the names of all defined load cases of the specified type. 

        Parameters
            NumberNames(int) : The number of load case names retrieved by the program. 
            MyName(list(str))      : This is a one-dimensional array of area object names. The MyName array is created as a dynamic, zero-based, array by the API user: 
                            The array is dimensioned to (NumberNames – 1) inside the ETABS program, filled with the names, and returned to the API user. 

            CaseType (Optional): eLoadCaseType
        """
        retVal = 0
        NumberNames = int()
        MyName      = list([])
        result = [NumberNames,MyName,retVal]
        result = self.RefApi.GetNameList(NumberNames,MyName)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        caseList = DataFrame([result[1]]).T
        return caseList

    def GetTypeOAPI  (self):
        pass

    def GetTypeOAPI_1(self):
        """Retrieves the case type, design type, and auto flag for the specified load case 
        """
        pass    

    def SetDesignType(self,Name : str,DesignTypeOption : int,DesignType : eLoadPatternType):
        result = self.RefApi.Delete(Name,DesignTypeOption,DesignType)   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")      


class CaseDirectHistoryLinear(LoadCase):
    def __init_subclass__(cls,RefApi) -> None:
        return super().__init_subclass__(RefApi)
    
    def GetLoads(self,Name : str):
        NumberLoads = int()
        LoadType    = list([])
        LoadName    = list([])
        Func        = list([])
        SF          = list([])
        Tf          = list([])
        At          = list([])
        CSys        = list([])
        Ang         = list([])
        retVal = 0

        result = [Name,NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang,retVal]
        result = self.RefApi.DirectHistoryLinear.GetLoads(NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

class CaseDirectHistoryNonlinear(LoadCase):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__(cls.RefApi)
    
    def GetLoads(self,Name : str):
        NumberLoads = int()
        LoadType    = list([])
        LoadName    = list([])
        Func        = list([])
        SF          = list([])
        Tf          = list([])
        At          = list([])
        CSys        = list([])
        Ang         = list([])
        retVal = 0

        result = [Name,NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang,retVal]
        result = self.RefApi.DirectHistoryNonlinear.GetLoads(NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])