import math as mt
import numpy as np
import matplotlib.pyplot as plt

def tbdy_mander(celiksınıfı,f_co,bw,h,s,etriye_çapı,boyuna_donatı_çapı,pas_payı,
                numBarsTop,numBarsBot,gövde_donatı_adeti,x_koladeti,y_koladeti,plot=1,annotate=1):

    """
    INPUT:

    celiksınıfı         : "S220","S420","B420C","B500C" çelik modelleri girilebilir sadece etriye için
    f_co                : Beton basınç dayanımı
    bw                  : Kesitin genişliği [mm]
    h                   : Kesitin yüksekliği
    s                   : Etriye aralığı
    A_s                 : Boyuna donatı alanı
    etriye_çapı         : Etriye donatı çapı (mm)
    boyuna_donatı_çapı  : Boyuna donatı çapı (mm)
    pas_payı            : Beton pas payı (mm)
    baslık_donatı_adeti : Kesit başlık bölgesindeki donatı sayısı 2 başlıkta bulunan toplam adet
    gövde_donatı_adeti  : Kesit gövde bölgesindeki donatı sayısı 2 tarafta bulunan toplam adet
    x_koladeti          : x eksenini kesen sargı kol adeti
    y_koladeti          : y eksenini kesen sargı kol adeti
    plot                : Malzeme modeli çizimi default 1 dir çizimi yapar.


    OUTPUT:
    
    eps_c: 0 dan ultimate strain değerine kadar 0.00001 adımla oluşturulmuş liste
    f_c  : Her eps_c değerine karşılık hesaplanmış beton gerilmesi

    """
    eps_co = 0.002


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

    
    #Donatı alanları
    #numBarsTop, numBarsBot, numBarsIntTot

    bar_area = 3.14*boyuna_donatı_çapı**2/4

    top_bar_area = numBarsTop * bar_area
    int_bar_area = numBarsBot * bar_area
    bot_bar_area = gövde_donatı_adeti * bar_area

    A_s = top_bar_area + bot_bar_area + int_bar_area

    #ke değerinin bulunması
    b_0 = bw-(pas_payı+etriye_çapı/2)*2 #core_x
    h_0 = h-(pas_payı+etriye_çapı/2)*2 #core_y
    #birim_x = (bw-2*pas_payı-2*etriye_çapı-boyuna_donatı_çapı)/(baslık_donatı_adeti-1) #birim aralık x
    birim_x_top= (bw-2*pas_payı-2*etriye_çapı-boyuna_donatı_çapı)/(numBarsTop-1)
    birim_x_bot= (bw-2*pas_payı-2*etriye_çapı-boyuna_donatı_çapı)/(numBarsBot-1)

    birim_y =(h-2*pas_payı-2*etriye_çapı-boyuna_donatı_çapı)/(gövde_donatı_adeti+1) #birim aralık y

    #ai_x = 2*(baslık_donatı_adeti-1)*birim_x**2
    ai_x_top= (numBarsTop-1)*birim_x_top**2
    ai_x_bot= (numBarsBot-1)*birim_x_bot**2
    ai_x_total= ai_x_top+ai_x_bot
    ai_y = 2*(gövde_donatı_adeti+1)*birim_y**2

    #toplam_ai2 =ai_x+ai_y
    toplam_ai2_tot = ai_x_total+ai_y

    #a = 1-(toplam_ai2/(6*b_0*h_0))
    a = 1-(toplam_ai2_tot/(6*b_0*h_0))
    b = 1-(s/(2*b_0))
    c = 1-(s/(2*h_0))
    d = (1-(A_s/(b_0*h_0)))**-1
    k_e =round((a*b*c*d),3)
    #ro_x = A_sx/(s*b_0)
    #ro_y = A_sx/(s*h_0)
    #Hacimsel oranların bulunması
    #check kol adetleri
    x_kol_max = max(numBarsBot,numBarsTop)
    y_kol_max = gövde_donatı_adeti+2 #Çift sıra başlık donatısı göz ardı edilmiştir.

    if x_koladeti > x_kol_max:
        x_koladeti = x_kol_max
        print(f"x_koladeti {x_kol_max} olarak değiştirildi maksimum {x_kol_max} kadar atılabiliyor")
    if y_koladeti > y_kol_max:
        y_koladeti = y_kol_max
        print(f"y_koladeti {y_kol_max} olarak değiştirildi maksimum {y_kol_max} kadar atılabiliyor")

    ro_x = round((x_koladeti*3.14*etriye_çapı**2/4)/(s*b_0),5) #hacimsel oran x
    ro_y = round((y_koladeti*3.14*etriye_çapı**2/4)/(s*h_0),5) #hacimsel oran y

    #f_e değerinin bulunması
    f_ex = round(k_e*ro_x*f_sy,3)
    f_ey = round(k_e*ro_y*f_sy,3)

    f_e=(f_ex+f_ey)/2
    f_e_sargısız = 0

    lamda_c=2.254*mt.sqrt(1+7.94*(f_e/f_co))-(2*f_e/f_co)-1.254
    lamda_c_sargısız = 2.254*mt.sqrt(1+7.94*(f_e_sargısız/f_co))-(2*f_e_sargısız/f_co)-1.254
    
    f_cc = lamda_c*f_co
    f_cc_sargısız = lamda_c_sargısız*f_co

    eps_cc = eps_co*(1+5*(lamda_c-1))
    eps_cc_sargısız = eps_co*(1+5*(lamda_c_sargısız-1))

    E_c = 5000*mt.sqrt(f_co)

    E_sec = f_cc/eps_cc
    E_sec_sargısız = f_cc_sargısız/eps_cc_sargısız

    r = E_c/(E_c-E_sec)
    r_sargısız = E_c/(E_c-E_sec_sargısız)

    eps_cu = 0.004+(1.4*((ro_x+ro_y)/2)*f_sy*eps_su)/f_cc
    eps_cu_sargısız=0.0035

    eps_c = np.arange(0,eps_cu,0.00001)
    eps_c_sargısız = np.arange(0,eps_cu_sargısız,0.00001)
    

    """
    # Material Properties
    # ------------------------------------------------------------------------
    # CONCRETE default değer   
    # ====================================================================================================         
    Ec = 5000*Unit.MPa*(fc/Unit.MPa)**0.5     # Young's modulus
    #Ec = 3250 * fc**0.5 +14000
    nu = 0.2                        # Poisson's ratio
    Gc = Ec/(2*(1+nu))              # Shear modulus

    # unconfined concrete
    Kres = 0.2          # ratio of residual/ultimate to maximum stress
    fc1U = -fc          # UNCONFINED concrete (todeschini parabolic model), maximum stress
    eps1U = -0.003      # strain at maximum strength of unconfined concrete
    fc2U = Kres*fc1U    # ultimate stress
    eps2U = -0.01       # strain at ultimate stress

    # confined concrete
    Kfc = 1.2           # ratio of confined to unconfined concrete strength
    fc1C = Kfc*fc1U     # CONFINED concrete (mander model), maximum stress
    eps1C = 2*fc1C/Ec   # strain at maximum stres
    fc2C = Kres*fc1C    # ultimate stress
    eps2C = 5*eps1C     # strain at ultimate stress 

    # tensile-strength properties
    Lambda = 0.1        # ratio between unloading slope at eps2 and initial slope Ec
    fct = 0.14*fc       # tensile strength +tension
    Ets = fct/0.002     # tension softening stiffness

    # REINFORCING STEEL
    #============================================================================================================
    fsy = 500*Unit.MPa     # Yield stress
    Es = 2*10**5;     # Young's modulus
    bs = 0.01           # strain-hardening ratio
    R0 = 18             # control the transition from elastic to plastic branches
    cR1 = 0.925         # control the transition from elastic to plastic branches
    cR2 = 0.15          # control the transition from elastic to plastic branches


    celikler = {                       fsu/fsy
        "S220" :[220,0.0011,0.011,0.12,1.20],
        "S420" :[420,0.0021,0.008,0.08,1.15],
        "B420C":[420,0.0021,0.008,0.08,1.15],
        "B500C":[500,0.0025,0.008,0.08,1.15]
        }

    f_sy = celikler[celiksınıfı][0]
    eps_sy = celikler[celiksınıfı][1] Donatı çeliğinin akma birim şekildeğiştirmesi
    eps_sh = celikler[celiksınıfı][2] Donatı çeliğinin pekleşme başlangıcındaki birim şekildeğiştirmesi
    eps_su = celikler[celiksınıfı][3] Donatı çeliğinin kopma birim şekildeğiştirmesi
    f_su = celikler[celiksınıfı][4]*f_sy

    steel = [fsy,Es,bs,R0,cR1,cR2]

    # Elastic section properties
    #==================================================================================================================
    kCol=1

    Acol = HCol*BCol                  # Cross-sectional area of columns m2
    Icol = kCol*1/12*BCol*HCol**3     # Effective moment of inertia of columns m4

    """


    #Performans düzeyleri için beton birim kısalmaları:
    alfa_se = a*b*c
    ro_sh_min = min(ro_x,ro_y)
    omega_we =alfa_se*ro_sh_min*f_sy/f_co
    eps_cgö = 0.0035+0.04*mt.sqrt(omega_we) #<= 0.018   

    if eps_cgö > 0.018:
        eps_cgö = 0.018
    x_gö = eps_cgö/eps_cc
    f_cgö = (f_cc*x_gö*r)/(r-1+x_gö**r)

    eps_ckh=eps_cgö*0.75
    x_kh = eps_ckh/eps_cc
    f_ckh = (f_cc*x_kh*r)/(r-1+x_kh**r)

    eps_csh = 0.0025
    x_sh = eps_csh/eps_cc
    f_csh = (f_cc*x_sh*r)/(r-1+x_sh**r)


    #Sargılı ve sargısız beton modelinin bulunması
    x = []
    x_sargısız=[]
    f_c = []
    f_c_sargısız =[]

    for eps in eps_c_sargısız:
        x_birim_sargısız = (eps/eps_cc_sargısız)
        x_sargısız.append(x_birim_sargısız)
        f_c_birim_sargısız = (f_cc_sargısız*x_birim_sargısız*r_sargısız)/(r_sargısız-1+x_birim_sargısız**r_sargısız)
        f_c_sargısız.append(f_c_birim_sargısız)

    for eps in eps_c:
        x_birim = (eps/eps_cc)
        x.append(x_birim)
        f_c_birim = (f_cc*x_birim*r)/(r-1+x_birim**r)
        f_c.append(f_c_birim)
        if eps == eps_co:
            f_co_sargılı = f_c_birim
    
    
    if plot == 1:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(10,10))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.grid()
        
        ax.plot(eps_c,f_c,label="Confined model")
        ax.plot(eps_c_sargısız,f_c_sargısız,label="UnConfined model")
        
        ax.plot(eps_cc,f_cc,'o',c="b")
        ax.plot(eps_co,f_co,'o',c="b")
        ax.plot(eps_co,f_co_sargılı,'o',c="b")
        ax.plot(eps_cu,f_c_birim,'o',c="b")
        ax.plot(eps_cu_sargısız,f_c_birim_sargısız,'o',c="b")

        ax.plot(eps_cgö,f_cgö,'o',c="r")
        ax.text(eps_cgö-0.001, f_cgö+0.8, f'GÖ {round(eps_cgö,4)}/{round(f_cgö,2)}', style='italic')
        ax.plot(eps_ckh,f_ckh,'o',c="y")
        ax.text(eps_ckh, f_ckh+0.5, f'KH {round(eps_ckh,4)}/{round(f_ckh,2)}', style='italic')
        ax.plot(eps_csh,f_csh,'o',c="g")
        ax.text(eps_csh, f_csh-0.8, f'SH {round(eps_csh,4)}/{round(f_csh,2)}', style='italic')

        ax.set_xlabel('Strain (mm)')  # Add an x-label to the axes.
        ax.set_ylabel('Stress (MPa)')  # Add a y-label to the axes.
        ax.set_title("Mander Model")  # Add a title to the axes.

        if annotate == 1:
            ax.annotate(f'{round(eps_cc,4)}/{round(f_cc,2)}', xy=(eps_cc, f_cc), xytext=(eps_cc+0.001, f_cc+0.005),
            arrowprops=dict(facecolor='black', shrink=0.05))
            ax.annotate(f'{round(eps_co,4)}/{round(f_co,2)}', xy=(eps_co, f_co), xytext=(eps_co+0.001, f_co+0.005),
                arrowprops=dict(facecolor='black', shrink=0.05))
            ax.annotate(f'{round(eps_cu,4)}/{round(f_c_birim,2)}', xy=(eps_cu, f_c_birim), xytext=(eps_cu+0.001, f_c_birim+2),
                arrowprops=dict(facecolor='black', shrink=0.05))
            ax.annotate(f'{round(eps_co,4)}/{round(f_co_sargılı,2)}', xy=(eps_co, f_co_sargılı), xytext=(eps_co+0.001, f_co_sargılı+0.005),
                arrowprops=dict(facecolor='black', shrink=0.05))
            ax.annotate(f'{round(eps_cu_sargısız,4)}/{round(f_c_birim_sargısız,2)}', xy=(eps_cu_sargısız, f_c_birim_sargısız), xytext=(eps_cu_sargısız+0.001, f_c_birim_sargısız+0.005),
                arrowprops=dict(facecolor='black', shrink=0.05))
            
        
        ax.legend(loc='upper left')

    return(eps_c,f_c)

def celik_modeli(celiksınıfı,E_s = 2*10**5):

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


