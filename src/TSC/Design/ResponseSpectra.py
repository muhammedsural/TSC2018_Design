import pandas as pd
from dataclasses import dataclass,field,asdict
import numpy as np 
import scipy as sc
import matplotlib.pyplot as plt
from TSC.Design.Definitions import DuctilityLevel,ResSystemType, SeismicResistanceBuildingsClass,SlabSystem,SeismicDesignClass

__all__ = ['SeismicInputs',
           'SeismicResistanceBuildingInputs',
           'SeismicInputsManager',
           'SeismicResistanceBuildingManeger',
           'Spectrum',
           'TimeSeriesSpectra']

# Spectral values
Ss_range = [0.25 , 0.50 , 0.75, 1.00 , 1.25 , 1.50 ]
FS_table = {"ZA": [0.8 , 0.8 , 0.8 , 0.8 , 0.8 , 0.8], 
            "ZB": [0.9 , 0.9 , 0.9 , 0.9 , 0.9 , 0.9], 
            "ZC": [1.3 , 1.3 , 1.2 , 1.2 , 1.2 , 1.2],
            "ZD": [1.6 , 1.4 , 1.2 , 1.1 , 1.0 , 1.0],
            "ZE": [2.4 , 1.7 , 1.3 , 1.1 , 0.9 , 0.8]}
S1_range = [0.10 , 0.20 , 0.30, 0.40 , 0.50 , 0.60 ]
F1_table = {"ZA": [0.8 , 0.8 , 0.8 , 0.8 , 0.8 , 0.8], 
            "ZB": [0.8 , 0.8 , 0.8 , 0.8 , 0.8 , 0.8], 
            "ZC": [1.5 , 1.5 , 1.5 , 1.5 , 1.5 , 1.4],
            "ZD": [2.4 , 2.2 , 2.0 , 1.9 , 1.8 , 1.7],
            "ZE": [4.2 , 3.3 , 2.8 , 2.4 , 2.2 , 2.0]}

TDTH = ".\\TSC\\Resource\\AFAD_TDTH_parametre.csv"

TABLE41 = pd.DataFrame({
    1  : [8, 3  , 3],
    2  : [7, 2.5, 2],
    3  : [6, 2.5, 2],
    5  : [8, 2.5, 2],
    6  : [7, 2.5, 2],
    7  : [3, 2  , 0],

    9  : [6, 2.5, 4],
    8  : [5, 2.5, 4],
    10 : [6, 2.5, 6],
    11 : [5, 2.5, 6],

    12 : [4, 2.5, 7],
    13 : [4, 2  , 6],
    14 : [4, 2  , 6],
    # TODO Prefabrik yapılar için R katsayıları bağlantı tipine göre ikili halde verilmiş. Problem şimdilik 1
    15 : [1,1,1],
    16 : [1,1,1],
    17 : [1,1,1],
    18 : [1,1,1],
    19 : [1,1,1],
    20 : [1,1,1],
    21 : [1,1,1],
    22 : [1,1,1],
    23 : [1,1,1],
    24 : [1,1,1],

    25 : [8, 3  , 3],
    26 : [8, 2.5, 2],
    27 : [5, 2  , 4],
    28 : [8, 3  , 2],
    29 : [6, 2.5, 2],
    30 : [4, 2  , 0],

    31 : [6, 2.5, 4],
    32 : [5, 2  , 4],

    33 : [4, 2.5, 7],
    34 : [3, 2  , 8],
    35 : [4, 2  , 7],

    36 : [4,2,8],
    37 : [3,2,8],

    38 : [4,2,7],
    39 : [4,2,7],
    40 : [3,2,8],
    41 : [2.5,1.5,8],

    42 : [4,2,7],
    43 : [3,2,8]
}).T
TABLE41.columns = ["R", "D", "BYS"]




@dataclass
class SeismicInputs:
    """
    Args:
        lat       : latitude of location
        lon       : longitude of location
        soil      : soil class
        intensity : intensity level 
                        options: DD1, DD2, DD3, DD4
        
    """

    lat       : float  
    lon       : float  
    soil      : str    
    intensity : str    
    

    def __repr__(self) -> str:
        return f"Latitude :{self.lat}\nLongitude :{self.lon}\nSoil Class :{self.soil}\nIntensity:{self.intensity}"

    def dict(self) -> dict:
        """Class property lerini sözlük olarak döndürür.

        Returns:
            dict: Class propertylerini içeren sözlük
        """
        return asdict(self)
    
    def convert_dataframe(self) -> pd.DataFrame:
        """Class property lerini pandas DataFrame olarak döndürür.

        Returns:
            dict: Class propertylerini içeren DataFrame
        """
        dumy = self.dict()
        dumy_df = pd.DataFrame([dumy.keys(),dumy.values()]).T
        del dumy
        return dumy_df
  
@dataclass
class SeismicResistanceBuildingInputs:
    """
    Args:
        Hn              : Bina serbest yüksekliği [m]
        R               : Yapi davranis katsayisi
        D               : Overstrength factor (Dayanim fazlalagi katsayisi)
        I               : Building important factor (Bina onem katsayisi)
        DTS             : Deprem tasarim sinifi 
        BYS             : Bina yükseklik sinifi
        DuctilityLevel  : Yapinin suneklilik duzeyi.
        ResSystemType_X : X doğrultusunda depreme dayanacak tasiyici sistem tipi
        ResSystemType_Y : Y doğrultusunda depreme dayanacak tasiyici sistem tipi
        SlabSystem      : Doseme sistemi
    """
    Hn              : float
    I               : float  
    DuctilLevel     : DuctilityLevel 
    ResSystemType_X : ResSystemType  
    ResSystemType_Y : ResSystemType  
    SlabSystem      : SlabSystem   


    def __repr__(self) -> str:
        return f"Hn :{self.Hn}\nI :{self.I}\nDuctilLevel :{self.DuctilLevel.name}\nResSystemType_X :{self.ResSystemType_X.name}\nResSystemType_Y :{self.ResSystemType_Y.name}\nSlabSystem :{self.SlabSystem.name}"

    def dict(self) -> dict:
        """Class property lerini sözlük olarak döndürür.

        Returns:
            dict: Class propertylerini içeren sözlük
        """
        return asdict(self)
    
    def convert_dataframe(self) -> pd.DataFrame:
        """Class property lerini pandas DataFrame olarak döndürür.

        Returns:
            dict: Class propertylerini içeren DataFrame
        """
        dumy = self.dict()
        dumy_df = pd.DataFrame([dumy.keys(),dumy.values()]).T
        del dumy
        return dumy_df


@dataclass
class SeismicInputsManager:
    """
        SeismicVariables : Harita bilgileri
        Ss        : Kisa periyot harita katsayisi
        S1        : 1 sn periyot harita katsayisi
        soil      : Zemin sinifi
        TL        : Spektrum hesabindaki en uç periyot
        PGA       : Peak ground acceleration
        PGV       : Peak ground acceleration
        Fs        : Kisa periyot harita spektral ivme katsayisi [boyutsuz]
        F1        : 1.0 saniye için harita spektral ivme katsayisi [boyutsuz]
        SDs       : Kisa periyot tasarim spektral ivme katsayisi [boyutsuz]
        SD1       : 1.0 saniye periyot için tasarim spektral ivme katsayisi [boyutsuz]
        TA        : Corner period in spectrum (Kose periyod)
        TB        : Corner period in spectrum (Kose periyod)
        TL        : Long period (Uzun periyod)
    """
    SeismicVariables : SeismicInputs = field(default_factory=SeismicInputs)
    Ss        : float  = field(default=0.)
    S1        : float  = field(default=0.)
    PGA       : float  = field(default=0.)
    PGV       : float  = field(default=0.)
    Fs        : float  = field(default=0.)
    F1        : float  = field(default=0.)
    SDs       : float  = field(default=0.)
    SD1       : float  = field(default=0.)
    TA        : float  = field(default=0.)
    TB        : float  = field(default=0.)
    TL        : float  = field(default=6.)

    
    def __repr__(self) -> str:
        return f"Ss :{self.Ss}\nS1 :{self.S1}\nPGA :{self.PGA}\nPGV :{self.PGV}\nFs :{self.Fs}\nF1 :{self.F1}\nSDs :{self.SDs}\nSD1 :{self.SD1}\nTA :{self.TA}\nTB :{self.TB}\nTL :{self.TL}"
    
    def SetVariables(self) ->None:
        """Hesaplanmasi gereken değerleri hesaplar ve set eder."""
        spec_val = self.GetSpectralMapVariables(self.SeismicVariables.intensity, self.SeismicVariables.lat, self.SeismicVariables.lon)
        self.Fs  = self.Get_Fs(Ss=self.Ss, Soil=self.SeismicVariables.soil)
        self.SDs = self.GetShortPeriodCoefficient(Fs=self.Fs, Ss=self.Ss)
        self.F1  = self.Get_F1(S1=self.S1, Soil=self.SeismicVariables.soil)
        self.SD1 = self.GetOneSecondsPeriodCoefficient(S1=self.S1, F1=self.F1)
        self.TA = self.Get_TA(SD1=self.SD1, SDs=self.SDs)
        self.TB = self.Get_TB(SD1=self.SD1, SDs=self.SDs)
    
    
    def GetSpectralMapVariables(self,Intensity : str, Latitude : float, Longitude : float) -> dict:
        """Spektrum haritasinda verilen koordinatlara göre spektral harita değerlerini bulur"""
        afad_spectra_params_df = pd.read_csv(TDTH)   

        # grid locattions
        x = afad_spectra_params_df["LAT"].to_list()
        y = afad_spectra_params_df["LON"].to_list()
        
        # spectral values dictionary
        spectral_value_dict = {}
        for column_name in ["Ss","S1","PGA","PGV"]:

            z = afad_spectra_params_df[ f"{column_name}-{self.SeismicVariables.intensity}"].to_list()

            interpolator = sc.interpolate.CloughTocher2DInterpolator( np.array([x,y]).T , z)

            spectral_value = np.round( interpolator( self.SeismicVariables.lat, self.SeismicVariables.lon)  , 3 )
            spectral_value_dict[column_name] = spectral_value
        
        self.Ss = spectral_value_dict["Ss"]
        self.S1 = spectral_value_dict["S1"]
        self.PGA = spectral_value_dict["PGA"]
        self.PGV = spectral_value_dict["PGV"]

        return spectral_value_dict
    
    def Get_Fs(self,Ss : float,Soil : str)-> float:
        # Short period
        if Ss < Ss_range[0]:
            Fs = FS_table[Soil][0]
        elif Ss > Ss_range[-1]:
            Fs = FS_table[Soil][-1]
        else:
            Fs = np.round( np.interp(Ss,Ss_range, FS_table[Soil]) , 3)
        return Fs
    
    def GetShortPeriodCoefficient(self,Fs : float, Ss : float)-> float:
        # Short period
        SDs = Ss * Fs
        return SDs
    
    def Get_F1(self,S1 : float,Soil : str)-> float:
        # 1sec period
        if S1 < S1_range[0] :
            F1 = F1_table[Soil][0]
            SD1 = S1 * F1
        elif S1 > S1_range[-1]:
            F1 = F1_table[Soil][-1]
            SD1 = S1 * F1
        else:
            F1 = np.round(np.interp(S1, S1_range, F1_table[Soil]), 3)
        return F1
    
    def GetOneSecondsPeriodCoefficient(self, S1 : float, F1 : float):
        # 1sec period
        SD1 = S1 * F1
        return SD1
    
    def Get_TA(self, SD1 : float, SDs : float) -> float:
        """Yatay elastik tasarim spektrum sol köşe periyodu."""
        TA = 0.2 * SD1 / SDs
        return TA
    
    def Get_TB(self, SD1 : float, SDs : float) -> float:
        """Yatay elastik tasarim elastik spektrum sağ köşe periyodu"""
        return SD1 / SDs
        


@dataclass
class SeismicResistanceBuildingManeger:
    """
    BuildingVariables type(SeismicResistanceBuildingInputs) :
    SeismicManager    type(SeismicInputsManager) :
    BuildingClass     type(SeismicResistanceBuildingsClass) :
    Total_M_DEV       type(float             ) : default=0
    Total_M_o         type(float             ) : default=0
    DTS               type(SeismicDesignClass) : default=0
    BYS               type(int               ) : default=0
    Rx                type(float             ) : default=1
    Ry                type(float             ) : default=1
    Dx                type(float             ) : default=1
    Dy                type(float             ) : default=1

    """
    BuildingVariables : SeismicResistanceBuildingInputs = field(default_factory=SeismicResistanceBuildingInputs)
    SeismicManager    : SeismicInputsManager            = field(default_factory=SeismicInputsManager)
    BuildingClass     : SeismicResistanceBuildingsClass = field(default_factory=SeismicResistanceBuildingsClass)
    Total_M_DEV       : float               = field(default=0)
    Total_M_o         : float               = field(default=0)
    DTS               : SeismicDesignClass  = field(default=0)
    BYS               : int                 = field(default=0.)
    Rx                : float               = field(default=1.)
    Ry                : float               = field(default=1.)
    Dx                : float               = field(default=1.)
    Dy                : float               = field(default=1.)
    
    def SetVariables(self)->None:
        self.DTS = self.GetDTS(self.SeismicManager.SDs, self.BuildingVariables.I)
        self.BYS = self.GetMaxBYS(self.DTS, self.BuildingVariables.Hn)

    def GetDTS(self, SDs : float, I : float) -> None:
        """Deprem tasarim sinifini bulur."""
        if SDs < .33 : 
            DTS = SeismicDesignClass.four_a.value

            if I ==2 or I == 3:
                DTS = SeismicDesignClass.four.value
                
        if SDs >= 0.33 and SDs < 0.50 : 
            DTS = SeismicDesignClass.three_a.value

            if I ==2 or I == 3:
                DTS = SeismicDesignClass.three.value
                
        if SDs >= 0.50 and SDs < 0.75 :
            DTS = SeismicDesignClass.two_a.value

            if I ==2 or I == 3:
                DTS = SeismicDesignClass.two.value

        if SDs >= 0.75 : 
            DTS = SeismicDesignClass.one_a.value

            if I ==2 or I == 3:
                DTS = SeismicDesignClass.one.value

        return DTS
    
    def GetMaxBYS(self, DTS : int, Hn : float) -> int: 
        """TBDY2018 Tablo 3.3 e göre BYS sinifini bulur."""
        if DTS in [1,2,3,4]:
            dts = 0
        if DTS in [5,6]:
            dts = 1
        if DTS in [7,8]:
            dts = 2
        
        BYS = {
            1 : [70.1,91.1,105.1],
            2 : [56.1,70.1,91.1],
            3 : [42.1,56.1,56.1],
            4 : [28.1,42.1,42.1],
            5 : [17.6,28.1,28.1],
            6 : [10.6,17.6,17.6],
            7 : [7.1,10.6,10.6],
            8 : [0,0,0]
        }
        df_bys = pd.DataFrame(BYS).T
        # BYS DataFrame de ilgili DTS için kısımı seçer, Hn değerinden küçük olanları filtreler en üstteki indek max BYS değeri olur.
        BYS = df_bys[dts][df_bys[dts] < Hn].index[0]
        return BYS

    def Check_4_3_1_2(self, DTS : int, BuildingClass : int, BYS : int)-> bool:
        """
        TBDY-4.3.1.2 : Tablo 4.1’de A21, A22 ve C21, C22 ile simgelenen taşıyıcı sistemlerde, sadece DTS = 4 olan binalar ile sınırlı olmak üzere, izin verilen Bina Yükseklik Sınıfı BYS ≥ 2’ye yükseltilebilir.

        Args:
            DTS (int): _description_
            BuildingClass (int): _description_
            BYS (int): _description_

        Returns:
            bool: _description_
        """
        result = True
        if BuildingClass in [SeismicResistanceBuildingsClass.A21.value,SeismicResistanceBuildingsClass.A22.value,SeismicResistanceBuildingsClass.C21.value,SeismicResistanceBuildingsClass.C22.value]:
            if DTS != 4 and BYS < 2:
                result = False
            else:
                if BYS < 2 :
                    result = False
        
        return result

    def Check_4_3_4_1a(self, DTS : int, DuctilityType : int)-> bool:
        """
        TBDY-4.3.4.1a : DTS=1a, DTS=2a, DTS=3a ve DTS=4a olarak sınıflandırılan binalarda süneklik düzeyi sınırlı taşıyıcı sistemler kullanılamaz.

        Args:
            DTS (int): _description_
            DuctilityType (int): _description_

        Returns:
            bool: _description_
        """
        result = True
        if DTS in [SeismicDesignClass.one_a.value, SeismicDesignClass.two_a.value, SeismicDesignClass.three_a.value, SeismicDesignClass.four_a.value] and DuctilityType == DuctilityLevel.Sinirli.value:
            result = False
        
        return result

    def Check_4_3_4_1b(self, DTS : int, DuctilityType : int, BYS : int)-> bool:
        """
        TBDY-4.3.4.1b : BYS ≤ 6 olan ve DTS=1a ve DTS=2a olarak sınıflandırılan binalarda süneklik düzeyi karma taşıyıcı sistemler kullanılamaz.

        Args:
            DTS (int): _description_
            DuctilityType (int): _description_
            BYS (int): _description_

        Returns:
            bool: _description_
        """

    def Get_SeismicResistanceSystemClasifications(self, Ductility : int, ResistanceSystem : int, SlabSystem : int):
        pass


@dataclass
class Spectrum:
    BuildingManager : SeismicResistanceBuildingManeger = field(default_factory=SeismicResistanceBuildingManeger)
    
    def SetVariables(self) ->None:
        """Hesaplanmasi gereken değerleri hesaplar ve set eder."""
        self.ElasticSpectrums = self.HorizontalElasticSpectrum(self.BuildingManager.SeismicManager.TA, self.BuildingManager.SeismicManager.TB,self.BuildingManager.SeismicManager.SDs, self.BuildingManager.SeismicManager.SD1, self.BuildingManager.SeismicManager.TL)
        self.HorizontalDisplacementSpectrum()
        self.VerticalElasticSpektrum(self.BuildingManager.SeismicManager.TA, self.BuildingManager.SeismicManager.TB,self.BuildingManager.SeismicManager.SDs, self.BuildingManager.BuildingVariables.I)
        self.ReducedTargetSpectrum(self.BuildingManager.Rx, 
                                   self.BuildingManager.Dx, 
                                   self.BuildingManager.Ry, 
                                   self.BuildingManager.Dy, 
                                   self.BuildingManager.SeismicManager.TB, 
                                   self.BuildingManager.BuildingVariables.I)

    def HorizontalElasticSpectrum(self,TA : float, TB : float, SDs : float, SD1 : float, TL : float)-> pd.DataFrame:
        """TBDY yatay elastik tasarim spektrumu"""

        T_list = np.arange(0.0, TL,.005)
            
        Sa = []
        
        for i in T_list:
            
            if i <TA:
                Sa.append(round((0.4 + 0.6*(i/TA))*SDs, 4))
                
            elif i >= TA and i <= TB:
                Sa.append(round(SDs, 4))
                
            elif i>TB and i <= TL:
                Sa.append(round(SD1/i, 4))
                
            elif i> TL:
                Sa.append(round(SD1 * TL/(i**2), 4))
                
        target_spec = {"T" : T_list,"Sae" : Sa}

        target_spec_df = pd.DataFrame().from_dict(target_spec)
        del target_spec,Sa,T_list
        
        return target_spec_df
    
    def HorizontalDisplacementSpectrum(self) -> None:
        """Tbdy elastik tasarim deplasman spektrumunun hesabi"""
        Sde = [(T**2/4*3.14**2)*9.81*Sae for T,Sae in zip(self.ElasticSpectrums["T"],self.ElasticSpectrums["Sae"])]
        self.ElasticSpectrums["Sde"] = Sde
    
    def VerticalElasticSpektrum(self,TA : float, TB : float, SDs : float, TL : float) -> None:
        """Dusey elastik dizayn spektrumu"""
        TAD , TBD , TLD = TA / 3 , TB / 3 , TL/2 
        Sve = []
        for T in self.ElasticSpectrums["T"] :
            if T < TAD :
                Sve.append(( 0.32 + 0.48*(T/TAD))* SDs)
                continue
            elif T >= TAD and T <= TBD:
                Sve.append(0.8 * SDs)
                continue
            elif T> TBD and T <= TLD:
                Sve.append( 0.8 * SDs * TBD / T)
                continue
            elif T> TLD:
                Sve.append( np.nan )
                continue
        self.ElasticSpectrums["Sve"] = Sve

        del Sve
    
    def Get_Ra(self,R : float, D : float, T : float, TB : float, I : float) -> float:
        """Verilen doğal titreşim periyoduna göre deprem yükü azaltma katsayisini hesaplar

        Args:
            T (float): Yapı doğal titreşim periyodu

        Returns:
            float: Deprem yükü azaltma katsayısı
        """
        if T > TB:
            Ra = R / I
        else:
            Ra = D + ((R/I)-D)*(T/TB)
        return Ra
    
    def ReducedTargetSpectrum(self, Rx : float, Dx : float, Ry :float, Dy : float, TB : float, I : float) -> None:
        """Azaltilmis elastik tasarim spektrumu"""
        Tw = self.ElasticSpectrums["T"]

        RaT_x = [ self.Get_Ra(Rx, Dx, T , TB, I) for T in Tw ]
        RaT_y = [ self.Get_Ra(Ry, Dy, T , TB, I) for T in Tw ]

        SaR_x = [(Sa/Ra) for Sa,Ra in zip(self.ElasticSpectrums["Sae"],RaT_x)]
        SaR_y = [(Sa/Ra) for Sa,Ra in zip(self.ElasticSpectrums["Sae"],RaT_y)]

        self.ElasticSpectrums["RaT_x"] = RaT_x
        self.ElasticSpectrums["SaR_x"] = SaR_x
        self.ElasticSpectrums["RaT_y"] = RaT_y
        self.ElasticSpectrums["SaR_y"] = SaR_y
        del SaR_x,SaR_y,RaT_x,RaT_y,Tw

    def Get_Sae_Tp(self,T : float, TA : float, TB : float, SDs : float, SD1 : float, TL : float) -> float:
        """ Binanin doğal titreşim periyoduna denk gelen elastik spektrum ivme değerini bulur. """
        #DEV fonksiyon girdileri çok fazla ve gereksiz bunlar önceden hesaplandığı için kullanılmasa nasıl olur?

        if T < TA:
            Sae = round((0.4 + 0.6*(T/TA))*SDs, 4)
            
        elif T >= TA and T<=TB:
           Sae = round(SDs, 4)
            
        elif T > TB and T <= TL:
            Sae = round(SD1/T, 4)
            
        elif T>TL:
            Sae = round(SD1 * TL / (T**2), 4)
        
        return round(Sae,4)
    
    def Get_SaR_Tp(self,R : float, D : float, T : float,TB : float, I : float, TA : float, SDs : float, SD1 : float, TL : float) -> float:
        """Verilen periyoda göre azaltilmiş elastik tasarim spektrum ivmesini hesaplar"""
        #DEV fonksiyon girdileri çok fazla ve gereksiz bunlar önceden hesaplandığı için kullanılmasa nasıl olur?
        Ra = self.Get_Ra(R, D , T, TB, I )
        Sae = self.Get_Sae_Tp(T,TA,TB, SDs, SD1, TL)
        return round(Sae / Ra,4)        
    
    def plot_Spectrums(self) -> None:
        #INFO grafikler tek bir bütün halde olacak şekilde çizildi.

        fig = plt.figure(figsize=(12, 8),layout="constrained",dpi=100)
        
        subfigs = fig.subfigures(1, 2, wspace=0.07,hspace=0.07)
        axs0 = subfigs[0].subplots(2, 1) # sol figure
        axs1 = subfigs[1].subplots(2, 1) # sağ figure

        # Sol üst taraftaki çizimler
        axs0[0].grid()
        axs0[0].axvline(c = "k");axs0[0].axhline(c = "k")
        axs0[0].set_xlabel('Period (sn)',fontsize = 12)  
        axs0[0].set_ylabel('Sa(T) (g)',fontsize = 12) 
        axs0[0].set_title("Horizontal Spectrums",fontsize = 14)  

        axs0[0].plot(self.ElasticSpectrums["T"] ,self.ElasticSpectrums["Sae"],label="Sae(T)")
        axs0[0].plot(self.ElasticSpectrums["T"] ,self.ElasticSpectrums["SaR_x"],label="SaR_x(T)")
        axs0[0].plot(self.ElasticSpectrums["T"] ,self.ElasticSpectrums["SaR_y"],label="SaR_y(T)")
        axs0[0].legend()

        # Sol_alt taraftaki çizimler
        axs0[1].grid()
        axs0[1].axvline(c = "k");axs0[1].axhline(c = "k")
        axs0[1].set_xlabel('Period (sn)',fontsize = 12)  
        axs0[1].set_ylabel('Ra(T) (g)',fontsize = 12) 
        axs0[1].set_title("Reduction Coefficient of Seismic Force",fontsize = 14)  
        axs0[1].plot(self.ElasticSpectrums["T"], self.ElasticSpectrums["RaT_x"],label="Ra_x(T)")
        axs0[1].plot(self.ElasticSpectrums["T"], self.ElasticSpectrums["RaT_y"],label="Ra_y(T)")
        axs0[1].legend()

        # Sağ üst taraftaki çizimler
        axs1[0].grid()
        axs1[0].axvline(c = "k");axs1[0].axhline(c = "k")
        axs1[0].set_xlabel('Period (sn)',fontsize = 12)  
        axs1[0].set_ylabel('Sde(T) (m)',fontsize = 12) 
        axs1[0].set_title("Design Displacement Spectrum",fontsize = 14)  

        axs1[0].plot(self.ElasticSpectrums["T"],self.ElasticSpectrums["Sde"],label="Sad(T)")
        axs1[0].legend()

        # Sağ alt taraftaki çizimler
        axs1[1].grid()
        axs1[1].axvline(c = "k");axs1[1].axhline(c = "k")
        axs1[1].set_xlabel('Period (sn)',fontsize = 12)  
        axs1[1].set_ylabel('Sae_v(T) (g)',fontsize = 12) 
        axs1[1].set_title("Vertical Spectrum",fontsize = 14) 

        axs1[1].plot(self.ElasticSpectrums["T"] ,self.ElasticSpectrums["Sve"],label="Sve(T)")
        axs1[1].legend()

        plt.legend()
        plt.show()


class TimeSeriesSpectra:
    
    def calc_timegap(Td : float, damp_ratio : float, T : float) -> float:
        """
        SUMMARY
            "Required time gap between mainshock and aftershock for dynamic analysis of structures" makalesinde iki ardışık deprem arasında doğal hareketi sıfırlamak için gerekli olan zaman aralığının hesaplanmasındaki  önerilen formülasyon kullanılmıştır.
        INPUT
            Td          : Kuvvetli yer hareketi süresi
            damp_ratio  : Yapının sönüm oranı
            T           : Yapının doğal titreşim periyodu
        OUTPUT
            R_timegap = durgun geçmesi gereken zaman (sn)
        """
        R_rest = Td*(0.05/damp_ratio)*(((21.8559*T)+0.0258)*(Td**(-0.9982))+0.0214)
        R_timegap = round(R_rest,0)
        return R_timegap
    
    def ReadRecord (filePath:str,gap:float,g=9.81,plot=1) -> pd.DataFrame:
        acceleration = []

        with open(filePath,"r") as file:
            for count,line in enumerate(file):
                if count >= 4:
                    #newfile = filePath.split('/')[-1].rsplit(".VT2")[0].rsplit(".AT2")[0].rsplit(".DT2")[0]
                    #dosya = open(newfile.join(".txt"),"w",encoding="utf-8")
                    #for satir in line:
                    #    dosya.write(line)
                    #dosya.close()
                    for i in line.strip().split():
                        acceleration.append(float(i)*g)
                if count == 3:
                    npts = float(line.replace(",","").replace("SEC","").split()[1])
                    dt = float(line.replace(",","").replace("SEC","").split()[3])
        time = np.arange(0,npts*dt,dt)
        
        if gap is not None:
            timegap = np.arange(time[-1],time[-1]+gap+dt,dt)
            accgap  = np.arange(0,len(timegap))*0
        
            time = np.append(time,timegap)
            acceleration = np.append(acceleration,accgap)
        
        if plot == 1:
            import matplotlib.pyplot as plt 
            fig, ax = plt.subplots(figsize=(20,10))
            fig.subplots_adjust(bottom=0.15, left=0.2)
            ax.grid()
            ax.plot(time,acceleration)
            ax.set_xlabel('Time [Sec]')
            ax.set_ylabel('Acceleration [cm/sn2]')
            #ax.axhline(0, color='black', lw=2)
            if g == 1:
                ax.set_ylabel('Acceleration [g]')
        TimeSeries = pd.DataFrame(columns=["Time","Acceleration"])
        
        TimeSeries["Time"] = time
        TimeSeries["Acceleration"] = acceleration

        return TimeSeries
        
    def load_PEERNGA_record(filepath):

        '''
            Load record in .at2 format (PEER NGA Databases)

            Input:
                filepath : file path for the file to be load
                
            Returns:
            
                acc : vector wit the acceleration time series
                dt : time step
                npts : number of points in record
                eqname : string with year_name_station_component info

        '''

        import numpy as np

        with open(filepath) as fp:
            line = next(fp)
            line = next(fp).split(',')
            year = (line[1].split('/'))[2]
            eqname = (year + '_' + line[0].strip() + '_' + 
                    line[2].strip() + '_comp_' + line[3].strip())
            line = next(fp)
            line = next(fp).split(',')
            npts = int(line[0].split('=')[1])
            dt = float(line[1].split('=')[1].split()[0])
            acc = np.array([p for l in fp for p in l.split()]).astype(float)
        
        return acc,dt,npts,eqname

    def TimeSeriesSpectra(self,Acceleration : pd.Series , Time : pd.Series ) -> pd.DataFrame:    
        """Piece-Wise exact method yardimi ile yer ivmesi kaydini spektral ivme kaydina cevirir """
        sampling_interval = Time[1]-Time[0]
        damping_ratio = 0.05
        Sd = []
        Sv = []
        Sa = []
        
        T = np.arange(0.05, 6.0,.01)
        for i in T:
            omega = 2*np.pi/i 
            mass = 1 
            k = ((omega)**2)*mass
            c = 2*mass*omega*damping_ratio
            K = k+3*c/sampling_interval + 6*mass/(sampling_interval**2)
            a = 6*mass / sampling_interval + 3*c
            b = 3*mass + sampling_interval*c/2
            u= [0]
            v= [0]
            ac= [0] 
            for j in range(len(Acceleration)-1) :
                df = - ( Acceleration[j+1] - Acceleration[j])+ a*v[j] + b*ac[j] # delta force
                du = df / K
                dv = 3*du / sampling_interval - 3*v[j] - sampling_interval * ac[j] /2    
                dac = 6* (du - sampling_interval*v[j]) / (sampling_interval**2) - 3* ac[j]
                u.append(u[j] + du)
                v.append(v[j] + dv)
                ac.append(ac[j] + dac)
            Sd.append(max([abs(x) for x in u]))
            #Sv.append(max([abs(x) for x in v]))
            #Sa.append(max([abs(x) for x in ac]))

            Sv.append(Sd[-1]*omega)
            Sa.append(Sd[-1]*omega**2)

          
        # plt.figure(figsize=[10,5] );
        # plt.suptitle(' Response Spectra' )
        # plt.subplot(3,1,1),plt.plot(T,Sd) ; plt.ylabel('Sd (m)') ; plt.grid()
        # plt.subplot(3,1,2),plt.plot(T,Sv) ; plt.ylabel('Sv (m/s)'); plt.grid()
        # plt.subplot(3,1,3),plt.plot(T,Sa) ; plt.ylabel('Sa (m/s2)'); plt.grid()

        dump_dict = {'Periods' : T, 'Sa' : Sa, 'Sv' : Sv, 'Sd' : Sd}
        Spec_variables = pd.DataFrame(dump_dict)
        del dump_dict

        return Spec_variables
    
    def LocationSeriesSpectra(self,T : float,Accelertions : pd.Series,Periods : pd.Series) -> float:
        """Verilen doğal titreşim periyodunun zaman serisinden elde edilen spektrumunda karsilik gelen spektral ivme değerini verir. Zaman serisinin spektrumlarinin(spektral ivme,spektral deplasman ve hiz) hesabi için TimeSeriesSpectra fonksiyonunu kullanin"""

        #issue: verilen periyod listede yoksa 0 dönecektir enterpolasyonla spektral ivme değeri bulunabilir...
        targetSa = 0
        for index,T_series in enumerate(Periods):
            if round(T_series,2) == T:
                targetSa = Accelertions[index]
                break
        return round(targetSa,4)

    def ChangeTimeSeriesForPGA(TimeSeries : pd.DataFrame,targetPGA : float) -> pd.DataFrame:
        """ Zaman serisini PGA değerine göre verilen ivme değeri ile orantılayarak yeniden oluşturur."""
        realPGA = TimeSeries.Acceleration.max()
        coef = targetPGA/realPGA
        newTimeSeries = [acc*coef for acc in TimeSeries.Acceleration]
        TimeSeries["ChangedAcc"] = newTimeSeries
        del newTimeSeries
        return TimeSeries
    
# def main() ->None:
#     # SeismicVariables = SeismicInputs(lat = 38.12949,lon = 32.45234,soil = "ZC",intensity = "DD2")
#     # print(SeismicVariables)
#     # print("="*80)
    

#     # RCBuilding = SeismicResistanceBuildingInputs(Hn=70,
#     #                                              I=1,
#     #                                              DuctilLevel=DuctilityLevel.Yuksek,
#     #                                              ResSystemType_X=ResSystemType.BAKarma,
#     #                                              ResSystemType_Y=ResSystemType.BAKarma,
#     #                                              SlabSystem=SlabSystem.Plak_kirisli)
#     # print(RCBuilding)
#     # print("="*80)
    

#     # SIM = SeismicInputsManager(SeismicVariables=SeismicVariables, TL=6.0)
#     # print(SIM)
#     # print("="*80)
    
    
#     # Srbm = SeismicResistanceBuildingManeger(BuildingVariables=RCBuilding, SeismicManager=SIM, BuildingClass=SeismicResistanceBuildingsClass.A14, Rx=6,Ry=3)
#     # Srbm.SetVariables()
#     # print("="*80)

#     # Spec = Spectrum(BuildingManager=Srbm)
#     # print(Spec)

#     # print(Spec.ElasticSpectrums)
#     # Spec.plot_HorizontalElasticSpectrum()

#     # print(f"DTS = {Srbm.DTS} ; BYS = {Srbm.BYS}")
#     # StructureVariables = SeismicResistanceBuildingInputs(Hn  = 70, 
#     #                                                      Rx   = 8.0, 
#     #                                                      Ry   = 8.0, 
#     #                                                      Dx   = 3.0, 
#     #                                                      Dy   = 3.0, 
#     #                                                      I   = 1.0, 
#     #                                                      DTS = SeismicDesignClass.one, 
#     #                                                      BYS = 1,
#     #                                                      DuctilLevel = DuctilityLevel.Yuksek,
#     #                                                      ResSystemType = ResSystemType.BACerceve,
#     #                                                      SlabSystem = SlabSystem.Plak_kirisli)

#     # rs = SeismicTSC(SeismicVariables = SeismicVariables,BuildingVariables = StructureVariables)

    
#     # print(StructureVariables)
#     # print(rs.ElasticSpectrums)
#     pass
    
# if __name__ == "__main__":
#     main()