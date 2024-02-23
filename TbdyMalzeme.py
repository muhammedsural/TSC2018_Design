import math as mt
import numpy as np
from pandas import DataFrame

@dataclass
class Mander:
    B                       : float
    H                       : float
    s                       : float
    TieRebarDiameter        : float
    LongnitRebarDiameter    : float
    ClearCoverConc          : float
    NumBarsTop              : float
    NumBarsInterior         : float
    NumBarsBot              : float
    X_tiebars               : float
    Y_tiebars               : float
    fsy                     : float
    f_co                    : float
    As                      : float = field(init = False)
    bo                      : float = field(init = False)
    ho                      : float = field(init = False)    
    Cumulative_ai2          : float = field(init = False)
    ke                      : float = field(init = False)
    ro_x                    : float = field(init = False)
    ro_y                    : float = field(init = False)
    fe_confined             : float = field(init = False)
    fe_unconfined           : float = field(init = False)
    lambda_c_confined       : float = field(init = False)
    lamda_c_unconfined      : float = field(init = False)
    f_cc_confined           : float = field(init = False)
    f_cc_unconfined         : float = field(init = False)
    eps_cc_confined         : float = field(init = False)
    eps_cc_unconfined       : float = field(init = False)
    Ec                      : float = field(init = False)
    Esec_confined           : float = field(init = False)
    Esec_unconfined         : float = field(init = False)
    r_confined              : float = field(init = False)
    r_unconfined            : float = field(init = False)
    eps_cu_confined         : float = field(init = False)
    eps_cu_unconfined       : float = field(init = False)
    
               
      
    
    def Cumulative_ai2(self,Bw : float, H : float, ClearCoverConc : float, TieRebarDiameter : float, LongnitRebarDiameter : float,
              NumBarsBot : int, NumBarsTop : int, NumBarsInterior : int) -> float:
        """_summary_

        Args:
            Bw (float): Kesit genisligi
            H (float): Kesit yuksekligi
            ClearCoverConc (float): Temiz beton ortusu
            TieRebarDiameter (float): Sargi donatisi capi
            LongnitRebarDiameter (float): Boyuna donati capi
            NumBarsBot (int): Kesit altindaki boyuna donati adeti
            NumBarsTop (int): Kesit ustundeki boyuna donati adeti
            NumBarsInterior (int): Kesit ortasindaki boyuna donati adeti

        Returns:
            float: Kumulatif boyuna donati araliklari karesi
        """
        
        a_x = (Bw- 2*ClearCoverConc - 2*TieRebarDiameter - LongnitRebarDiameter)
        a_y = (H - 2*ClearCoverConc - 2*TieRebarDiameter - LongnitRebarDiameter)
        
        birim_x_top = a_x / (NumBarsTop-1)
        birim_x_bot = a_x / (NumBarsBot-1)

        birim_y = a_y / (NumBarsInterior + 1) #birim aralık y

        #ai_x = 2*(baslık_donatı_adeti-1)*birim_x**2
        ai_x_top    = (NumBarsTop-1) * birim_x_top**2
        ai_x_bot    = (NumBarsBot-1) * birim_x_bot**2
        ai_x_total  = ai_x_top + ai_x_bot
        ai_y        = 2*(NumBarsInterior+1) * birim_y**2

        #toplam_ai2 =ai_x+ai_y
        Cumulative_ai_2 = ai_x_total + ai_y
        return Cumulative_ai_2

    def Get_bo(self,Bw : float, ClearCoverConc : float, TieRebarDiameter : float) -> float:
        """_summary_

        Args:
            Bw (float): Kesit genisligi
            ClearCoverConc (float): Temiz beton ortusu
            TieRebarDiameter (float): Sargi donatisi capi

        Returns:
            float: cekirdek beton bolgesi genisligi
        """
        bo = Bw-(ClearCoverConc + TieRebarDiameter/2) * 2
        return bo

    def Get_ho(self,H : float, ClearCoverConc : float, TieRebarDiameter : float) -> float:
        """_summary_

        Args:
            H (float): Kesit yuksekligi
            ClearCoverConc (float): Temiz beton ortusu
            TieRebarDiameter (float): Sargi donatisi capi

        Returns:
            float: cekirdek beton bolgesi yuksekligi
        """
        ho = H-(ClearCoverConc + TieRebarDiameter/2) * 2
        return ho

    def Get_RebarArea(self,LongnitRebarDiameter : float,NumBarsBot : int, NumBarsTop : int, NumBarsInterior : int) -> float:
        """_summary_

        Args:
            LongnitRebarDiameter (float): Boyuna donati capi
            NumBarsBot (int): Kesit altindaki boyuna donati adeti
            NumBarsTop (int): Kesit ustundeki boyuna donati adeti
            NumBarsInterior (int): Kesit ortasindaki boyuna donati adeti

        Returns:
            float: Boyuna donati alani
        """
        bar_area = 3.14*LongnitRebarDiameter**2/4

        top_bar_area = NumBarsTop * bar_area
        int_bar_area = NumBarsInterior * bar_area
        bot_bar_area = NumBarsBot * bar_area

        A_s = top_bar_area + bot_bar_area + int_bar_area
        
        return A_s

    def Get_ke(self,As : float,s : int,bo : float, ho : float, Cumulative_ai_2 : float) -> float:
        """_summary_

        Args:
            bo (float): Cekirdek beton bolgesi genisligi
            ho (float): Cekirdek beton bolgesi yuksekligi
            Cumulative_ai_2 (float): Kumulatif boyuna donati araliklari karesi

        Returns:
            float: Sargilama etkinlik katsayisi orani
        """
        
        a = 1-(Cumulative_ai_2/(6*bo*ho))
        b = 1-(s/(2*bo))
        c = 1-(s/(2*ho))
        d = (1-(As/(bo*ho)))**-1
        k_e =round((a*b*c*d),3)
        
        return k_e

    def Get_TieVolumetricRate(self,PieceOfTieBarCurrentDirection : int, TieRebarDiameter : float, s : int, CoreConcLengthCurrentDirection) -> float:
        """_summary_

        Args:
            PieceOfTieBarCurrentDirection (int): İlgili dogrultudaki sargi donatisi kol sayisi
            TieRebarDiameter (float): Sargi donatisi capi
            s (int): Enine donati araligi
            CoreConcLengthCurrentDirection (float): İlgili dogrultudaki cekirek beton uzunlugu

        Returns:
            float: Hacimsel sargi donatisi orani
        """
        TieBarArea = 3.14*TieRebarDiameter**2/4
        Ash = (PieceOfTieBarCurrentDirection * TieBarArea)
        ro = round(Ash / (s * CoreConcLengthCurrentDirection),5)
        return ro

    def Get_f_e(self,k_e : float, ro_x : float, ro_y : float, f_sy : float,IsConfined : bool = True) -> float:
        """_summary_

        Args:
            k_e (float): Sargilama etkinlik katsayisi orani
            ro_x (float): X dogrultusundaki hacimsel sargi donatisi orani
            ro_y (float): Y dogrultusundaki hacimsel sargi donatisi orani
            f_sy (float): Donati celiginin akma dayanimi
            IsConfined (bool, optional): Sargili beton mu? Dogru ise True yanlis ise False. Defaults to True.

        Returns:
            float: Etkili sargilama basinci
        """
        f_e = 0.0
        if IsConfined:
            f_ex = round(k_e*ro_x*f_sy,3)
            f_ey = round(k_e*ro_y*f_sy,3)

            f_e=(f_ex+f_ey)/2
        
        return f_e

    def Get_Lambda_c(self,f_e : float, f_co : float) -> float:
        """_summary_

        Args:
            f_e (float): Etkili sargilama basinci
            f_co (float): Sargisiz betonun basinc dayanimi

        Returns:
            float: Sargilama etki katsayisi
        """
        ratio = f_e/f_co
        lamda_c = 2.254 * mt.sqrt(1+7.94*ratio) - (2*ratio) - 1.254
        return lamda_c

    def Get_f_cc(self,lamda_c : float, f_co : float) -> float:
        """_summary_

        Args:
            lamda_c (float): Sargilama etki katsayisi
            f_co (float): Sargisiz betonun basinc dayanimi

        Returns:
            float: Sargili beton dayanimi
        """
        f_cc = lamda_c*f_co
        return f_cc

    def Get_eps_cc(self,lambda_c : float, eps_co : float = 0.002) -> float:
        """_summary_

        Args:
            lambda_c (float): Sargilama etki katsayisi
            eps_co (float, optional): Sargisiz beton basinc dayanimindaki sekil degistirmesi. Defaults to 0.002.

        Returns:
            float: _description_
        """
        eps_cc = eps_co*(1+5*(lambda_c-1))
        return eps_cc

    def Get_E_c(self,f_co : float) -> float:
        """_summary_

        Args:
            f_co (float): Sargisiz betonun basinc dayanimi

        Returns:
            float: Betonun elastisite modülü
        """
        E_c = 5000*mt.sqrt(f_co)
        return E_c

    def Get_E_secant(self,f_cc : float, eps_cc : float) -> float:
        """_summary_

        Args:
            f_cc (float): Sargili beton basinc dayanimi
            eps_cc (float): Sargili beton basinc dayanimindaki birim şekildegistermesi

        Returns:
            float: Sargili beton sekant elastisite modülü
        """
        E_sec = f_cc/eps_cc
        return E_sec

    def Get_eps_cu(self,ro_x : float, ro_y : float, f_sy : float, f_cc : float, eps_su : float) -> float:
        """_summary_

        Args:
            ro_x (float): X dogrultusundaki hacimsel sargi donatisi orani
            ro_y (float): Y dogrultusundaki hacimsel sargi donatisi orani
            f_sy (float): Donati celigi akma dayanimi
            f_cc (float): Sargili beton dayanimi
            eps_su (float): Donati celiginin kopma birim sekildegistirmesi

        Returns:
            float: Sargili betondaki maksimum basinc birim sekildegistirmesi
        """
        eps_cu = 0.004+(1.4*((ro_x+ro_y)/2)*f_sy*eps_su)/f_cc
        return eps_cu

    def Get_r(self,E_c : float,E_sec : float) -> float:
        return E_c/(E_c-E_sec)
    
    def Get_x(self,eps : float, eps_cc : float) -> float:
        """_summary_

        Args:
            eps (float): Birim şekildeğiştirme değeri
            eps_cc (float): Sargili beton basinc dayanimindaki birim şekildegistermesi

        Returns:
            float: _description_
        """
        return eps/eps_cc
    
    def Get_fc(self,f_cc : float, x : float, r : float):
        fc = (f_cc * x * r)/(r -1 + x**r)
        return fc
    
    
    def Get_Stress_Strain(self, eps_cc : float, f_cc : float, r : float, StrainIncrement : float = 0.00001) -> DataFrame:
        x = []
        fc = []
        eps_c  = np.arange(0,eps_cu,0.00001)
        
        for eps in eps_c:
            x_birim = self.Get_x(eps,eps_cc) 
            x.append(x_birim)
            
            f_c_birim = self.Get_fc(f_cc, x_birim, r)
            f_c.append(f_c_birim)
            
            # if eps == eps_co:
            #     f_co_sargılı = f_c_birim
        
        StressStrainDictionary = {"fc" : fc, "eps_c" : eps_c}
        df_StressStrain = DataFrame(StressStrainDictionary)
        
        return df_StressStrain
    
    def Get_eps_c(fc : float):
        pass
    
def main() -> None:
    """Units N,mm"""
    B = 300
    H = 500
    s = 150
    TieRebarDiameter = 10
    LongnitRebarDiameter = 20
    ClearCoverConc = 30
    NumBarsTop,NumBarsInterior,NumBarsBot = 4,1,4
    X_tiebars = 2
    Y_tiebars = 4
    fsy = 420
    f_co = 30
    Tbdy_mander = Mander()
    
    Tbdy_mander.Get_Stress_Strain(eps_cc,f_cc,r)
    pass

if __name__=="__main__":
        
    main()
    