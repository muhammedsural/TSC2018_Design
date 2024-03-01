import pandas as pd
from dataclasses import dataclass,field,asdict
import numpy as np 
import scipy as sc
from enum import Enum


@dataclass
class SeismicInputs:
    """
    Args:
        lat       : latitude of location
        lon       : longitude of location
        soil      : soil class
        intensity : intensity level 
                        options: DD1, DD2, DD3, DD4
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

    lat       : float  = field(default_factory=float)
    lon       : float  = field(default_factory=float)
    soil      : str    = field(default_factory=str)
    intensity : str    = field(default_factory=str)
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
        return f"Latitude :{self.lat}\nLongitude :{self.lon}\nSoil Class :{self.soil}\nIntensity:{self.intensity}\nSs :{self.Ss}\nS1 :{self.S1}\nPGA :{self.PGA}\nPGV :{self.PGV}\nFs :{self.Fs}\nF1 :{self.F1 }\nSDs :{self.SDs}\nSD1 :{self.SD1}\nTA :{self.TA}\nTB :{self.TB}\nTL :{self.TL}"

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
        Hn        : Bina serbest yüksekliği [m]
        R         : Yapi davranis katsayisi
        D         : Overstrength factor (Dayanim fazlalagi katsayisi)
        I         : Building important factor (Bina onem katsayisi)
        DTS       : Deprem tasarim sinifi 
        BYS       : Bina yükseklik sinifi
    """
    Hn        : float  = field(default=10)
    R         : float  = field(default=8.)
    D         : float  = field(default=3.)
    I         : float  = field(default=1.)
    DTS       : str    = field(default="1") 
    BYS       : int    = field(default=1)

    def __repr__(self) -> str:
        return f"Hn :{self.Hn}\nR :{self.R}\nD :{self.D}\nI :{self.I}\nDTS :{self.DTS}\nBYS :{self.BYS}"

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
class SeismicTSC:
    SeismicVariables  : SeismicInputs = field(default_factory=SeismicInputs)
    BuildingVariables : SeismicResistanceBuildingInputs = field(default_factory=SeismicResistanceBuildingInputs)

    def __post_init__(self) -> None:
        self.SetVariables()
    
    def SetVariables(self) ->None:
        """Hesaplanmasi gereken değerleri hesaplar ve set eder."""
        self.__GetSpectralMapVariables()
        self.__Get_SpectrumCoefficients()
        self.__GetDTS()
        self.__GetMaxBYS()
        self.__Get_TA()
        self.__Get_TB()
        self.ElasticSpectrums = self.__HorizontalElasticSpectrum()
        self.__HorizontalDisplacementSpectrum()
        self.__VerticalElasticSpektrum()
        self.__ReducedTargetSpectrum()
 
    def __GetSpectralMapVariables(self) -> dict:
        """Spektrum haritasinda verilen koordinatlara göre spektral harita değerlerini bulur"""
        afad_spectra_params_df = pd.read_csv("Resource\AFAD_TDTH_parametre.csv")   

        # grid locattions
        x = afad_spectra_params_df["LAT"].to_list()
        y = afad_spectra_params_df["LON"].to_list()
        
        # spectral values dictionary
        spectral_value_dict = {}
        for column_name in ["Ss","S1","PGA","PGV"]:

            z = afad_spectra_params_df[ f"{column_name}-{self.SeismicVariables.intensity}"].to_list()

            interpolator = sc.interpolate.CloughTocher2DInterpolator( np.array([x,y]).T , z)

            spectral_value = round( interpolator( self.SeismicVariables.lat, self.SeismicVariables.lon)  , 3 )
            spectral_value_dict[column_name] = spectral_value
        
        self.SeismicVariables.Ss = spectral_value_dict["Ss"]
        self.SeismicVariables.S1 = spectral_value_dict["S1"]
        self.SeismicVariables.PGA = spectral_value_dict["PGA"]
        self.SeismicVariables.PGV = spectral_value_dict["PGV"]

    def __Get_SpectrumCoefficients(self)->None:
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

        

        # Short period
        if self.SeismicVariables.Ss < Ss_range[0]:
            self.SeismicVariables.Fs = FS_table[self.SeismicVariables.soil][0]
            self.SeismicVariables.SDs = self.SeismicVariables.Ss * self.SeismicVariables.Fs
        elif self.SeismicVariables.Ss > Ss_range[-1]:
            self.SeismicVariables.Fs = FS_table[self.SeismicVariables.soil][-1]
            self.SeismicVariables.SDs = self.SeismicVariables.Ss * self.SeismicVariables.Fs    
        else:
            self.SeismicVariables.Fs = round( np.interp(self.SeismicVariables.Ss,Ss_range, FS_table[self.SeismicVariables.soil]) , 3) 
            self.SeismicVariables.SDs = self.SeismicVariables.Ss * self.SeismicVariables.Fs

        # 1sec period
        if self.SeismicVariables.S1 < S1_range[0] :
            self.SeismicVariables.F1 = F1_table[self.SeismicVariables.soil][0]
            self.SeismicVariables.SD1 = self.SeismicVariables.S1 * self.SeismicVariables.F1
        elif self.SeismicVariables.S1 > S1_range[-1]:
            self.SeismicVariables.F1 = F1_table[self.SeismicVariables.soil][-1]
            self.SeismicVariables.SD1 = self.SeismicVariables.S1 * self.SeismicVariables.F1
        else:
            self.SeismicVariables.F1 = round(np.interp(self.SeismicVariables.S1, S1_range, F1_table[self.SeismicVariables.soil]), 3)
            self.SeismicVariables.SD1 = self.SeismicVariables.S1 * self.SeismicVariables.F1


        del Ss_range,FS_table,S1_range,F1_table
   
    def __GetDTS(self) -> None:
        """Deprem tasarim sinifini bulur."""
        if self.SeismicVariables.SDs < .33 : 
            self.BuildingVariables.DTS = "4a"
            if self.BuildingVariables.I ==2 or self.BuildingVariables.I == 3:
                self.BuildingVariables.DTS = "4"
                
        if self.SeismicVariables.SDs >= 0.33 and self.SeismicVariables.SDs < 0.50 : 
            self.BuildingVariables.DTS = "3a"
            if self.BuildingVariables.I ==2 or self.BuildingVariables.I == 3:
                self.BuildingVariables.DTS = "3"
                
        if self.SeismicVariables.SDs >= 0.50 and self.SeismicVariables.SDs < 0.75 :
            self.BuildingVariables.DTS = "2a" 
            if self.BuildingVariables.I ==2 or self.BuildingVariables.I == 3:
                self.BuildingVariables.DTS = "2"
        if self.SeismicVariables.SDs >= 0.75 : 
            self.BuildingVariables.DTS = "1a"
            if self.BuildingVariables.I ==2 or self.BuildingVariables.I == 3:
                self.BuildingVariables.DTS = "1"
    
    def __GetMaxBYS(self): 
        """TBDY2018 Tablo 3.3 e göre BYS sinifini bulur."""
        if self.BuildingVariables.DTS in ["1","1a","2","2a"]:
            dts = 0
        if self.BuildingVariables.DTS in ["3","3a"]:
            dts = 1
        if self.BuildingVariables.DTS in ["4","4a"]:
            dts = 1
        
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
        self.BuildingVariables.BYS = df_bys[dts][df_bys[dts] < self.BuildingVariables.Hn].index[0]
        del BYS,dts,df_bys
        
    def __Get_TA(self) -> float:
        """Yatay elastik tasarim spektrum sol köşe periyodu."""
        self.SeismicVariables.TA = 0.2 * self.SeismicVariables.SD1 / self.SeismicVariables.SDs

    def __Get_TB(self) -> float:
        """Yatay elastik tasarim elastik spektrum sağ köşe periyodu"""
        self.SeismicVariables.TB = self.SeismicVariables.SD1 / self.SeismicVariables.SDs
    
    def __HorizontalElasticSpectrum(self)-> pd.DataFrame:
        """TBDY yatay elastik tasarim spektrumu"""

        T_list = np.arange(0.0, self.SeismicVariables.TL,.005)
            
        Sa = []
        
        for i in T_list:
            
            if i <self.SeismicVariables.TA:
                Sa.append(round((0.4 + 0.6*(i/self.SeismicVariables.TA))*self.SeismicVariables.SDs, 4))
                
            elif i >= self.SeismicVariables.TA and i <= self.SeismicVariables.TB:
                Sa.append(round(self.SeismicVariables.SDs, 4))
                
            elif i>self.SeismicVariables.TB and i <= self.SeismicVariables.TL:
                Sa.append(round(self.SeismicVariables.SD1/i, 4))
                
            elif i> self.SeismicVariables.TL:
                Sa.append(round(self.SeismicVariables.SD1 * self.SeismicVariables.TL/(i**2), 4))
                
        target_spec = {"T" : T_list,"Sae" : Sa}

        target_spec_df = pd.DataFrame().from_dict(target_spec)
        del target_spec,Sa,T_list
        
        return target_spec_df
    
    def __HorizontalDisplacementSpectrum(self) -> None:
        """Tbdy elastik tasarim deplasman spektrumunun hesabi"""
        Sde = [(T**2/4*3.14**2)*9.81*Sae for T,Sae in zip(self.ElasticSpectrums["T"],self.ElasticSpectrums["Sae"])]
        self.ElasticSpectrums["Sde"] = Sde
    
    def __VerticalElasticSpektrum(self) -> None:
        """Dusey elastik dizayn spektrumu"""
        TAD , TBD , TLD = self.SeismicVariables.TA / 3 , self.SeismicVariables.TB / 3 , self.SeismicVariables.TL / 2
        Sve = []
        for T in self.ElasticSpectrums["T"] :
            if T < TAD :
                Sve.append(( 0.32 + 0.48*(T/TAD))* self.SeismicVariables.SDs)
                continue
            elif T >= TAD and T <= TBD:
                Sve.append(0.8 * self.SeismicVariables.SDs)
                continue
            elif T> TBD and T <= TLD:
                Sve.append( 0.8 * self.SeismicVariables.SDs * TBD / T)
                continue
            elif T> TLD:
                Sve.append( np.nan )
                continue
        self.ElasticSpectrums["Sve"] = Sve

        del Sve
    
    def __Get_Ra(self,T : float) -> float:
        """Verilen doğal titreşim periyoduna göre deprem yükü azaltma katsayisini hesaplar

        Args:
            T (float): Yapı doğal titreşim periyodu

        Returns:
            float: Deprem yükü azaltma katsayısı
        """
        if T > self.SeismicVariables.TB:
            Ra = self.BuildingVariables.R / self.BuildingVariables.I
        else:
            Ra = self.BuildingVariables.D + ((self.BuildingVariables.R/self.BuildingVariables.I)-self.BuildingVariables.D)*(T/self.SeismicVariables.TB)
        return Ra
    
    def __ReducedTargetSpectrum(self) -> None:
        """Azaltilmis elastik tasarim spektrumu"""
        Tw = self.ElasticSpectrums["T"]
        RaT = [ self.__Get_Ra(T) for T in Tw ]
        SaR = [(Sa/Ra) for Sa,Ra in zip(self.ElasticSpectrums["Sae"],RaT)]
        self.ElasticSpectrums["RaT"] = RaT
        self.ElasticSpectrums["SaR"] = SaR
        del SaR,RaT,Tw

    def Get_Sae_Tp(self,T : float) -> float:
        """ Binanin doğal titreşim periyoduna denk gelen elastik spektrum ivme değerini bulur. """

        if T < self.SeismicVariables.TA:
            Sae = round((0.4 + 0.6*(T/self.SeismicVariables.TA))*self.SeismicVariables.SDs, 4)
            
        elif T >= self.SeismicVariables.TA and T<=self.SeismicVariables.TB:
           Sae = round(self.SeismicVariables.SDs, 4)
            
        elif T > self.SeismicVariables.TB and T <= self.SeismicVariables.TL:
            Sae = round(self.SeismicVariables.SD1/T, 4)
            
        elif T>self.SeismicVariables.TL:
            Sae = round(self.SeismicVariables.SD1 * self.SeismicVariables.TL / (T**2), 4)
        
        return round(Sae,4)
    
    def Get_SaR_Tp(self,T : float) -> float:
        """Verilen periyoda göre azaltilmiş elastik tasarim spektrum ivmesini hesaplar"""
        Ra = self.__Get_Ra(T)
        Sae = self.Get_Sae_Tp(T)
        return round(Sae / Ra,4)        
    
    def plot_HorizontalElasticSpectrum(self) -> None:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(5,5))
        fig.dpi=200
        ax.grid()
        ax.axvline(c = "k");ax.axhline(c = "k")
        ax2 = ax.twinx()
        ax.plot(self.ElasticSpectrums["T"] ,self.ElasticSpectrums["Sae"],label="Response Acc. Spec.")
        ax2.plot(self.ElasticSpectrums["T"],self.ElasticSpectrums["Sde"],label="Response Disp. Spec.",color = 'g')

        ax.set_xlabel('Period (sn)',fontsize = 12)  # Add an x-label to the axes.
        ax.set_ylabel('Pseudo-Spectral Accelerations (g)',fontsize = 12)  # Add a y-label to the axes.
        ax2.set_ylabel('Pseudo-Spectral Displacements (m)',fontsize = 12)  # Add a y-label to the axes.
        ax.set_title("TSC-2018 Design Elastic Spectrum",fontsize = 16)  # Add a title to the axes.
        plt.show()

class TimeSeriesSpectra:
    
    def calc_timegap(Td : float, damp_ratio : float, T : float) -> float:
        """
        INFO
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

# def main() ->None:
#     SeismicVariables = SeismicInputs(lat = 39.85, lon = 30.2, soil ="ZC", intensity="DD2")
#     rs = SeismicTSC(Variables = SeismicVariables)
#     rs.plot_HorizontalElasticSpectrum()
    
    
# if __name__ == "__main__":
#     main()