

from dataclasses import dataclass

from TSC.MSCSI.ErrorHandler import ApiReturnError


@dataclass
class Analyze:
    RefApi : object # SapModel.RefApi.Analyze

    def CreateAnalysisModel(self) -> None | ApiReturnError:
        """Creates the analysis model. If the analysis model is already created and current, nothing is done."""  
        result = self.RefApi.CreateAnalysisModel()   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def DeleteResults(self,Name : str,All : bool = False) -> None | ApiReturnError:
        """Deletes results for load cases.

        Args:
            Name (str): The name of an existing load case that is to have its results deleted. 
                        This item is ignored when the All item is True. 

            All (bool, optional): If this item is True, the results are deleted for all load cases, and the Name item is ignored. . Defaults to False.

        Raises:
            ApiReturnError: Error description
        """
        result = self.RefApi.DeleteResults(Name,All)   
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
     
    def GetActiveDOF(self) -> list | ApiReturnError:
        """Retrieves the model global degrees of freedom."""  
        DOF = list([])
        retVal = 0
        result = [DOF,retVal]
        result = self.RefApi.GetActiveDOF(DOF)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result

    def GetCaseStatus(self) -> list | ApiReturnError:
        """Retrieves the status for all load cases.  """
        NumberItems = int()
        CaseName = list([])
        Status = list([])
        retVal = 0
        result = [NumberItems,CaseName,Status,retVal]
        result = self.RefApi.GetCaseStatus(NumberItems,CaseName,Status)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result

    def GetDesignResponseOption(self) -> list | ApiReturnError:
        """Retrieves the design and response recovery options.  """
        NumberDesignThreads = int()
        NumberResponseRecoveryThreads = int()
        UseMemoryMappedFilesForResponseRecovery = int()
        ModelDifferencesOKWhenMergingResults = bool()
        retVal = 0
        result = [NumberDesignThreads,NumberResponseRecoveryThreads,UseMemoryMappedFilesForResponseRecovery,ModelDifferencesOKWhenMergingResults,retVal]
        result = self.RefApi.GetDesignResponseOption(NumberDesignThreads,NumberResponseRecoveryThreads,UseMemoryMappedFilesForResponseRecovery,ModelDifferencesOKWhenMergingResults)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result
    
    def GetRunCaseFlag(self) -> list | ApiReturnError:
        """Retrieves the run flags for all analysis cases.""" 
        NumberItems = int()
        CaseName = list([])
        Run = list([])
        retVal = 0
        result = [NumberItems,CaseName,Run,retVal]
        result = self.RefApi.GetRunCaseFlag(NumberItems,CaseName,Run)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result
    
    def GetSolverOption(self) -> list | ApiReturnError:
        """DEPRECATED. Please see GetSolverOption_2(Int32, Int32, Int32, String) or GetSolverOption_3(Int32, Int32, Int32, Int32, Int32, String) """
        pass
    
    def GetSolverOption_1(self) -> list | ApiReturnError:
        """DEPRECATED. Please see GetSolverOption_2(Int32, Int32, Int32, String) or GetSolverOption_3(Int32, Int32, Int32, Int32, Int32, String) """
        pass
    
    def GetSolverOption_2(self) -> list | ApiReturnError:
        """Retrieves the model solver options."""  
        SolverType = int()
        SolverProcessType = int()
        NumberParallelRuns = int()
        StiffCase = str()
        retVal = 0

        result = [SolverType,SolverProcessType,NumberParallelRuns,StiffCase,retVal]
        result = self.RefApi.GetSolverOption_2(SolverType,SolverProcessType,NumberParallelRuns,StiffCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result
    
    def GetSolverOption_3(self) -> list | ApiReturnError:
        """Retrieves the model solver options."""  
        SolverType = int()
        SolverProcessType = int()
        NumberParallelRuns = int()
        ResponseFileSizeMaxMB = int()
        NumberAnalysisThreads = int()
        StiffCase = str()
        retVal = 0

        result = [SolverType,SolverProcessType,NumberParallelRuns,ResponseFileSizeMaxMB,NumberAnalysisThreads,StiffCase,retVal]
        result = self.RefApi.GetSolverOption_3(SolverType,SolverProcessType,NumberParallelRuns,ResponseFileSizeMaxMB,NumberAnalysisThreads,StiffCase)
        if result[-1] != 0:
            raise ApiReturnError(result[-1])
        else:
            print("Operation completed...")
        return result
    
    def MergeAnalysisResults(self,SourceFileName : str) -> None | ApiReturnError:
        """Merges analysis results from a given model.

        Args:
            SourceFileName (str): Full path to the model file to import results from. 

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.MergeAnalysisResults(SourceFileName)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    def ModifyUndeformedGeometry(self,CaseName : str,SF : float,Stage :int = -1, Original : bool = False) -> None | ApiReturnError:
        """Modifies the undeformed geometry based on displacements obtained from a specified load case 

        Args:
            CaseName (str): The name of the static load case from which displacements are obtained. 
            SF (float): The scale factor applied to the displacements.
            Stage (int, optional): This item applies only when the specified load case is a staged construction load case. It is the stage number from which the displacements are obtained. Specifying a -1 for this item means to use the last run stage. Defaults to -1.
            Original (bool, optional): If this item is True, all other input items in this function are ignored and the original undeformed geometry data is reinstated. . Defaults to False.
        
        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.ModifyUndeformedGeometry(CaseName,SF,Stage,Original)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")

    
    def ModifyUndeformedGeometryModeShape(self,CaseName : str,Mode : int,MaxDispl : float,Direction : int, Original : bool) -> None | ApiReturnError:
        """Modifies the undeformed geometry based on the shape of a specified mode 

        Args:
            CaseName (str): The name of a load case 
            Mode (int): The mode shape
            MaxDispl (float): The maximum displacement to which the mode shape will be scaled
            Direction (int): The direction in which to apply the geometry modification 
                                1-  X
                                2-  Y
                                3-  Z
                                4-  Resultant
            Original (bool): If this item is True, all other input items in this function are ignored and the original undeformed geometry data is reinstated. 

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.ModifyUndeformedGeometryModeShape(CaseName,Mode,MaxDispl,Direction,Original)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def RunAnalysis(self) -> None | ApiReturnError:
        """Runs the analysis.

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.RunAnalysis()
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def SetActiveDOF(self,DOF : list) -> None | ApiReturnError:
        """Sets the model global degrees of freedom.
        Args:
            DOF(list) : Global degrees of freedoms list

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """  
        result = self.RefApi.SetActiveDOF(DOF)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def SetDesignResponseOption(self,NumberDesignThreads : int,NumberResponseRecoveryThreads : int,UseMemoryMappedFilesForResponseRecovery : int,ModelDifferencesOKWhenMergingResults : bool ) -> None | ApiReturnError:
        """Sets the design and response recovery options.

        Args:
            NumberDesignThreads (int): Number of threads that design can use. Set to positive for user specified, non-positice for program determined. 
            NumberResponseRecoveryThreads (int): Number of threads that response recovery can use. Set to positive for user specified, non-positive for program determined. 
            UseMemoryMappedFilesForResponseRecovery (int): Flag for using memory mapped files for response recovery. Set to 
                                                            -1 = Do not use memory mapped files.
                                                            0 = Program determined.
                                                            1 = Use memory mapped files.
            ModelDifferencesOKWhenMergingResults (bool): Flag for merging results in presence of any model differences. Set to true to enable merging of results from two models that are not identical, to false otherwise. 


        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetDesignResponseOption(NumberDesignThreads,NumberResponseRecoveryThreads,UseMemoryMappedFilesForResponseRecovery,ModelDifferencesOKWhenMergingResults)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def SetRunCaseFlag(self,Name :str,Run : bool,All : bool = False) -> None | ApiReturnError:
        """Sets the run flag for load cases.

        Args:
            Name (str): The name of an existing load case that is to have its run flag set. 
                        This item is ignored when the All item is True
            Run (bool): If this item is True, the specified load case is to be run.
            All (bool, optional): If this item is True, the run flag is set as specified by the Run item for all load cases, and the Name item is ignored. Defaults to False.

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetRunCaseFlag(Name,Run,All)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def SetSolverOption(self) -> None | ApiReturnError:
        """DEPRECATED. Please see SetSolverOption_2(Int32, Int32, Int32, String) or SetSolverOption_3(Int32, Int32, Int32, Int32, Int32, String)""" 
        pass
    
    def SetSolverOption_1(self) -> None | ApiReturnError:
        """DEPRECATED. Please see SetSolverOption_2(Int32, Int32, Int32, String) or SetSolverOption_3(Int32, Int32, Int32, Int32, Int32, String)""" 
        pass
    
    def SetSolverOption_2(self,SolverType : int,SolverProcessType : int,NumberParallelRuns : int,StiffCase :str = "") -> None | ApiReturnError:
        """Sets the model solver options.

        Args:
            SolverType (int): This is 0, 1 or 2, indicating the solver type. 
                                    0 = Standard solver
                                    1 = Advanced solver
                                    2 = Multi-threaded solver
            SolverProcessType (int): This is 0, 1 or 2, indicating the process the analysis is run. 
                                        0 = Auto (program determined)
                                        1 = GUI process
                                        2 = Separate process
            NumberParallelRuns (int): This is an integer not including -1. 
                                            -Less than -1 = Auto parallel (use up to all physical cores - limited by license). Treated the same as 0.
                                            -1 = Illegal value; will return an error
                                            0 = Auto parallel (use up to all physical cores)
                                            1 = Serial
                                            Greater than 1 = User defined parallel (use up to this fixed number of cores - limited by license)
            StiffCase (str, optional): The name of the load case used when outputting the mass and stiffness matrices to text files. If this item is blank, no matrices are output. Defaults to "".

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetRunCaseFlag(SolverType,SolverProcessType,NumberParallelRuns,StiffCase)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
    def SetSolverOption_3(self,SolverType : int,SolverProcessType : int,NumberParallelRuns : int,ResponseFileSizeMaxMB : int,NumberAnalysisThreads : int,StiffCase :str = "") -> None | ApiReturnError:
        """Sets the model solver options.

        Args:
            SolverType (int)            : This is 0, 1 or 2, indicating the solver type. 
                                                0 = Standard solver
                                                1 = Advanced solver
                                                2 = Multi-threaded solver
            SolverProcessType (int)     : This is 0, 1 or 2, indicating the process the analysis is run. 
                                                0 = Auto (program determined)
                                                1 = GUI process
                                                2 = Separate process
            NumberParallelRuns (int)    : This is an integer not including -1. 
                                                -Less than -1 = Auto parallel (use up to all physical cores - limited by license). Treated the same as 0.
                                                -1 = Illegal value; will return an error
                                                0 = Auto parallel (use up to all physical cores)
                                                1 = Serial
                                                Greater than 1 = User defined parallel (use up to this fixed number of cores - limited by license)
            ResponseFileSizeMaxMB(int)  : The maximum size of a response file in MB before a new response file is created. Non-positive means program determined.
            NumberAnalysisThreads(int)  : Number of threads that the analysis can use. Non-positive means program determined. 
            StiffCase (str, optional)   : The name of the load case used when outputting the mass and stiffness matrices to text files. If this item is blank, no matrices are output. Defaults to "".

        Raises:
            ApiReturnError: Error descriptions

        Returns:
            None | ApiReturnError: _description_
        """
        result = self.RefApi.SetRunCaseFlag(SolverType,SolverProcessType,NumberParallelRuns,ResponseFileSizeMaxMB,NumberAnalysisThreads,StiffCase)
        if result != 0:
            raise ApiReturnError(result)
        else:
            print("Operation completed...")
    
