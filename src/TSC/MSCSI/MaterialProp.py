
from TSC.MSCSI.Enums import eMatType


class PropMaterial:
    # SapModel.PropMaterial
    RefApi : object

    def AddMaterial(self,Name : str, MatType : eMatType, Region : str, Standart : str, Grade : str, Username : str) -> int:
        result = self.RefApi.AddMaterial(Name,MatType,Region,Standart,Grade,Username)
        return result
    
    def ChangeName(self):
        pass

    def Count(self):
        pass

    def Delete(self):
        pass

    def GetTypeOAPI(self):
        pass

    def GetNameList(self):
        pass


    def GetDamping(self):
        pass

    def SetDamping(self):
        pass


    def GetMassSource(self):
        pass

    def SetMassSource(self):
        pass


    def GetMassSource_1(self):
        pass

    def SetMassSource_1(self):
        pass


    def GetMaterial(self):
        pass

    def SetMaterial(self):
        pass


    def GetMPAnisotropic(self):
        pass

    def SetMPAnisotropic(self):
        pass


    def GetMPIsotropic(self):
        pass

    def SetMPIsotropic(self):
        pass


    def GetMPOrthotropic(self):
        pass

    def SetMPOrthotropic(self):
        pass


    def GetMPUniaxial(self):
        pass

    def SetMPUniaxial(self):
        pass


    def GetOConcrete(self):
        pass

    def SetOConcrete(self):
        pass


    def GetOConcrete_1(self, Name:str, Fc:float, IsLightweight:bool, FcsFactor:float, SSType:int, SSHysType:int,
                       StrainAtFc:float, StrainUltimate:float, FinalSlope:float, 
                       FrictionAngle:float=0., DilatationalAngle:float=0., Temp:float=0.) -> list:
        """Sets the other material property data for concrete materials. 

        Args:
            Name (str): The name of an existing concrete material property.
            Fc (float): _description_
            IsLightweight (bool): If this item is True, the concrete is assumed to be lightweight concrete.
            FcsFactor (float): _description_
            SSType (int): This is 0, 1 or 2, indicating the stress-strain curve type. 

                                0 User defined 
                                1 Parametric - Simple 
                                2 Parametric - Mander 

            SSHysType (int): This is 0 through 7, indicating the stress-strain curve type. 

                                0 Elastic 
                                1 Kinematic 
                                2 Takeda 
                                3 Pivot 
                                4 Concrete 
                                5 BRB Hardening 
                                6 Degrading 
                                7 Isotropic 

            StrainAtFc (float): _description_
            StrainUltimate (float): This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity. This item must be larger than the StrainAtfc item
            FinalSlope (float): This item applies only to parametric stress-strain curves. It is a multiplier on the material modulus of elasticity, E. This value multiplied times E gives the final slope on the compression side of the curve.
            FrictionAngle (float, optional): The Drucker-Prager friction angle. This item must be smaller or equal to 0 and less than 90. [deg]. Defaults to 0..
            DilatationalAngle (float, optional): The Drucker-Prager dilatational angle. This item must be smaller or equal to 0 and less than 90. [deg]. Defaults to 0..
            Temp (float, optional): The temperature at which the specified data applies. The temperature must have been defined previously for the material. 
                                    This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.
                                    . Defaults to 0..
        """
        result = self.RefApi.SetOConcrete_1(Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType,
                       StrainAtFc, StrainUltimate, FinalSlope, 
                       FrictionAngle, DilatationalAngle, Temp)
        return result

    def SetOConcrete_1(self, Name:str, Fc:float, IsLightweight:bool, FcsFactor:float, SSType:int, SSHysType:int,
                       StrainAtFc:float, StrainUltimate:float, FinalSlope:float, 
                       FrictionAngle:float=0., DilatationalAngle:float=0., Temp:float=0.) -> int:
        """Sets the other material property data for concrete materials. 

        Args:
            Name (str): The name of an existing concrete material property.
            Fc (float): _description_
            IsLightweight (bool): If this item is True, the concrete is assumed to be lightweight concrete.
            FcsFactor (float): _description_
            SSType (int): This is 0, 1 or 2, indicating the stress-strain curve type. 

                                0 User defined 
                                1 Parametric - Simple 
                                2 Parametric - Mander 

            SSHysType (int): This is 0 through 7, indicating the stress-strain curve type. 

                                0 Elastic 
                                1 Kinematic 
                                2 Takeda 
                                3 Pivot 
                                4 Concrete 
                                5 BRB Hardening 
                                6 Degrading 
                                7 Isotropic 

            StrainAtFc (float): _description_
            StrainUltimate (float): This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity. This item must be larger than the StrainAtfc item
            FinalSlope (float): This item applies only to parametric stress-strain curves. It is a multiplier on the material modulus of elasticity, E. This value multiplied times E gives the final slope on the compression side of the curve.
            FrictionAngle (float, optional): The Drucker-Prager friction angle. This item must be smaller or equal to 0 and less than 90. [deg]. Defaults to 0..
            DilatationalAngle (float, optional): The Drucker-Prager dilatational angle. This item must be smaller or equal to 0 and less than 90. [deg]. Defaults to 0..
            Temp (float, optional): The temperature at which the specified data applies. The temperature must have been defined previously for the material. 
                                    This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.
                                    . Defaults to 0..
        """
        result = self.RefApi.SetOConcrete_1(Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType,
                       StrainAtFc, StrainUltimate, FinalSlope, 
                       FrictionAngle, DilatationalAngle, Temp)
        return result


    def GetONoDesign(self):
        pass

    def SetONoDesign(self):
        pass


    def GetORebar_1(self, Name : str, Fy : float, Fu : float, EFy:float, EFu:float, SSType:int, SSHysType:int, StrainAtHardening:float, StrainUltimate:float, FinalSlope:float, UseCaltransSSDefaults:bool, Temp:float = 0) -> list:
        result = []
        result = self.RefApi.GetORebar_1(Name , Fy , Fu , EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, FinalSlope, UseCaltransSSDefaults, Temp)
        return result

    def SetORebar_1(self,Name : str, Fy : float, Fu : float, EFy:float, EFu:float, SSType:int, SSHysType:int, StrainAtHardening:float, StrainUltimate:float, FinalSlope:float, UseCaltransSSDefaults:bool, Temp:float = 0) -> int:
        """Sets the other material property data for rebar materials. 
                Parameters
                        Name
                            Type: System.String
                            The name of an existing rebar material property.
                        Fy
                            Type: System.Double

                        Fu
                            Type: System.Double
                            The minimum tensile stress. [F/L2]
                        EFy
                            Type: System.Double

                        EFu
                            Type: System.Double

                        SSType
                            Type: System.Int32
                            This is 0, 1 or 2, indicating the stress-strain curve type. 
                                        Value  SSType 
                                        0      User defined 
                                        1      Parametric - Simple 
                                        2      Parametric - Park 

                        SSHysType
                            Type: System.Int32
                            This is 0 through 7, indicating the stress-strain curve type. 
                                    Value SSHysType 
                                    0     Elastic 
                                    1     Kinematic 
                                    2     Takeda 
                                    3     Pivot 
                                    4     Concrete 
                                    5     BRB Hardening 
                                    6     Degrading 
                                    7     Isotropic 

                        StrainAtHardening
                            Type: System.Double
                            This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the strain at the onset of strain hardening.
                        StrainUltimate
                            Type: System.Double
                            This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the ultimate strain capacity. This item must be larger than the StrainAtHardening item.
                        FinalSlope
                            Type: System.Double
                            This item applies only to parametric stress-strain curves. It is a multiplier on the material modulus of elasticity, E. This value multiplied times E gives the final slope of the curve.
                        UseCaltransSSDefaults
                            Type: System.Boolean
                            If this item is True, the program uses Caltrans default controlling strain values, which are bar size dependent.
                        Temp (Optional)
                            Type: System.Double
                            The temperature at which the specified data applies. The temperature must have been defined previously for the material. 
                            This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.


        """
        result = self.RefApi.SetORebar_1(Name , Fy , Fu , EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, FinalSlope, UseCaltransSSDefaults, Temp)
        return result



    def GetOSteel(self):
        pass

    def SetOSteel(self):
        pass


    def GetOSteel_1(self):
        pass

    def SetOSteel_1(self):
        pass
    

    def GetOTendon(self):
        pass

    def SetOTendon(self):
        pass

    
    def GetOTendon_1(self):
        pass

    def SetOTendon_1(self):
        pass


    def GetSSCurve(self,Name : str,NumberPoints:int,PointID : list[int],Strain : list[float],Stress : list[float],SectName : str = "", RebarArea : float = 0,Temp : float = 0) -> list:
        """Retrieves the material stress-strain curve.

        Args:
            Name (str): The name of an existing material property.
            NumberPoints (int): The number of points in the stress-strain curve. This item must be at least 3.
            PointID (list[int]): This is one of the following integers which sets the point ID. The point ID controls the color that will be displayed for hinges in a deformed shape plot. 
                                    Value Point ID 
                                    -5      -E 
                                    -4      -D 
                                    -3      -C 
                                    -2      -B 
                                    -1      -A 
                                     0      None 
                                     1       A 
                                     2       B 
                                     3       C 
                                     4       D 
                                     5       E 
                                    The point IDs must be input in numerically increasing order, except that 0 (None) values are allowed anywhere. No duplicate values are allowed excepth for 0 (None).
            Strain (list[float]): This is an array that includes the strain at each point on the stress strain curve. The strains must increase monotonically.
            Stress (list[float]): This is an array that includes the stress at each point on the stress strain curve. [F/L2] 
                                    Points that have a negative strain must have a zero or negative stress. Similarly, points that have a positive strain must have a zero or positive stress.

                                    There must be one point defined that has zero strain and zero stress.

            Temp (float, optional): The temperature at which the specified data applies. The temperature must have been defined previously for the material. 
                                    This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.
                                    . Defaults to 0.
        """
        result = self.RefApi.GetSSCurve(Name,NumberPoints,PointID,Strain,Stress,SectName,RebarArea,Temp)
        return result
        

    def SetSSCurve(self,Name : str,NumberPoints:int,PointID : list[int],Strain : list[float],Stress : list[float],Temp : float = 0) -> int:
        """Sets the material stress-strain curve for materials that are specified to have user-defined stress-strain curves

        Args:
            Name (str): The name of an existing material property.
            NumberPoints (int): The number of points in the stress-strain curve. This item must be at least 3.
            PointID (list[int]): This is one of the following integers which sets the point ID. The point ID controls the color that will be displayed for hinges in a deformed shape plot. 
                                    Value Point ID 
                                    -5      -E 
                                    -4      -D 
                                    -3      -C 
                                    -2      -B 
                                    -1      -A 
                                     0      None 
                                     1       A 
                                     2       B 
                                     3       C 
                                     4       D 
                                     5       E 
                                    The point IDs must be input in numerically increasing order, except that 0 (None) values are allowed anywhere. No duplicate values are allowed excepth for 0 (None).
            Strain (list[float]): This is an array that includes the strain at each point on the stress strain curve. The strains must increase monotonically.
            Stress (list[float]): This is an array that includes the stress at each point on the stress strain curve. [F/L2] 
                                    Points that have a negative strain must have a zero or negative stress. Similarly, points that have a positive strain must have a zero or positive stress.

                                    There must be one point defined that has zero strain and zero stress.

            Temp (float, optional): The temperature at which the specified data applies. The temperature must have been defined previously for the material. 
                                    This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.
                                    . Defaults to 0.
        """
        result = self.RefApi.SetSSCurve(Name,NumberPoints,PointID,Strain,Stress,Temp)
        return result

    def GetTemp(self):
        pass

    def SetTemp(self):
        pass


    def GetWeightAndMass(self):
        pass

    def SetWeightAndMass(self):
        pass


    


    

    

    

    

    


