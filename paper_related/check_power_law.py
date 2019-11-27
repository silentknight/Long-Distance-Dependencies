#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

ptb = np.array([2.1225719219279906,1.4788227635983109,1.277459824606355,1.1716215235644256,1.1277714224270028,1.1088983364165301,1.0973574940079605,1.0912095121776666,1.0856029460157917,1.0814100215285496])
text8 = np.array([2.3535536862369977,1.662998946199144,1.4374992436676415,1.309776723760562,1.269552947580376,1.2559122228535546,1.2430708311837684,1.2355851027792735,1.2297780520279922,1.2279952763903452])
wiki2 = np.array([2.399869185899478,1.79508495121609,1.5888136485487987,1.4630628799952738,1.4135178375220825,1.3993464224923695,1.3838687301478831,1.3718849381083675,1.3621709350299955,1.350591280957513])
wiki103 = np.array([2.1866751016364496,1.3735698330827741,1.045950127059161,0.890952412695313,0.8210691158921044,0.7940012562767329,0.7714721146392609,0.7547453446583212,0.7417668796055423,0.7300535025275359])

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):

	ax = plt.subplot(2, 2, 1)
	plt.loglog(np.arange(1,len(ptb)+1), ptb/ptb[0], np.arange(1,len(ptb)+1), np.power(np.linspace(1,len(ptb)+1,10),-0.47))
	plt.title('PTB', fontsize=15)
	plt.tick_params(labelsize='large', width=3)
	plt.grid(True)
	# plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	# plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.text(1.5, 0.3, r'$I(d)=2.12*d^{-0.47}$', fontsize=13)
	ax.set_ylim(0.2, 1)

	ax = plt.subplot(2, 2, 2)
	plt.loglog(np.arange(1,len(text8)+1), text8/text8[0], np.arange(1,len(text8)+1), np.power(np.linspace(1,len(text8)+1,10),-0.47))
	plt.title('Text8')
	plt.tick_params(labelsize='large', width=3)
	plt.grid(True)
	# plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	# plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.text(1.5, 0.3, r'$I(d)=2.35*d^{-0.47}$', fontsize=13)
	ax.set_ylim(0.2, 1)

	ax = plt.subplot(2, 2, 3)
	plt.loglog(np.arange(1,len(wiki2)+1), wiki2/wiki2[0], np.arange(1,len(wiki2)+1), np.power(np.linspace(1,len(wiki2)+1,10),-0.37))
	plt.title('Wiki2')
	plt.tick_params(labelsize='large', width=3)
	plt.grid(True)
	# plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	# plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.text(1.5, 0.3, r'$I(d)=2.4*d^{-0.37}$', fontsize=13)
	ax.set_ylim(0.2, 1)

	ax = plt.subplot(2, 2, 4)
	plt.loglog(np.arange(1,len(wiki103)+1), wiki103/wiki103[0], np.arange(1,len(wiki103)+1), np.power(np.linspace(1,len(wiki103)+1,10),-0.60))
	plt.title('Wiki103')
	plt.tick_params(labelsize='large', width=3)
	plt.grid(True)
	# plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	# plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.text(1.5, 0.3, r'$I(d)=2.18*d^{-0.60}$', fontsize=13)
	ax.set_ylim(0.2, 1)

	# plt.savefig('scaling', bbox_extra_artists=(lgd,), bbox_inches='tight')
	plt.show()