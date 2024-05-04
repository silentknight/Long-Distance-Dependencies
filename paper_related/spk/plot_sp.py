#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filenames = ["penn_tree_letters_15000_grassberger_logx","wiki2_letters_15000_grassberger_logx","text8_letters_15000_grassberger_logx","enwik8_letters_15000_grassberger_logx","sp2_20","sp2_100","sp2_200",
             "sp2_500","sp2_5000","sp2_10000","sp2_v4_20","sp4_v4_20","sp8_v4_20","sp2_v26_20","sp4_v26_20","sp2_v61_20","sp2_v4_200","sp4_v4_200","sp8_v4_200","sp2_v26_200","sp4_v26_200","sp2_v61_200",]
#              "sp2_100_comp","sp4_100_comp","sp16_100_comp","sp2_20_comp","sp2_20_v26","sp8_20_comp","sp8_20_v26","sp2_20_small","sp2_100_small","sp2_20_f1",
#              "sp2_100_f1","sp2_20_new_f1","sp2_20_new_f2","sp2_v26_100","sp4_v26_100","sp6_v26_100","sp8_v26_100","sp10_v26_100"]

all_mi = []

for filename in filenames:
    f = open(filename+"_mi.dat", "r")
    lines = f.readlines()
    f.close()

    start = 0
    end = 0
    index = 0

    mi = np.zeros([len(lines)-1])
    Hx = np.zeros([len(lines)-1])
    Hy = np.zeros([len(lines)-1])
    Hxy = np.zeros([len(lines)-1])

    temp = lines[0].split()
    if temp[0] == "data:":
        for line in lines:
            temp = line.strip().split(":")
            if temp[0] == "d":
                temp1 = temp[2].split(",")
                mi[int(temp[1])-1] = float(temp1[0])
                Hx[int(temp[1])-1] = float(temp1[1])
                Hy[int(temp[1])-1] = float(temp1[2])
                Hxy[int(temp[1])-1] = float(temp1[3])
                d = int(temp[1])+1
            index+=1
    else:
        print("Not a valid file")

    all_mi.append(np.abs(mi).tolist())

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    ax = plt.axes()

    plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], label="PTB Characters")
    plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], label="WikiText2 Characters")
    plt.loglog(np.arange(1,len(all_mi[2])+1), all_mi[2], label="Text8 Characters")
    # plt.loglog(np.arange(1,len(all_mi[3])+1), all_mi[3], label="Enwik8 Characters")

    plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], label="SP2, L=20, V=4, FS={ab,bc}")
    plt.loglog(np.arange(1,len(all_mi[5])+1), all_mi[5], label="SP2, L=100, V=4, FS={ab,bc}")
    plt.loglog(np.arange(1,len(all_mi[6])+1), all_mi[6], label="SP2, L=200, V=4, FS={ab,bc}")
    plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], label="SP2, L=500, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[8])+1), all_mi[8], label="SP2, L=5000, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[9])+1), all_mi[9], label="SP2, L=10000, V=4, FS={ab,bc}")

    # plt.loglog(np.arange(1,len(all_mi[10])+1), all_mi[10], label="SP2, L=20, V=4, FS={ab,bc,cd,dc}")
    # plt.loglog(np.arange(1,len(all_mi[11])+1), all_mi[11], label="SP4, L=20, V=4, FS={abba,bccb,cddc,adda}")
    # plt.loglog(np.arange(1,len(all_mi[12])+1), all_mi[12], label="SP8, L=20, V=4, FS={abbaabba,bccbbccb,cddccddc,addaadda}")
    # plt.loglog(np.arange(1,len(all_mi[13])+1), all_mi[13], label="SP2, L=20, V=26, FS={ab,bc,cd,de,ef,fg}")
    # plt.loglog(np.arange(1,len(all_mi[14])+1), all_mi[14], label="SP4, L=20, V=26, FS={abba,deed,ghhg,accf,hiih,ijji,lmml,noon,stts,vwwv}")
    # plt.loglog(np.arange(1,len(all_mi[15])+1), all_mi[15], label="SP2, L=20, V=61, FS={ab,bc,cd,de,ef,fg,AB,GH,Aa,Cd,A1,M2,K4,W5,Q6,A7}")

    # plt.loglog(np.arange(1,len(all_mi[16])+1), all_mi[16], label="SP2, L=200, V=4, FS={ab,bc,cd,dc}")
    # plt.loglog(np.arange(1,len(all_mi[17])+1), all_mi[17], label="SP4, L=200, V=4, FS={abba,bccb,cddc,adda}")
    # plt.loglog(np.arange(1,len(all_mi[18])+1), all_mi[18], label="SP8, L=200, V=4, FS={abbaabba,bccbbccb,cddccddc,addaadda}")
    # plt.loglog(np.arange(1,len(all_mi[19])+1), all_mi[19], label="SP2, L=200, V=26, FS={ab,bc,cd,de,ef,fg}")
    # plt.loglog(np.arange(1,len(all_mi[20])+1), all_mi[20], label="SP4, L=200, V=26, FS={abba,deed,ghhg,accf,hiih,ijji,lmml,noon,stts,vwwv}")
    # plt.loglog(np.arange(1,len(all_mi[21])+1), all_mi[21], label="SP2, L=200, V=61, FS={ab,bc,cd,de,ef,fg,AB,GH,Aa,Cd,A1,M2,K4,W5,Q6,A7}")


#####################
    # plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], label="SP2, L=100, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[5])+1), all_mi[5], label="SP4, L=100, V=4, FS={abba,bccb}")
    # plt.loglog(np.arange(1,len(all_mi[6])+1), all_mi[6], label="SP16, L=100, V=4, FS={abbaabbaabbaabba,bccbbccbbccbbccb}")

    # plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], label="SP2, L=20, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[8])+1), all_mi[8], label="SP2, L=20, V=26, FS={ab,bc,cd,de,ef,fg}")

    # plt.loglog(np.arange(1,len(all_mi[9])+1), all_mi[9], label="SP8, L=20, V=4") # FS={abbaabba,bccbbccb}
    # plt.loglog(np.arange(1,len(all_mi[10])+1), all_mi[10], label="SP8, L=20, V=26") # FS={abbaabba,bccbbccb,cddccddc,deeddeed,\n effeeffe,fggffggf,ffhhiikk}")

    # plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], label="SP2, L=20, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[11])+1), all_mi[11], label="SP2, L=20, V=4, FS={ab,bc}, Small")

    # plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], label="SP2, L=100, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[12])+1), all_mi[12], label="SP2, L=100, V=4, FS={ab,bc}, Small")

    # plt.loglog(np.arange(1,len(all_mi[7])+1), all_mi[7], label="SP2, L=20, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[13])+1), all_mi[13], label="SP2, L=20, V=4, FS={ab,bc,cd,dc}")

    # plt.loglog(np.arange(1,len(all_mi[4])+1), all_mi[4], label="SP2, L=100, V=4, FS={ab,bc}")
    # plt.loglog(np.arange(1,len(all_mi[14])+1), all_mi[14], label="SP2, L=100, V=4, FS={ab,bc,cd,dc}")

    # plt.loglog(np.arange(1,len(all_mi[17])+1), all_mi[17], label="SP2, L=100, V=26")
    # plt.loglog(np.arange(1,len(all_mi[18])+1), all_mi[18], label="SP4, L=100, V=26")
    # plt.loglog(np.arange(1,len(all_mi[19])+1), all_mi[19], label="SP6, L=100, V=26")
    # plt.loglog(np.arange(1,len(all_mi[20])+1), all_mi[20], label="SP8, L=100, V=26")
    # plt.loglog(np.arange(1,len(all_mi[21])+1), all_mi[21], label="SP10, L=100, V=26")

    # plt.loglog(np.arange(1,len(all_mi[2])+1), all_mi[2], label="Constant Mutual Information")

    # plt.loglog(np.arange(1,len(all_mi[0])+1), all_mi[0], label="sp2_20")
    # plt.loglog(np.arange(1,len(all_mi[1])+1), all_mi[1], label="sp2_v4_20")

    # plt.loglog(np.arange(1,len(all_mi[2])+1), all_mi[2], label="sp2_200")
    # plt.loglog(np.arange(1,len(all_mi[3])+1), all_mi[3], label="sp2_v4_200")


    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax.set_xlim(1, 1000)
    # ax.set_ylim(4.3e-11, 0.65)
    print(ax.get_ylim())
    ax.set_xlabel('Distance between symbols (Lag), d', fontsize=15)
    ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
    lgd = ax.legend(loc='lower left', shadow=True, fancybox=True, numpoints=3, prop={'size': 10})
    # plt.savefig('hyper_sp', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
