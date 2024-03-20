from dataclasses import dataclass
from typing import Any
from TSC.MSCSI.ErrorHandler import ApiReturnError


@dataclass
class CaseStaticNonlinear:
    # con.RefApi.LoadCases.StaticNonlinear
    RefApi : object

    def GetGeometricNonlinearity(self,Name : str) -> Any | ApiReturnError :
        NLGeomType = int()
        retVal = 0
        result = [Name, NLGeomType, retVal]
        result = self.RefApi.GetGeometricNonlinearity(Name, NLGeomType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetGeometricNonlinearity(self,*args) -> None | ApiReturnError :
        """Sets the geometric nonlinearity option for the specified load case.
        Args
            Name(str) : The name of an existing static nonlinear load case. 
            NLGeomType(int) : Type of eLoadCaseType.NonlinearStatic.value
        """  
        result = self.RefApi.SetGeometricNonlinearity(*args)
        if result != 0:
            ApiReturnError(result)

    def GetHingeUnloading(self,Name : str) -> Any | ApiReturnError  :
        UnloadType = int()
        retVal = 0
        result = [Name, UnloadType, retVal]
        result = self.RefApi.GetHingeUnloading(Name, UnloadType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetHingeUnloading(self,*args) -> None | ApiReturnError  :
        """
        Args :
            Name(str)
            UnloadType(int)
        """
        result = self.RefApi.SetHingeUnloading(*args)
        if result != 0:
            ApiReturnError(result)

    def GetInitialCase(self,Name : str) -> Any | ApiReturnError  :
        InitialCase = str()
        retVal = 0
        result = [Name, InitialCase, retVal]
        result = self.RefApi.GetInitialCase(Name, InitialCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetInitialCase(self,*args) -> None | ApiReturnError  :
        """
        Args :
            Name(str)
            InitialCase(str)
        """
        result = self.RefApi.SetHingeUnloading(*args)
        if result != 0:
            ApiReturnError(result)

    def GetLoadApplication(self,Name : str) -> Any | ApiReturnError  :
        LoadControl = int()
        DispType    = int()
        Displ       = float()
        Monitor     = int()
        DOF         = int()
        PointName   = str()
        GDispl      = str()
        retVal      = 0
        result = [Name, LoadControl, DispType, Displ, Monitor, DOF, PointName, GDispl, retVal]
        result = self.RefApi.GetLoadApplication(Name, LoadControl, DispType, Displ, Monitor, DOF, PointName, GDispl)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetLoadApplication(self,*args) -> None | ApiReturnError  :
        """
        Args :
            Name(str)
            LoadControl(str)
            DispType(int)
            Displ(float)
            Monitor(int)
            DOF(int)
            PointName(str)
            GDispl(str)
        """
        result = self.RefApi.SetLoadApplication(*args)
        if result != 0:
            ApiReturnError(result)

    def GetLoads(self,Name : str) -> Any | ApiReturnError  :
        """Retrieves the load data for the specified load case"""  
        NumberLoads = int()
        LoadType    = list([])
        LoadName    = list([])
        SF          = float()
        
        retVal      = 0
        result = [Name, NumberLoads, LoadType, LoadName, SF, retVal]
        result = self.RefApi.GetLoads(Name, NumberLoads, LoadType, LoadName, SF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetLoads(self,*args) -> None | ApiReturnError  :
        """Sets the load data for the specified analysis case.
        Args :
            Name(str)         : The name of an existing static nonlinear load case. 
            NumberLoads(int)  : The number of loads assigned to the specified analysis case. 
            LoadType(str)     : This is an array that includes either Load or Accel, indicating the type of each load assigned to the load case. 
            LoadName(str)     : This is an array that includes the name of each load assigned to the load case. 
                                If the LoadType item is Load, this item is the name of a defined load pattern. 
                                If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load. 
            SF(float)         : This is an array that includes the scale factor of each load assigned to the load case. [L/s^2] for Accel UX UY and UZ; otherwise unitless 
        """  
        result = self.RefApi.SetLoads(*args)
        if result != 0:
            ApiReturnError(result)

    def GetMassSource(self,Name : str) -> Any | ApiReturnError  :
        mSource = str()
        retVal = 0
        result = [Name, mSource, retVal]
        result = self.RefApi.GetMassSource(Name, mSource)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetMassSource(self,*args) -> None | ApiReturnError  :
        """ 
        Args :
            Name(str)     :
            mSource(str)  :

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetMassSource(*args)
        if result != 0:
            ApiReturnError(result)

    def GetModalCase(self,Name : str) -> Any | ApiReturnError  :
        ModalCase = str()
        retVal = 0
        result = [Name, ModalCase, retVal]
        result = self.RefApi.GetModalCase(Name, ModalCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetModalCase(self,*args) -> None | ApiReturnError  :
        """
        Args :
            Name(str)       :
            ModalCase(str)  :

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetModalCase(*args)
        if result != 0:
            ApiReturnError(result)

    def GetResultsSaved(self,Name : str) -> Any | ApiReturnError  :
        SaveMultipleSteps   = bool()
        MinSavedStates      = int()
        MaxSavedStates      = int()
        PositiveOnly        = bool()
        retVal = 0
        result = [Name, SaveMultipleSteps, MinSavedStates, MaxSavedStates, PositiveOnly, retVal]
        result = self.RefApi.GetResultsSaved(Name, SaveMultipleSteps, MinSavedStates, MaxSavedStates, PositiveOnly)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetResultsSaved(self,*args) -> None | ApiReturnError  :
        """
        Args :
            Name(str)                :
            SaveMultipleSteps(bool)  :
            MinSavedStates (int)     : it's optional. Default to value = 10
            MaxSavedStates  (int)    : it's optional. Default to value = 100
            PositiveOnly   (bool)    : it's optional. Default to value = True

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetResultsSaved(*args)
        if result != 0:
            ApiReturnError(result)

    def GetSolControlParameters(self,Name : str) -> Any | ApiReturnError  :
        MaxTotalSteps           = int()
        MaxFailedSubSteps       = int()
        MaxIterCS               = int()
        MaxIterNR               = int()
        TolConvD                = float()
        UseEventStepping        = bool()
        TolEventD               = float()
        MaxLineSearchPerIter    = int()
        TolLineSearch           = float()
        LineSearchStepFact      = float()
        retVal = 0
        result = [Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact, retVal]
        result = self.RefApi.GetSolControlParameters(Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact,)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetSolControlParameters(self,*args) -> None | ApiReturnError  :
        """_summary_

        Args :
            Name(str)                :
            MaxTotalSteps    (int)   :
            MaxFailedSubSteps(int)   :
            MaxIterCS        (int)   :
            MaxIterNR        (int)   :
            TolConvD         (float) :
            UseEventStepping (bool)  :
            TolEventD        (float) :
            MaxLineSearchPerIter (int)   :
            TolLineSearch     (float) :
            LineSearchStepFact (float) :

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetSolControlParameters(*args)
        if result != 0:
            ApiReturnError(result)

    def GetTargetForceParameters(self,Name : str) -> Any | ApiReturnError  :
        TolConvF       = float()
        MaxIter        = int()
        AccelFact      = float()
        NoStop         = bool()
        retVal = 0
        result = [Name, TolConvF, MaxIter, AccelFact, NoStop, retVal]
        result = self.RefApi.GetSolControlParameters(Name, TolConvF, MaxIter, AccelFact, NoStop)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    def SetTargetForceParameters(self,*args) -> None | ApiReturnError  :
        """_summary_
        
        Args :
            Name(str)        :
            TolConvF (float) : 
            MaxIter  (int)   : 
            AccelFact(float) : 
            NoStop   (bool)  : 

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetTargetForceParameters(*args)
        if result != 0:
            ApiReturnError(result)
    
    def SetCase(self,Name : str) -> None | ApiReturnError  :
        """Initializes a static nonlinear load case.
        Args
            Name(str) : The name of an existing or new load case. If this is an existing case, that case is modified; otherwise, a new case is added. 
        """
        result = self.RefApi.SetCase(Name)
        if result != 0:
            raise ApiReturnError(result[-1])





