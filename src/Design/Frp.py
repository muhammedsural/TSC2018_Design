"""
    As = Kolon donati alani (tek çubuk için)
    Ash = Enine donati alani
    b = Kesit genişliği
    bw = Kiriş gövde ya da kolon genişliği
    d = Kesitin faydali yüksekliği
    d′ = Beton örtüsü kalinliği
    Ef = Lifli polimerin elastisite modülü
    Es = Çelik donati elastisite modülü
    fcc = Lifli polimerle sargilanmiş betonun basinç dayanimi
    fcd = Beton basinç dayanimi
    fcm = 15.2.4.3’e göre tanimlanan mevcut beton basinç dayanimi
    fhs = Enine donatida 0.001’lik birim uzamaya karşilik gelen yanal basinç
    fhs = Enine donatidaki 0.001’lik birim uzama durumunda enine donati ve lifli polimerin sağlamasi gereken toplam yanal basinç
    fym = 15.2.4.3’e göre tanimlanan mevcut çelik akma dayanimi
    fl = Lifli polimerin sağladiği yanal basinç
    h = Çalişan doğrultudaki kesit boyutu
    LP = Lifli polimer
    Ls = Mevcut bindirme boyu
    n = Bindirme yapilmiş donati sayisi
    nf = Tek yüzdeki LP sargi tabaka sayisi
    p = Çekirdek kesiti çevresi
    rc = Köşelerde yapilan yuvarlatma yariçapi
    sf = Lifli polimer şeritlerin eksenden eksene araliği
    tf = Bir tabaka lifli polimer için etkili kalinlik (yetersiz bindirme boyu için yapilan sargilamada gerekli lifli polimer etkili kalinliği)
    Vc = Kesme kuvveti dayanimina betonun katkisi
    Vf = Lifli polimerin kesme kuvveti dayanimina katkisi
    Vmax = Asal basinç gerilmelerini sinirlamak için tanimlanan kesme kuvveti
    Vr = Kolon veya kirişin kesme dayanimi
    Vw = Kesme kuvveti dayanimina enine donatinin katkisi
    wf = Lifli polimer şeritinin genişliği
    εcc = Sargilanmiş beton basinç dayanimina karşi gelen birim kisalma
    εf = Lifli polimerin etkin birim uzama siniri
    εfu = Lifli polimerin kopma birim uzamasi
    κa = Kesit şekil etkinlik katsayisi
    φ = Boyuna donati çapi
    ρf = Lifli polimerin hacimsel orani
    ρsh = Enine donati orani, Ash/(s*bw)
"""
# from dataclasses import dataclass, field

from attr import define,field,validators
import pandas as pd

@define(frozen=True)
class FRPMaterial:
    """
        Name   (str)   : Frp malzemesinin ismi        
        Ef     (float) : Lifli polimerin elastisite modülü
        tf     (float) : Bir tabaka lifli polimer için etkili kalınlık
        eps_fu (float) : Lifli polimer kopma birim uzaması
        eps_f  (float) : Lifli polimer etkin birim uzama sınırı
    """
    Name   : str   = field(converter=str) 
    Ef     : float = field(validator=validators.ge(0))
    tf     : float = field(validator=validators.ge(0))
    eps_fu : float = field(validator=validators.ge(0))
    eps_f  : float = field(default=0.004)

    def Set_epsf(self, Tip : int):
        if Tip in [0,1]:
            raise ValueError("'Tip' değişkeni 0 veya 1 olabilir 0 : Kesme dayanımı için, 1 : Süneklilik artımı için")
        if Tip == 0:
            eps_f = min(0.004, 0.50*self.eps_fu)
        if Tip == 1:
            eps_f = min(0.01, 0.50*self.eps_fu)
        return eps_f
    
@define(frozen=True)
class FRPManager:
    """FRP sargısı ile ilgili hesapları yapar.
    Lp    (FRPMaterial) : LP malzeme özelliklerini içeren sınıf
    nf    (int)   : Tek yüzeydeki sargı tabakası sayısı
    wf    (float) : LP şeridinin genişliği
    eps_f (float) : LP etkin birim uzama sınırı
    d     (float) : Kesit faydalı yüksekliği
    sf    (float) : LP şeritlerinin eksenden eksene olan mesafesi
    """
    Lp    : FRPMaterial = field()
    nf    : int   = field(validator=validators.ge(0))
    wf    : float = field(validator=validators.ge(0))
    eps_f : float = field(validator=validators.ge(0))
    d     : float = field(validator=validators.ge(0))
    sf    : float = field(validator=validators.ge(0))


    def Get_Vf(self, nf : int, tf : float, wf : float, Ef : float, eps_f : float, d : float, sf : float, IsContinious : bool)-> float | ValueError:
        """_summary_

        Args:
            nf (int): Tek yüzdeki LP sargi tabaka sayisi
            tf (float): Bir tabaka lifli polimer için etkili kalinlik (yetersiz bindirme boyu için yapilan sargilamada gerekli lifli polimer etkili kalinliği)
            wf (float): LP şeridinin genişliği
            Ef (float): Lifli polimerin elastisite modülü
            eps_f (float): Lifli polimerin etkin birim uzama siniri
            d (float): Kesitin faydali yüksekliği
            sf (float): Lifli polimer şeritlerin eksenden eksene araliği
            IsContinious (bool): Sürekli sargılamamı yapıldı? Evet ise True Hayırsa False

        Raises:
            ValueError: Sürekli değilse ve sf sınır değeri aşıyorsa hata verilir

        Returns:
            float | ValueError: _description_
        """
        trashold = wf + (d/4)
        if IsContinious:
            sf = wf
        if IsContinious is False and sf > trashold:
            raise ValueError("sf space too long {} > {}".format(sf,trashold))
        Vf = 2 * nf * tf * wf * Ef * eps_f * d / sf
        return Vf
    
    def Get_Ka_ForRectangularSection(self, b : float, h : float, rc : float) -> float:
        """_summary_

        Args:
            b (float): Kesit genişliği
            h (float): Çalişan doğrultudaki kesit boyutu
            rc (float): Köşelerde yapilan yuvarlatma yariçapi

        Returns:
            float: _description_
        """
        
        
        Ka = 1 - (( (b - 2 * rc)**2 + (h - 2 * rc) ) / (3 * b * h))
        return Ka
    
    def Get_Ka_EllipseSection(self, b : float, h : float)-> float:
        return b/h
    
    def Get_Ka_CircularSection(self)-> int:
        return 1
        
    def Get_f1(self, Ka : float, ro_f : float, Ef : float, Tip : int) -> float:
        """_summary_

        Args:
            Ka (float): Kesit şekil etkinlik katsayisi
            ro_f (float): Lifli polimerin hacimsel orani
            eps_f (float): Lifli polimerin etkin birim uzama siniri
            Ef (float): Lifli polimerin elastisite modülü

        Returns:
            float: _description_
        """
        eps_f = self.Lp.Set_epsf(Tip)
        f1 = 0.5 * Ka * ro_f * eps_f * Ef
        return f1
    
    def Get_fcc(self, fcm:float, f1:float)-> float:
        """_summary_

        Args:
            fcm (float): TBDY2018 - 15.2.4.3’e göre tanimlanan mevcut beton basinç dayanimi
            f1 (float): Lifli polimerin sağladiği yanal basinç

        Returns:
            float: Eksenel basınç dayanımı
        """
        fcc = fcm * 1 + 2.4 * (f1/fcm)
        if fcc < 1.2*fcm:
            fcc = 1.2*fcm
        return fcc

    def Get_eps_cc(self, fcm:float, f1:float) -> float:
        """_summary_

        Args:
            fcm (float): _description_
            f1 (float): _description_

        Returns:
            float: _description_
        """
        eps_cc = 0.002 * ( 1 + 15 * (f1/fcm)**0.75 )
        return eps_cc









# if __name__ == "__main__":
#     FRPLIB = {
#         #                          mm   ,  MPa   ,  MPa  ,   ,  MPa
#         # Name                 ,   tf   ,  Ef    ,  Efu  ,   ,  fy
#     0  : ["DowAksa CFU10T      ", .5334 , 250000 , .013  , 1 , 4900],
#     1  : ["DowAksa CFU20T      ", .889  , 250000 , .013  , 1 , 4900],
#     2  : ["DowAksa CFU40T      ", 1.854 , 250000 , .0093 , 1 , 4900],
#     3  : ["DowAksa CFB10T      ", .6096 , 250000 , .011  , 1 , 4900],
#     4  : ["DowAksa CFB20T      ", .8182 , 250000 , .016  , 1 , 4900],
#     5  : ["TeknoWrap 300       ", .17   , 230000 , .021  , 1 , 4900],
#     6  : ["TeknoWrap 600       ", .34   , 230000 , .021  , 1 , 4900],
#     7  : ["MasterBrace-FIB 230 ", .111  , 230000 , .021  , 1 , 4900],
#     8  : ["MasterBrace-FIB 300 ", .166  , 230000 , .021  , 1 , 4900],
#     9  : ["MasterBrace-FIB 600 ", .337  , 230000 , .021  , 1 , 4900],
#     10 : ["MasterBrace-FIB 300H", .167  , 340000 , .014  , 1 , 4600],
#     11 : ["Grada Karbo F300    ", .166  , 240000 , .02   , 1 , 4900],
#     12 : ["Grada Karbo F600    ", .335  , 240000 , .02   , 1 , 4900],
#     13 : ["KRATOS C-FABRIC 300 ", .166  , 235000 , .02   , 1 , 4800],
#     14 : ["KRATOS C-FABRIC 600 ", .337  , 235000 , .02   , 1 , 4800],
#     15 : ["Tetraglobe CFB UD300", .17   , 230000 , .021  , 1 , 4900],
#     16 : ["Tetraglobe CFB UD600", .35   , 230000 , .021  , 1 , 4900],
#     17 : ["Tetraglobe CFB BA600", .35   , 230000 , .021  , 1 , 4900],
#     18 : ["MapeWrap C UNI-AX320", .18   , 240000 , .02   , 1 , 4900],
#     19 : ["MapeWrap C UNI-AX300", .164  , 252000 , .02   , 1 , 4900],
#     20 : ["MapeWrap C UNI-AX600", .331  , 252000 , .02   , 1 , 4900],
#     21 : ["MegaKarbon Wrap 300 ", .168  , 235000 , .02   , 1 , 4000],
#     22 : ["DowAksaCarbonWrap300", .28   , 240000 , .018  , 1 , 4200],
#     23 : ["DowAksaCarbonWrap600", .58   , 240000 , .018  , 1 , 4200],
#     24 : ["Carbonier SPN U 200 ", .111  , 240000 , .018  , 1 , 4900],
#     25 : ["Carbonier SPN U 300 ", .167  , 240000 , .018  , 1 , 4900],
#     26 : ["Carbonier SPN U 600 ", .333  , 240000 , .018  , 1 , 4900],
#     27 : ["Carbonier SPN U 800 ", .444  , 240000 , .018  , 1 , 4900]
#     }
#     df_frp = pd.DataFrame(FRPLIB).T
#     df_frp.columns = ['Name', 'tf', 'Ef', 'eps_fu', 'unit', 'fy']
    
#     LP = FRPMaterial(11,-5,.35,0.01)
#     print(LP)

