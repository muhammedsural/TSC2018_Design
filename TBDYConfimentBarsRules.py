from dataclasses import dataclass, field
from math import floor


@dataclass
class ConfimentRebarSpace:
    Nd                      : float
    Width                   : float
    Height                  : float
    Cover                   : float
    Xkol                    : int
    Ykol                    : int
    Fck                     : float
    Fywk                    : float
    ConfimentRebarDiameter  : float
    LongnitudeRebarDiameter : float
    Ac                      : float = field(init=False)
    Ack                     : float = field(init=False)
    bkx                     : float = field(init=False)
    bky                     : float = field(init=False)
    ax                      : float = field(init=False)
    ay                      : float = field(init=False)
    Ashx                    : float = field(init=False)
    Ashy                    : float = field(init=False)
    Ash                     : float = field(init=False)
    s_EndConfAreaMax        : float = field(init=False)
    s_MiddleConfAreaMax     : float = field(init=False)
    s_OtherConfAreaMax      : float = field(init=False)
    s_OptEndConfArea        : float = field(init=False)
    s_OptMiddleConfArea     : float = field(init=False)
    

    def __post_init__(self):
        self.Set_Variables()
        
    def Set_Variables(self) -> None:
        self.Ac                  = self.GetAc(self.Height,self.Width)
        self.Ack                 = self.GetAck(self.Height,self.Width,self.Cover)
        self.bkx                 = self.Get_bk(self.Width)
        self.bky                 = self.Get_bk(self.Height)
        self.ax                  = self.Get_a_i(self.bkx,self.Xkol)
        self.ay                  = self.Get_a_i(self.bky,self.Ykol)
        ConfRebarArea            = self.GetRebarArea(self.ConfimentRebarDiameter)
        self.Ashx                = self.GetAshw_i(self.Xkol,ConfRebarArea)
        self.Ashy                = self.GetAshw_i(self.Ykol,ConfRebarArea)
        self.Ash                 = self.Ashx + self.Ashy
        bmin                     = min(self.Height,self.Width)

        self.s_EndConfAreaMax    = self.UcSarilmaBolgesiKontrolleri(self.LongnitudeRebarDiameter,bmin)
        self.s_MiddleConfAreaMax = self.OrtaSarilmaBolgesiKontrolleri(bmin,self.LongnitudeRebarDiameter)
        self.s_OtherConfAreaMax  = self.DigerSarilmaBolgesiKontrolleri(bmin,self.LongnitudeRebarDiameter)


        self.s_OptEndConfArea    = self.OptimizeConfinmentRebarSpace(smax= self.s_EndConfAreaMax,
                                                                    Ash= self.Ash,
                                                                    Nd= self.Nd,
                                                                    Ac= self.Ac,
                                                                    fck= self.Fck,
                                                                    fywk= self.Fywk,
                                                                    Ack= self.Ack,
                                                                    bkx= self.bkx,
                                                                    bky= self.bky
                                                                    )
        self.s_OptMiddleConfArea = self.OptimizeConfinmentRebarSpace(smax= self.s_MiddleConfAreaMax,
                                                                    Ash= self.Ash,
                                                                    Nd= self.Nd,
                                                                    Ac= self.Ac,
                                                                    fck= self.Fck,
                                                                    fywk= self.Fywk,
                                                                    Ack= self.Ack,
                                                                    bkx= self.bkx,
                                                                    bky= self.bky
                                                                    )

    def GetAc(self,Height : float, Width : float)->float:
        """Brüt enkesit alanını hesaplar

        Args:
            Height (float): Kesit yüksekliği
            Width (float): Kesit genişliği

        Returns:
            float: Brüt kesit alanı 
        """
        Ac = Height * Width
        return Ac
    
    def GetAck(self,Height : float, Width : float,Cover : float) -> float:
        """Çekirdek betonun brüt alanını hesaplar

        Args:
            Height (float): Kesit yüksekliği
            Width (float): Kesit genişliği
            Cover (float): Net beton örtüsü

        Returns:
            float: Brüt çekirdek beton alanı
        """
        Ack = (Height - 2*Cover) * (Width - 2*Cover)
        return Ack
    
    def Get_bk(self, Dimension : float) -> float:
        """Çekirdek beton kenar uzunluğunu hesaplar

        Args:
            Dimension (float): Kesit kenar uzunluğu
            Cover (float): Net beton örtüsü

        Returns:
            float: Çekirdek beton kenar uzunluğu
        """
        bk = Dimension - 2*self.Cover
        return bk
    
    def Get_a_i(self,bk : float, koladet : int):
        """Sargı donatıları arasındaki kol mesafesini hesaplar

        Args:
            bk (float): Çekirdek beton kenar ölçüsü
            koladet (int): İlgili kenar doğrultusundaki sargı kol adeti

        Returns:
            _type_: _description_
        """
        return bk / koladet

    def GetRebarArea(self,RebarDiameter : float) -> float:
        confrebararea = 3.14 * (RebarDiameter)**2 / 4
        return confrebararea

    def GetAshw_i(self,koladet : int,confrebararea : float) -> float:
        Ash = koladet * confrebararea
        return Ash

    def CheckConfinmendRebarDiameter(self,ConfRebarDia : float, LongRebarDia : float) -> bool:
        if ConfRebarDia < (LongRebarDia/3):
            print(f"Sargı donatısı çapı boyuna donatı çapının üçte birinden az olamaz!!! - TS500-7.4.1")
            return False
        return True

    def Check_a_i(self,ai : float,confrebardia : float):
        if ai > 25*(confrebardia/10):
            print(f"İlgili doğrultuda kol aralığı izin verilenin sınırın üstünde {ai}mm > {25*confrebardia}mm - TBDY-7.3.4.2")

        if ai > 300:
            print(f"İlgili doğrultuda kol aralığı izin verilenin sınırın üstünde {ai}mm > 300mm - TS500 7.4.1")
            
    def CheckNd(self,Nd : float,Ac : float, fck : float) -> bool:
        """Nd değerinin (0.2 * Ac * fck) değerinden büyük veya küçük eşit olma durumunu inceler. Büyükse False küçükse True döndürür.

        Args:
            Nd (float): Yük katsayıları ile çarpılmış düşey yükler ve deprem yüklerinin ortak etkisi
                        altında hesaplanan eksenel kuvvet
            Ac (float): Brüt kesit alani
            fck (float): Karakteristik beton dayanimi

        Returns:
            bool: True or False 
        """
        limit = 0.2 * Ac * fck
        if Nd > limit:
            return False
        else:
            return True

    def UcSarilmaBolgesiKontrolleri(self,LongRebar : int, b_min : float) -> float:
        """Kolon veya perde başlıklarında uç sarılma bölgelerinde yapılabilecek maximum etriye aralığını verir.

        Args:
            LongRebar (int): Boyuna donatı çapı
            b_min (float): En küçük kenar uzunluğu

        Returns:
            float: maximum uç sarılma bölgesi etriye aralığı
        """
        s1 = 50 # TBDY2018
        s2 = 150 # TBDY2018
        s3 = b_min/3 # TBDY2018
        s4 = 6 * LongRebar  # TBDY2018
        s5 = 12 * LongRebar # TS500
        s_max = min(s2,s3,s4,s5)

        if s_max < s1 :
            s_max = s1

        return s_max

    def OrtaSarilmaBolgesiKontrolleri(self,b_min : float,LongRebar : int) -> float:
        s1 = 150
        s2 = b_min/3
        s3 = 12 * LongRebar # TS500
        # s4 = 6 * LongRebar # TBDY2018
        s_max = min(s1,s2,s3)

        return s_max

    def DigerSarilmaBolgesiKontrolleri(self, b_min : float,LongRebar : int) -> float:
        s1 = 200
        s2 = b_min/2
        s3 = floor(12 * LongRebar) # TS500
        s_max = min(s1,s2,s3)
        return s_max
    
    def MinEnineDonatiOraniDikdörtgen(self,s : float, b_kx : float,b_ky : float, Ac : float, Ack : float, fck : float, fywk : float,NdControl : bool) -> float:
        """_summary_
        Args:
            s   (float) : Etriye aralığı 
            b_kx(float) : X doğrultusu için, kolon veya perde uç bölgesi
                            çekirdeğinin enkesit boyutu (en dıştaki enine donatı eksenleri arasındaki mesafe)
            b_ky(float) : Y doğrultusu için, kolon veya perde uç bölgesi
                            çekirdeğinin enkesit boyutu (en dıştaki enine donatı eksenleri arasındaki mesafe)
            Ac  (float) : Kolonun veya perde uç bölgesinin brüt enkesit alanı  
            Ack (float) : Sargı donatısının dışından dışına alınan ölçü içinde kalan çekirdek beton alanı 
            fck (float) : Betonun karakteristik silindir basınç dayanımı 
            fywk(float) : Enine donatının tasarım akma dayanımı

        Returns:
            Ash_min(float)
        """

        Ash1x = 0.30  * s * b_kx * ((Ac/Ack) - 1) * (fck/fywk)
        Ash2x = 0.075 * s * b_kx * (fck / fywk)
        Ash1y = 0.30  * s * b_ky * ((Ac/Ack) - 1) * (fck/fywk)
        Ash2y = 0.075 * s * b_ky * (fck / fywk)

        Ash1 = Ash1x + Ash1y
        Ash2 = Ash2x + Ash2y

        Ash = max(Ash1,Ash2)
        if NdControl:
            Ash = Ash * 2/3        
        return Ash

    def OptimizeConfinmentRebarSpace(self,smax : float,Ash : float, Nd : float, Ac : float, fck : float, fywk : float, Ack : float, bkx : float, bky : float) -> int:
        s    = [i for i in range(50,210)]   # cm
        s_ideal = 0
        for s_opt in s :
            if s_opt > smax:
                break
            NdControl = self.CheckNd(Nd,Ac,fck)
            Ashmin_dikd = self.MinEnineDonatiOraniDikdörtgen(s_opt,bkx,bky,Ac,Ack,fck,fywk,NdControl)
            if Ash < Ashmin_dikd:
                if s_opt == 50:
                    #info :  İlk iterasyonda Ash_min değerinin altında kalıyorsa diğerlerinde zaten sağlayamaz s_opt değeri 50mm e eşitlenip uyarı verilir.
                    print(f"Ash = {Ash}mm2 < Ash_min = {Ashmin_dikd}mm2 kesitteki çiroz,etriye arttırılmalı ve/veya sargı donatı çapı büyütülmeli...")
                    break
                s_ideal = s_opt
                break
            s_ideal = s_opt

        return s_ideal

    def Get_lb(self, fsy : float, fctd : float, LognRebarDia : float, Nervur : bool = True, LocationClass : int = 2):
        """TS 500’de çekme donatısı için verilen kenetlenme boyunu hesaplar

        Args:
            fsy (float): Boyuna donatı tasarım akma dayanımı
            fctd (float): Beton tasarım eksenel çekme dayanımı
            LognRebarDia (float): Boyuna donatı çapı (çeşitli çaplar varsa, en büyüğü)
            Nervur (bool, optional): Nervür donatimi kullanılan. Defaults to True.
            LocationClass (int, optional): Konum 1 mi veya konum 2 mi. Defaults to 2.

        Raises:
            ValueError: Konum bilgisi yanlışsa döndürülür.

        Returns:
            _type_: kenetlenme boyu
        """
        # 
        
        lb = 0.12 * (fsy/fctd) * LognRebarDia
        minlimit = 20 * LognRebarDia
        
        if lb < minlimit :
            lb = minlimit
        
        if LocationClass == 1 :
            lb = 1.4 * lb
            
        if LocationClass != 1 and LocationClass != 2:
            raise ValueError("Konum tanımı 1 veya 2 olmalıdır...")
        
        if Nervur != True:
            lb = 2 * lb
        
        return lb
    
    def Get_EndRegionConfinmentLength(self, b_max : float, ln : float):
        """Uç sarılma bölgelerinin uzunluklarını hesaplar.

        Args:
            b_max (float): kolon en büyük kesit boyutu
            ln (float): kolon serbest yüksekliği

        Returns:
            _type_: Uç sarılma bölgelerinin uzunlukları
        """
        l1 = 1.5 * b_max
        l2 = 500
        l3 = ln/6
        l = max(l1,l2,l3)
        return l
        
        
        
        
# def main() -> None:
#     """Units N,mm"""
#     Nd     = 16000 
#     B = 300
#     H = 500
#     s = 250
#     TieRebarDiameter = 8
#     LongnitRebarDiameter = 14
#     ClearCoverConc = 25
#     NumBarsTop,NumBarsInterior,NumBarsBot = 2,1,2
#     X_tiebars = 2
#     Y_tiebars = 3
#     fsy = 220
#     fywe = 220
#     eps_su = 0.08
#     f_co = 25
#     f_ce = 25
#     ETRIYEARALIKLARI = ConfimentRebarSpace(Nd, B/10, H/10, ClearCoverConc/10, X_tiebars, Y_tiebars, f_co, fywe, TieRebarDiameter, LongnitRebarDiameter)
#     print(f"Uç sarılma bölgesi optimum etriye aralığı : {ETRIYEARALIKLARI.s_OptEndConfArea},\nOrta sarılma bölgesi optimum etriye aralığı : {ETRIYEARALIKLARI.s_OptMiddleConfArea},\nSarılma bölgesi dışındaki optimum etriye aralığı : {ETRIYEARALIKLARI.s_OtherConfAreaMax}")
    
# #     Nd     = 16000 
# #     Width  = 30 # cm
# #     Height = 50 # cm
# #     Cover  = 2.5 # cm
# #     x_kol  = 4
# #     y_kol  = 4
# #     fck    = 25   # N/mm2 
# #     fywk   = 420  # N/mm2 
# #     ConfRebarDia = 8  # mm
# #     LognRebarDia = 14 # mm

# #     ETRIYEARALIKLARI = ConfimentRebarSpace(Nd,Width,Height,Cover,x_kol,y_kol,fck,fywk,ConfRebarDia,LognRebarDia)
# #     print(f"Uç sarılma bölgesi optimum etriye aralığı : {ETRIYEARALIKLARI.s_OptEndConfArea},\nOrta sarılma bölgesi optimum etriye aralığı : {ETRIYEARALIKLARI.s_OptMiddleConfArea},\nSarılma bölgesi dışındaki optimum etriye aralığı : {ETRIYEARALIKLARI.s_OtherConfAreaMax}")
# if __name__ == "__main__":
#     main()
