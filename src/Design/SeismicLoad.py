# import pandas as pd
# from dataclasses import dataclass,field,asdict

#TODO bu bölümdeki geliştirmeler devam etmektedir.

# @dataclass
# class SeismicInput:
#     """
#     TL   : Spektrum hesabindaki en uç periyot
#     R    : Yapi davranis katsayisi
#     I    : Bina onem katsayisi
#     D    : Dayanim fazlalagi katsayisi
#     SDs  : Kisa periyot tasarim spektral ivme katsayisi [boyutsuz]
#     Sd1  : 1.0 saniye periyot için tasarim spektral ivme katsayisi [boyutsuz]
#     """
#     SDs  : float= field(default_factory=float)
#     SD1  : float= field(default_factory=float)
#     TL   : float= field(default_factory=float)
#     R    : float= field(default_factory=float)
#     I    : float= field(default_factory=float)
#     D    : float= field(default_factory=float)

# @dataclass
# class EquivalentLateralLoad:
#     """Eşdeğer deprem yükünün hesabi 
#     Args
#         Floors           : Katlarla alakalı bilgilerin tutuldugu DataFrame [Kat,Kat kütlesi,Kat yüksekliği] kütlelerinin tutuldugu DataFrame
#         Tpx              : X yönündeki doğal titresim periyodu
#         Tpy              : Y yönündeki doğal titresim periyodu
#         SeismicVariables : Sismik verilerin bulunduğu sinif
#     """
#     Floors       : pd.DataFrame 
#     Tpx          : float
#     Tpy          : float
#     Var_Seismic  : SeismicInput = field(default_factory=SeismicInput)
#     Vte_x        : float = 0.0
#     Vte_y        : float = 0.0

#     def __post_init__(self) -> None:
#         self.calc_Total_Force()

#     def __repr__(self) -> str:
#         return super().__repr__()
    
#     # Fonksiyon hazır
#     def get_Total_Mass(self) -> float:
#         """Kat kütlelerinden toplam kütlenin hesabi"""
#         return self.Floors["Masses"].sum()
    
#     # Fonksiyon hazır
#     def calc_Total_Force(self):
#        """Eşdeğer deprem yükü yöntemine göre taban kesme kuvveti hesabi"""
#        SaR_Tpx = self.Var_Seismic.Get_SaR(T = self.Tpx)
#        SaR_Tpy = self.Var_Seismic.Get_SaR(T = self.Tpy)
#        print(f"SaR(Tpx) = {SaR_Tpx}; SaR(Tpy) = {SaR_Tpy} ")

#        self.Vte_x = round((self.Floors["Masses"].sum() * SaR_Tpx * 9.81),2)
#        self.Vte_y = round((self.Floors["Masses"].sum() * SaR_Tpy * 9.81),2)

#        min_Force = round((0.04 * self.Floors["Masses"].sum() * self.Var_Seismic.SeismicVariables.I * self.Var_Seismic.SeismicVariables.SDs * 9.81),2)

#        if self.Vte_x < min_Force :
#            print(f"Minimum deprem kuvvetinden az ciktigi icin toplam deprem kuveti revize edildi => {self.Vte_x} < {min_Force} ")
#            self.Vte_x = min_Force

#        if self.Vte_y < min_Force :
#            print(f"Minimum deprem kuvvetinden az ciktigi icin toplam deprem kuveti revize edildi => {self.Vte_y} < {min_Force} ")
#            self.Vte_y = min_Force
    
#     # Fonksiyon hazır değil
#     def calc_Story_Load(self):
#         """Toplam tabana kesme kuvvetinin katlara dagitilmasi"""

#         #Kamçı yükü
#         F_NE_X = 0.0075 * self.Floors["Floors"].count() * self.Vte_x
#         F_NE_Y = 0.0075 * self.Floors["Floors"].count() * self.Vte_y


#         #Kat yükleri
#         Force_x = self.Vte_x  - F_NE_X
#         Force_y = self.Vte_y  - F_NE_Y

#         Story_Forces = self.Floors.copy()
#         #df.assign(e=pd.Series(np.random.randn(sLength)).values)
#         Hi_list =[]
#         Hi = 0
#         for i in self.Floors["Height"]:
#             Hi += i
#             Hi_list.append(Hi)
#         Story_Forces["Hi"] = Hi_list           
#         Story_Forces["miHi"] = Story_Forces["Masses"] * Story_Forces["Hi"]

#         Total = Story_Forces["miHi"].sum()

#         Vtx = [round((Force_x *(miHi/Total)),2) for miHi in Story_Forces["miHi"]]
#         Vty = [round((Force_y *(miHi/Total)),2) for miHi in Story_Forces["miHi"]]
        
#         Story_Forces["Fx"] = Vtx
#         Story_Forces["Fy"] = Vty

#         return Story_Forces
    
#     # Fonksiyon hazır değil
#     def calc_Approximate_Fundimental_Period(self):
#         """Yaklasik periyot hesabi"""
#         pass
    
#     # Fonksiyon hazır değil
#     def Get_Ct(self,BuildingType : int) -> float:
#         """
#             BuildingType : Bina tasiyici sisteminin tipi 
#                             0 -> betonarme çerçevelerden oluşan binalar
#                             1 -> çelik çerçevelerden veya çaprazli çelik çerçevelerden oluşan binalar
#                             2 -> Deprem etkilerinin tamaminin betonarme perdeler tarafindan karsilandigi binalar
#                             3 -> Diğer binalar
#         """
#         if BuildingType == 0:
#             Ct = 0.1
#         if BuildingType == 1:
#             Ct = 0.08
#         if BuildingType == 3:
#             Ct = 0.07
#         if BuildingType == 2:
#             pass
#         pass

#     # Fonksiyon hazır değil
#     def Approximate_Period(self,BuildingType : int) -> float:
#         """
#         BuildingType : Bina tasiyici sisteminin tipi 
#                             0 -> betonarme çerçevelerden oluşan binalar
#                             1 -> çelik çerçevelerden veya çaprazli çelik çerçevelerden oluşan binalar
#                             2 -> Deprem etkilerinin tamaminin betonarme perdeler tarafindan karsilandigi binalar
#                             3 -> Diğer binalar

#         TSC2018-4.7.3.3:  DTS = 1, 1a, 2, 2a ve BYS ≥ 6 olan binalarda ve DTS = 3, 3a, 4, 4a olan tüm binalarda hakim doğal titreşim periyodu, 4.7.3.1’den hesaplanmaksizin, doğrudan 4.7.3.4’te verilen ampirik TpA periyodu olarak alinabilir
#                                                                                                     TpA = Ct HN**(3/4)
#         HN : Rijit bodrum üstündeki üst yapinin toplam yüksekliği (m)
#         """
#         Ct = self.Get_Ct(BuildingType)
#         HN = self.Floors["StoryHeight"].sum()
#         TpA = Ct * HN**(3/4)
#         return TpA

#     # Fonksiyon hazır
#     def calc_Torsional_Coefficient(self,n_bi,isA1 = True) -> float:
#         """Eşdeğer deprem yükü hesabi icin ek eksantrisite katsayisinin hesabi"""

#         if isA1 is True and n_bi> 1.2 and n_bi <= 2.0:
#             D_bi = (n_bi/1.2)**2
        
#         if isA1 is not True:
#             D_bi = 1.0
        
#         if n_bi > 2.0 :
#             return ValueError("nbi degeri 2 den fazla")
        
#         return D_bi
        

