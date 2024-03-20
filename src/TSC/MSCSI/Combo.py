

from dataclasses import dataclass
from TSC.MSCSI.Enums import eCNameType, eComboType
from TSC.MSCSI.ErrorHandler import ApiReturnError

@dataclass
class Combo:
    # con.RefApi.RespCombo
    RefApi : object

    def Add(self, Name : str, Type : eComboType) -> None | ApiReturnError :
        """Adds a new load combination.

        Args:
            Name (str): The name of a new load combination
            Type (eComboType): this is 0,1,2,3 or 4 indicating the load combination type
        """
        result = self.RefApi.Add(Name,Type)
        if result != 0:
            raise ApiReturnError(result)
        
    def AddDesignDefaultCombos  (self,DesignSteel : bool, DesignConcrete : bool, DesignAluminum : bool, DesignColdFormed : bool) -> None | ApiReturnError  :
        """"""
        result = self.RefApi.Add(DesignSteel,DesignConcrete,DesignAluminum,DesignColdFormed)
        if result != 0:
            raise ApiReturnError(result)
        
    def Delete(self, Name : str) :
        """Deletes the specified load combination."""  
        result = self.RefApi.Delete(Name)
        if result != 0:
            raise ApiReturnError(result)

    def DeleteCase(self, Name : str, CNameType : eCNameType, CName : str) -> None | ApiReturnError:
        """Deletes one load case or load combination from the list of cases included in the specified load combination.
        
        Args :
            Name        : The name of an existing load combination. 
            CNameType   : This is one of the following items in the eCNameType enumeration: 
                            LoadCase = 0
                            LoadCombo = 1
                          This item indicates whether the CName item is an analysis case (LoadCase) or a load combination (LoadCombo). 

            CName       : The name of the load case or load combination to be deleted from the specified combination. 
        """  
        result = self.RefApi.DeleteCase(Name)
        if result != 0:
            raise ApiReturnError(result)
        
    def GetCaseList(self, Name : str) :
        """Retrieves all load cases and response combinations included in the load combination specified by the Name item.
        
        Name        : The name of an existing load combination. 
        NumberItems : The total number of load cases and load combinations included in the load combination specified by the Name item. 
        CNameType   : This is one of the following items in the eCNameType enumeration: 
                        LoadCase = 0
                        LoadCombo = 1
                      This item indicates whether the CName item is an analysis case (LoadCase) or a load combination (LoadCombo). 

        CName       : This is an array of the names of the load cases or load combinations included in the load combination specified by the Name item. 
        SF          : The scale factor multiplying the case or combination indicated by the CName item. 
        """  
        retVal = 0
        NumberItems = int()
        CNameType   = int()
        CName       = list([])
        SF          = list([])
        result = [Name,NumberItems,CNameType,CName,SF,retVal]
        result = self.RefApi.GetCaseList(Name,NumberItems,CNameType,CName,SF)
        if result[-1] != 0:
            raise ApiReturnError(result)
        return result
        
    def SetCaseList(self, Name : str, CNameType : eCNameType, CName : str, SF : float) :
        """Adds or modifies one load case or response combination in the list of cases included in the load combination specified by the Name item."""  
        result = self.RefApi.GetCaseList(Name)
        if result != 0:
            raise ApiReturnError(result)
        
    def GetCaseList_1(self, Name : str) :
        """Retrieves all load cases and response combinations included in the load combination specified by the Name item. 
        Name
            Type: System.String
            The name of an existing load combination. 
        NumberItems
            Type: System.Int32
            The total number of load cases and load combinations included in the load combination specified by the Name item. 
        CNameType
            Type: ETABSv1.eCNameType[]
            This is one of the following items in the eCNameType enumeration: 
            LoadCase = 0
            LoadCombo = 1
            This item indicates whether the CName item is an analysis case (LoadCase) or a load combination (LoadCombo). 
        CName
            Type: System.String[]
            This is an array of the names of the load cases or load combinations included in the load combination specified by the Name item. 
        ModeNumber
            Type: System.Int32[]
            The mode number for the case indicated by the CName item. This item applies when by the CNameType item is LoadCase and the type of load case specified by the CName item is either Modal or Buckling. Any other case type or combo returns a zero for this item. 
        SF
            Type: System.Double[]
            The scale factor multiplying the case or combination indicated by the CName item. 
        """
        retVal = 0
        NumberItems = int()
        CNameType   = list([])
        CName       = list([])
        ModeNumber  = list([])
        SF          = list([])
        result = [Name,NumberItems,CNameType,CName,ModeNumber,SF,retVal]
        result = self.RefApi.GetCaseList_1(Name,NumberItems,CNameType,CName,ModeNumber,SF)
        if result[-1] != 0:
            raise ApiReturnError(result)
        return result
    
    def SetCaseList_1(self, Name : str, CNameType : list[eCNameType], CName : list[str], ModeNumber : list[int], SF : list[float]) :
        """Adds or modifies one load case or response combination in the list of cases included in the load combination specified by the Name item.
        Name
            Type: System.String
            The name of an existing load combination. 
        CNameType
            Type: ETABSv1.eCNameType[]
            This is one of the following items in the eCNameType enumeration: 
            LoadCase = 0
            LoadCombo = 1
            This item indicates whether the CName item is an analysis case (LoadCase) or a load combination (LoadCombo). 

        CName
            Type: System.String[]
            This is an array of the names of the load cases or load combinations included in the load combination specified by the Name item. 
        ModeNumber
            Type: System.Int32[]
            The mode number for the case indicated by the CName item. This item applies when by the CNameType item is LoadCase and the type of load case specified by the CName item is either Modal or Buckling. Any other case type or combo returns a zero for this item. 
        SF
            Type: System.Double[]
            The scale factor multiplying the case or combination indicated by the CName item. 
        """
        result = self.RefApi.GetCaseList_1(Name,CNameType,CName,ModeNumber,SF)
        if result != 0:
            raise ApiReturnError(result)

    def GetNameList(self) :
        """Retrieves the names of all defined response combinations.
        NumberNames
            Type: System.Int32
            The number of load combination names retrieved by the program. 
        MyName
            Type: System.String[]
            This is a one-dimensional array of load combination names. The MyName array is created as a dynamic, zero-based, array by the API user: 
            Dim MyName() as String

            The array is dimensioned to (NumberNames – 1) inside the ETABS program, filled with the names, and returned to the API user. 

        """  
        retVal = 0
        NumberNames = int()
        MyName = list([])
        result =[NumberNames,MyName,retVal]
        result = self.RefApi.GetNameList(NumberNames,MyName)
        if retVal != 0:
            raise ApiReturnError(retVal)
        return result
    
    def GetTypeCombo(self, Name : str) :
        """Retrieves the combination type for specified load combination.
        Name
            Type: System.String
            The name of an existing load combination. 
        CNameType
            Type: ETABSv1.eCNameType[]
            This is one of the following items in the eCNameType enumeration: 
            LoadCase = 0
            LoadCombo = 1
            This item indicates whether the CName item is an analysis case (LoadCase) or a load combination (LoadCombo). 

        """ 
        CNameType = int()
        retVal = 0
        result = [Name,CNameType,retVal]
        result = self.RefApi.GetTypeCombo(Name,CNameType)
        if retVal != 0:
            raise ApiReturnError(retVal)
        return result
    
    def GetTypeOAPI(self, Name : str) :
        """"""
        ComboType = int()
        retVal = 0
        result = [Name,ComboType,retVal]
        result = self.RefApi.GetTypeOAPI(Name,ComboType)
        if retVal != 0:
            raise ApiReturnError(retVal)
        return result
