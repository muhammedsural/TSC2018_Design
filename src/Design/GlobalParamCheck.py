
from dataclasses import dataclass, field

import pandas as pd


@dataclass
class StoryDriftCheck:
    StoryDriftTable : pd.DataFrame
    DD3_Sds         : float
    DD2_Sds         : float
    R               : float
    I               : float
    k               : float = field(default = 0.5)
    IsWallWithFlexibleJoints : bool = field(default=False)
    
    def Set(self)->None:
        self.lamda = self.Get_lambda(self.DD3_Sds,self.DD2_Sds)
        self.ERSD  = self.EffectiveRelativeStoreyDrift()
        self.ERSDCheck = self.Check_ERSD_Ratio()


    def Get_lambda(self, DD3_SDs : float, DD2_SDs : float) -> float:
        return DD3_SDs/DD2_SDs
    
    #TODO bu fonksiyonda etkin göreli kat ötelemeleri tablosunun oluşturulması hedeflenmektedir. Verilecek kombinasyon sonuçları için bir filtreleme yapmaz bunu bilerek storydrift tablosu gönderilmeli.
    def EffectiveRelativeStoreyDrift(self) -> pd.DataFrame:
        pass
    
    #TODO bu fonksiyonda etkin göreli kat ötelemelerinin oranlarının kontrol tablosunun oluşturulması hedeflenmektedir. Fonksiyondaki girdi tablosu `EffectiveRelativeStoreyDrift` fonksiyonunun çıktı tablosudur.
    def Check_ERSD_Ratio(self)->pd.DataFrame:
        pass

@dataclass
class SecondOrderEffectCheck:
    pass