import numpy as np
import math as mt
import matplotlib.pyplot as plt

class Unit():
        # Define units
        # ------------------------------------------------------------------------
        # Basic Units
        m = 1.0
        kN = 1.0
        sec = 1.0

        # Length
        mm = m / 1000.0
        cm = m / 100.0
        inch = 25.4 * mm
        ft = 12.0 * inch

        # Force
        N = kN / 1000.0
        kips = kN * 4.448221615
        lb = kips / 1.0e3

        # Stress (kN/m2 or kPa)
        Pa = N / (m ** 2)
        kPa = Pa * 1.0e3
        MPa = Pa * 1.0e6
        GPa = Pa * 1.0e9
        ksi = 6.8947573 * MPa
        psi = 1e-3 * ksi

        # Mass - Weight
        tonne = kN * sec ** 2 / m
        kg = N * sec ** 2 / m
        lb = psi*inch**2

        # Gravitational acceleration
        g = 9.81*m/sec**2

        # Time
        min = 60*sec
        hr = 60*min

class define_material:

    def steel(celiksınıfı,bs = 1.15 ,perfectlyplastic="true",plot="true"):
        """
        celiksınıfı         : "S220","S420","B420C","B500C"
        bs                  : strain-hardining ratio default 1.15
        returns : dict
        """
        import numpy as np
        import matplotlib.pyplot as plt
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
        f_su = bs*f_sy
        if celiksınıfı == "S220" and bs == 1.15:
               f_su = celikler[celiksınıfı][4]*f_sy

        

        eps_s_list = np.arange(0,eps_su,0.0001)
        E_s = 2*10**5
        fs_list =[]
        for eps_s in eps_s_list:
            if eps_s <= eps_sy:
                f_s = E_s*eps_s
            elif eps_sy < eps_s <= eps_sh:
                f_s = f_sy
            elif eps_sh < eps_s <= eps_su:
                if perfectlyplastic == "true":
                    f_s = f_sy
                else:
                    f_s = f_su-(f_su-f_sy)*((eps_su-eps_s)**2/(eps_su-eps_sh)**2)
            fs_list.append(f_s)


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
                if perfectlyplastic == "true":
                    fs_perfm = f_sy
            fs_perf.append(fs_perfm)
        
        celik = {"f_sy":f_sy,"eps_sy":eps_sy,"eps_sh":eps_sh,"eps_su":eps_su,"f_su":f_su,
        "GÖ":eps_perf[0],"KH":eps_perf[1],"SH":eps_perf[2],"eps_list":eps_s_list,"f_list":fs_list}

        if plot == "true":
            fig, ax = plt.subplots(figsize=(10,10))
            fig.subplots_adjust(bottom=0.15, left=0.2)
            ax.grid()
            ax.plot(eps_s_list,fs_list)
            ax.plot(eps_sgö,fs_perf[0],'o',c="r")
            ax.plot(eps_skh,fs_perf[1],'o',c="y")
            ax.plot(eps_ssh,fs_perf[2],'o',c="b")

            ax.annotate(f'f_göçme/eps_göçme = {round(eps_sgö,4)}/{round(fs_perf[0],2)}',
                        xy=(eps_sgö, fs_perf[0]), xytext=(eps_sgö, fs_perf[0]-20),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            
            ax.annotate(f'f_kh/eps_kh = {round(eps_skh,4)}/{round(fs_perf[1],2)}',
                        xy=(eps_skh, fs_perf[1]), xytext=(eps_skh, fs_perf[1]+20),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            
            ax.annotate(f'f_sh/eps_sh = {round(eps_ssh,4)}/{round(fs_perf[2],2)}',
                        xy=(eps_ssh, fs_perf[2]), xytext=(eps_ssh, fs_perf[2]-20),
                        arrowprops=dict(facecolor='black', shrink=0.05))

        return celik

    def conc_unconfined(f_co=25,eps_co = 0.002,plot="true"):
        f_e_sargısız = 0   
        lamda_c_sargısız = 2.254*mt.sqrt(1+7.94*(f_e_sargısız/f_co))-(2*f_e_sargısız/f_co)-1.254 
        f_cc_sargısız = lamda_c_sargısız*f_co
        eps_cc_sargısız = eps_co*(1+5*(lamda_c_sargısız-1))
        E_c = 5000*mt.sqrt(f_co)
        E_sec_sargısız = f_cc_sargısız/eps_cc_sargısız
        r_sargısız = E_c/(E_c-E_sec_sargısız)
        eps_cu_sargısız=0.0035
        eps_c_sargısız = np.arange(0,eps_cu_sargısız,0.00001)
        x_sargısız=[]
        f_c_sargısız =[]
        for eps in eps_c_sargısız:
            x_birim_sargısız = (eps/eps_cc_sargısız)
            x_sargısız.append(x_birim_sargısız)
            f_c_birim_sargısız = (f_cc_sargısız*x_birim_sargısız*r_sargısız)/(r_sargısız-1+x_birim_sargısız**r_sargısız)
            f_c_sargısız.append(f_c_birim_sargısız)
        
        if plot =="true":
            fig, ax = plt.subplots(figsize=(10,10))
            fig.subplots_adjust(bottom=0.15, left=0.2)
            ax.grid()
            ax.plot(eps_c_sargısız,f_c_sargısız,label="UnConfined model")
            ax.set_xlabel('Strain (mm)')  # Add an x-label to the axes.
            ax.set_ylabel('Stress (MPa)')  # Add a y-label to the axes.
            ax.set_title("Mander Model")  # Add a title to the axes.
            ax.legend(loc='upper left')

        unconf = {"f_co":f_co,"f_list":f_c_sargısız,"eps_list":eps_c_sargısız,"E_c":E_c,"E_sec":E_sec_sargısız}
        return unconf

    def section_prop(Bsec,Hsec,f_co,celiksinifi,
        shape="rectangle",K=1,numBarsTop = 8,numBarsBot = 8,numBarsInt = 6,
        barAreaTop = 1,barAreaBot = 1,barAreaInt = 1):
            Kv=5/6
            celik_def = define_material.steel(celiksinifi)
            conc = define_material.conc_unconfined(f_co)


            pass

