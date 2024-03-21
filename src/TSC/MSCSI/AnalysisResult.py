from dataclasses import dataclass, field,asdict
from typing import Any
from pandas import DataFrame
from TSC.MSCSI.Enums import eItemTypeElm
from TSC.MSCSI.ErrorHandler import CustomCommentError

# Tamamlananlar
@dataclass
class BaseReact:
     """Class for base_react return"""
     number_results      : int     = field(default_factory=int)
     load_case           : list[str]   = field(default_factory=list)
     step_type           : list[str]   = field(default_factory=list)
     step_number         : list[float] = field(default_factory=list)
     force_x             : list[float] = field(default_factory=list)
     force_y             : list[float] = field(default_factory=list)
     force_z             : list[float] = field(default_factory=list)
     moment_x            : list[float] = field(default_factory=list)
     moment_y            : list[float] = field(default_factory=list)
     moment_z            : list[float] = field(default_factory=list)
     x_coordinate        : float   = field(default_factory=float)
     y_coordinate        : float   = field(default_factory=float)
     z_coordinate        : float   = field(default_factory=float)
     
     def __repr__(self) -> str:
          return f"Load cases : {self.load_case}\nForce_x : {self.force_x}\nForce_y : {self.force_y}\nForce_z : {self.force_z}\nMoment_x : {self.moment_x}\nMoment_y : {self.moment_y}\nMoment_z : {self.moment_z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
          dumydict = self.to_dict()
          df = DataFrame([dumydict["load_case"], dumydict["force_x"], dumydict["force_y"], dumydict["force_z"], dumydict["moment_x"], dumydict["moment_y"], dumydict["moment_z"]]).T
          df.columns = ["load_case","force_x","force_y","force_z","moment_x","moment_y","moment_z"]
          del dumydict
          return df
     
     def GetBaseReact(self,ResultService : Any):
          [self.number_results,
           self.load_case,
           self.step_type,
           self.step_number,
           self.force_x,
           self.force_y,
           self.force_z,
           self.moment_x,
           self.moment_y,
           self.moment_z,
           self.x_coordinate,
           self.y_coordinate,
           self.z_coordinate,
           Successfulvalue] = ResultService.BaseReact(self.number_results,
                                                                 self.load_case, 
                                                                 self.step_type, 
                                                                 self.step_number,
                                                                 self.force_x,
                                                                 self.force_y,
                                                                 self.force_z,
                                                                 self.moment_x,
                                                                 self.moment_y,
                                                                 self.moment_z,
                                                                 self.x_coordinate,
                                                                 self.y_coordinate,
                                                                 self.z_coordinate)
@dataclass
class BaseReactWithCentroid:
    """Class for base_react_with_centroid return"""
    number_results         : int             = field(default_factory=int)
    load_case              : list[str]       = field(default_factory=list)
    step_type              : list[str]       = field(default_factory=list)
    step_number            : list[float]     = field(default_factory=list)
    force_x                : list[float]     = field(default_factory=list)
    force_y                : list[float]     = field(default_factory=list)
    force_z                : list[float]     = field(default_factory=list)
    moment_x               : list[float]     = field(default_factory=list)
    moment_y               : list[float]     = field(default_factory=list)
    moment_z               : list[float]     = field(default_factory=list)
    x_coordinate           : float           = field(default_factory=float)
    y_coordinate           : float           = field(default_factory=float)
    z_coordinate           : float           = field(default_factory=float)
    x_centroid_for_force_x : list[float]     = field(default_factory=list)
    y_centroid_for_force_x : list[float]     = field(default_factory=list)
    z_centroid_for_force_x : list[float]     = field(default_factory=list)
    x_centroid_for_force_y : list[float]     = field(default_factory=list)
    y_centroid_for_force_y : list[float]     = field(default_factory=list)
    z_centroid_for_force_y : list[float]     = field(default_factory=list)
    x_centroid_for_force_z : list[float]     = field(default_factory=list)
    y_centroid_for_force_z : list[float]     = field(default_factory=list)
    z_centroid_for_force_z : list[float]     = field(default_factory=list)
    
    def __repr__(self) -> str:
         return f"Load cases : {self.load_case}\nStep_type : {self.step_type}\nStep_number : {self.step_number}\nForce_x : {self.force_x}\nForce_y : {self.force_y}\nForce_z : {self.force_z}\nMoment_x : {self.moment_x}\nMoment_y : {self.moment_y}\nMoment_z : {self.moment_z}\nX_coordinate : {self.x_coordinate}\nY_coordinate : {self.y_coordinate}\nZ_coordinate : {self.z_coordinate}\nX_centroid_for_force_X : {self.x_centroid_for_force_x}\nY_centroid_for_force_X : {self.y_centroid_for_force_x}\nZ_centroid_for_force_X : {self.z_centroid_for_force_x}\nX_centroid_for_force_Y : {self.x_centroid_for_force_y}\nY_centroid_for_force_Y : {self.y_centroid_for_force_y}\nZ_centroid_for_force_Y : {self.z_centroid_for_force_y}\nX_centroid_for_force_Z : {self.x_centroid_for_force_z}\nY_centroid_for_force_Z : {self.y_centroid_for_force_z}\nZ_centroid_for_force_Z : {self.z_centroid_for_force_z}"  
      
    def to_dict(self) -> dict:
         return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
          dumydict = self.to_dict()
          df = DataFrame([dumydict["load_case"], dumydict["force_x"], dumydict["force_y"], dumydict["force_z"], dumydict["moment_x"], dumydict["moment_y"], dumydict["moment_z"]]).T
          df.columns = ["load_case","force_x","force_y","force_z","moment_x","moment_y","moment_z"]
          del dumydict
          return df
    
    def GetBaseReactWithCentroid(self,ResultService : Any) :
         [  self.number_results        , self.load_case             , self.step_type, self.step_number,
            self.force_x               , self.force_y               , self.force_z, 
            self.moment_x              , self.moment_y              , self.moment_z,
            self.x_coordinate          , self.y_coordinate          , self.z_coordinate,
            self.x_centroid_for_force_x, self.y_centroid_for_force_x, self.z_centroid_for_force_x,
            self.x_centroid_for_force_y, self.y_centroid_for_force_y, self.z_centroid_for_force_y,
            self.x_centroid_for_force_z, self.y_centroid_for_force_z, self.z_centroid_for_force_z,Successfulvalue] = ResultService.BaseReactWithCentroid(self.number_results        , self.load_case             , self.step_type, self.step_number,
                                                                                                                                                              self.force_x               , self.force_y               , self.force_z,
                                                                                                                                                              self.moment_x              , self.moment_y              , self.moment_z,
                                                                                                                                                              self.x_coordinate          , self.y_coordinate          , self.z_coordinate,
                                                                                                                                                              self.x_centroid_for_force_x, self.y_centroid_for_force_y, self.z_centroid_for_force_x,
                                                                                                                                                              self.x_centroid_for_force_y, self.y_centroid_for_force_y, self.z_centroid_for_force_y,
                                                                                                                                                              self.x_centroid_for_force_z, self.y_centroid_for_force_z, self.z_centroid_for_force_z)
@dataclass
class BucklingFactor:
    
    """TypedDict class for buckling_factor return"""
    
    number_results  : int          = field(default_factory=int)
    load_case       : list[str]    = field(default_factory=list)
    step_type       : list[str]    = field(default_factory=list)
    step_number     : list[float]  = field(default_factory=list)
    factor          : list[float]  = field(default_factory=list)
    
    def __repr__(self) -> str:
         return f"Load cases : {self.load_case}\nStep_type : {self.step_type}\nStep_number : {self.step_number}\nfactor : {self.factor}" 
       
    def to_dict(self) -> dict:
         return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
       dumydict = self.to_dict()
       df = DataFrame([dumydict["load_case"], dumydict["step_type"], dumydict["step_number"], dumydict["factor"]]).T
       df.columns = ["load_case","load_case","step_type","step_number","factor"]
       del dumydict
       return df
    
    def GetBucklingFactor(self,ResultService : Any):
         [self.number_results,self.load_case,self.step_type,self.step_number,self.factor,SuccessesfulValue] = ResultService.BucklingFactor(self.number_results,self.load_case,self.step_type,self.step_number,self.factor)
         if SuccessesfulValue != 0 or self.factor.__len__() == 0:
              raise CustomCommentError("Buckling faktör elde edilemedi...")
@dataclass
class JointDisplacement:
    """Class for joint_displacement 
    Parameters
     Name
          Type: System.String
          The name of an existing point object, point element, or group of objects depending on the value of the ItemTypeElm item. 
     ItemTypeElm
          Type: ETABSv1.eItemTypeElm
          This is one of the following items in the eItemTypeElm enumeration. 
          If this item is ObjectElm, the result request is for the point element corresponding to the point object specified by the Name item. 

          If this item is Element, the result request is for the point element specified by the Name item. 

          If this item is GroupElm, the result request is for all point elements directly or indirectly specified in the group specified by the Name item. 

          If this item is SelectionElm, the result request is for all point elements directly or indirectly selected and the Name item is ignored. 

     NumberResults
          Type: System.Int32
          The total number of results returned by the program. 
     Obj
          Type: System.String[]
          This is an array that includes the point object name associated with each result, if any. Some results will have no point object associated with them. For those cases, this item will be blank. 
     Elm
          Type: System.String[]
          This is an array that includes the point element name associated with each result. 
     LoadCase
          Type: System.String[]
          This is an array that includes the name of the analysis case or load combination associated with each result. 
     StepType
          Type: System.String[]
          This is an array that includes the step type, if any, for each result. 
     StepNum
          Type: System.Double[]
          This is an array that includes the step number, if any, for each result. 
     U1
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 1 direction for each result. [L] 
     U2
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 2 direction for each result. [L] 
     U3
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 3 direction for each result. [L] 
     R1
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 1 direction for each result. [rad] 
     R2
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 2 direction for each result. [rad] 
     R3
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 3 direction for each result. [rad] 

    """
    
    Name            : str          = field(default_factory=str)
    ItemType        : eItemTypeElm = field(default_factory=eItemTypeElm)
    Number_results  : int          = field(default_factory=int)
    Object_name     : list[str]    = field(default_factory=list)
    Element_name    : list[str]    = field(default_factory=list)
    Load_case       : list[str]    = field(default_factory=list)
    Step_type       : list[str]    = field(default_factory=list)
    Step_number     : list[float]  = field(default_factory=list)
    U1              : list[float]  = field(default_factory=list)
    U2              : list[float]  = field(default_factory=list)
    U3              : list[float]  = field(default_factory=list)
    R1              : list[float]  = field(default_factory=list)
    R2              : list[float]  = field(default_factory=list)
    R3              : list[float]  = field(default_factory=list)

    
    def __repr__(self) -> str:
         return f"name : {self.Element_name}\nload_case : {self.Load_case}\nU1 : {self.U1}\nU2 : {self.U2}\nU3 : {self.U3}\nR1 : {self.R1}\nR2 : {self.R2}\nR3 : {self.R3}" 
       
    def to_dict(self) -> dict:
         return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
       dumydict = self.to_dict()
       df = DataFrame([dumydict["Element_name"], dumydict["Load_case"], dumydict["U1"], dumydict["U2"], dumydict["U3"], dumydict["R1"], dumydict["R2"], dumydict["R3"]]).T
       df.columns = ["Element_name","Load_case","U1","U2","U3","R1","R2","R3"]
       del dumydict
       return df
    
    def GetJointDisplacement(self,ResultService : Any):
         [self.number_results, self.object_name, self.element_name, self.load_case, self.step_type,
          self.step_number   , self.U1    , self.U2     , self.U3  , self.R1, 
          self.R2, self.R3, SuccessesfulValue] = ResultService.JointDispl(self.name,self.itemType,self.number_results, self.object_name, self.element_name, self.load_case, self.step_type,
                                                                                               self.step_number   , self.U1    , self.U2     , self.U3  , self.R1,
                                                                                               self.R2, self.R3)
         if SuccessesfulValue != 0 or self.U1.__len__() == 0:
              raise CustomCommentError("...")
@dataclass
class JointDisplacementAbs:
    """Class for joint_displacement, Reports the absolute joint displacements for the specified point elements. 
    Absolute and relative displacements are the same except when reported for time history load cases subjected to acceleration loading  
    Parameters
     Name
          Type: System.String
          The name of an existing point object, point element, or group of objects depending on the value of the ItemTypeElm item. 
     ItemTypeElm
          Type: ETABSv1.eItemTypeElm
          This is one of the following items in the eItemTypeElm enumeration. 
          If this item is ObjectElm, the result request is for the point element corresponding to the point object specified by the Name item. 

          If this item is Element, the result request is for the point element specified by the Name item. 

          If this item is GroupElm, the result request is for all point elements directly or indirectly specified in the group specified by the Name item. 

          If this item is SelectionElm, the result request is for all point elements directly or indirectly selected and the Name item is ignored. 

     NumberResults
          Type: System.Int32
          The total number of results returned by the program. 
     Obj
          Type: System.String[]
          This is an array that includes the point object name associated with each result, if any. Some results will have no point object associated with them. For those cases, this item will be blank. 
     Elm
          Type: System.String[]
          This is an array that includes the point element name associated with each result. 
     LoadCase
          Type: System.String[]
          This is an array that includes the name of the analysis case or load combination associated with each result. 
     StepType
          Type: System.String[]
          This is an array that includes the step type, if any, for each result. 
     StepNum
          Type: System.Double[]
          This is an array that includes the step number, if any, for each result. 
     U1
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 1 direction for each result. [L] 
     U2
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 2 direction for each result. [L] 
     U3
          Type: System.Double[]
          This is a one dimensional array that includes the displacement in the point element local 3 direction for each result. [L] 
     R1
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 1 direction for each result. [rad] 
     R2
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 2 direction for each result. [rad] 
     R3
          Type: System.Double[]
          This is a one dimensional array that includes the rotation about the point element local 3 direction for each result. [rad] 

    """
    
    Name            : str          = field(default_factory=str)
    ItemType        : eItemTypeElm = field(default_factory=eItemTypeElm)
    Number_results  : int          = field(default_factory=int)
    Object_name     : list[str]    = field(default_factory=list)
    Element_name    : list[str]    = field(default_factory=list)
    Load_case       : list[str]    = field(default_factory=list)
    Step_type       : list[str]    = field(default_factory=list)
    Step_number     : list[float]  = field(default_factory=list)
    U1              : list[float]  = field(default_factory=list)
    U2              : list[float]  = field(default_factory=list)
    U3              : list[float]  = field(default_factory=list)
    R1              : list[float]  = field(default_factory=list)
    R2              : list[float]  = field(default_factory=list)
    R3              : list[float]  = field(default_factory=list)

    
    def __repr__(self) -> str:
         return f"name : {self.Element_name}\nload_case : {self.Load_case}\nU1 : {self.U1}\nU2 : {self.U2}\nU3 : {self.U3}\nR1 : {self.R1}\nR2 : {self.R2}\nR3 : {self.R3}" 
       
    def to_dict(self) -> dict:
         return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
       dumydict = self.to_dict()
       df = DataFrame([dumydict["Element_name"], dumydict["Load_case"], dumydict["U1"], dumydict["U2"], dumydict["U3"], dumydict["R1"], dumydict["R2"], dumydict["R3"]]).T
       df.columns = ["Element_name","Load_case","U1","U2","U3","R1","R2","R3"]
       del dumydict
       return df
    
    def GetJointDisplacementAbs(self,ResultService : Any):
         [self.number_results, self.object_name, self.element_name, self.load_case, self.step_type,
          self.step_number   , self.U1    , self.U2     , self.U3  , self.R1, 
          self.R2, self.R3, SuccessesfulValue] = ResultService.JointDisplAbs(self.name,self.itemType,self.number_results, self.object_name, self.element_name, self.load_case, self.step_type,
                                                                                               self.step_number   , self.U1    , self.U2     , self.U3  , self.R1,
                                                                                               self.R2, self.R3)
         if SuccessesfulValue != 0 or self.U1.__len__() == 0:
              raise CustomCommentError("...")
@dataclass
class StoryDrift:
     """Parameters
          NumberResults
               The total number of results returned by the program 
          Story
               This is an array of the story levels for each result 
          LoadCase
               This is an array of the names of the analysis case or load combination associated with each result 
          StepType
               This is an array of the step types, if any, for each result 
          StepNum
               This is an array of the step numbers, if any, for each result 
          Direction
               This is an array of the directions of the Drift values 
          Drift
               This is an array of the drift values 
          Label
               This is an array of the point labels for each result 
          Delta_X
               This is an array of the displacements in the X direction [L] 
          Delta_Y
               This is an array of the displacements in the Y direction [L] 
          Delta_Z
               This is an array of the displacements in the Z direction [L] 

     """
       
     NumberResults       : int     = field(default_factory=int)
     Story               : list[str]   = field(default_factory=list)
     LoadCase            : list[str]   = field(default_factory=list)
     StepType            : list[str]   = field(default_factory=list)
     StepNum             : list[float] = field(default_factory=list)
     Direction           : list[str]   = field(default_factory=list)
     Drift               : list[float] = field(default_factory=list)
     Label               : list[str]   = field(default_factory=list)
     Delta_X             : list[float] = field(default_factory=list)
     Delta_Y             : list[float] = field(default_factory=list)
     Delta_Z             : list[float] = field(default_factory=list)
     
     def __repr__(self) -> str:
          return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\nDirection : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["Story"], dumydict["LoadCase"], dumydict["Direction"], dumydict["Drift"], dumydict["Delta_X"], dumydict["Delta_Y"], dumydict["Delta_Z"]]).T
        df.columns = ["Story","LoadCase","Direction","Drift","Delta_X","Delta_Y","Delta_Z"]
        del dumydict
        return df
     
     def GetStoryDrift(self,ResultService : Any):
          [self.NumberResults,
           self.Story,
           self.LoadCase,
           self.StepType,
           self.StepNum,
           self.Direction,
           self.Drift,
           self.Label,
           self.Delta_X,
           self.Delta_Y,
           self.Delta_Z,
           Successfulvalue] = ResultService.StoryDrifts(self.NumberResults,
                                                                 self.Story,
                                                                 self.LoadCase,
                                                                 self.StepType,
                                                                 self.StepNum,
                                                                 self.Direction,
                                                                 self.Drift,
                                                                 self.Label,
                                                                 self.Delta_X,
                                                                 self.Delta_Y,
                                                                 self.Delta_Z,)

@dataclass
class ModalPeriod:
    """Class for modal_period return"""
    Number_results       : int             = field(default_factory=int)
    Load_case            : list[str]       = field(default_factory=list)
    Step_type            : list[str]       = field(default_factory=list)
    Step_number          : list[int]       = field(default_factory=list)
    Period               : list[float]     = field(default_factory=list)
    Frequency            : list[float]     = field(default_factory=list)
    Circular_frequency   : list[float]     = field(default_factory=list)
    Eigen_value          : list[float]     = field(default_factory=list)

    def __repr__(self) -> str:
         return f"Load cases : {self.Load_case}\nStep_type : {self.Step_type}\nStep_number : {self.Step_number}\nPeriod : {self.Period}\nFrequency : {self.Frequency}\nCircular_frequency : {self.Circular_frequency}\nEigen_value : {self.Eigen_value}"  
      
    def to_dict(self) -> dict:
         return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
       dumydict = self.to_dict()
       df = DataFrame([dumydict["Step_number"], dumydict["Period"], dumydict["Frequency"], dumydict["Circular_frequency"], dumydict["Eigen_value"]]).T
       df.columns = ["ModeNo","Period","Frequency","Circular_frequency","Eigen_value"]
       del dumydict
       return df
    
    
    
    def GetModalPeriod(self,ResultService : Any):
         [self.Number_results, self.Load_case, self.Step_type, self.Step_number,
         self.Period, self.Frequency, self.Circular_frequency, self.Eigen_value,Successfulvalue] = ResultService.ModalPeriod(self.Number_results, self.Load_case, self.Step_type, self.Step_number,
                                                                                                                                       self.Period, self.Frequency, self.Circular_frequency, self.Eigen_value)
@dataclass
class ModalLoadParticipationRatios:
     """Class for modal_load_participation_ratios, Reports the modal load participation ratios for each selected modal analysis case 
    
     Parameters
          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          LoadCase
               Type: System.String[]
               This is an array that includes the name of the modal load case associated with each result 
          ItemType
               Type: System.String[]
               This is an array that includes Load Pattern, Acceleration, Link or Panel Zone. It specifies the type of item for which the modal load participation is reported 
          Item
               Type: System.String[]
               This is an array whose values depend on the ItemType. If the ItemType is Load Pattern, this is the name of the load pattern. 
               If the ItemType is Acceleration, this is UX, UY, UZ, RX, RY, or RZ, indicating the acceleration direction. 

               If the ItemType is Link, this is the name of the link followed by U1, U2, U3, R1, R2, or R3 (in parenthesis), indicating the link degree of freedom for which the output is reported. 

               If the ItemType is Panel Zone, this is the name of the joint to which the panel zone is assigned, followed by U1, U2, U3, R1, R2, or R3 (in parenthesis), indicating the degree of freedom for which the output is reported. 

          Stat
               Type: System.Double[]
               This is an array that includes the percent static load participation ratio 
          Dyn
               Type: System.Double[]
               This is an array that includes the percent dynamic load participation ratio 
     """
     
     Number_results  : int          = field(default_factory=int)
     Load_case       : list[str]    = field(default_factory=list)
     Item_type       : list[str]    = field(default_factory=list)
     Item            : list[str]    = field(default_factory=list)
     Static_ratios   : list[float]  = field(default_factory=list)
     Dynamic_ratios  : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Load cases : {self.LoadCase}\nItemType : {self.ItemType}\Item : {self.Item}\nStatic_ratios : {self.Static_ratios}\nDynamic_ratios : {self.Dynamic_ratios}"
     
     def GetModalLoadParticipationRatios(self,ResultService : Any):
          [self.Number_results,
           self.Load_case,
           self.Item_type, 
           self.Item,
           self.Static_ratios, 
           self.Dynamic_ratios,
           SuccessfulValue] = ResultService.ModalLoadParticipationRatios(self.Number_results, 
                                                                              self.Load_case,
                                                                              self.Item_type, 
                                                                              self.Item,
                                                                              self.Static_ratios, 
                                                                              self.Dynamic_ratios)
     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["Load_case"], dumydict["Item_type"], dumydict["Item"], dumydict["Static_ratios"], dumydict["Dynamic_ratios"]]).T
        df.columns = ["Load_case","Item_type","Item","Static_ratios","Dynamic_ratios"]
        del dumydict
        return df
@dataclass
class ModalParticipatingMassRatios:
     """Class for modal_participating_mass_ratios, Reports the modal participating mass ratios for each mode of each selected modal analysis case 
     
     Parameters
          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          LoadCase
               Type: System.String[]
               This is an array that includes the name of the modal load case associated with each result 
          StepType
               Type: System.String[]
               This is an array that includes the step type, if any, for each result. For modal results, this will always be Mode 
          StepNum
               Type: System.Double[]
               This is an array that includes the step number for each result. For modal results, this is always the mode number 
          Period
               Type: System.Double[]
               This is an array that includes the period for each result. [s] 
          UX
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Ux degree of freedom. The ratio applies to the specified mode 
          UY
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Uy degree of freedom. The ratio applies to the specified mode 
          UZ
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Uz degree of freedom. The ratio applies to the specified mode 
          SumUX
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Ux degree of freedom 
          SumUY
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Uy degree of freedom 
          SumUZ
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Uz degree of freedom 
          RX
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Rx degree of freedom. The ratio applies to the specified mode 
          RY
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Ry degree of freedom. The ratio applies to the specified mode 
          RZ
               Type: System.Double[]
               This is an array that includes the modal participating mass ratio for the structure Rz degree of freedom. The ratio applies to the specified mode 
          SumRX
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Rx degree of freedom 
          SumRY
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Ry degree of freedom 
          SumRZ
               Type: System.Double[]
               This is an array that includes the cumulative sum of the modal participating mass ratios for the structure Rz degree of freedom 
     """
     
     Number_results  : int          = field(default_factory=int)
     Load_case       : list[str]    = field(default_factory=list)
     Step_type       : list[str]    = field(default_factory=list)
     Step_number     : list[float]  = field(default_factory=list)
     Period          : list[float]  = field(default_factory=list)
     Ux              : list[float]  = field(default_factory=list)
     Uy              : list[float]  = field(default_factory=list)
     Uz              : list[float]  = field(default_factory=list)
     Sum_Ux          : list[float]  = field(default_factory=list)
     Sum_Uy          : list[float]  = field(default_factory=list)
     Sum_Uz          : list[float]  = field(default_factory=list)
     Rx              : list[float]  = field(default_factory=list)
     Ry              : list[float]  = field(default_factory=list)
     Rz              : list[float]  = field(default_factory=list)
     Sum_Rx          : list[float]  = field(default_factory=list)
     Sum_Ry          : list[float]  = field(default_factory=list)
     Sum_Rz          : list[float]  = field(default_factory=list)


     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["Load_case"], 
                        dumydict["Step_number"], 
                        dumydict["Period"], 
                        dumydict["Sum_Ux"], 
                        dumydict["Sum_Uy"],
                        dumydict["Sum_Uz"],
                        dumydict["Sum_Rx"],
                        dumydict["Sum_Ry"],
                        dumydict["Sum_Rz"]]).T
        
        df.columns = ["Load_case","ModeNo","Period","Sum_Ux","Sum_Uy","Sum_Uz","Sum_Rx","Sum_Ry","Sum_Rz"]
        del dumydict
        return df
     
     def GetModalParticipatingMassRatios(self,ResultService : Any):
          [self.Number_results,
           self.Load_case,     
           self.Step_type ,    
           self.Step_number   ,
           self.Period       , 
           self.Ux       ,
           self.Uy       ,
           self.Uz     ,  
           self.Sum_Ux  , 
           self.Sum_Uy  , 
           self.Sum_Uz  , 
           self.Rx ,   
           self.Ry  ,  
           self.Rz  ,  
           self.Sum_Rx,
           self.Sum_Ry,
           self.Sum_Rz,
           Successfulvalue] = ResultService.ModalParticipatingMassRatios(self.Number_results,
                                                             self.Load_case,     
                                                             self.Step_type ,    
                                                             self.Step_number   ,
                                                             self.Period       , 
                                                             self.Ux       ,
                                                             self.Uy       ,
                                                             self.Uz     ,  
                                                             self.Sum_Ux  , 
                                                             self.Sum_Uy  , 
                                                             self.Sum_Uz  , 
                                                             self.Rx ,   
                                                             self.Ry  ,  
                                                             self.Rz  ,  
                                                             self.Sum_Rx,
                                                             self.Sum_Ry,
                                                             self.Sum_Rz,
                                                                 )
@dataclass
class ModalParticipationFactors:
     """Class for modal_participation_factors, Reports the modal participation factors for each mode of each selected modal analysis case 
     
     Parameters
          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          LoadCase
               Type: System.String[]
               This is an array that includes the name of the modal load case associated with each result 
          StepType
               Type: System.String[]
               This is an array that includes the step type, if any, for each result. For modal results, this will always be Mode 
          StepNum
               Type: System.Double[]
               This is an array that includes the step number for each result. For modal results, this is always the mode number 
          Period
               Type: System.Double[]
               This is an array that includes the period for each result. [s] 
          UX
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Ux degree of freedom. The ratio applies to the specified mode. [Fs2] 
          UY
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Uy degree of freedom. The ratio applies to the specified mode. [Fs2] 
          UZ
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Uz degree of freedom. The ratio applies to the specified mode. [Fs2] 
          RX
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Rx degree of freedom. The ratio applies to the specified mode. [FLs2] 
          RY
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Ry degree of freedom. The ratio applies to the specified mode. [FLs2] 
          RZ
               Type: System.Double[]
               This is an array that includes the modal participation factor for the structure Rz degree of freedom. The ratio applies to the specified mode. [FLs2] 
          ModalMass
               Type: System.Double[]
               This is an array that includes the modal mass for the specified mode. This is a measure of the kinetic energy in the structure as it is deforming in the specified mode. [FLs2] 
          ModalStiff
               Type: System.Double[]
               This is an array that includes the modal stiffness for the specified mode. This is a measure of the strain energy in the structure as it is deforming in the specified mode. [FL] 

     """
     Number_results  : int               = field(default_factory=int)
     Load_case       : list[str]         = field(default_factory=list)
     Step_type       : list[str]         = field(default_factory=list)
     Step_number     : list[float]       = field(default_factory=list)
     Period          : list[float]       = field(default_factory=list)
     Ux              : list[float]       = field(default_factory=list)
     Uy              : list[float]       = field(default_factory=list)
     Uz              : list[float]       = field(default_factory=list)
     Rx              : list[float]       = field(default_factory=list)
     Ry              : list[float]       = field(default_factory=list)
     Rz              : list[float]       = field(default_factory=list)
     Modal_mass      : list[float]       = field(default_factory=list)
     Modal_stiff     : list[float]       = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["Load_case"], 
                        dumydict["Step_number"], 
                        dumydict["Period"], 
                        dumydict["Ux"], 
                        dumydict["Uy"],
                        dumydict["Uz"],
                        dumydict["Rx"],
                        dumydict["Ry"],
                        dumydict["Rz"],
                        dumydict["Modal_mass"]]).T
        
        df.columns = ["Load_case","ModeNo","Period","Ux","Uy","Uz","Rx","Ry","Rz","Modal_mass"]
        del dumydict
        return df
     
     def GetModalParticipationFactors(self,ResultService : Any) -> None:
         [self.Number_results,
          self.Load_case     ,
          self.Step_type     ,
          self.Step_number   ,
          self.Period        ,
          self.Ux            ,
          self.Uy            ,
          self.Uz            ,
          self.Rx            ,
          self.Ry            ,
          self.Rz            ,
          self.Modal_mass    ,
          self.Modal_stiff   ,SuccessfulValue] = ResultService.ModalParticipationFactors(self.Number_results,
                                                                                               self.Load_case,     
                                                                                               self.Step_type,     
                                                                                               self.Step_number ,  
                                                                                               self.Period,        
                                                                                               self.Ux,            
                                                                                               self.Uy,            
                                                                                               self.Uz,            
                                                                                               self.Rx,            
                                                                                               self.Ry,            
                                                                                               self.Rz,            
                                                                                               self.Modal_mass,    
                                                                                               self.Modal_stiff   )
@dataclass
class ModeShape:
     Name           : str          = field(default="ALL")
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm) 
     NumberResults  : int          = field(default_factory=int) 
     Obj            : list[str]    = field(default_factory=list) 
     Elm            : list[str]    = field(default_factory=list) 
     LoadCase       : list[str]    = field(default_factory=list) 
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list)
     U1             : list[float]  = field(default_factory=list)
     U2             : list[float]  = field(default_factory=list)
     U3             : list[float]  = field(default_factory=list)
     R1             : list[float]  = field(default_factory=list)
     R2             : list[float]  = field(default_factory=list)
     R3             : list[float]  = field(default_factory=list)  

     def __post_init__(self) -> None:
          # self.GetModeShape()
          pass
     
     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["LoadCase"], 
                        dumydict["StepNum"], 
                        dumydict["Elm"], 
                        dumydict["U1"], 
                        dumydict["U2"],
                        dumydict["U3"],
                        dumydict["R1"],
                        dumydict["R2"],
                        dumydict["R3"]]).T
        
        df.columns = ["LoadCase","StepNum","Elm","U1","U2","U3","R1","R2","R3"]
        del dumydict
        return df
     
     def GetModeShape(self,ResultService : Any):
          [self.NumberResults,
          self.Obj,          
          self.Elm,          
          self.LoadCase,     
          self.StepType,     
          self.StepNum,      
          self.U1,           
          self.U2,           
          self.U3,           
          self.R1,           
          self.R2,           
          self.R3,SuccessfulValue] = ResultService.ModeShape(self.Name         ,
                                                                  self.ItemTypeElm  ,
                                                                  self.NumberResults,
                                                                  self.Obj          ,
                                                                  self.Elm          ,
                                                                  self.LoadCase     ,
                                                                  self.StepType     ,
                                                                  self.StepNum      ,
                                                                  self.U1           ,
                                                                  self.U2           ,
                                                                  self.U3           ,
                                                                  self.R1           ,
                                                                  self.R2           ,
                                                                  self.R3           )   

@dataclass
class PierForce:
     """Class for pir_force return
     
     Parameters
          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          StoryName
               Type: System.String[]
               The story name of the pier object 
          PierName
               Type: System.String[]
               The name of the pier object 
          LoadCase
               Type: System.String[]
               The names of the load case 
          Location
               Type: System.String[]
               The location on the pier, either "Top" or "Bottom", of the result being reported 
          P
               Type: System.Double[]
               The axial force [F] 
          V2
               Type: System.Double[]
               The shear force in the local 2 direction [F] 
          V3
               Type: System.Double[]
               The shear force in the local 3 direction [F] 
          T
               Type: System.Double[]
               The torsion [FL] 
          M2
               Type: System.Double[]
               The moment about the local 2 axis [FL] 
          M3
               Type: System.Double[]
               The moment about the local 3 axis [FL] 
               """
     Number_results  : int               = field(default_factory=int)
     Story_name      : list[str]         = field(default_factory=list)
     Pier_name       : list[str]         = field(default_factory=list)
     Load_case       : list[str]         = field(default_factory=list)
     Location        : list[str]         = field(default_factory=list)
     P               : list[float]       = field(default_factory=list)
     V2              : list[float]       = field(default_factory=list)
     V3              : list[float]       = field(default_factory=list)
     T               : list[float]       = field(default_factory=list)
     M2              : list[float]       = field(default_factory=list)
     M3              : list[float]       = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetPierForce(self,ResultService : Any) -> None:
         [self.Number_results,
          self.Story_name    ,
          self.Pier_name     ,
          self.Load_case     ,
          self.Location      ,
          self.P             ,
          self.V2            ,
          self.V3            ,
          self.T             ,
          self.M2            ,
          self.M3            ,SuccessfulValue] = ResultService.PierForce(  self.Number_results,
                                                                                self.Story_name    ,
                                                                                self.Pier_name     ,
                                                                                self.Load_case     ,
                                                                                self.Location      ,
                                                                                self.P             ,
                                                                                self.V2            ,
                                                                                self.V3            ,
                                                                                self.T             ,
                                                                                self.M2            ,
                                                                                self.M3            )
@dataclass
class SpandrelForce:
     """Class for spandrel_force return, Retrieves spandrel forces for any defined spandrel objects in the model 
     
     Parameters
          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          StoryName
               Type: System.String[]
               The story name of the spandrel object 
          SpandrelName
               Type: System.String[]
               The name of the spandrel object 
          LoadCase
               Type: System.String[]
               The names of the load case 
          Location
               Type: System.String[]
               The location on the spandrel, either "Left" or "Right", of the result being reported 
          P
               Type: System.Double[]
               The axial force [F] 
          V2
               Type: System.Double[]
               The shear force in the local 2 direction [F] 
          V3
               Type: System.Double[]
               The shear force in the local 3 direction [F] 
          T
               Type: System.Double[]
               The torsion [FL] 
          M2
               Type: System.Double[]
               The moment about the local 2 axis [FL] 
          M3
               Type: System.Double[]
               The moment about the local 3 axis [FL] 
     """
     Number_results  : int               = field(default_factory=int)
     Story_name      : list[str]         = field(default_factory=list)
     Spandrel_name   : list[str]         = field(default_factory=list)
     Load_case       : list[str]         = field(default_factory=list)
     Location        : list[str]         = field(default_factory=list)
     P               : list[float]       = field(default_factory=list)
     V2              : list[float]       = field(default_factory=list)
     V3              : list[float]       = field(default_factory=list)
     T               : list[float]       = field(default_factory=list)
     M2              : list[float]       = field(default_factory=list)
     M3              : list[float]       = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetSpandrelForce(self,ResultService : Any):
         [self.Number_results,
          self.Story_name    ,
          self.Spandrel_name ,
          self.Load_case     ,
          self.Location      ,
          self.P             ,
          self.V2            ,
          self.V3            ,
          self.T             ,
          self.M2            ,
          self.M3            ,SuccessfulValue] = ResultService.SpandrelForce(self.Number_results,
                                                                                  self.Story_name    ,
                                                                                  self.Spandrel_name ,
                                                                                  self.Load_case     ,
                                                                                  self.Location      ,
                                                                                  self.P             ,
                                                                                  self.V2            ,
                                                                                  self.V3            ,
                                                                                  self.T             ,
                                                                                  self.M2            ,
                                                                                  self.M3             )      
@dataclass
class SectionCutAnalysis:
     """Class for section_cut_analysis, Reports the section cut force for sections cuts that are specified to have an Analysis (F1, F2, F3, M1, M2, M3) result type 
     Parameters
          NumberResults
               Type: System.Int32
               The number total of results returned by the program 
          SCut
               Type: System.String[]
               This is an array that includes the name of the section cut associated with each result 
          LoadCase
               Type: System.String[]
               This is an array that includes the name of the analysis case or load combination associated with each result. 
          StepType
               Type: System.String[]
               This is an array that includes the step type, if any, for each result. 
          StepNum
               Type: System.Double[]
               This is an array that includes the step number, if any, for each result. 
          F1
               Type: System.Double[]
               This is an array that includes the force in the section cut local 1-axis directions for each result. [F] 
          F2
               Type: System.Double[]
               This is an array that includes the force in the section cut local 2-axis directions for each result. [F] 
          F3
               Type: System.Double[]
               This is an array that includes the force in the section cut local 3-axis directions for each result. [F] 
          M1
               Type: System.Double[]
               This is an array that includes the moment about the section cut local 1-axis for each result. [FL] 
          M2
               Type: System.Double[]
               This is an array that includes the moment about the section cut local 1-axis for each result. [FL] 
          M3
               Type: System.Double[]
               This is an array that includes the moment about the section cut local 1-axis for each result. [FL] 
     """
     NumberResults  : int             = field(default_factory=int)
     SCut           : list[str]       = field(default_factory=list)
     LoadCase       : list[str]       = field(default_factory=list)
     StepType       : list[str]       = field(default_factory=list)
     StepNum        : list[float]     = field(default_factory=list)
     F1             : list[float]     = field(default_factory=list)
     F2             : list[float]     = field(default_factory=list)
     F3             : list[float]     = field(default_factory=list)
     M1             : list[float]     = field(default_factory=list)
     M2             : list[float]     = field(default_factory=list)
     M3             : list[float]     = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetSectionCutAnalysis(self,ResultService : Any):
         
         [self.NumberResults, 
          self.SCut,          
          self.LoadCase,      
          self.StepType,      
          self.StepNum,       
          self.F1,            
          self.F2,            
          self.F3,            
          self.M1,            
          self.M2,            
          self.M3,SuccessfulValue] = ResultService.SectionCutAnalysis(self.NumberResults, 
                                                                           self.SCut,          
                                                                           self.LoadCase,      
                                                                           self.StepType,      
                                                                           self.StepNum,       
                                                                           self.F1,            
                                                                           self.F2,            
                                                                           self.F3,            
                                                                           self.M1,            
                                                                           self.M2,            
                                                                           self.M3)
@dataclass
class SectionCutDesign:
     """Class for section_cut_design return, Reports the section cut force for sections cuts that are specified to have a Design (P, V2, V3, T, M2, M3) result type """
     NumberResults  : int               = field(default_factory=int)
     SCut           : list[str]         = field(default_factory=list)
     LoadCase       : list[str]         = field(default_factory=list)
     StepType       : list[str]         = field(default_factory=list)
     StepNum        : list[float]       = field(default_factory=list)
     P              : list[float]       = field(default_factory=list)
     V2             : list[float]       = field(default_factory=list)
     V3             : list[float]       = field(default_factory=list)
     T              : list[float]       = field(default_factory=list)
     M2             : list[float]       = field(default_factory=list)
     M3             : list[float]       = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetSectionCutDesign(self,ResultService : Any):
         [self.ResultService,  
          self.NumberResults,  
          self.SCut         ,  
          self.LoadCase     ,  
          self.StepType     ,  
          self.StepNum      ,  
          self.P            ,  
          self.V2           ,  
          self.V3           ,  
          self.T            ,  
          self.M2           ,  
          self.M3           ,SuccessfullValue  ] = ResultService.SectionCutDesign(   self.ResultService,  
                                                                                          self.NumberResults,  
                                                                                          self.SCut         ,  
                                                                                          self.LoadCase     ,  
                                                                                          self.StepType     ,  
                                                                                          self.StepNum      ,  
                                                                                          self.P            ,  
                                                                                          self.V2           ,  
                                                                                          self.V3           ,  
                                                                                          self.T            ,  
                                                                                          self.M2           ,  
                                                                                          self.M3           )



# Tamamlanmayanlar    

@dataclass
class AreaForceShell:
     """Reports the area forces for the specified area elements that are assigned shell section properties (not plane or asolid properties). Note that the forces reported are per unit of in-plane length. 

          Args:
               Name
                    Type: String
                    The name of an existing area object, area element or group of objects, depending on the value of the ItemTypeElm item 
               ItemTypeElm
                    Type: ETABSv1.eItemTypeElm
                    This is one of the following items in the eItemTypeElm enumeration. 
                    If this item is ObjectElm, the result request is for the area elements corresponding to the area object specified by the Name item. 

                    If this item is Element, the result request is for the area element specified by the Name item. 

                    If this item is GroupElm, the result request is for the area elements corresponding to all area objects included in the group specified by the Name item. 

                    If this item is SelectionElm, the result request is for area elements corresponding to all selected area objects and the Name item is ignored. 

               NumberResults
                    Type: Int32
                    The total number of results returned by the program 
               Obj
                    Type: String[]
                    This is an array that includes the area object name associated with each result, if any 
               Elm
                    Type: String[]
                    This is an array that includes the area element name associated with each result 
               PointElm
                    Type: String[]
                    This is an array that includes the name of the point element where the results are reported 
               LoadCase
                    Type: String[]
                    This is an array that includes the name of the analysis case or load combination associated with each result 
               StepType
                    Type: String[]
                    This is an array that includes the step type, if any, for each result 
               StepNum
                    Type: Double[]
                    This is an array that includes the step number, if any, for each result 
               F11
                    Type: Double[]
                    The area element internal F11 membrane direct force per length reported in the area element local coordinate  [F/L] 
               F22
                    Type: Double[]
                    The area element internal F22 membrane direct force per length reported in the area element local coordinate  [F/L] 
               F12
                    Type: Double[]
                    The area element internal F12 membrane shear force per length reported in the area element local coordinate  [F/L] 
               FMax
                    Type: Double[]
                    The maximum principal membrane force per length. [F/L] 
               FMin
                    Type: Double[]
                    The minimum principal membrane force per length. [F/L] 
               FAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of the maximum principal membrane force. [deg] 
               FVM
                    Type: Double[]
                    The area element internal Von Mises membrane force per length. [F/L] 
               M11
                    Type: Double[]
                    The area element internal M11 plate bending moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               M22
                    Type: Double[]
                    The area element internal M22 plate bending moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               M12
                    Type: Double[]
                    The area element internal M12 plate twisting moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MMax
                    Type: Double[]
                    The maximum principal plate moment per length. This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MMin
                    Type: Double[]
                    The minimum principal plate moment per length. This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of the maximum principal plate moment. This item is only reported for area elements with properties that allow plate bending behavior. [deg] 
               V13
                    Type: Double[]
                    The area element internal V13 plate transverse shear force per length reported in the area element local coordinate system. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               V23
                    Type: Double[]
                    The area element internal V23 plate transverse shear force per length reported in the area element local coordinate system. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               VMax
                    Type: Double[]
                    The maximum plate transverse shear force. It is equal to the square root of the sum of the squares of V13 and V23. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               VAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of Vmax. This item is only reported for area elements with properties that allow plate bending behavior. [deg] 

     """
     Name           : str          = field(default_factory=str)
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : list[int  ]  = field(default_factory=int)
     Obj            : list[str  ]  = field(default_factory=list)
     Elm            : list[str  ]  = field(default_factory=list) 
     PointElm       : list[str  ]  = field(default_factory=list) 
     LoadCase       : list[str  ]  = field(default_factory=list) 
     StepType       : list[str  ]  = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list)
     F11            : list[float]  = field(default_factory=list)
     F22            : list[float]  = field(default_factory=list)
     F12            : list[float]  = field(default_factory=list)
     FMax           : list[float]  = field(default_factory=list)
     FMin           : list[float]  = field(default_factory=list) 
     FAngle         : list[float]  = field(default_factory=list) 
     FVM            : list[float]  = field(default_factory=list) 
     M11            : list[float]  = field(default_factory=list) 
     M22            : list[float]  = field(default_factory=list) 
     M12            : list[float]  = field(default_factory=list) 
     MMax           : list[float]  = field(default_factory=list) 
     MMin           : list[float]  = field(default_factory=list) 
     MAngle         : list[float]  = field(default_factory=list) 
     V13            : list[float]  = field(default_factory=list) 
     V23            : list[float]  = field(default_factory=list)
     VMax           : list[float]  = field(default_factory=list)
     VAngle         : list[float]  = field(default_factory=list) 

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetAreaForceShell(self,ResultService : Any) -> None:
          [self.NumberResults,
           self.Obj          ,
           self.Elm          ,
           self.PointElm     ,
           self.LoadCase     ,
           self.StepType     ,
           self.StepNum      ,
           self.F11          ,
           self.F22          ,
           self.F12          ,
           self.FMax         ,
           self.FMin         ,
           self.FAngle       ,
           self.FVM          ,
           self.M11          ,
           self.M22          ,
           self.M12          ,
           self.MMax         ,
           self.MMin         ,
           self.MAngle       ,
           self.V13          ,
           self.V23          ,
           self.VMax         ,
           self.VAngle,SuccessfullValue] = ResultService.AreaForceShell(self.Name         ,
                                                                      self.ItemTypeElm  ,
                                                                      self.NumberResults,
                                                                      self.Obj          ,
                                                                      self.Elm          ,
                                                                      self.PointElm     ,
                                                                      self.LoadCase     ,
                                                                      self.StepType     ,
                                                                      self.StepNum      ,
                                                                      self.F11          ,
                                                                      self.F22          ,
                                                                      self.F12          ,
                                                                      self.FMax         ,
                                                                      self.FMin         ,
                                                                      self.FAngle       ,
                                                                      self.FVM          ,
                                                                      self.M11          ,
                                                                      self.M22          ,
                                                                      self.M12          ,
                                                                      self.MMax         ,
                                                                      self.MMin         ,
                                                                      self.MAngle       ,
                                                                      self.V13          ,
                                                                      self.V23          ,
                                                                      self.VMax         ,
                                                                      self.VAngle       )

@dataclass
class AreaJointForceShell :
     """Reports the area joint forces for the point elements at each corner of the specified area elements that have shell-type properties 
     Parameters
Name
Type: System.String
The name of an existing area object, area element or group of objects, depending on the value of the ItemTypeElm item 
ItemTypeElm
Type: ETABSv1.eItemTypeElm
This is one of the following items in the eItemTypeElm enumeration. 
If this item is ObjectElm, the result request is for the area elements corresponding to the area object specified by the Name item. 

If this item is Element, the result request is for the area element specified by the Name item. 

If this item is GroupElm, the result request is for the area elements corresponding to all area objects included in the group specified by the Name item. 

If this item is SelectionElm, the result request is for area elements corresponding to all selected area objects and the Name item is ignored. 

NumberResults
Type: System.Int32
The total number of results returned by the program 
Obj
Type: System.String[]
This is an array that includes the area object name associated with each result, if any 
Elm
Type: System.String[]
This is an array that includes the area element name associated with each result 
PointElm
Type: System.String[]
This is an array that includes the name of the point element where the results are reported 
LoadCase
Type: System.String[]
This is an array that includes the name of the analysis case or load combination associated with each result 
StepType
Type: System.String[]
This is an array that includes the step type, if any, for each result 
StepNum
Type: System.Double[]
This is an array that includes the step number, if any, for each result 
F1
Type: System.Double[]
This is an array that contains the joint force component in the point element local 1 axis direction. [F].
F2
Type: System.Double[]
This is an array that contains the joint force component in the point element local 2 axis direction. [F].
F3
Type: System.Double[]
This is an array that contains the joint force component in the point element local 3 axis direction. [F].
M1
Type: System.Double[]
This is an array that contains the joint moment component about the point element local 1 axis direction. [FL].
M2
Type: System.Double[]
This is an array that contains the joint moment component about the point element local 2 axis direction. [FL].
M3
Type: System.Double[]
This is an array that contains the joint moment component about the point element local 3 axis direction. [FL].
     """
     Name                : str          = field(default_factory=str)
     ItemTypeElm         : eItemTypeElm = field(default_factory=eItemTypeElm) 
     NumberResults       : int         = field(default_factory=list)
     Obj                 : list[str]   = field(default_factory=list)
     Elm                 : list[str]   = field(default_factory=list)
     PointElm            : list[str]   = field(default_factory=list)
     LoadCase            : list[str]   = field(default_factory=list)
     StepType            : list[str]   = field(default_factory=list)
     StepNum             : list[float] = field(default_factory=list) 
     F1                  : list[float] = field(default_factory=list) 
     F2                  : list[float] = field(default_factory=list)
     F3                  : list[float] = field(default_factory=list)
     M1                  : list[float] = field(default_factory=list)
     M2                  : list[float] = field(default_factory=list)
     M3                  : list[float] = field(default_factory=list)

@dataclass
class AreaStrainShell : 
        Name             : str          = field(default_factory=str) 
        ItemTypeElm      : eItemTypeElm =field(default_factory=eItemTypeElm)
        NumberResults    : list[int]   = field(default_factory=list)
        obj              : list[str]   = field(default_factory=list)
        elm              : list[str]   = field(default_factory=list) 
        PointElm         : list[str]   = field(default_factory=list) 
        LoadCase         : list[str]   = field(default_factory=list) 
        StepType         : list[str]   = field(default_factory=list) 
        StepNum          : list[float] = field(default_factory=list) 
        e11top           : list[float] = field(default_factory=list) 
        e22top           : list[float] = field(default_factory=list) 
        g12top           : list[float] = field(default_factory=list) 
        emaxtop          : list[float] = field(default_factory=list) 
        emintop          : list[float] = field(default_factory=list) 
        eangletop        : list[float] = field(default_factory=list) 
        evmtop           : list[float] = field(default_factory=list) 
        e11bot           : list[float] = field(default_factory=list) 
        e22bot           : list[float] = field(default_factory=list) 
        g12bot           : list[float] = field(default_factory=list) 
        emaxbot          : list[float] = field(default_factory=list) 
        eminbot          : list[float] = field(default_factory=list) 
        eanglebot        : list[float] = field(default_factory=list) 
        evmbot           : list[float] = field(default_factory=list) 
        g13avg           : list[float] = field(default_factory=list) 
        g23avg           : list[float] = field(default_factory=list) 
        gmaxavg          : list[float] = field(default_factory=list) 
        gangleavg        : list[float] = field(default_factory=list)

@dataclass
class AreaStrainShellLayered : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm) 
     NumberResults  : int          = field(default_factory=int) 
     obj            : list[str]    = field(default_factory=list)
     elm            : list[str]    = field(default_factory=list)
     Layer          : list[str]    = field(default_factory=list)
     IntPtNum       : list[int]    = field(default_factory=list) 
     IntPtLoc       : list[float]  = field(default_factory=list) 
     PointElm       : list[str]    = field(default_factory=list) 
     LoadCase       : list[str]    = field(default_factory=list) 
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list)
     E11            : list[float]  = field(default_factory=list)
     E22            : list[float]  = field(default_factory=list)
     G12            : list[float]  = field(default_factory=list)
     EMax           : list[float]  = field(default_factory=list)
     EMin           : list[float]  = field(default_factory=list)
     EAngle         : list[float]  = field(default_factory=list)
     EVM            : list[float]  = field(default_factory=list)
     G13avg         : list[float]  = field(default_factory=list)
     G23avg         : list[float]  = field(default_factory=list)
     GMaxavg        : list[float]  = field(default_factory=list)
     GAngleavg      : list[float]  = field(default_factory=list)

@dataclass
class AreaStressShell : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm) 
     NumberResults  : int         = field(default_factory=int)
     Obj            : list[str]   = field(default_factory=list)
     Elm            : list[str]   = field(default_factory=list)
     PointElm       : list[str]   = field(default_factory=list)
     LoadCase       : list[str]   = field(default_factory=list)
     StepType       : list[str]   = field(default_factory=list)
     StepNum        : list[float] = field(default_factory=list)
     S11Top         : list[float] = field(default_factory=list)
     S22Top         : list[float] = field(default_factory=list)
     S12Top         : list[float] = field(default_factory=list)
     SMaxTop        : list[float] = field(default_factory=list)
     SMinTop        : list[float] = field(default_factory=list)
     SAngleTop      : list[float] = field(default_factory=list)
     SVMTop         : list[float] = field(default_factory=list)
     S11Bot         : list[float] = field(default_factory=list)
     S22Bot         : list[float] = field(default_factory=list)
     S12Bot         : list[float] = field(default_factory=list)
     SMaxBot        : list[float] = field(default_factory=list)
     SMinBot        : list[float] = field(default_factory=list)
     SAngleBot      : list[float] = field(default_factory=list)
     SVMBot         : list[float] = field(default_factory=list)
     S13Avg         : list[float] = field(default_factory=list)
     S23Avg         : list[float] = field(default_factory=list)
     SMaxAvg        : list[float] = field(default_factory=list)
     SAngleAvg      : list[float] = field(default_factory=list)

@dataclass
class AreaStressShellLayered : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm) 
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list) 
     Elm            : list[str]    = field(default_factory=list) 
     Layer          : list[str]    = field(default_factory=list)
     IntPtNum       : list[int]    = field(default_factory=list) 
     IntPtLoc       : list[float]  = field(default_factory=list)
     PointElm       : list[str]    = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float] = field(default_factory=list)
     S11            : list[float] = field(default_factory=list)
     S22            : list[float] = field(default_factory=list)
     S12            : list[float] = field(default_factory=list)
     SMax           : list[float] = field(default_factory=list)
     SMin           : list[float] = field(default_factory=list)
     SAngle         : list[float] = field(default_factory=list)
     SVM            : list[float] = field(default_factory=list)
     S13Avg         : list[float] = field(default_factory=list)
     S23Avg         : list[float] = field(default_factory=list)
     SMaxAvg        : list[float] = field(default_factory=list)
     SAngleAvg      : list[float] = field(default_factory=list)

@dataclass
class AssembledJointMass : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int) 
     PointElm       : list[str  ]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list)
     U2             : list[float]  = field(default_factory=list)
     U3             : list[float]  = field(default_factory=list)
     R1             : list[float]  = field(default_factory=list)
     R2             : list[float]  = field(default_factory=list)
     R3             : list[float]  = field(default_factory=list)

     def __post_init__(self) -> None:
          self.GetAssembledJointMass()
     
     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetAssembledJointMass(self):
          [self.NumberResults,
           self.PointElm     ,
           self.U1           ,
           self.U2           ,
           self.U3           ,
           self.R1           ,
           self.R2           ,
           self.R3,SuccessfulValue] = self.ResultService.AssembledJointMass(self.Name         ,
                                                                            self.ItemTypeElm  ,
                                                                            self.NumberResults,
                                                                            self.PointElm     ,
                                                                            self.U1           ,
                                                                            self.U2           ,
                                                                            self.U3           ,
                                                                            self.R1           ,
                                                                            self.R2           ,
                                                                            self.R3           )

@dataclass
class AssembledJointMass_1 : 
     MassSourceName : str          = field(default_factory=str) 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int) 
     PointElm       : list[str  ]  = field(default_factory=list) 
     MassSource     : list[str  ]  = field(default_factory=list)
     U1             : list[float]  = field(default_factory=list)
     U2             : list[float]  = field(default_factory=list)
     U3             : list[float]  = field(default_factory=list)
     R1             : list[float]  = field(default_factory=list)
     R2             : list[float]  = field(default_factory=list)
     R3             : list[float]  = field(default_factory=list)

     def __post_init__(self) -> None:
          self.GetAssembledJointMass_1()
     
     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetAssembledJointMass_1(self):
          [self.NumberResults,
           self.PointElm     ,
           self.MassSource,
           self.U1           ,
           self.U2           ,
           self.U3           ,
           self.R1           ,
           self.R2           ,
           self.R3,SuccessfulValue] = self.ResultService.AssembledJointMass_1(self.Name         ,
                                                                            self.ItemTypeElm  ,
                                                                            self.NumberResults,
                                                                            self.PointElm     ,
                                                                            self.MassSource,
                                                                            self.U1           ,
                                                                            self.U2           ,
                                                                            self.U3           ,
                                                                            self.R1           ,
                                                                            self.R2           ,
                                                                            self.R3           )

@dataclass
class FrameForce : 
     """
     Parameters
          Name
               Type: System.String
               The name of an existing line object, line element or group of objects, depending on the value of the ItemTypeElm item. 
          ItemTypeElm
               Type: ETABSv1.eItemTypeElm
               This is one of the following items in the eItemTypeElm enumeration. 
               If this item is ObjectElm, the result request is for the line elements corresponding to the line object specified by the Name item.    

               If this item is Element, the result request is for the line element specified by the Name item. 

               If this item is GroupElm, the result request is for the line elements corresponding to all line objects included in the group specified by the Name item. 

               If this item is SelectionElm, the result request is for line elements corresponding to all selected line objects and the Name item is ignored. 

          NumberResults
               Type: System.Int32
               The total number of results returned by the program 
          Obj
               Type: System.String[]
               This is an array that includes the line object name associated with each result, if any 
          ObjSta
               Type: System.Double[]
               This is an array that includes the distance measured from the I-end of the line object to the result location 
          Elm
               Type: System.String[]
               This is an array that includes the line element name associated with each result 
          ElmSta
               Type: System.Double[]
               This is an array that includes the distance measured from the I-end of the line element to the result location 
          LoadCase
               Type: System.String[]
               This is an array that includes the name of the analysis case or load combination associated with each result 
          StepType
               Type: System.String[]
               This is an array that includes the step type, if any, for each result 
          StepNum
               Type: System.Double[]
               This is an array that includes the step number, if any, for each result 
          P
               Type: System.Double[]
               This is a one dimensional array of the axial force for each result. [F] 
          V2
               Type: System.Double[]
               This is a one dimensional array of the shear force in the local 2 direction for each result. [F] 
          V3
               Type: System.Double[]
               This is a one dimensional array of the shear force in the local 3 direction for each result. [F] 
          T
               Type: System.Double[]
               This is a one dimensional array of the torsion for each result. [FL] 
          M2
               Type: System.Double[]
               This is a one dimensional array of the moment about the local 2-axis for each result. [FL] 
          M3
               Type: System.Double[]
               This is a one dimensional array of the moment about the local 3-axis for each result. [FL] 
     """
     Name           : str          = field(default_factory=str)           
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)
     ObjSta         : list[float]  = field(default_factory=list)
     Elm            : list[str]    = field(default_factory=list)
     ElmSta         : list[float]  = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     P              : list[float]  = field(default_factory=list)
     V2             : list[float]  = field(default_factory=list)
     V3             : list[float]  = field(default_factory=list)
     T              : list[float]  = field(default_factory=list)
     M2             : list[float]  = field(default_factory=list)
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        df = DataFrame([dumydict["Elm"], 
                        dumydict["ElmSta"], 
                        dumydict["LoadCase"], 
                        dumydict["P"], 
                        dumydict["V2"],
                        dumydict["V3"],
                        dumydict["T"],
                        dumydict["M2"],
                        dumydict["M3"]]).T
        
        df.columns = ["Element","Element Location","LoadCase","P","V2","V3","T","M2","M3"]
        del dumydict
        return df
     
     def GetFrameForce(self,ResultService : Any):
          [self.NumberResults,
           self.Obj     ,     
           self.ObjSta  ,     
           self.Elm     ,     
           self.ElmSta  ,     
           self.LoadCase,     
           self.StepType,     
           self.StepNum ,     
           self.P       ,     
           self.V2      ,     
           self.V3      ,     
           self.T       ,     
           self.M2      ,     
           self.M3      ,SuccessfulValue ] = ResultService.FrameForce(self.Name       ,
                                                                           self.ItemTypeElm,
                                                                           self.NumberResults,
                                                                           self.Obj     ,
                                                                           self.ObjSta  ,
                                                                           self.Elm     ,
                                                                           self.ElmSta  ,
                                                                           self.LoadCase,
                                                                           self.StepType,
                                                                           self.StepNum ,
                                                                           self.P       ,
                                                                           self.V2      ,
                                                                           self.V3      ,
                                                                           self.T       ,
                                                                           self.M2      ,
                                                                           self.M3       )
@dataclass
class FrameJointForce : 
     Name           : str          = field(default_factory=str)           
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)
     Elm            : list[str]    = field(default_factory=list)
     PointElm       : list[float]  = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     F1             : list[float]  = field(default_factory=list)
     F2             : list[float]  = field(default_factory=list)
     F3             : list[float]  = field(default_factory=list)
     M1             : list[float]  = field(default_factory=list)
     M2             : list[float]  = field(default_factory=list)
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetFrameJointForce(self,ResultService : Any):
          [self.NumberResults,
          self.Obj          ,
          self.Elm          ,
          self.PointElm     ,
          self.LoadCase     ,
          self.StepType     ,
          self.StepNum      ,
          self.F1           ,
          self.F2           ,
          self.F3           ,
          self.M1           ,
          self.M2           ,
          self.M3           ,SuccessfulValue] = ResultService.FrameJointForce(self.Name         ,
                                                                                     self.ItemTypeElm  ,
                                                                                     self.NumberResults,
                                                                                     self.Obj          ,
                                                                                     self.Elm          ,
                                                                                     self.PointElm     ,
                                                                                     self.LoadCase     ,
                                                                                     self.StepType     ,
                                                                                     self.StepNum      ,
                                                                                     self.F1           ,
                                                                                     self.F2           ,
                                                                                     self.F3           ,
                                                                                     self.M1           ,
                                                                                     self.M2           ,
                                                                                     self.M3            )
@dataclass
class GeneralizedDispl : 
     Name           : str          = field(default_factory=str) 
     NumberResults  : int          = field(default_factory=int)  
     GD             : list[str]   = field(default_factory=list)
     LoadCase       : list[str]   = field(default_factory=list)
     StepType       : list[str]   = field(default_factory=list)
     StepNum        : list[float] = field(default_factory=list)
     DType          : list[str]   = field(default_factory=list)
     Value          : list[float] = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetGeneralizedDispl(self,ResultService : Any):
          pass

@dataclass
class JointAcc : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list) 
     Elm            : list[str]    = field(default_factory=list) 
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list) 

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointAcc(self,ResultService : Any):
          pass
@dataclass
class JointAccAbs : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointAccAbs(self,ResultService : Any):
          pass
@dataclass
class JointDisplAbs : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointDisplAbs(self,ResultService : Any):
          pass
@dataclass
class JointDrifts : 
     NumberResults  : int          = field(default_factory=int) 
     Story          : list[str]    = field(default_factory=list)
     Label          : list[str]    = field(default_factory=list)
     Name           : list[str]    = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     DisplacementX  : list[float]  = field(default_factory=list)
     DisplacementY  : list[float]  = field(default_factory=list)
     DriftX         : list[float]  = field(default_factory=list)
     DriftY         : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointDrifts(self,ResultService : Any):
          pass
@dataclass
class JointReact : 
     Name           : str          = field(default_factory=str)           
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)
     Elm            : list[str]    = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     F1             : list[float]  = field(default_factory=list)
     F2             : list[float]  = field(default_factory=list)
     F3             : list[float]  = field(default_factory=list)
     M1             : list[float]  = field(default_factory=list)
     M2             : list[float]  = field(default_factory=list)
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointReact(self,ResultService : Any):
          pass
@dataclass
class JointVel : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointVel(self,ResultService : Any):
          pass
@dataclass
class JointVelAbs : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetJointVelAbs(self,ResultService : Any):
          pass
@dataclass
class LinkDeformation : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetLinkDeformation(self,ResultService : Any):
          pass
@dataclass
class LinkForce : 
     Name           : str          = field(default_factory=str)           
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list)
     Elm            : list[str]    = field(default_factory=list)
     PointElm       : list[str]  = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     P              : list[float]  = field(default_factory=list)
     V2             : list[float]  = field(default_factory=list)
     V3             : list[float]  = field(default_factory=list)
     T              : list[float]  = field(default_factory=list)
     M2             : list[float]  = field(default_factory=list)
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetLinkForce(self,ResultService : Any):
          pass
@dataclass
class LinkJointForce : 
     Name           : str          = field(default_factory=str)
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Obj            : list[str]    = field(default_factory=list) 
     Elm            : list[str]    = field(default_factory=list) 
     PointElm       : list[str]    = field(default_factory=list) 
     LoadCase       : list[str]    = field(default_factory=list) 
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     F1             : list[float]  = field(default_factory=list) 
     F2             : list[float]  = field(default_factory=list) 
     F3             : list[float]  = field(default_factory=list) 
     M1             : list[float]  = field(default_factory=list) 
     M2             : list[float]  = field(default_factory=list) 
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetLinkJointForce(self,ResultService : Any):
          pass
@dataclass
class PanelZoneDeformation : 
     Name           : str          = field(default_factory=str) 
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)  
     Elm            : list[str]    = field(default_factory=list)  
     LoadCase       : list[str]    = field(default_factory=list)  
     StepType       : list[str]    = field(default_factory=list) 
     StepNum        : list[float]  = field(default_factory=list) 
     U1             : list[float]  = field(default_factory=list) 
     U2             : list[float]  = field(default_factory=list) 
     U3             : list[float]  = field(default_factory=list) 
     R1             : list[float]  = field(default_factory=list) 
     R2             : list[float]  = field(default_factory=list) 
     R3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetPanelZoneDeformation(self,ResultService : Any):
          pass
@dataclass
class PanelZoneForce : 
     Name           : str          = field(default_factory=str)           
     ItemTypeElm    : eItemTypeElm = field(default_factory=eItemTypeElm)
     NumberResults  : int          = field(default_factory=int)
     Elm            : list[str]    = field(default_factory=list)
     PointElm       : list[str]    = field(default_factory=list)
     LoadCase       : list[str]    = field(default_factory=list)
     StepType       : list[str]    = field(default_factory=list)
     StepNum        : list[float]  = field(default_factory=list)
     P              : list[float]  = field(default_factory=list)
     V2             : list[float]  = field(default_factory=list)
     V3             : list[float]  = field(default_factory=list)
     T              : list[float]  = field(default_factory=list)
     M2             : list[float]  = field(default_factory=list)
     M3             : list[float]  = field(default_factory=list)

     # def __repr__(self) -> str:
     #      return f"Story : {self.Story}\nLoad cases : {self.LoadCase}\Direction : {self.Direction}\Drift : {self.Drift}\nNodes : {self.Label}\nDelta_X : {self.Delta_X}\nDelta_Y : {self.Delta_Y}\nDelta_Z : {self.Delta_Z}"

     def to_dict(self) -> dict:
          return asdict(self)
    
     def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])
     
     def GetPanelZoneForce(self,ResultService : Any):
          pass


# Analysis Results maneger classes
@dataclass
class AnalysisResultsSetup:
     RefResultsSetup : Any # con.RefApi.Results.Setup

     def DeselectAllCasesAndCombosForOutput(self)-> CustomCommentError | int:
        """Deselects all load cases and response combinations for output. 

         Returns:
             CustomCommentError | int: successful value
        """
        val = self.RefResultsSetup.DeselectAllCasesAndCombosForOutput()
        if val != 0.0:
            return CustomCommentError(val,"Kombolor seçili halden çıkarılamadı")
        return val
     
     def GetCaseSelectedForOutput(self, Name: str, Selected : bool)-> CustomCommentError | int:
        val = self.RefResultsSetup.GetCaseSelectedForOutput(Name,Selected)
        if val != 0.0:
            return CustomCommentError(val,"Seçilemedi kombolor...")
        return val
     
     def GetComboSelectedForOutput(self,Name: str, Selected : bool)-> int:
          val = self.RefResultsSetup.GetComboSelectedForOutput(Name,Selected)
          return val
     
     def GetOptionBaseReactLoc(self, GX : float, GY : float, GZ : float)-> int:
        """Retrieves the global coordinates of the location at which the base reactions are reported 

         Args:
             GX (float): The global X coordinate of the location at which the base reactions are reported 
             GY (float): The global Y coordinate of the location at which the base reactions are reported 
             GZ (float): The global Z coordinate of the location at which the base reactions are reported 

         Returns:
             _type_: Returns zero if the coordinates are successfully retrieved, otherwise it returns nonzero
        """
        val = self.RefApi.Setup.Results.Setup.GetOptionBaseReactLoc(GX,GY,GZ)
        return val
     
     def GetOptionBucklingMode(self, BuckModeStart : int, BuckModeEnd : int, BuckModeAll : bool)-> int:
        """_summary_

         Args:
             BuckModeStart (int): _description_
             BuckModeEnd (int): _description_
             BuckModeAll (bool): _description_

         Returns:
             int: _description_
        """
        val = self.RefApi.Setup.Results.Setup.GetOptionBucklingMode(BuckModeStart,BuckModeEnd,BuckModeAll)
        return val
     
     def GetOptionDirectHist(self,Value : int) -> int:
         """Retrieves the output option for direct history results.

         Args:
             Value (int): This item is 1, 2 or 3 
                          1-  Envelopes
                          2-  Step-by-Step
                          3-  Last Step

         Returns:
             _type_: Returns zero if the output option is successfully retrieved, otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.GetOptionBucklingMode(Value)
         return val
          
     def GetOptionModalHist(self,Value : int) -> int:
         """Retrieves the output option for modal history results. 

         Args:
             Value (int): This item is 1, 2 or 3 
                          1-  Envelopes
                          2-  Step-by-Step
                          3-  Last Step

         Returns:
             _type_: Returns zero if the output option is successfully retrieved, otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.GetOptionModalHist(Value)
         return val
     
     def GetOptionModeShape(self,ModeShapeStart : int, ModeShapeEnd : int, ModeShapesAll : bool):
          val = self.RefResultsSetup.GetOptionModeShape(ModeShapeStart,ModeShapeEnd,ModeShapesAll)
          return val
     
     def GetOptionMultiStepStatic(self,Value : int) -> int:
          val = self.RefResultsSetup.GetOptionMultiStepStatic(Value)
          return val
     
     def GetOptionMultiValuedCombo(self,Value : int) -> int:
          val = self.RefResultsSetup.GetOptionMultiValuedCombo(Value)
          return val
     
     def GetOptionNLStatic(self,Value : int) -> int:
          val = self.RefResultsSetup.GetOptionNLStatic(Value)
          return val
     
     
     def SetCaseSelectedForOutput(self,Name: str, Selected : bool = True):
         """Sets a load case selected for output flag. 

         Args:
             Name (str): The name of an existing load case.
             Selected (bool): This item is True if the specified load case is to be selected for output, otherwise it is False.

         Returns:
             _type_: Returns zero if the selected flag is successfully set; otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.SetCaseSelectedForOutput(Name,Selected)
         if val != 0.0:
            return CustomCommentError(val,"Seçilemedi caseler...") 
         return val
     
     def SetComboSelectedForOutput(self,Name: str, Selected : bool):
         """Sets a load combination selected for output flag 

         Args:
             Name (str): The name of an existing load case.
             Selected (bool): This item is True if the specified load case is to be selected for output, otherwise it is False.

         Returns:
             _type_: Returns zero if the selected flag is successfully set; otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.SetComboSelectedForOutput(Name,Selected)
         return val
     
     def SetOptionBaseReactLoc(self, GX : float, GY : float, GZ : float)-> int:
        """Sets the global coordinates of the location at which the base reactions are reported 

         Args:
             GX (float): The global X coordinate of the location at which the base reactions are reported 
             GY (float): The global Y coordinate of the location at which the base reactions are reported 
             GZ (float): The global Z coordinate of the location at which the base reactions are reported 

         Returns:
             _type_: Returns zero if the coordinates are successfully retrieved, otherwise it returns nonzero
        """
        val = self.RefResultsSetup.SetOptionBaseReactLoc(GX,GY,GZ)
        return val
     
     def SetOptionBucklingMode(self, BuckModeStart : int, BuckModeEnd : int, BuckModeAll : bool)-> int:
        """_summary_

         Args:
             BuckModeStart (int): _description_
             BuckModeEnd (int): _description_
             BuckModeAll (bool): _description_

         Returns:
             int: _description_
        """
        val = self.RefResultsSetup.SetOptionBucklingMode(BuckModeStart,BuckModeEnd,BuckModeAll)
        return val
     
     def SetOptionDirectHist(self,Value : int) -> int:
         """Retrieves the output option for direct history results.

         Args:
             Value (int): This item is 1, 2 or 3 
                          1-  Envelopes
                          2-  Step-by-Step
                          3-  Last Step

         Returns:
             _type_: Returns zero if the output option is successfully retrieved, otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.SetOptionDirectHist(Value)
         return val
     
     def SetOptionModalHist(self,Value : int) -> int:
         """Sets the output option for modal history results. 

         Args:
             Value (int): This item is 1, 2 or 3 
                          1-  Envelopes
                          2-  Step-by-Step
                          3-  Last Step

         Returns:
             _type_: Returns zero if the output option is successfully retrieved, otherwise it returns nonzero.
         """
         val = self.RefResultsSetup.SetOptionModalHist(Value)
         return val
     
     def SetOptionModeShape(self,ModeShapeStart : int, ModeShapeEnd : int, ModeShapesAll : bool):
          val = self.RefResultsSetup.SetOptionModeShape(ModeShapeStart,ModeShapeEnd,ModeShapesAll)
          return val
     
     def SetOptionMultiStepStatic(self,Value : int) -> int:
          val = self.RefResultsSetup.SetOptionMultiStepStatic(Value)
          return val
     
     def SetOptionMultiValuedCombo(self,Value : int) -> int:
          val = self.RefResultsSetup.SetOptionMultiValuedCombo(Value)
          return val
     
     def SetOptionNLStatic(self,Value : int) -> int:
          val = self.RefResultsSetup.SetOptionNLStatic(Value)
          return val

@dataclass
class AnalysisResults:
     RefResults : Any #con.RefApi.Results

     def AreaForceShell( self,*args) -> int:
          """Reports the area forces for the specified area elements that are assigned shell section properties (not plane or asolid properties). Note that the forces reported are per unit of in-plane length. 

          Args:
               Name
                    Type: String
                    The name of an existing area object, area element or group of objects, depending on the value of the ItemTypeElm item 
               ItemTypeElm
                    Type: ETABSv1.eItemTypeElm
                    This is one of the following items in the eItemTypeElm enumeration. 
                    If this item is ObjectElm, the result request is for the area elements corresponding to the area object specified by the Name item. 

                    If this item is Element, the result request is for the area element specified by the Name item. 

                    If this item is GroupElm, the result request is for the area elements corresponding to all area objects included in the group specified by the Name item. 

                    If this item is SelectionElm, the result request is for area elements corresponding to all selected area objects and the Name item is ignored. 

               NumberResults
                    Type: Int32
                    The total number of results returned by the program 
               Obj
                    Type: String[]
                    This is an array that includes the area object name associated with each result, if any 
               Elm
                    Type: String[]
                    This is an array that includes the area element name associated with each result 
               PointElm
                    Type: String[]
                    This is an array that includes the name of the point element where the results are reported 
               LoadCase
                    Type: String[]
                    This is an array that includes the name of the analysis case or load combination associated with each result 
               StepType
                    Type: String[]
                    This is an array that includes the step type, if any, for each result 
               StepNum
                    Type: Double[]
                    This is an array that includes the step number, if any, for each result 
               F11
                    Type: Double[]
                    The area element internal F11 membrane direct force per length reported in the area element local coordinate  [F/L] 
               F22
                    Type: Double[]
                    The area element internal F22 membrane direct force per length reported in the area element local coordinate  [F/L] 
               F12
                    Type: Double[]
                    The area element internal F12 membrane shear force per length reported in the area element local coordinate  [F/L] 
               FMax
                    Type: Double[]
                    The maximum principal membrane force per length. [F/L] 
               FMin
                    Type: Double[]
                    The minimum principal membrane force per length. [F/L] 
               FAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of the maximum principal membrane force. [deg] 
               FVM
                    Type: Double[]
                    The area element internal Von Mises membrane force per length. [F/L] 
               M11
                    Type: Double[]
                    The area element internal M11 plate bending moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               M22
                    Type: Double[]
                    The area element internal M22 plate bending moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               M12
                    Type: Double[]
                    The area element internal M12 plate twisting moment per length reported in the area element local coordinate  This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MMax
                    Type: Double[]
                    The maximum principal plate moment per length. This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MMin
                    Type: Double[]
                    The minimum principal plate moment per length. This item is only reported for area elements with properties that allow plate bending behavior. [FL/L] 
               MAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of the maximum principal plate moment. This item is only reported for area elements with properties that allow plate bending behavior. [deg] 
               V13
                    Type: Double[]
                    The area element internal V13 plate transverse shear force per length reported in the area element local coordinate system. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               V23
                    Type: Double[]
                    The area element internal V23 plate transverse shear force per length reported in the area element local coordinate system. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               VMax
                    Type: Double[]
                    The maximum plate transverse shear force. It is equal to the square root of the sum of the squares of V13 and V23. This item is only reported for area elements with properties that allow plate bending behavior. [F/L] 
               VAngle
                    Type: Double[]
                    The angle measured counter clockwise (when the local 3 axis is pointing toward you) from the area local 1 axis to the direction of Vmax. This item is only reported for area elements with properties that allow plate bending behavior. [deg] 

          """
          result = self.RefResults.AreaForceShell(*args)
          return result
     
     def AreaJointForceShell(self,*args):
          result = self.RefResults.AreaJointForceShell(*args)
          return result
     
     def AreaStrainShell(self,*args):
          result = self.RefResults.AreaStrainShell(*args)
          return result
     
     def AreaStrainShellLayered(self,*args):
          result = self.RefResults.AreaStrainShellLayered(*args)
          return result
     
     def AreaStressShell(self,*args):
          result = self.RefResults.AreaStressShell(*args)
          return result
     
     def AreaStressShellLayered(self,*args):
          result = self.RefResults.AreaStressShellLayered(*args)
          return result
     
     def AssembledJointMass(self,*args):
          result = self.RefResults.AssembledJointMass(*args)
          return result
     
     def AssembledJointMass_1(self,*args):
          result = self.RefResults.AssembledJointMass_1(*args)
          return result
     
     def BaseReact(self,*args) -> BaseReact:
          """Reports the structure total base reactions 

          Args:
              NumberResults (int): The total number of results returned by the program
              LoadCase (list): This is an array that includes the name of the analysis case or load combination 
              StepType (list): This is an array that includes the step type, if any, for each result 
              StepNum (list): This is an array that includes the step number, if any, for each result 
              FX (list): This array contains the base reaction force in the global X direction for each result.
              FY (list): This array contains the base reaction force in the global Y direction for each result.
              FZ (list): This array contains the base reaction force in the global Z direction for each result.
              MX (list): This array contains the base reaction moment about the global X axis for each result. [FL] 
              ParamMy (list): This array contains the base reaction moment about the global Y axis for each result. [FL] 
              MZ (list): This array contains the base reaction moment about the global Z axis for each result. [FL]
              GX (float): The global X coordinate of the point at which the base reactions are reported. [L]
              GY (float): The global Y coordinate of the point at which the base reactions are reported. [L] 
              GZ (float): The global Z coordinate of the point at which the base reactions are reported. [L]

          Returns:
              _type_: Returns zero if the reactions are successfully recovered, otherwise it returns a nonzero value 
          """
          
          result = self.RefResults.BaseReact(*args)
          return result
          
     
     def BaseReactWithCentroid(self,*args):
          result = self.RefResults.BaseReactWithCentroid(*args)
          return result
     
     def BucklingFactor(self,*args):
          result = self.RefResults.BucklingFactor(*args)
          return result
     
     def FrameForce(self,*args):
          result = self.RefResults.FrameForce(*args)
          return result
     
     def FrameJointForce(self,*args):
          result = self.RefResults.FrameJointForce(*args)
          return result
     
     def GeneralizedDispl(self,*args):
          result = self.RefResults.GeneralizedDispl(*args)
          return result
     
     def JointAcc(self,*args):
          result = self.RefResults.JointAcc(*args)
          return result
     
     def JointAccAbs(self,*args):
          result = self.RefResults.JointAccAbs(*args)
          return result
     
     def JointDispl(self,*args):
          result = self.RefResults.JointDispl(*args)
          return result
     
     def JointDisplAbs(self,*args):
          result = self.RefResults.JointDisplAbs(*args)
          return result
     
     def JointDrifts(self,*args):
          result = self.RefResults.JointDrifts(*args)
          return result
     
     def JointReact(self,*args):
          result = self.RefResults.JointReact(*args)
          return result
     
     def JointVel(self,*args):
          result = self.RefResults.JointVel(*args)
          return result
     
     def JointVelAbs(self,*args):
          result = self.RefResults.JointVelAbs(*args)
          return result
     
     def LinkDeformation(self,*args):
          result = self.RefResults.LinkDeformation(*args)
          return result
     
     def LinkForce(self,*args):
          result = self.RefResults.LinkForce(*args)
          return result
     
     def LinkJointForce(self,*args):
          result = self.RefResults.LinkJointForce(*args)
          return result
     
     def ModalLoadParticipationRatios(self,*args):
          result = self.RefResults.ModalLoadParticipationRatios(*args)
          return result
     
     def ModalParticipatingMassRatios(self,*args):
          result = self.RefResults.ModalParticipatingMassRatios(*args)
          return result
     
     def ModalParticipationFactors(self,*args):
          result = self.RefResults.ModalParticipationFactors(*args)
          return result
     
     def ModalPeriod(self,*args):
          result = self.RefResults.ModalPeriod(*args)
          return result
     
     def ModeShape(self,*args):
          result = self.RefResults.ModeShape(*args)
          return result
     
     def PanelZoneDeformation(self,*args):
          result = self.RefResults.PanelZoneDeformation(*args)
          return result
     
     def PanelZoneForce(self,*args):
          result = self.RefResults.PanelZoneForce(*args)
          return result
     
     def PierForce(self,*args):
          result = self.RefResults.PierForce(*args)
          return result
     
     def SectionCutAnalysis(self,*args):
          result = self.RefResults.SectionCutAnalysis(*args)
          return result
     
     def SectionCutDesign(self,*args):
          result = self.RefResults.SectionCutDesign(*args)
          return result
     
     def SpandrelForce(self,*args):
          result = self.RefResults.SpandrelForce(*args)
          return result
     
     def StoryDrifts(self,*args) -> int: 
          
          result = self.RefResults.StoryDrifts(*args)
          return result






# def main() -> None:
#      from preproc import ApiConnector,SapModel
#      import Enums as en

#      SapPath         = "C:\\Program Files\\Computers and Structures\\SAP2000 23\\SAP2000.exe"
#      EtabsPath       = "C:\\Program Files\\Computers and Structures\\ETABS 20\\ETABS.exe"
#      con             = ApiConnector(ProgramPath=EtabsPath)
#      ResultsSetup    = AnalysisResultsSetup(RefResultsSetup=con.RefApi.Results.Setup)
#      RefResults      = AnalysisResults(RefResults=con.RefApi.Results)

#      ResultsSetup.DeselectAllCasesAndCombosForOutput()
#      # MODAL
#      # ResultsSetup.SetCaseSelectedForOutput(Name="MODAL")
#      # Modal = ModalPeriod(ResultService=RefResults)
#      # print(Modal)

#      ResultsSetup.SetCaseSelectedForOutput(Name="G-DEAD")
#      # ResultsSetup.SetCaseSelectedForOutput("RESPX")

#      # BASEREACTION
#      # MesnetTepkileri = BaseReact(ResultService=RefResults)
#      # print(MesnetTepkileri)

#      # BASEREACTION WITH CENTROID
#      # MesnetTepkileriMerkez = BaseReactWithCentroid(ResultService=RefResults)
#      # print(MesnetTepkileriMerkez)
     
#      # STORYDRIFT
#      # GKatÖtelemeleri = StoryDrift(ResultService=RefResults)
#      # print(GKatÖtelemeleri)
     
#      # BUCKLINGFACTOR
#      # BuckFactor = BucklingFactor(ResultService=RefResults)
#      # print(BuckFactor)

#      # JOINTDISPLACEMENT
#      # jointdisp = JointDisplacement(ResultService=RefResults,name="ALL",itemType=eItemTypeElm.GroupElm.value)
#      # print(jointdisp)

#      # MODAL_LOAD_PARTICIPATION_RATIO
#      # MODALLOADPARTICIPATION = ModalLoadParticipationRatios(ResultService=RefResults)
#      # print(MODALLOADPARTICIPATION)

#      # MODAL_PARTICIPATING_MASS_RATIO
#      # MODALPARTICIPATINGMASS = ModalParticipatingMassRatios(ResultService=RefResults)
#      # print(MODALPARTICIPATINGMASS)

#      # MODAL_PARTICIPATION_FACTORS
#      # MODALPARTICIPATIONFACTORS = ModalParticipationFactors(ResultService=RefResults)
#      # print(MODALPARTICIPATIONFACTORS)

#      # MODE SHAPE
#      # MODESHAPE = ModeShape(ResultService=RefResults,ItemTypeElm=eItemTypeElm.GroupElm.value)
#      # print(MODESHAPE)

#      # PIER FORCE
#      # PIERFORCE = PierForce(ResultService=RefResults)
#      # print(PIERFORCE)

#      # SPANDREL FORCE
#      # SPANDRELFORCE = SpandrelForce(ResultService=RefResults)
#      # print(SPANDRELFORCE)

#      # SECTION CUT ANALYSIS
#      # SECTIONCUT = SectionCutAnalysis(ResultService=RefResults)
#      # print(SECTIONCUT)



# if __name__ == "__main__":
#      # main()
#      pass