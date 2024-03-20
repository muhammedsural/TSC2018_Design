from dataclasses import dataclass
from pandas import DataFrame
from TSC.MSCSI.ErrorHandler import ApiReturnError,CustomCommentError
import numpy as np


@dataclass
class DatabaseTables:
    # con.RefApi.DatabaseTables
    RefApi : object

    def ApplyEditedTables(self):
        """Instructs the program to interactively import all of the tables stored in the table list using the SetTableForEditing... functions."""  
        FillImportLog   = bool()
        NumFatalErrors  = int()
        NumErrorMsgs    = int()
        NumWarnMsgs     = int()
        NumInfoMsgs     = int()
        ImportLog       = str()
        retVal = 0
        result = [FillImportLog,NumFatalErrors,NumErrorMsgs,NumWarnMsgs,NumInfoMsgs,ImportLog,retVal]
        result = self.RefApi.ApplyEditedTables(FillImportLog,NumFatalErrors,NumErrorMsgs,NumWarnMsgs,NumInfoMsgs,ImportLog)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
            
        return result
    
    def CancelTableEditing(self):
        """Clears all tables that were stored in the table list using one of the SetTableForEditing... functions."""  
        self.RefApi.CancelTableEditing()

    def GetAllFieldsInTable(self,TableKey:str) -> DataFrame | ApiReturnError:
        """Returns the available fields in a specified table.""" 
        TableVersion        = int()
        NumberFields        = int()
        FieldKey            = list([])
        FieldName           = list([])
        Description         = list([])
        UnitsString         = list([])
        IsImportable        = list([])
        retVal = 0
        result = [TableVersion,NumberFields,FieldKey,FieldName,Description,UnitsString,IsImportable,retVal]
        result = self.RefApi.GetAllFieldsInTable(TableKey,TableVersion,NumberFields,FieldKey,FieldName,Description,UnitsString,IsImportable)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        aaa = {"FieldKey"    : result[2],
               "FieldName"   : result[3],
               "Description" : result[4],
               "UnitsString" : result[5]}
        df_result = DataFrame(aaa)
        return df_result

    def GetAllTables(self):
        """Returns all of the tables along with their import type and indicates if any data is available in the model to fill the table."""  
        NumberTables = int()
        TableKey     = list([])
        TableName    = list([])
        ImportType   = list([])
        IsEmpty      = list([])
        retVal = 0
        result = [NumberTables,TableKey,TableName,ImportType,IsEmpty,retVal]
        result = self.RefApi.GetAllTables(NumberTables,TableKey,TableName,ImportType,IsEmpty)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        
        dict_result = {
            "TableKey"      : result[1],
            "TableName"     : result[2],
            "ImportType"    : result[3]   ,
            "IsEmpty"       : result[4] 
        }

        df_result = DataFrame(dict_result)
        return df_result
    
    def GetTablesIndex(self,FindTableKey : str) -> DataFrame:
        """asdasdas

        Args:
            FindTableKey (str): _description_

        Returns:
            DataFrame: _description_
        """
        dbTables = self.GetAllTables()
        findTable = dbTables[dbTables["TableKey"] == FindTableKey]
        del dbTables
        return findTable
    
    def GetAvailableTables(self):
        """Returns the tables that are currently available for display."""  
        NumberTables = int()
        TableKey     = list([])
        TableName    = list([])
        ImportType   = list([])
        retVal = 0
        result = [NumberTables,TableKey,TableName,ImportType,retVal]
        result = self.RefApi.GetAvailableTables(NumberTables,TableKey,TableName,ImportType)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        result_dict = {"TableKey" : result[1],"ImportType" : result[3]}
        db_available = DataFrame(result_dict)
        del result_dict
        return db_available
    
    def GetAvailableTablesIndex(self,FindTableKey : str) -> DataFrame:
        """Aktif olan tablonun bilgilerini döndürür...

        Args:
            FindTableKey (str): Aranan tablonun ismi
        Returns:
            DataFrame: Tablo bilgileri
        """
        dbTables = self.GetAvailableTables()
        findTable = dbTables[dbTables["TableKey"] == FindTableKey]
        del dbTables
        return findTable

    def GetLoadCasesSelectedForDisplay(self):
        """"Returns a list of load cases that are selected for table display."""
        retVal                  = 0 
        NumberSelectedLoadCases = int()
        LoadCaseList            = list([])        
        result                  = [NumberSelectedLoadCases,LoadCaseList,retVal]
        result                  = self.RefApi.GetLoadCasesSelectedForDisplay(NumberSelectedLoadCases,LoadCaseList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result

    def GetLoadCombinationsSelectedForDisplay(self):
        """Returns a list of load combinations that are selected for table display."""  
        retVal                  = 0 
        NumberSelectedLoadCombinations = int()
        LoadCombinationList            = list([])        
        result                  = [NumberSelectedLoadCombinations,LoadCombinationList,retVal]
        result                  = self.RefApi.GetLoadCombinationsSelectedForDisplay(NumberSelectedLoadCombinations,LoadCombinationList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetLoadPatternsSelectedForDisplay    (self):
        """Returns a list of load patterns that are selected for table display."""  
        retVal                  = 0 
        NumberSelectedLoadPatterns = int()
        LoadPatternList            = list([])        
        result                  = [NumberSelectedLoadPatterns,LoadPatternList,retVal]
        result                  = self.RefApi.GetLoadPatternsSelectedForDisplay(NumberSelectedLoadPatterns,LoadPatternList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetObsoleteTableKeyList(self):
        """Returns a list of obsolete table keys for the program.
        
        Return array:
            NumberTableKeys : The number of obsolete table keys.
            TableKeyList: A zero-based list of obsolete table keys.
            NotesList: A zero-based list of notes, one for each table key.
        """  
        retVal                  = 0 
        NumberTableKeys = int()
        TableKeyList            = list([])        
        NotesList            = list([])        
        result                  = [NumberTableKeys,TableKeyList,NotesList,retVal]
        result                  = self.RefApi.GetObsoleteTableKeyList(NumberTableKeys,TableKeyList,NotesList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        return result
    
    def GetOutputOptionsForDisplay(self):
        """Returns the database table output options for load case results."""  
        pass
    
    def GetTableForDisplayArray(self,TableKey:str,GroupName : str = 'ALL'):
        """Returns data for a single table in a single array. If there is nothing to be shown in the table then no data is returned."""  
        retVal              = 0 
        FieldKeyList        = list([])
        TableVersion        = int()
        FieldsKeysIncluded  = list([])
        NumberRecords       = int()
        TableData           = list([])
        result = [FieldKeyList,TableVersion,FieldsKeysIncluded,NumberRecords,TableData,retVal]
        result = self.RefApi.GetTableForDisplayArray(TableKey,FieldKeyList,GroupName,TableVersion,FieldsKeysIncluded,NumberRecords,TableData)
        if result[-1] != 0:
            raise CustomCommentError(result[-1],"Tablo verisi alinamadi veya veri yok!!!")
        return result
    
    def GetTableForDisplayCSVFile(self,csvFilePath : str, sepChar : str = ","):
        """Returns data for a single table in a CSV file. If there is nothing to be shown in the table then no data is returned."""  
        retVal                  = 0
        TableKey = str()
        FieldKeyList= list([])
        GroupName= str()
        TableVersion= int()
        result = [TableKey,FieldKeyList,GroupName,TableVersion,csvFilePath,sepChar,retVal]
        result = self.RefApi.GetTableForDisplayCSVFile(TableKey,FieldKeyList,GroupName,TableVersion,csvFilePath,sepChar)

        if result[-1] != 0:
            raise ApiReturnError(result[-1])

        return result
    
    def GetTableForDisplayCSVString(self):
        """Returns data for a single table in a CSV string. If there is nothing to be shown in the table then no data is returned."""  
        pass
    
    def GetTableForDisplayXMLString(self):
        """Returns data for a single table as XML in a single string. If there is nothing to be shown in the table then no data is returned."""  
        pass
    
    def GetTableForEditingArray(self):
        """Returns a single table in a string array for interactive editing."""  
        pass
    
    def GetTableForEditingCSVFile(self):
        """Returns a single table in a CSV file for interactive editing."""  
        pass
    
    def GetTableForEditingCSVString(self):
        """Returns a single table in a CSV-formatted string for interactive editing."""  
        pass
    
    def SetLoadCasesSelectedForDisplay(self,LoadCaseList : list) -> None | ApiReturnError:
        """Sets the load cases that are selected for table display."""  
        retVal = 0
        result = [LoadCaseList,retVal]
        result= self.RefApi.SetLoadCasesSelectedForDisplay(LoadCaseList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
    
    def SetLoadCombinationsSelectedForDisplay(self,LoadCombinationList : list) -> None | ApiReturnError:
        """
        Sets the load combinations that are selected for table display.Sets the database table output options for load case results. 
        
        LoadCombinationList(list[str]): The zero-based list of load combinations selected for table display.    
        """  
        retVal = 0
        result = [LoadCombinationList,retVal]
        result= self.RefApi.SetLoadCombinationsSelectedForDisplay(LoadCombinationList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
    
    def SetLoadPatternsSelectedForDisplay(self,LoadPatternList : list) -> None | ApiReturnError:
        """Sets the load patterns that are selected for table display.

        LoadPatternList(list[str]): The zero-based list of load patterns selected for table display.
        """  
        retVal = 0
        result = [LoadPatternList,retVal]
        result= self.RefApi.SetLoadCombinationsSelectedForDisplay(LoadPatternList)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
    
    def SetOutputOptionsForDisplay(self,IsUserBaseReactionLocation : bool,
                                        UserBaseReactionX : float,
                                        UserBaseReactionY : float,
                                        UserBaseReactionZ : float,
                                        IsAllModes : bool,
                                        StartMode : int,
                                        EndMode : int,
                                        IsAllBucklingModes : bool,
                                        StartBucklingMode : int,
                                        EndBucklingMode : int,
                                        MultistepStatic : int,
                                        NonlinearStatic : int,
                                        ModalHistory : int,
                                        DirectHistory : int,
                                        Combo : int):
        """Sets the database table output options for load case results.
        
            IsUserBaseReactionLocation  : Indicates if the base reaction location is user specified instead of program determined.
            UserBaseReactionX           : The global X coordinate of the user specified base reaction location. This item only applies when the IsUserBaseReactionLocation item is True.
            UserBaseReactionY           : The global Y coordinate of the user specified base reaction location. This item only applies when the IsUserBaseReactionLocation item is True.
            UserBaseReactionZ           : The global Z coordinate of the user specified base reaction location. This item only applies when the IsUserBaseReactionLocation item is True.
            IsAllModes                  : Indicates if results are to be displayed for all modes of modal load cases.
            StartMode                   : The first mode for which results are shown for modal load cases. This item only applies when the IsAllModes item is False.
            EndMode                     : The last mode for which results are shown for modal load cases. This item only applies when the IsAllModes item is False.
            IsAllBucklingModes          : Indicates if results are to be displayed for all modes of buckling load cases.
            StartBucklingMode           : The first mode for which results are shown for buckling load cases. This item only applies when the IsAllBucklingModes item is False.
            EndBucklingMode             : The last mode for which results are shown for buckling load cases. This item only applies when the IsAllBucklingModes item is False.
            MultistepStatic             : Indicates how multistep static load case results are displayed: 1=Envelopes, 2=Step-by-step, 3=Last Step.
            NonlinearStatic             : Indicates how nonlinear static load case results are displayed: 1=Envelopes, 2=Step-by-step, 3=Last Step.
            ModalHistory                : Indicates how multistep modal time history load case results are displayed: 1=Envelopes, 2=Step-by-step, 3=Last Step.
            DirectHistory               : Indicates how direct integration time load case results are displayed: 1=Envelopes, 2=Step-by-step, 3=Last Step.
            Combo                       : Indicates how load combination results are displayed: 1=Envelopes, 2=Multiple Values If Possible.
        
        """  
        retVal = 0
        result = [IsUserBaseReactionLocation,UserBaseReactionX,UserBaseReactionY,UserBaseReactionZ,IsAllModes,StartMode,EndMode,IsAllBucklingModes,StartBucklingMode,EndBucklingMode,MultistepStatic,NonlinearStatic,ModalHistory,DirectHistory,Combo,retVal]
        result= self.RefApi.SetLoadCombinationsSelectedForDisplay(IsUserBaseReactionLocation,UserBaseReactionX,UserBaseReactionY,UserBaseReactionZ,IsAllModes,StartMode,EndMode,IsAllBucklingModes,StartBucklingMode,EndBucklingMode,MultistepStatic,NonlinearStatic,ModalHistory,DirectHistory,Combo)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
    
    def SetTableForEditingArray(self,TableKey : str, TableData : list, NumberRecords : int):
        """Reads a table from a string array and adds it to a stored table list until either the ApplyEditedTables(Boolean, Int32, Int32, Int32, Int32, String) or CancelTableEditing()  command is issued.
        
        TableKey: The table key for a table which has been interactively edited. The table must be one that can be interactively edited.
        TableVersion: The version number of the specified table.
        FieldsKeysIncluded: A zero-based array listing the field keys associated with the specified table for which data is reported in the order it is reported in the TableData array. These are essentially the column headers of the data reported in TableData. 
        NumberRecords: The number of records of data for each field. This is essentially the number of rows of data.
        TableData: A zero-based, one-dimensional array of the table data, excluding headers, reported row by row. See GetTableForDisplayArray(String,String[] , String, Int32,String[] , Int32,String[] ) for a more detailed explanation of the data format. 
        """  
        retVal = 0
        TableVersion = int()
        FieldsKeysIncluded = list([])
        TableData = list([])
        result = [TableKey,TableVersion,FieldsKeysIncluded,NumberRecords,TableData,retVal]
        result = self.RefApi.SetTableForEditingArray(TableKey,TableVersion,FieldsKeysIncluded,NumberRecords,TableData)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
    
    def SetTableForEditingCSVFile(self):
        """Reads a table from a CSV file and adds it to a stored table list until either the ApplyEditedTables(Boolean, Int32, Int32, Int32, Int32, String) or CancelTableEditing()  command is issued."""  
        pass
    
    def SetTableForEditingCSVString(self):
        """Reads a table from a CSV-formatted string and adds it to a stored table list until either the ApplyEditedTables(Boolean, Int32, Int32, Int32, Int32, String) or CancelTableEditing()  command is issued."""
        pass
    
    def ShowTablesInExcel(self):
        """Exports the specified tables to Excel.""" 
        pass

    def ConvertDataFrame(self,Table : list, DeletedColumns : list = None) -> DataFrame:
        """Etabsdan çekilen datalar DataFrame yapisina çevirir.

        Args:
            Table (list): Etabs verilerinin bulunduğu liste
            DeletedColumns (list(str)): Veride silinmesi istenen kolon basliklarinin listesi. Opsiyoneldir girilmezse tüm kolonlar döndürülür. Default is None

        Returns:
            DataFrame: Dataların bulunduğu DataFrame
        """
        output = DataFrame(columns=[i for i in Table[2]])
        dataColumnslen = len(output.columns)
        line = []
        lineindex = 0
        for colindex,value in enumerate(Table[4],start=1):
            sinir = colindex%dataColumnslen
            if sinir == 0:
                line.append(value)
                output.loc()[lineindex] = np.array(line)
                line.clear()
                lineindex += 1
            else:
                line.append(value)
        if DeletedColumns is not None:
            output.drop([col for col in DeletedColumns],axis=1,inplace=True)
        return output

    def ConvertDataFrame2(self,Table : list,DeletedColumns : list = None) -> DataFrame:
        """Etabsdan çekilen datalar DataFrame yapisina çevirir.

        Args:
            Table (list)              : Etabs verilerinin bulunduğu liste
            DeletedColumns (list(str)): Veride silinmesi istenen kolon basliklarinin listesi. Opsiyoneldir girilmezse tüm kolonlar döndürülür. Default is None

        Returns:
            DataFrame: Dataların bulunduğu DataFrame
        """
        output = DataFrame(columns=[i for i in Table[2]])
        dataColumnslen = len(output.columns)
        data = np.array(Table[4])
        count = 0
        datalength = len(Table[4])

        for colindex in range(1,datalength+1):
            sinir = colindex%dataColumnslen
            if sinir == 0:
                output.loc()[count] = data[count*dataColumnslen:count*dataColumnslen+dataColumnslen]
                count += 1
        if DeletedColumns is not None:
            output.drop([col for col in DeletedColumns],axis=1,inplace=True)
        return output

    def ConvertDataFrame3(self,Table : list,DeletedColumns : list = None) -> DataFrame:
            """Etabsdan çekilen datalar DataFrame yapisina çevirir.

            Args:
                Table (list): Etabs verilerinin bulunduğu liste
                DeletedColumns (list(str)): Veride silinmesi istenen kolon basliklarinin listesi. Opsiyoneldir girilmezse tüm kolonlar döndürülür. Default is None

            Returns:
                DataFrame: Dataların bulunduğu DataFrame
            """
            data = np.array(Table[4])
            colLength = len(Table[2])
            data_dict = {key :data[index :: colLength] for index,key in enumerate(Table[2])}
            db = DataFrame(data_dict)
            if DeletedColumns is not None:
                db.drop([col for col in DeletedColumns],axis=1,inplace=True)
            return db
        