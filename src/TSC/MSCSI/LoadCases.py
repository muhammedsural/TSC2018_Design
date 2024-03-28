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
        DampType    = int()
        NumberItems = int() 
        Time        = list([])
        Damp        = list([]) 
        retVal = 0
        result = [Name,DampType,NumberItems,Time,Damp,retVal]
        result = Referance.GetDampInterpolated(Name,DampType,NumberItems,Time,Damp)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDampOverrides(self, Referance : object, Name : str) -> list | ApiReturnError:
        NumberItems = int()
        Mode = list([])
        Damp        = list([]) 
        retVal = 0
        result = [Name,NumberItems,Mode,Damp,retVal]
        result = Referance.GetDampOverrides(Name,NumberItems,Mode,Damp)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDampProportional(self, Referance : object, Name : str) -> list | ApiReturnError:
        DampType = int()
        DampA    = float() 
        DampB    = float()
        DampF1   = float()
        DampF2   = float()
        DampD1   = float()
        DampD2   = float()
        retVal = 0
        result = [Name,DampType,DampA,DampB,DampF1,DampF2,DampD1,DampD2,retVal]
        result = Referance.GetDampProportional(Name,DampType,DampA,DampB,DampF1,DampF2,DampD1,DampD2)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDampType(self, Referance : object, Name : str) -> list | ApiReturnError:
        DampType = int()
        retVal = 0
        result = [Name,DampType,retVal]
        result = Referance.GetDampType(Name,DampType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDiaphragmEccentricityOverride(self, Referance : object, Name : str) -> list | ApiReturnError:
        Num = int()
        Diaph = list([])
        Eccen = list([])
        retVal = 0
        result = [Name,Num,Diaph,Eccen,retVal]
        result = Referance.GetDiaphragmEccentricityOverride(Name,Num,Diaph,Eccen)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetDirComb(self, Referance : object, Name : str) -> list | ApiReturnError:
        MyType = int()
        SF = float()
        retVal = 0
        result = [Name,MyType,SF,retVal]
        result = Referance.GetDirComb(Name,MyType,SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetEccentricity(self, Referance : object, Name : str) -> list | ApiReturnError:
        Eccen = float()
        retVal = 0
        result = [Name,Eccen,retVal]
        result = Referance.GetEccentricity(Name,Eccen)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetLoads(self, Referance : object, Name : str) -> list | ApiReturnError:
        NumberLoads = int()
        LoadName = list([])
        Func = list([])
        SF = list([])
        CSys = list([])
        Ang = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadName,Func,SF,CSys,Ang,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadName,Func,SF,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetModalCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        ModalCase = str()
        retVal = 0
        result = [Name,ModalCase,retVal]
        result = Referance.GetModalCase(Name,ModalCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetModalComb(self, Referance : object, Name : str) -> list | ApiReturnError:
        MyType = int()
        F1 = float()
        F2 = float()
        Td = float()
        retVal = 0
        result = [Name,MyType,F1,F2,Td,retVal]
        result = Referance.GetModalComb(Name,MyType,F1,F2,Td)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetModalComb_1(self, Referance : object, Name : str) -> list | ApiReturnError:
        MyType = int()
        F1 = float()
        F2 = float()
        PeriodicRigidCombType = int()
        Td = float()
        retVal = 0
        result = [Name,MyType,F1,F2,PeriodicRigidCombType,Td,retVal]
        result = Referance.GetModalComb_1(Name,MyType,F1,F2,PeriodicRigidCombType,Td)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def SetCase(self, Referance : object, Name : str) -> None | ApiReturnError:
        result = Referance.SetCase(Name)
        if result != 0:
            raise ApiReturnError(result)

    def SetEccentricity(self, Referance : object, Name : str, Eccen : float) -> None | ApiReturnError:
        result = Referance.SetEccentricity(Name, Eccen)
        if result != 0:
            raise ApiReturnError(result)

    def SetLoads(self, Referance : object, Name : str, NumberLoads : int) -> None | ApiReturnError:
        LoadName = list([])
        Func = list([])
        SF = list([])
        CSys = list([])
        Ang = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadName,Func,SF,CSys,Ang,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadName,Func,SF,CSys,Ang)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

    def SetModalCase(self, Referance : object, Name : str, ModalCase : str) -> None | ApiReturnError:
        result = Referance.SetModalCase(Name, ModalCase)
        if result != 0:
            raise ApiReturnError(result)

class CaseStaticLinear:

    def GetInitialCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        InitialCase = str()
        retVal = 0
        result = [Name,InitialCase,retVal]
        result = Referance.GetInitialCase(Name,InitialCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetLoads(self, Referance : object, Name : str) -> list | ApiReturnError:
        NumberLoads = int()
        LoadType = list([])
        LoadName = list([])
        SF = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,SF,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def SetCase(self, Referance : object, Name : str) -> None | ApiReturnError:
        result = Referance.SetCase(Name)
        if result != 0:
            raise ApiReturnError(result)
 
    def SetInitialCase(self, Referance : object, Name : str, InitialCase : str) -> None | ApiReturnError:
        result = Referance.SetInitialCase(Name,InitialCase)
        if result != 0:
            raise ApiReturnError(result)
 
    def SetLoads(self, Referance : object, Name : str, NumberLoads : int) -> None | ApiReturnError:
        LoadType = list([])
        LoadName = list([])
        SF = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,SF,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])

class CaseStaticNonlinear:

    def GetGeometricNonlinearity(self, Referance : object, Name : str) -> list | ApiReturnError:
        NLGeomType = int()
        retVal = 0
        result = [Name,NLGeomType,retVal]
        result = Referance.GetGeometricNonlinearity(Name,NLGeomType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetHingeUnloading(self, Referance : object, Name : str) -> list | ApiReturnError:
        UnloadType = int()
        retVal = 0
        result = [Name,UnloadType,retVal]
        result = Referance.GetHingeUnloading(Name,UnloadType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetInitialCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        InitialCase = str()
        retVal = 0
        result = [Name,InitialCase,retVal]
        result = Referance.GetInitialCase(Name,InitialCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetLoadApplication(self, Referance : object, Name : str) -> list | ApiReturnError:
        LoadControl = int()
        DispType    = int()
        Displ       = float()
        Monitor     = int()
        DOF         = int()
        PointName   = str()
        GDispl      = str()
        retVal = 0
        result = [Name,LoadControl,DispType,Displ,Monitor,DOF,PointName,GDispl,retVal]
        result = Referance.GetLoadApplication(Name,LoadControl,DispType,Displ,Monitor,DOF,PointName,GDispl)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetLoads(self, Referance : object, Name : str) -> list | ApiReturnError:
        NumberLoads = int() 
        LoadType    = list([])
        LoadName    = list([]) 
        SF          = list([])
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,SF,retVal]
        result = Referance.GetLoads(Name,NumberLoads,LoadType,LoadName,SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetMassSource(self, Referance : object, Name : str) -> list | ApiReturnError:
        mSource = str()
        retVal = 0
        result = [Name,mSource,retVal]
        result = Referance.GetMassSource(Name,mSource)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetModalCase(self, Referance : object, Name : str) -> list | ApiReturnError:
        ModalCase = str()
        retVal = 0
        result = [Name,ModalCase,retVal]
        result = Referance.GetModalCase(Name,ModalCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetResultsSaved(self, Referance : object, Name : str) -> list | ApiReturnError:
        SaveMultipleSteps = bool()
        MinSavedStates = int()
        MaxSavedStates = int()
        PositiveOnly = bool()
        retVal = 0
        result = [Name,SaveMultipleSteps,MinSavedStates,MaxSavedStates,PositiveOnly,retVal]
        result = Referance.GetResultsSaved(Name,SaveMultipleSteps,MinSavedStates,MaxSavedStates,PositiveOnly)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetSolControlParameters(self, Referance : object, Name : str) -> list | ApiReturnError:
        MaxTotalSteps       = int()
        MaxFailedSubSteps   = int()
        MaxIterCS   = int()
        MaxIterNR   = int()
        TolConvD   = float()
        UseEventStepping   = bool()
        TolEventD    = float()
        MaxLineSearchPerIter   = int()
        TolLineSearch    = float()
        LineSearchStepFact    = float()
        retVal = 0
        result = [Name,MaxTotalSteps,MaxFailedSubSteps,MaxIterCS,MaxIterNR,TolConvD,UseEventStepping,TolEventD,MaxLineSearchPerIter,TolLineSearch,LineSearchStepFact,retVal]
        result = Referance.GetSolControlParameters(Name,MaxTotalSteps,MaxFailedSubSteps,MaxIterCS,MaxIterNR,TolConvD,UseEventStepping,TolEventD,MaxLineSearchPerIter,TolLineSearch,LineSearchStepFact)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetTargetForceParameters(self, Referance : object, Name : str) -> list | ApiReturnError:
        TolConvF = float()
        MaxIter = int()
        AccelFact = float()
        NoStop = bool()
        retVal = 0
        result = [Name,TolConvF,MaxIter,AccelFact,NoStop,retVal]
        result = Referance.GetTargetForceParameters(Name,TolConvF,MaxIter,AccelFact,NoStop)
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
        if result != 0:
            raise ApiReturnError(result)
    
    def SetGeometricNonlinearity(self,Referance : object, Name : str, NLGeomType : int) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_
            NLGeomType (int): 
                                0 : None
                                1 : P-Delta
                                2 : P-Delta + Large Disp


        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetGeometricNonlinearity(Name,NLGeomType)
        if result != 0:
            raise ApiReturnError(result)
    
    def SetHingeUnloading(self, Referance : object, Name : str, UnloadType : int) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_
            UnloadType (int): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetHingeUnloading(Name,UnloadType)
        if result != 0:
            raise ApiReturnError(result)
    
    def SetInitialCase(self, Referance : object, Name : str, InitialCase : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_
            InitialCase (str): Mevcut nonlinearcase ismi verilirse verilen nonlinearcase öncül olarak çözülür . 'None' girişi yapılırsa direk bu case çözülür.

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetInitialCase(Name,InitialCase)
        if result != 0:
            raise ApiReturnError(result)
    
    def SetLoadApplication(self, Referance : object, Name : str, LoadControl : int, DispType : int, Monitor : int, DOF : int, PointName : str, GDispl : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_
            LoadControl (int): _description_
            DispType (int): _description_
            Monitor (int): _description_
            DOF (int): _description_
            PointName (str): _description_
            GDispl (str): _description_

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetLoadApplication(Name,LoadControl,DispType,Monitor,DOF,PointName,GDispl)
        if result != 0:
            raise ApiReturnError(result)
    
    def SetLoads(self, Referance : object, Name : str, NumberLoads : int, LoadType : [str], LoadName : [str], SF : [float]) -> None | ApiReturnError: # type: ignore
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): _description_
            NumberLoads (int): _description_
            LoadType (list):  'Load','Acceleration','Mode'
            LoadName (list): 'Load' için LoadPattern nameler,
                                'Acceleration' için DOF isimleri
                                'Mode' için mode isimleri
            SF (list): Scale faktörler

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        retVal = 0
        result = [Name,NumberLoads,LoadType,LoadName,SF,retVal]        
        result = Referance.SetLoads(Name,NumberLoads,LoadType,LoadName,SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print(f"{__class__.SetLoads.__name__} Operation completed...")
    
    def SetMassSource(self, Referance : object, Name : str, mSource : str) -> None | ApiReturnError:
        """_summary_

        Args:
            Referance (object): _description_
            Name (str): Exist load case name
            mSource (str): Exist mass source name

        Raises:
            ApiReturnError: _description_

        Returns:
            None | ApiReturnError: _description_
        """
        result = Referance.SetMassSource(Name,mSource)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print(f"{__class__.SetMassSource.__name__} Operation completed...")
    
    def SetModalCase(self, Referance : object, Name : str, ModalCase : str) -> None | ApiReturnError:
        result = Referance.SetModalCase(Name,ModalCase)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print(f"{__class__.SetModalCase.__name__} Operation completed...")
    
    def SetResultsSaved(self, Referance : object, Name : str, SaveMultipleSteps : bool, MinSavedStates : int = 10, MaxSavedStates : int = 100, PositiveOnly : bool = True) -> None | ApiReturnError:
        result = Referance.SetResultsSaved(Name,SaveMultipleSteps,MinSavedStates,MaxSavedStates,PositiveOnly)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print(f"{__class__.SetResultsSaved.__name__} Operation completed...")
    
    def SetSolControlParameters(self, Referance : object, Name : str, MaxTotalSteps : int, MaxFailedSubSteps : int, MaxIterCS : int, MaxIterNR : int, TolConvD : float, UseEventStepping : bool, TolEventD : float, MaxLineSearchPerIter : int, TolLineSearch : float, LineSearchStepFact : float) -> None | ApiReturnError:
        result = Referance.SetSolControlParameters(Name,
                                                   MaxTotalSteps,
                                                   MaxFailedSubSteps,
                                                   MaxIterCS,
                                                   MaxIterNR,
                                                   TolConvD,
                                                   UseEventStepping,
                                                   TolEventD,
                                                   MaxLineSearchPerIter,
                                                   TolLineSearch,
                                                   LineSearchStepFact)
        if result != 0:
            raise ApiReturnError(result)
    
    def SetTargetForceParameters(self, Referance : object, Name : str, TolConvF : float, MaxIter : int, AccelFact : float, NoStop : bool) -> None | ApiReturnError:
        result = Referance.SetTargetForceParameters(Name,TolConvF,MaxIter,AccelFact,NoStop)
        if result != 0:
            raise ApiReturnError(result)

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


# def main()->None:
#     from TSC.MSCSI.Connector import ConnectionEtabs
#     from TSC.MSCSI.Model import SapModel

#     ModelPath="C:\\CSi_ETABS_API_Example\\ETABS_API_Example.EDB"
#     MySapModel,myETABSObject  = ConnectionEtabs(ModelPath)
#     etabs                   = SapModel(RefApi=MySapModel)
#     loadCase        = LoadCase(RefApi=MySapModel.LoadCases)
#     if etabs.GetModelIsLocked():
#         etabs.SetModelIsLocked(Lockit=False)
#     # CaseModalRitz Testing
#     loadCase.ModalRitz.SetCase(Referance=loadCase.RefApi.ModalRitz,Name='Ritz1')

#     # CaseStaticNonlinear Testing
#     loadCase.StaticNonlinear.SetCase(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase')
#     # loadCase.StaticNonlinear.SetMassSource(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',mSource='aaa')
#     # loadCase.StaticNonlinear.SetInitialCase(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',InitialCase='None')
#     loadCase.StaticNonlinear.SetLoads(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',NumberLoads=2)
#     loadCase.StaticNonlinear.SetModalCase(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',ModalCase='None')
#     loadCase.StaticNonlinear.SetGeometricNonlinearity(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',NLGeomType=1)
#     loadCase.StaticNonlinear.SetLoadApplication(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',LoadControl=1,DispType=1,Monitor=1,DOF=1,PointName='None',GDispl='None')
#     loadCase.StaticNonlinear.SetResultsSaved(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase',SaveMultipleSteps=True,MinSavedStates=10,MaxSavedStates=100,PositiveOnly=True)
#     loadCase.StaticNonlinear.SetSolControlParameters(Referance=loadCase.RefApi.StaticNonlinear,Name='TestNonlinearCase', MaxTotalSteps=10,MaxFailedSubSteps=2,MaxIterCS=1,MaxIterNR=1,TolConvD=.1,UseEventStepping=True,TolEventD=1.2,MaxLineSearchPerIter=1,TolLineSearch=.1,LineSearchStepFact=1)


# if __name__ == "__main__":
#     main()