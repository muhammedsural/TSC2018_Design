import math as mt
import numpy as np
from pandas import DataFrame
from dataclasses import dataclass,field
import matplotlib.pyplot as plt

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
    f_ywe                   : float
    eps_su                  : float
    f_co                    : float
    f_ce                    : float
    eps_co                  : float = field(default=0.002)
    eps_io                  : float = field(default=0.0025)
    As                      : float = field(init = False)
    bo                      : float = field(init = False)
    ho                      : float = field(init = False)    
    Cumulative_ai_2         : float = field(init = False)
    ke                      : float = field(init = False)
    Ash_x                   : float = field(init = False)  
    Ash_y                   : float = field(init = False)  
    ro_x                    : float = field(init = False)
    ro_y                    : float = field(init = False)
    fe_confined             : float = field(init = False)
    fe_unconfined           : float = field(init = False)
    lambda_c_confined       : float = field(init = False)
    lambda_c_unconfined     : float = field(init = False)
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
    f_cu_confined           : float = field(init=False)
    f_cu_unconfined         : float = field(init=False)
    #Performans sınırları için
    alfa_se                 : float = field(init=False)
    ro_sh_min               : float = field(init=False)
    omega_we                : float = field(init=False)
    eps_cp                  : float = field(init=False)
    fc_cp                   : float = field(init=False)
    eps_ls                  : float = field(init=False)
    fc_ls                   : float = field(init=False)
    fc_io                   : float = field(init=False)
    
    
    def __post_init__(self) -> None:
        self.Set_Variables()
                  
    def Get_Cumulative_ai2(self,Bw : float, H : float, ClearCoverConc : float, TieRebarDiameter : float, LongnitRebarDiameter : float,
              NumBarsBot : int, NumBarsTop : int, NumBarsInterior : int) -> float:
        """Boyuna donati araliklari karelerinin toplamini hesaplar.

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
        """Çekirdek beton bölgesinin genisligini hesaplar.

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
        """Çekirdek beton bölgesinin yuksekligini hesaplar.

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
        """Boyuna donati alanini hesaplar.

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
        int_bar_area = 2 * NumBarsInterior * bar_area #Sağ ve solda olduğu düşünüldüğü için 2 ile çarpıldı Gövde donatı adeti girilirken tek bir doğrultudaki giriliyor bundan dolayı 2 ile çarpmak gerekir.
        bot_bar_area = NumBarsBot * bar_area

        A_s = top_bar_area + bot_bar_area + int_bar_area
        
        return A_s

    def Get_ke(self,As : float,s : int,bo : float, ho : float, Cumulative_ai_2 : float) -> float:
        """Sargilama etkinlik katsayisi oranini hesaplar.

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
        d = 1/(1-(As/(bo*ho)))
        k_e =round((a*b*c*d),3)
        
        return k_e

    def Get_Ash(self,PieceOfTieBarCurrentDirection : int, TieRebarDiameter : float)-> float:
        """İlgili dogrultuda sargi donati alaninin hesaplar

        Args:
            PieceOfTieBarCurrentDirection (int): İlgili dogrultudaki sargi donatisi kol sayisi
            TieRebarDiameter (float): Sargi donatisi capi

        Returns:
            float: Sargi donati alani
        """
        TieBarArea = 3.14*TieRebarDiameter**2/4
        Ash = (PieceOfTieBarCurrentDirection * TieBarArea)
        return Ash
        
    def Get_TieVolumetricRate(self, Ash : float, s : int, CoreConcLengthCurrentDirection) -> float:
        """Hacimsel sargi donatisi oranini hesaplar.

        Args:
            Ash (int): Enine donati alani
            s (int): Enine donati araligi
            CoreConcLengthCurrentDirection (float): İlgili dogrultudaki cekirek beton uzunlugu

        Returns:
            float: Hacimsel sargi donatisi orani
        """
        ro = round(Ash / (s * CoreConcLengthCurrentDirection),5)
        return ro

    def Get_f_e(self,k_e : float, ro_x : float, ro_y : float, f_ywe : float,IsConfined : bool = True) -> float:
        """Etkili sargilama basincini hesaplar

        Args:
            k_e (float): Sargilama etkinlik katsayisi orani
            ro_x (float): X dogrultusundaki hacimsel sargi donatisi orani
            ro_y (float): Y dogrultusundaki hacimsel sargi donatisi orani
            f_syw (float): Donati celiginin akma dayanimi
            IsConfined (bool, optional): Sargili beton mu? Dogru ise True yanlis ise False. Defaults to True.

        Returns:
            float: Etkili sargilama basinci
        """
        f_e = 0.0
        if IsConfined:
            f_ex = round(k_e*ro_x*f_ywe,3)
            f_ey = round(k_e*ro_y*f_ywe,3)

            f_e=(f_ex+f_ey)/2
        
        return f_e

    def Get_Lambda_c(self,f_e : float, f_co : float) -> float:
        """Sargilama etki katsayisini hesaplar.

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
        """Sargili beton basinc dayanimini hesaplar.

        Args:
            lamda_c (float): Sargilama etki katsayisi
            f_co (float): Sargisiz betonun basinc dayanimi

        Returns:
            float: Sargili beton basinc dayanimi
        """
        f_cc = lamda_c*f_co
        return f_cc

    def Get_eps_cc(self,lambda_c : float, eps_co : float = 0.002) -> float:
        """Sargili beton basinc dayanimindaki birim sekildegistirmeyi hesaplar.

        Args:
            lambda_c (float): Sargilama etki katsayisi
            eps_co (float, optional): Sargisiz beton basinc dayanimindaki sekil degistirmesi. Defaults to 0.002.

        Returns:
            float: Sargili beton basinc dayanimindaki birim sekildegistirme
        """
        eps_cc = eps_co*(1+5*(lambda_c-1))
        return eps_cc

    def Get_E_c(self,f_co : float) -> float:
        """Betonun elastisite modülünü hesaplar.

        Args:
            f_co (float): Sargisiz betonun basinc dayanimi

        Returns:
            float: Betonun elastisite modülü
        """
        E_c = 5000*mt.sqrt(f_co)
        return E_c

    def Get_E_secant(self,f_cc : float, eps_cc : float) -> float:
        """Sargili beton sekant elastisite modülünü hesaplar.

        Args:
            f_cc (float): Sargili beton basinc dayanimi
            eps_cc (float): Sargili beton basinc dayanimindaki birim şekildegistermesi

        Returns:
            float: Sargili beton sekant elastisite modülü
        """
        E_sec = f_cc/eps_cc
        return E_sec

    def Get_eps_cu2(self,ro_x : float, ro_y : float, f_sy : float, f_cc : float, eps_su : float) -> float:
        """Sargili betondaki maksimum basinc birim sekildegistirmesini hesaplar. 

        Args:
            ro_x (float): X dogrultusundaki hacimsel sargi donatisi orani
            ro_y (float): Y dogrultusundaki hacimsel sargi donatisi orani
            f_sy (float): Donati celigi akma dayanimi
            f_cc (float): Sargili beton dayanimi
            eps_su (float): Donati celiginin kopma birim sekildegistirmesi

        Returns:
            float: Sargili betondaki maksimum basinc birim sekildegistirmesi
        """
        eps_cu = 0.004 + (1.4 * ((ro_x + ro_y) / 2) * f_sy * eps_su) / f_cc  
        return eps_cu

    def Get_r(self,E_c : float,E_sec : float) -> float:
        """Normalize edilmiş elastisite katsayisini hesaplar.

        Args:
            E_c (float): Betonun elastisite modülü
            E_sec (float): Sargili beton sekant elastisite modülü

        Returns:
            float: Normalize edilmiş elastisite katsayisi
        """
        return E_c/(E_c-E_sec)
    
    def Get_x(self,eps : float, eps_cc : float) -> float:
        """Normalize edilmiş beton birim şekildeğiştirmesi katsayisini hesaplar.

        Args:
            eps (float): Birim şekildeğiştirme değeri
            eps_cc (float): Sargili beton basinc dayanimindaki birim şekildegistermesi

        Returns:
            float: Normalize edilmiş beton birim şekildeğiştirmesi katsayisi
        """
        return eps/eps_cc
    
    def Get_fc(self,f_cc : float, x : float, r : float):
        """Sargili betonda beton basinc gerilmesini hesaplar.

        Args:
            f_cc (float): Sargili beton basinc dayanimi
            x (float): Normalize edilmiş beton birim şekildeğiştirmesi katsayisi
            r (float): Normalize edilmiş elastisite katsayisi

        Returns:
            _type_: Sargili betonda beton basinc gerilmesi
        """
        fc = (f_cc * x * r)/(r -1 + x**r)
        return fc
        
    def Get_Stress_Strain(self,eps_cu : float, eps_cc : float, f_cc : float, r : float, StrainIncrement : float = 0.00001) -> DataFrame:
        """TBDY mander formulasyonlari ile hesaplanan gerilme-sekildegistirme degerlerinin hesaplar ve DataFrame olarak dondurur. 

        Args:
            eps_cu (float): Sargili betondaki maksimum basinc birim şekildeğiştirmesi
            eps_cc (float): Sargili beton basinc dayanimindaki birim sekildegistirme
            f_cc (float): Sargili beton basinc dayanimi
            r (float): Normalize edilmiş elastisite katsayisi
            StrainIncrement (float, optional): Birim sekildegistirme icin artim orani. Her verilen birim sekil degistirme icin bir gerilme hesaplar bunun icin artirim orani verilir. Defaults to 0.00001.

        Returns:
            DataFrame: Gerilme-sekildegistirme degerleri
        """
        x = []
        fc = []
        eps_c  = np.arange(0,eps_cu,0.00001)
        
        for eps in eps_c:
            x_birim = self.Get_x(eps,eps_cc) 
            x.append(x_birim)
            
            f_c_birim = self.Get_fc(f_cc, x_birim, r)
            fc.append(f_c_birim)
            
            # if eps == eps_co:
            #     f_co_sargılı = f_c_birim
        
        StressStrainDictionary = {"fc" : fc, "eps_c" : eps_c}
        df_StressStrain = DataFrame(StressStrainDictionary)
        
        return df_StressStrain
    
    def Get_eps_cu(self,fcu : float, eps_cp : float, eps_cc : float, f_cc: float, r : float):
        """_summary_

        Args:
            fcu (float): _description_
            eps_cp (float): _description_
            eps_cc (float): _description_
            f_cc (float): _description_
            r (float): _description_

        Returns:
            _type_: _description_
        """
        eps_c  = np.arange(eps_cp,eps_cp+5,0.0001)
        eps_cu = 0.0
        
        for eps in eps_c:
            x_birim = self.Get_x(eps,eps_cc)             
            f_c_birim = round(self.Get_fc(f_cc, x_birim, r),3)
            
            if f_c_birim - fcu < 0.001 or f_c_birim == fcu:
                eps_cu = eps
                break
            
        return eps_cu
        
    def Set_Variables(self)->None:
        """Hesaplanmasi gereken degerleri hesaplayip set eder."""
        
        self.As = self.Get_RebarArea(self.LongnitRebarDiameter,self.NumBarsBot,self.NumBarsTop,self.NumBarsInterior)
    
        self.bo = self.Get_bo(self.B,self.ClearCoverConc,self.TieRebarDiameter)
        self.ho = self.Get_ho(self.H,self.ClearCoverConc,self.TieRebarDiameter)
        
        self.Ash_x = self.Get_Ash(self.X_tiebars,self.TieRebarDiameter)
        self.Ash_y = self.Get_Ash(self.Y_tiebars,self.TieRebarDiameter)
        
        Ash = self.Ash_x + self.Ash_y
        
        self.ro_x = self.Get_TieVolumetricRate(Ash,self.s,self.bo)
        self.ro_y = self.Get_TieVolumetricRate(Ash,self.s,self.ho)
        
        self.Cumulative_ai_2 = self.Get_Cumulative_ai2(self.B, self.H, self.ClearCoverConc, self.TieRebarDiameter, self.LongnitRebarDiameter, self.NumBarsBot, self.NumBarsTop, self.NumBarsInterior)
        
        self.Ec = self.Get_E_c(self.f_co)
        
        
        self.ke = self.Get_ke(self.As,self.s,self.bo,self.ho,self.Cumulative_ai_2)
        #===================================================================================
        self.fe_confined   = self.Get_f_e(self.ke,self.ro_x,self.ro_y,self.f_ywe)
        self.fe_unconfined = self.Get_f_e(self.ke,self.ro_x,self.ro_y,self.f_ywe,IsConfined=False)
        #===================================================================================
        self.lambda_c_confined   = self.Get_Lambda_c(self.fe_confined,self.f_co)
        self.lambda_c_unconfined = self.Get_Lambda_c(self.fe_unconfined,self.f_co)
        #===================================================================================
        self.eps_cc_confined   = self.Get_eps_cc(self.lambda_c_confined,self.eps_co)
        self.eps_cc_unconfined = self.Get_eps_cc(self.lambda_c_unconfined,self.eps_co)
        #===================================================================================
        self.f_cc_confined   = self.Get_f_cc(self.lambda_c_confined,self.f_co)
        self.f_cc_unconfined = self.Get_f_cc(self.lambda_c_unconfined,self.f_co)
        
        #===================================================================================
        #Göçme öncesi strain sınırı hesaplamalari
        self.alfa_se   = self.Get_Alfa_se(self.As,self.s,self.bo,self.ho,self.Cumulative_ai_2)
        self.ro_sh_min = min(self.ro_x,self.ro_y)
        self.omega_we  = self.Get_Omega_we(self.alfa_se,self.ro_sh_min,self.f_ywe,self.f_ce)
        
        self.eps_cp    = self.Get_eps_cp(self.omega_we)
        #===================================================================================
                
        self.Esec_confined   = self.Get_E_secant(self.f_cc_confined,self.eps_cc_confined)
        self.Esec_unconfined = self.Get_E_secant(self.f_cc_unconfined,self.eps_cc_unconfined)
        
        self.r_confined   = self.Get_r(self.Ec,self.Esec_confined)
        self.r_unconfined = self.Get_r(self.Ec,self.Esec_unconfined)
        #===================================================================================
        # Kopma basinc gerilmesi maximum basınc gerilmesinin %10 daha az degeri olarak dusunulmustur. Buna karsılık gelen kopma birim sekildegistirmesi
        # hesabı yapilmaktadir. Bu noktada kesitteki etriyenin koptugu veya boyuna donatinin burkuldugu kabul edilir.
        f = round(self.f_cc_confined - (self.f_cc_confined * 0.1),3)
        self.eps_cu_confined   = self.Get_eps_cu(f, self.eps_cp, self.eps_cc_confined, self.f_cc_confined, self.r_confined)
        self.eps_cu_unconfined = 0.0035
        #===================================================================================        
        x_confined   = self.Get_x(self.eps_cu_confined,self.eps_cc_confined)
        x_unconfined = self.Get_x(self.eps_cu_unconfined,self.eps_cc_unconfined)
        #===================================================================================
        self.f_cu_confined   = self.Get_fc(self.f_cc_confined,x_confined,self.r_confined)
        self.f_cu_unconfined = self.Get_fc(self.f_cc_unconfined,x_unconfined,self.r_unconfined)
        #===================================================================================        
        #Performans sınırları hesaplamalari
        
        self.eps_ls    = self.Get_eps_ls(self.eps_cp)
        
        x_cp           = self.Get_x(self.eps_cp,self.eps_cc_confined)
        x_ls           = self.Get_x(self.eps_ls,self.eps_cc_confined)
        x_io           = self.Get_x(self.eps_io,self.eps_cc_confined)
        
        self.f_cp      = self.Get_fc(self.f_cc_confined,x_cp,self.r_confined)
        self.f_ls      = self.Get_fc(self.f_cc_confined,x_ls,self.r_confined)
        self.f_io      = self.Get_fc(self.f_cc_confined,x_io,self.r_confined)
    
    def Get_Alfa_se(self,As : float,s : int,bo : float, ho : float, Cumulative_ai_2 : float)-> float:
        """sargı donatısı etkinlik katsayısıni hesaplar

        Args:
            As (float): Boyuna donati alani
            s (int): Enine donati araliği
            bo (float): Cekirdek beton bolgesi genisligi
            ho (float): Cekirdek beton bolgesi yuksekligi
            Cumulative_ai_2 (float): Kumulatif boyuna donati araliklari karesi

        Returns:
            float: sargı donatısı etkinlik katsayısı
        """
        a = 1-(Cumulative_ai_2/(6*bo*ho))
        b = 1-(s/(2*bo))
        c = 1-(s/(2*ho))
        return a*b*c
    
    def ro_sh(self,Ash : float, bk : float, s : float):
        return Ash/(bk * s)
        
    def Get_Omega_we(self,alfa_se : float, ro_sh_min : float, f_ywe : float, f_ce : float)-> float:
        """Etkin sargi donatisinin mekanik donati oranini hesaplar.

        Args:
            alfa_se (float): sargi donatisi etkinlik katsayisi
            ro_sh_min (float): dikdörtgen kesitte iki yatay doğrultuda hacimsel enine donati oraninin küçük olani
            f_ywe (float): Enine donatinin ortalama (beklenen) akma dayanimi [MPa]
            f_ce (float): Betonun ortalama (beklenen) basinc dayanimi [MPa]

        Returns:
            float: etkin sargi donatisinin mekanik donati orani
        """
        return alfa_se * ro_sh_min * f_ywe / f_ce
    
    def Get_eps_cp(self,omega_we : float) -> float:
        """TBDY2018 denklem 5.4a ya göre göçme öncesi birim şekildeğiştirme sinir değerini hesaplar

        Args:
            omega_we (float): etkin sargi donatisinin mekanik donati orani'ni göstermektedir

        Returns:
            float: göçme öncesi birim şekildeğiştirme sinir değeri
        """
        eps_cp = 0.0035 + 0.04*mt.sqrt(omega_we) #<= 0.018   

        if eps_cp > 0.018:
            eps_cp = 0.018

        return eps_cp
    
    def Get_eps_ls(self,eps_cp : float)-> float:
        """TBDY2018 denklem 5.7a ya göre kontrollü hasar birim şekildeğiştirme sinir değerini hesaplar

        Args:
            eps_cp (float): göçme öncesi birim şekildeğiştirme sinir değeri

        Returns:
            float: kontrollü hasar birim şekildeğiştirme sinir değeri
        """
        return eps_cp*0.75
    
    def Plot_Manders(self):
        """Sargili ve sargisiz modelin grafigini cizer ve sargili model üzerinde deprem yönetmeligi sinirlarini gösterir."""
        
        df_confined   = self.Get_Stress_Strain(self.eps_cu_confined,self.eps_cc_confined,self.f_cc_confined,self.r_confined)
        df_unconfined = self.Get_Stress_Strain(self.eps_cu_unconfined,self.eps_cc_unconfined,self.f_cc_unconfined,self.r_unconfined)

        fig, ax = plt.subplots(figsize=(15,10))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.grid()

        #Confined model plot
        ax.plot(df_confined["eps_c"],df_confined["fc"],label="Confined")
        ax.plot(self.eps_cc_confined, self.f_cc_confined,'o', c="y"     , label = f"eps_cc/f_cc = {round(self.eps_cc_confined,4)}/{round(self.f_cc_confined,2)}")
        ax.plot(self.eps_cu_confined, self.f_cu_confined,'o', c="black" , label = f"eps_cu/f_cu = {round(self.eps_cu_confined,4)}/{round(self.f_cu_confined,2)}")

        #Performance levels plot
        ax.plot(self.eps_cp, self.f_cp,'*', c="red",   label = f"eps_cp/f_cp = {round(self.eps_cp,4)}/{round(self.f_cp,2)}")
        ax.plot(self.eps_ls, self.f_ls,'*', c="green", label = f"eps_ls/f_ls = {round(self.eps_ls,4)}/{round(self.f_ls,2)}")
        ax.plot(self.eps_io, self.f_io,'*', c="blue",  label = f"eps_io/f_io = {round(self.eps_io,4)}/{round(self.f_io,2)}")

        #Unconfined model plot
        ax.plot(df_unconfined["eps_c"],df_unconfined["fc"],label="Unconfined")
        ax.plot(self.eps_cc_unconfined, self.f_cc_unconfined, 's', c="g", label = f"eps_cc/f_cc = {self.eps_cc_unconfined}/{self.f_cc_unconfined}")
        ax.plot(self.eps_cu_unconfined, self.f_cu_unconfined, 's', c="r", label = f"eps_cu/f_cu = {round(self.eps_cu_unconfined,4)}/{round(self.f_cu_unconfined,2)}")

        ax.set_xlabel('Strain (mm)')  # Add an x-label to the axes.
        ax.set_ylabel('Stress (MPa)')  # Add a y-label to the axes.
        ax.set_title("Mander Model")  # Add a title to the axes.

        ax.legend()
        plt.show()

    
class SteelModel:
    
    def SteelHardening(self,celiksınıfı,E_s = 2*10**5):

        celikler = {
            "S220" :[220,0.0011,0.011,0.12,1.20],
            "S420" :[420,0.0021,0.008,0.08,1.15],
            "B420C":[420,0.0021,0.008,0.08,1.15],
            "B500C":[500,0.0025,0.008,0.08,1.15]
            }
        f_sy = celikler[celiksınıfı][0]
        eps_sy = celikler[celiksınıfı][1]
        eps_sh = celikler[celiksınıfı][2]
        eps_su = celikler[celiksınıfı][3]
        f_su = celikler[celiksınıfı][4]*f_sy




        #Göçmenin Önlenmesi performans düzeyi için çeliğin birim şekildeğiştirmesi:
        eps_sgö = eps_su*0.4
        eps_skh = 0.75 * eps_sgö
        eps_ssh = 0.0075
        eps_perf = [eps_sgö,eps_skh,eps_ssh]
        fs_perf=[]
        eps_s_list = np.arange(0,eps_su,0.0001)

        for eps in eps_perf:
            if eps <= eps_sy:
                fs_perfm = E_s*eps
            elif eps_sy < eps <= eps_sh:
                fs_perfm = f_sy
            elif eps_sh < eps <= eps_su:
                fs_perfm = f_su-(f_su-f_sy)*((eps_su-eps)**2/(eps_su-eps_sh)**2)
            
            fs_perf.append(fs_perfm)
        
        
        fs_list =[]
        for eps_s in eps_s_list:
            if eps_s <= eps_sy:
                f_s = E_s*eps_s
            elif eps_sy < eps_s <= eps_sh:
                f_s = f_sy
            elif eps_sh < eps_s <= eps_su:
                f_s = f_su-(f_su-f_sy)*((eps_su-eps_s)**2/(eps_su-eps_sh)**2)
            
            fs_list.append(f_s)

        fig, ax = plt.subplots(figsize=(10,10))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.grid()
        ax.plot(eps_s_list,fs_list)
        ax.plot(eps_sgö,fs_perf[0],'o',c="r")
        ax.plot(eps_skh,fs_perf[1],'o',c="y")
        ax.plot(eps_ssh,fs_perf[2],'o',c="b")

        ax.annotate(f'f_göçme/eps_göçme = {round(eps_sgö,4)}/{round(fs_perf[0],2)}',
                    xy=(eps_sgö, fs_perf[0]), xytext=(eps_sgö+0.01, fs_perf[0]),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        
        ax.annotate(f'f_kh/eps_kh = {round(eps_skh,4)}/{round(fs_perf[1],2)}',
                    xy=(eps_skh, fs_perf[1]), xytext=(eps_skh+0.01, fs_perf[1]-10),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        
        ax.annotate(f'f_sh/eps_sh = {round(eps_ssh,4)}/{round(fs_perf[2],2)}',
                    xy=(eps_ssh, fs_perf[2]), xytext=(eps_ssh+0.01, fs_perf[2]),
                    arrowprops=dict(facecolor='black', shrink=0.05))


        return(eps_s_list,fs_list)

