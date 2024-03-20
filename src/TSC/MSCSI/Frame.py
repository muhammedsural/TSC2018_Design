from dataclasses import dataclass
from TSC.MSCSI.Enums import eCNameType, eComboType
from TSC.MSCSI.ErrorHandler import ApiReturnError

@dataclass
class Frame:
    RefApi : object
    def AddByCoord              (self):
        pass
    def AddByPoint              (self):
        pass
    def ChangeName              (self):
        pass

    def Count                   (self):
        pass

    def Delete                  (self):
        pass
    def DeleteLateralBracing    (self):
        pass

    def DeleteLoadDistributed   (self):
        pass
    def DeleteLoadPoint         (self):
        pass
    def DeleteLoadTemperature   (self):
        pass

    def DeleteMass              (self):
        pass

    def DeleteModifiers         (self):
        pass

    def DeleteSpring            (self):
        pass

    def GetAllFrames            (self):
        pass
    def GetColumnSpliceOverwrite(self):
        pass
    def GetCurved_2             (self):
        pass
    def GetDesignOrientation    (self):
        pass
    def GetDesignProcedure      (self):
        pass
    def GetElm                  (self):
        pass

    def GetEndLengthOffset      (self):
        pass
    def GetGroupAssign          (self):
        pass
    def GetGUID                 (self):
        pass
    def GetHingeAssigns(self, Name :str) -> list | ApiReturnError:
        """DEPRECATED Retrieves frame object hinge assignments. 

        Args:
            Name (str)          : The name of an existing frame object. 
            NumberHinges (int)  : The number of frame hinges assigned to the frame object. 
            HingeNum list(int)  : An array of size NumberHinges. This is the hinge identification number.
            Prop     list(str)  : An array of size NumberHinges. This is the name of the property of the hinge. 
            MyType   list(int)  : An array of size NumberHinges. This is a numeric value from 1 to 14 that specifies the type of the hinge. 
                                    1 - P
                                    2 - V2
                                    3 - V3
                                    4 - T
                                    5 - M2
                                    6 - M3
                                    7 - Interacting P-M2
                                    8 - Interacting P-M3
                                    9 - Interacting M2-M3
                                    10- Interacting P-M2-M3
                                    11- Fiber P-M2-M3
                                    12- Fiber P-M3
                                    13- Parametric Concrete P-M2-M3
                                    14- Parametric Steel P-M2-M3
            Behavior list(int)  : An array of size NumberHinges. This is a numeric value from 1 to 2 that specifies behavior of the hinge. 
                                    1- Force-controlled
                                    2- Deformation-controlled
            Source   list(str)  : An array of size NumberHinges. This is the name of the assigned hinge property, or "Auto" if an auto-generated hinge. 
            RD       list(float): An array of size NumberHinges. This is the distance of the hinge from the end of the i-end offset, as a ratio to the clear length of the frame object

        Returns:
            list | ApiReturnError: Hinge properties list
        """
        NumberHinges= int()
        HingeNum= list([])
        Prop    = list([])
        MyType  = list([])  
        Behavior= list([])  
        Source  = list([])   
        RD      = list([])
        retVal  = 0
        result  = [Name,NumberHinges,HingeNum,Prop,MyType,Behavior,Source,RD,retVal]
        result  = self.RefApi.GetHingeAssigns(Name,NumberHinges,HingeNum,Prop,MyType,Behavior,Source,RD)
        if retVal != 0:
            raise ApiReturnError(retVal)
        return result
    
    def GetHingeAssigns_1(self,Name : str) -> list | ApiReturnError:
        """DEPRECATED Retrieves frame object hinge assignments. 

        Args:
            Name (str)          : The name of an existing frame object. 
            NumberHinges (int)  : The number of frame hinges assigned to the frame object. 
            HingeNum list(int)  : An array of size NumberHinges. This is the hinge identification number.
            Prop     list(str)  : An array of size NumberHinges. This is the name of the property of the hinge. 
            MyType   list(int)  : An array of size NumberHinges. This is a numeric value from 1 to 14 that specifies the type of the hinge. 
                                    1 - P
                                    2 - V2
                                    3 - V3
                                    4 - T
                                    5 - M2
                                    6 - M3
                                    7 - Interacting P-M2
                                    8 - Interacting P-M3
                                    9 - Interacting M2-M3
                                    10- Interacting P-M2-M3
                                    11- Fiber P-M2-M3
                                    12- Fiber P-M3
                                    13- Parametric Concrete P-M2-M3
                                    14- Parametric Steel P-M2-M3
            Behavior list(int)  : An array of size NumberHinges. This is a numeric value from 1 to 2 that specifies behavior of the hinge. 
                                    1- Force-controlled
                                    2- Deformation-controlled
            Source   list(str)  : An array of size NumberHinges. This is the name of the assigned hinge property, or "Auto" if an auto-generated hinge. 
            RD       list(float): An array of size NumberHinges. This is the distance of the hinge from the end of the i-end offset, as a ratio to the clear length of the frame object

        Returns:
            list | ApiReturnError: Hinge properties list
        """
        NumberHinges= int()
        HingeNum= list([])
        Prop    = list([])
        MyType  = list([])  
        Behavior= list([])  
        Source  = list([])  
        LocType = list([]) 
        RD      = list([])
        AD      = list([])
        retVal  = 0
        # result  = [Name,NumberHinges,HingeNum,Prop,MyType,Behavior,Source,LocType,RD,AD,retVal]
        result  = self.RefApi.GetHingeAssigns_1(Name,NumberHinges,HingeNum,Prop,MyType,Behavior,Source,LocType,RD,AD)
        if retVal != 0:
            raise ApiReturnError(retVal)
        return result
        pass
    
    def GetInsertionPoint       (self):
        pass
    def GetInsertionPoint_1     (self):
        pass

    def GetLabelFromName        (self):
        pass 
    def GetLabelNameList        (self):
        pass
    def GetLateralBracing       (self):
        pass

    def GetLoadDistributed      (self):
        pass
    def GetLoadPoint            (self):
        pass
    def GetLoadTemperature      (self):
        pass
    def GetLocalAxes            (self):
        pass
    def GetMass                 (self):
        pass

    def GetMaterialOverwrite    (self):
        pass

    def GetModifiers            (self):
        pass
    def GetNameFromLabel        (self):
        pass
    def GetNameList             (self):
        pass
    def GetNameListOnStory      (self):
        pass
    def GetOutputStations       (self):
        pass
    def GetPier                 (self):
        pass
    def GetPoints               (self):
        pass

    def GetReleases             (self):
        pass

    def GetSection              (self):
        pass
    def GetSectionNonPrismatic  (self):
        pass

    def GetSelected             (self):
        pass

    def GetSpandrel             (self):
        pass
    def GetSpringAssignment     (self):
        pass
    def GetSupports             (self):
        pass  
    def GetTCLimits             (self):
        pass

    def GetTransformationMatrix (self):
        pass

    def GetTypeOAPI             (self):
        pass
    def SetColumnSpliceOverwrite(self):
        pass
    def SetDesignProcedure      (self):
        pass
    def SetEndLengthOffset      (self):
        pass
    def SetGroupAssign          (self):
        pass
    def SetGUID                 (self):
        pass
    def SetInsertionPoint       (self):
        pass
    def SetInsertionPoint_1     (self):
        pass

    def SetLateralBracing       (self):
        pass

    def SetLoadDistributed      (self):
        pass
    def SetLoadPoint            (self):
        pass
    def SetLoadTemperature      (self):
        pass

    def SetLocalAxes            (self):
        pass
    def SetMass                 (self):
        pass

    def SetMaterialOverwrite    (self):
        pass

    def SetModifiers            (self):
        pass
    def SetOutputStations       (self):
        pass
    def SetPier                 (self):
        pass
    def SetReleases             (self):
        pass 
    def SetSection              (self):
        pass 
    def SetSelected             (self):
        pass
    def SetSpandrel             (self):
        pass
    def SetSpringAssignment     (self):
        pass 
    def SetTCLimits             (self):
        pass  

