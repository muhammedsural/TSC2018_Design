class define_material:
    def steel(celiksınıfı,perfectlyplastic="true"):
        """
        celiksınıfı         : "S220","S420","B420C","B500C"

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
        f_su = celikler[celiksınıfı][4]*f_sy

        celik = {"f_sy":f_sy,"eps_sy":eps_sy,"eps_sh":eps_sh,"eps_su":eps_su,"f_su":f_su}
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

        fig, ax = plt.subplots(figsize=(10,10))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.grid()
        ax.plot(eps_s_list,fs_list)

        return celik

    def conc(self,betonsinifi):
        pass