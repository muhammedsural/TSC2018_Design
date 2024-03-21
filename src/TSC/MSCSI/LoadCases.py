from dataclasses import dataclass, field
from pandas import DataFrame
from TSC.MSCSI.Enums import eLoadCaseType, eLoadPatternType
from TSC.MSCSI.ErrorHandler import ApiReturnError

__all__ = ["LoadCase"]

class Buckling:
    pass

class CaseDirectHistoryLinear:

    def GetLoads(self,Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): SapModel.LoadCases.DirectHistoryLinear
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list: _description_
        """
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
        result = Referance.GetLoads(NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

class CaseDirectHistoryNonlinear:

    def GetLoads(self,Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): SapModel.LoadCases.DirectHistoryNonlinear
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list: _description_
        """
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
        result = Referance.GetLoads(NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

class CaseHyperStatic:
    
    def GetBaseCase(self,Referance : object, Name : str) -> list | ApiReturnError:
        """Retrieves the base case for the specified hyperstatic load case 

        Args:
            Referance (object): SapModel.LoadCases.HyperStatic
            Name (str): The name of an existing hyperstatic load case 

        Raises:
            ApiReturnError: Return error code and message

        Returns:
            list | ApiReturnError: _description_
        """
        HyperStaticCase = str() # The name of an existing static linear load case that is the base case for the specified hyperstatic load case 
        retVal = 0
        result = [Name,HyperStaticCase,retVal]
        result = Referance.GetBaseCase(Name,HyperStaticCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def SetBaseCase(self,Referance : object, Name : str):
        pass

    def SetCase(self,Referance : object, Name : str):
        pass

class CaseModalEigen:

    def GetInitialCase(self):
        pass

    def GetLoads(self):
        pass

    def GetNumberModes(self):
        pass

    def GetParameters(self):
        pass

    def SetCase(self):
        pass

    def SetInitialCase(self):
        pass

    def SetLoads(self):
        pass

    def SetNumberModes(self):
        pass

    def SetParameters(self):
        pass

class CaseModalHistoryLinear:

    def GetLoads(self):
        pass

    def SetCase(self):
        pass

    def SetLoads(self):
        pass

class CaseModalHistoryNonlinear:
    def GetLoads(self):
        pass

class CaseModalRitz:
    
    def GetInitialCase(self):
        pass

    def GetLoads(self):
        pass

    def GetNumberModes(self):
        pass

    def SetCase(self):
        pass

    def SetInitialCase(self):
        pass

    def SetLoads(self):
        pass

    def SetNumberModes(self):
        pass

class CaseResponseSpectrum:

    def GetDampConstant(self):
        pass

    def GetDampInterpolated(self):
        pass

    def GetDampOverrides(self):
        pass

    def GetDampProportional(self):
        pass

    def GetDampType(self):
        pass

    def GetDiaphragmEccentricityOverride(self):
        pass

    def GetDirComb(self):
        pass

    def GetEccentricity(self):
        pass

    def GetLoads(self):
        pass

    def GetModalCase(self):
        pass

    def GetModalComb(self):
        pass

    def GetModalComb_1(self):
        pass

    def SetCase(self):
        pass

    def SetEccentricity(self):
        pass

    def SetLoads(self):
        pass

    def SetModalCase(self):
        pass

class CaseStaticLinear:

    def GetInitialCase(self):
        pass

    def GetLoads(self):
        pass
    def SetCase(self):
        pass
 
    def SetInitialCase(self):
        pass
 
    def SetLoads(self):
        pass

class CaseStaticNonlinear:

    def GetGeometricNonlinearity(self):
        pass

    def GetHingeUnloading(self):
        pass
    
    def GetInitialCase(self):
        pass
    
    def GetLoadApplication(self):
        pass
    
    def GetLoads(self):
        pass
    
    def GetMassSource(self):
        pass
    
    def GetModalCase(self):
        pass
    
    def GetResultsSaved(self):
        pass
    
    def GetSolControlParameters(self):
        pass
    
    def GetTargetForceParameters(self):
        pass
    
    def SetCase(self):
        pass
    
    def SetGeometricNonlinearity(self):
        pass
    
    def SetHingeUnloading(self):
        pass
    
    def SetInitialCase(self):
        pass
    
    def SetLoadApplication(self):
        pass
    
    def SetLoads(self):
        pass
    
    def SetMassSource(self):
        pass
    
    def SetModalCase(self):
        pass
    
    def SetResultsSaved(self):
        pass
    
    def SetSolControlParameters(self):
        pass
    
    def SetTargetForceParameters(self):
        pass

class CaseStaticNonlinearStaged:

    def GetGeometricNonlinearity(self):
        pass

    def GetHingeUnloading(self):
        pass
    
    def GetInitialCase(self):
        pass
    
    def GetMassSource(self):
        pass
    
    def GetMaterialNonlinearity(self):
        pass
    
    def GetResultsSaved(self):
        pass
    
    def GetSolControlParameters(self):
        pass
    
    def GetStageData(self):
        pass
    
    def GetStageData_1(self):
        pass
    
    def GetStageData_2(self):
        pass
     
    def GetStageDefinitions(self):
        pass
      
    def GetStageDefinitions_1(self):
        pass
    
    def GetStageDefinitions_2(self):
        pass
    
    def GetTargetForceParameters(self):
        pass
    
    def SetCase(self):
        pass
    
    def SetGeometricNonlinearity(self):
        pass
    
    def SetHingeUnloading(self):
        pass
    
    def SetInitialCase(self):
        pass
    
    def SetMassSource(self):
        pass
    
    def SetMaterialNonlinearity(self):
        pass
    
    def SetResultsSaved(self):
        pass
    
    def SetSolControlParameters(self):
        pass
    
    def SetStageData(self):
        pass
    
    def SetStageData_1(self):
        pass
    
    def SetStageData_2(self):
        pass
    
    def SetStageDefinitions(self):
        pass
    
    def SetStageDefinitions_1(self):
        pass
    
    def SetStageDefinitions_2(self):
        pass
    
    def SetTargetForceParameters(self):
        pass
    


@dataclass
class LoadCase:
    RefApi                :  object
    buckling              :  Buckling                   = field(default_factory=Buckling)
    DirHistLinear         :  CaseDirectHistoryLinear    = field(default_factory=CaseDirectHistoryLinear)  
    DirHistNonlinear      :  CaseDirectHistoryNonlinear = field(default_factory=CaseDirectHistoryNonlinear)
    HyperStatic           :  CaseHyperStatic            = field(default_factory=CaseHyperStatic)  
    ModalEigen            :  CaseModalEigen             = field(default_factory=CaseModalEigen)
    ModalRitz             :  CaseModalRitz              = field(default_factory=CaseModalRitz)
    ModHistLinear         :  CaseModalHistoryLinear     = field(default_factory=CaseModalHistoryLinear)
    ModHistNonlinear      :  CaseModalHistoryNonlinear  = field(default_factory=CaseModalHistoryNonlinear)
    ResponseSpectrum      :  CaseResponseSpectrum       = field(default_factory=CaseResponseSpectrum)
    StaticLinear          :  CaseStaticLinear           = field(default_factory=CaseStaticLinear)
    StaticNonlinear       :  CaseStaticNonlinear        = field(default_factory=CaseStaticNonlinear)
    StaticNonlinearStaged :  CaseStaticNonlinearStaged  = field(default_factory=CaseStaticNonlinearStaged)

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


