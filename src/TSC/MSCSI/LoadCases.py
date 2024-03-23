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

    def SetBaseCase(self,Referance : object, Name : str, HyperStaticCase : str) -> None | ApiReturnError:
        """Sets the base case for the specified hyperstatic load case 

        Args:
            Referance (object): SapModel.LoadCases.HyperStatic
            Name (str): The name of an existing hyperstatic load case
            HyperStaticCase (str): The name of an existing static linear load case that is the base case for the specified hyperstatic load case 

        Raises:
            ApiReturnError: Return error code and message
        """
        result = Referance.SetBaseCase(Name,HyperStaticCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetCase(self,Referance : object, Name : str) -> None | ApiReturnError:
        """Initializes a hyperstatic load case. If this function is called for an existing load case, all items for the case are reset to their default value 

        Args:
            Referance (object): SapModel.LoadCases.HyperStatic
            Name (str): The name of an existing or new load case. If this is an existing case, that case is modified; otherwise, a new case is added

        Raises:
            ApiReturnError: Return error code and message

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetBaseCase(Name)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

class CaseModalEigen:

    def GetInitialCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list | ApiReturnError: _description_
        """
        InitialCase = str()
        retVal = 0
        result = [Name,InitialCase,retVal]
        result = Referance.GetParameters(Name,InitialCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetLoads(self, Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list | ApiReturnError: _description_
        """
        NumberLoads    = int()
        LoadType       = list([])
        LoadName       = list([])
        TargetPar      = list([])
        StaticCorrect  = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,TargetPar,StaticCorrect,retVal]
        result = Referance.GetParameters(Name,NumberLoads,LoadType,LoadName,TargetPar,StaticCorrect)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetNumberModes(self, Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list | ApiReturnError: _description_
        """
        MaxModes = int()
        MinModes = int()
        retVal = 0
        result = [Name,MaxModes,MinModes,retVal]
        result = Referance.GetParameters(Name,MaxModes,MinModes)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetParameters(self, Referance : object, Name : str) -> list | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): The name of an existing modal Eigen load case. 

        Raises:
            ApiReturnError: _description_

        Returns:
            list | ApiReturnError: _description_
        """
        EigenShiftFreq = float()
        EigenCutOff = float()
        EigenTol = float()
        AllowAutoFreqShift = int()
        retVal = 0
        result = [Name,EigenShiftFreq,EigenCutOff,EigenTol,AllowAutoFreqShift,retVal]
        result = Referance.GetParameters(Name,EigenShiftFreq,EigenCutOff,EigenTol,AllowAutoFreqShift)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
        
    def SetCase(self, Referance : object, Name : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetCase(Name)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetInitialCase(self, Referance : object, Name : str, InitialCase : str) -> None | ApiReturnError:
        """This function sets the initial condition for the specified load case. 

        Args:
            Referance (object): _description_
            Name (str): The name of an existing modal Eigen load case. 
            InitialCase (str): This is blank, None, or the name of an existing analysis case. This item specifies if the load case starts from zero initial conditions, that is, an unstressed state, or if it starts using the stiffness that occurs at the end of a nonlinear static or nonlinear direct integration time history load case. If the specified initial case is a nonlinear static or nonlinear direct integration time history load case, the stiffness at the end of that case is used. If the initial case is anything else, zero initial conditions are assumed. 


        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetInitialCase(Name,InitialCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetLoads(self, Referance : object, Name : str, NumberLoads : int) -> None | ApiReturnError:
        """This function sets the load data for the specified load case. 

        Args:
            Referance (object): SapModel.LoadCases.ModalEigen
            Name (str): The name of an existing modal Eigen load case. 
            NumberLoads (int): The number of loads assigned to the specified analysis case. 

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        retVal = 0
        LoadType      = list([])
        LoadName      = list([])
        TargetPar     = list([])
        StaticCorrect = list([])
        result = [Name,NumberLoads,LoadType,LoadName,TargetPar,StaticCorrect,retVal]
        result = Referance.SetLoads(Name,NumberLoads,LoadType,LoadName,TargetPar,StaticCorrect)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetNumberModes(self, Referance : object, Name : str, MaxModes : int, MinModes : int) -> None | ApiReturnError:
        """This function sets the number of modes requested for the specified load case. 

        Args:
            Referance (object): SapModel.LoadCases.ModalEigen
            Name (str): The name of an existing modal Eigen load case.
            MaxModes (int): The maximum number of modes requested. 
            MinModes (int): The minimum number of modes requested. 


        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetNumberModes(Name,MaxModes,MinModes)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetParameters(self, Referance : object, Name : str, EigenShiftFreq : float, EigenCutOff : float, EigenTol : float, AllowAutoFreqShift : int) -> None | ApiReturnError:
        """This function sets various parameters for the specified load case. 

        Args:
            Referance (object): SapModel.LoadCases.ModalEigen
            Name (str): The name of an existing modal Eigen load case. 
            EigenShiftFreq (float): The Eigenvalue shift frequency. [cyc/s] 
            EigenCutOff (float): The Eigencutoff frequency radius. [cyc/s] 
            EigenTol (float): The relative convergence tolerance for Eigenvalues. 
            AllowAutoFreqShift (int): This is either 0 or 1, indicating if automatic frequency shifting is allowed. 
                                        0 = Automatic frequency shifting is NOT allowed 
                                        1 = Automatic frequency shifting Is allowed 

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetParameters(Name,EigenShiftFreq,EigenCutOff,EigenTol,AllowAutoFreqShift)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

class CaseModalHistoryLinear:

    def GetLoads(self,Referance : object, Name : str) -> list | ApiReturnError:
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
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def SetCase(self,Referance : object, Name : str) -> None | ApiReturnError:
        result = Referance.SetCase(Name)
        if result != 0:
            raise ApiReturnError(result)

    def SetLoads(self,Referance : object, Name : str, NumberLoads : int) -> None | ApiReturnError:
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
        result = Referance.SetLoads(Name,NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

class CaseModalHistoryNonlinear:

    def GetLoads(self,Referance : object, Name : str) -> list | ApiReturnError:
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
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,Func,SF,Tf,At,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

class CaseModalRitz:
    
    def GetInitialCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        """Name:    The name of an existing modal Ritz load case.
InitialCase: This is blank, None, or the name of an existing analysis case. This item specifies if the load case starts from zero initial conditions, that is, an unstressed state, or if it starts using the stiffness that occurs at the end of a nonlinear static or nonlinear direct integration time history load case. 
If the specified initial case is a nonlinear static or nonlinear direct integration time history load case, the stiffness at the end of that case is used. If the initial case is anything else, zero initial conditions are assumed. 


        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            list | ApiReturnError: _description_
        """
        InitialCase = str()
        retVal = 0
        result = [Name,InitialCase,retVal]
        result = Referance.GetInitialCase(Name,InitialCase,retVal)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetLoads(self, Referance : object, Name : str):
        """Name:    The name of an existing modal Ritz load case. 
        NumberLoads: The number of loads assigned to the specified analysis case. 
        LoadType:   This is an array that includes Load, Accel or Link, indicating the type of each load assigned to the load case. 
        LoadName:   This is an array that includes the name of each load assigned to the load case. If the LoadType item is Load, this item is the name of a defined load pattern. If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load. If the LoadType item is Link, this item is not used. 
        RitzMaxCyc: This is an array that includes the maximum number of generation cycles to be performed for the specified ritz starting vector. A value of 0 means there is no limit on the number of cycles. 
        TargetPar:  This is an array that includes the target mass participation ratio. 

        Args:
            Referance (object): _description_
            Name (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            _type_: _description_
        """
        NumberLoads = int()
        LoadType    = list([])
        LoadName    = list([])
        RitzMaxCyc  = list([])
        TargetPar   = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,RitzMaxCyc,TargetPar,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,RitzMaxCyc,TargetPar)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetNumberModes(self, Referance : object, Name : str):
        MaxModes = int()
        MinModes = int()
        retVal = 0
        result = [Name,MaxModes,MinModes,retVal]
        result = Referance.GetNumberModes(Name,MaxModes,MinModes)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def SetCase(self, Referance : object, Name : str):
        result = Referance.SetCase(Name)
        if result != 0:
            raise ApiReturnError(result)

    def SetInitialCase(self, Referance : object, Name : str, InitialCase : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): SapModel.LoadCases.ModalRitz
            Name (str): The name of an existing modal Ritz load case.
            InitialCase (str): This is blank, None, or the name of an existing analysis case. This item specifies if the load case starts from zero initial conditions, that is, an unstressed state, or if it starts using the stiffness that occurs at the end of a nonlinear static or nonlinear direct integration time history load case. If the specified initial case is a nonlinear static or nonlinear direct integration time history load case, the stiffness at the end of that case is used. If the initial case is anything else, zero initial conditions are assumed.

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetInitialCase(Name,InitialCase)
        if result != 0:
            raise ApiReturnError(result[-1])

    def SetLoads(self, Referance : object, Name : str, NumberLoads : int):
        LoadType    = list([])
        LoadName    = list([])
        RitzMaxCyc  = list([])
        TargetPar   = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,RitzMaxCyc,TargetPar,retVal]
        result = Referance.SetLoads(Name,NumberLoads,LoadType,LoadName,RitzMaxCyc,TargetPar)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def SetNumberModes(self, Referance : object, Name : str, MaxModes : int, MinModes : int):
        result = Referance.SetNumberModes(Name,MaxModes,MinModes)
        if result != 0:
            raise ApiReturnError(result)

class CaseResponseSpectrum:

    def GetDampConstant(self,Referance : object, Name : str) -> list | ApiReturnError:
        retVal = 0
        Damp = float()
        result = [Name,Damp,retVal]
        result = Referance.GetDampConstant(Name,Damp)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDampInterpolated(self,Referance : object, Name : str):
        pass

    def GetDampOverrides(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetDampProportional(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetDampType(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetDiaphragmEccentricityOverride(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetDirComb(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetEccentricity(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetLoads(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetModalCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetModalComb(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def GetModalComb_1(self, Referance : object, Name : str) -> list | ApiReturnError:
        pass

    def SetCase(self, Referance : object, Name : str) -> None | ApiReturnError:
        pass

    def SetEccentricity(self, Referance : object, Name : str) -> None | ApiReturnError:
        pass

    def SetLoads(self, Referance : object, Name : str) -> None | ApiReturnError:
        pass

    def SetModalCase(self, Referance : object, Name : str) -> None | ApiReturnError:
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


def main()->None:
    from TSC.MSCSI.Connector import ConnectionEtabs
    from TSC.MSCSI.Model import SapModel

    ModelPath="C:\\CSi_ETABS_API_Example\\ETABS_API_Example.EDB"
    MySapModel,myETABSObject  = ConnectionEtabs(ModelPath)
    etabs                   = SapModel(RefApi=MySapModel)
    loadCase        = LoadCase(RefApi=MySapModel.LoadCases)
    if etabs.GetModelIsLocked():
        etabs.SetModelIsLocked(Lockit=False)
    # CaseModalRitz Testing
    loadCase.ModalRitz.SetCase(Referance=loadCase.RefApi.ModalRitz,Name='Ritz1')
    pass

if __name__ == "__main__":
    main()