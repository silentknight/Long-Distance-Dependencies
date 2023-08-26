#!/usr/bin/env python

import numpy as np

# ptb = np.array([[4966,20676,99706700,140325,126920,413],[1898,42031,99541383,236028,178449,211],[829,44223,99515123,257879,181711,235],[658,44235,99508174,263245,183505,183]])
# wiki2 = np.array([[9534,41134,1106725105,330313,318109,1089],[4301,88461,1106314868,530096,486747,811],[1817,94353,1106249544,576074,502860,636],[1574,94953,1106239529,581661,506988,579]])
# wiki103 = np.array([[255500,1084984,71670961219,4998715,4724766,5041],[90897,2512515,71659012922,11530096,8881262,2533],[27946,2689438,71656335842,13502894,9472812,1293],[13574,2759476,71655225828,14387975,9642725,647]])

# print("Between 1 and db1")
# for j in range(6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[0,j],ptb_2=ptb[1,j],ptb_p=(ptb[1,j]-ptb[0,j])/ptb[0,j]*100,w2_1=wiki2[0,j],w2_2=wiki2[1,j],w2_p=(wiki2[1,j]-wiki2[0,j])/wiki2[0,j]*100,w103_1=wiki103[0,j],w103_2=wiki103[1,j],w103_p=(wiki103[1,j]-wiki103[0,j])/wiki103[0,j]*100))

# print("Between dr1 and db2")
# for j in range(6):
# 		print("PTB: w1={ptb_1:12d}, w2={ptb_2:12d}, p_i={ptb_p:9.5f} - WikiText2: w1={w2_1:12d}, w2={w2_2:12d}, p_i={w2_p:9.5f} - WikiText103: w1={w103_1:12d}, w2={w103_2:12d}, p_i={w103_p:9.5f}".format(ptb_1=ptb[2,j],ptb_2=ptb[3,j],ptb_p=(ptb[3,j]-ptb[2,j])/ptb[2,j]*100,w2_1=wiki2[2,j],w2_2=wiki2[3,j],w2_p=(wiki2[3,j]-wiki2[2,j])/wiki2[2,j]*100,w103_1=wiki103[2,j],w103_2=wiki103[3,j],w103_p=(wiki103[3,j]-wiki103[2,j])/wiki103[2,j]*100))


text8 = np.array([[57637,304708,64437960321,1617650,2150362,16492],[13597,525625,64435959774,2808122,2788047,12005],[4884,545777,64435338772,3084214,2873214,6454],[2239,551458,64433940421,3204054,2883227,2641]])
text8_subset = np.array([[11389,45526,7947943084,359458,503154,18881],[4428,85099,7947603180,552869,620503,15412],[2235,89703,7947459464,592954,635990,11989],[1528,91206,7945306332,607267,636428,9806]])
text8_subset_wor = np.array([[12032,50513,1268621946,362646,412290,1843],[4683,90631,1268285194,558526,520991,1244],[2375,95409,1268233006,597991,531578,911],[1638,96455,1268186329,611156,529303,759]])
text8_subset_wor_4 = np.array([[12357,52331,621344865,349405,369126,222],[4700,92978,621015637,543229,471743,18],[2408,97531,620965417,582132,480817,1],[1670,98449,620954816,595203,478168,0]])

print("Between 1 and db1")
for j in range(6):
		print("text8: w1={text8_1:12d}, w2={text8_2:12d}, p_i={text8_p:9.5f} - text8_subset: w1={text8_subset_1:12d}, w2={text8_subset_2:12d}, p_i={text8_subset_p:9.5f} - text8_subset_wor: w1={text8_subset_wor_1:12d}, w2={text8_subset_wor_2:12d}, p_i={text8_subset_wor_p:9.5f} - text8_subset_wor_4: w1={text8_subset_wor_4_1:12d}, w2={text8_subset_wor_4_2:12d}, p_i={text8_subset_wor_4_p:9.5f}".format(text8_1=text8[0,j],text8_2=text8[1,j],text8_p=(text8[1,j]-text8[0,j])/text8[0,j]*100,text8_subset_1=text8_subset[0,j],text8_subset_2=text8_subset[1,j],text8_subset_p=(text8_subset[1,j]-text8_subset[0,j])/text8_subset[0,j]*100,text8_subset_wor_1=text8_subset_wor[0,j],text8_subset_wor_2=text8_subset_wor[1,j],text8_subset_wor_p=(text8_subset_wor[1,j]-text8_subset_wor[0,j])/text8_subset_wor[0,j]*100,text8_subset_wor_4_1=text8_subset_wor_4[0,j],text8_subset_wor_4_2=text8_subset_wor_4[1,j],text8_subset_wor_4_p=(text8_subset_wor_4[1,j]-text8_subset_wor_4[0,j])/text8_subset_wor_4[0,j]*100))

print("Between dr1 and db2")
for j in range(6):
		print("text8: w1={text8_1:12d}, w2={text8_2:12d}, p_i={text8_p:9.5f} - text8_subset: w1={text8_subset_1:12d}, w2={text8_subset_2:12d}, p_i={text8_subset_p:9.5f} - text8_subset_wor: w1={text8_subset_wor_1:12d}, w2={text8_subset_wor_2:12d}, p_i={text8_subset_wor_p:9.5f} - text8_subset_wor_4: w1={text8_subset_wor_4_1:12d}, w2={text8_subset_wor_4_2:12d}, p_i={text8_subset_wor_4_p:9.5f}".format(text8_1=text8[2,j],text8_2=text8[3,j],text8_p=(text8[3,j]-text8[2,j])/text8[2,j]*100,text8_subset_1=text8_subset[2,j],text8_subset_2=text8_subset[3,j],text8_subset_p=(text8_subset[3,j]-text8_subset[2,j])/text8_subset[2,j]*100,text8_subset_wor_1=text8_subset_wor[2,j],text8_subset_wor_2=text8_subset_wor[3,j],text8_subset_wor_p=(text8_subset_wor[3,j]-text8_subset_wor[2,j])/text8_subset_wor[2,j]*100,text8_subset_wor_4_1=text8_subset_wor_4[2,j],text8_subset_wor_4_2=text8_subset_wor_4[3,j],text8_subset_wor_4_p=(text8_subset_wor_4[3,j]-text8_subset_wor_4[2,j])/text8_subset_wor_4[2,j]*100))

# wiki19 = np.array([[52181,267515,30811360374,1553275,1758607,1812],[17336,572575,30808477559,3024299,2901021,974],[4462,611469,30808002847,3374298,3000155,533],[2546,620686,30807815516,3517375,3037300,341]])
# wiki19L = np.array([[59480,289469,38535078443,1508144,1849655,8778],[12151,544295,38532708816,2763522,2564212,4660],[4175,559481,38532396452,3035170,2600049,2329],[2293,567400,38531655537,3176198,2606120,1169]])

# print("Between 1 and db1")
# for j in range(6):
# 		print("wiki19: w1={wiki19_1:12d}, w2={wiki19_2:12d}, p_i={wiki19_p:9.5f} - wiki19L: w1={wiki19L_1:12d}, w2={wiki19L_2:12d}, p_i={wiki19L_p:9.5f}".format(wiki19_1=wiki19[0,j],wiki19_2=wiki19[1,j],wiki19_p=(wiki19[1,j]-wiki19[0,j])/wiki19[0,j]*100,wiki19L_1=wiki19L[0,j],wiki19L_2=wiki19L[1,j],wiki19L_p=(wiki19L[1,j]-wiki19L[0,j])/wiki19L[0,j]*100))

# print("Between dr1 and db2")
# for j in range(6):
# 		print("wiki19: w1={wiki19_1:12d}, w2={wiki19_2:12d}, p_i={wiki19_p:9.5f} - wiki19L: w1={wiki19L_1:12d}, w2={wiki19L_2:12d}, p_i={wiki19L_p:9.5f}".format(wiki19_1=wiki19[2,j],wiki19_2=wiki19[3,j],wiki19_p=(wiki19[3,j]-wiki19[2,j])/wiki19[2,j]*100,wiki19L_1=wiki19L[2,j],wiki19L_2=wiki19L[3,j],wiki19L_p=(wiki19L[3,j]-wiki19L[2,j])/wiki19L[2,j]*100))