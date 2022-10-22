#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from scipy import stats
import argparse

parser = argparse.ArgumentParser(description='PyTorch Transformer Language Model')
parser.add_argument('--filename_ID', type=int, required=True, help='ID of the filename to analyze')
parser.add_argument('--end_point', type=int, help='End Point calculation')
parser.add_argument('--standard_bpl', action='store_true', help='Plot standard broken power-law')
parser.add_argument('--compute_LSMR', action='store_true', help='Compute Long Short Memory Ratio')
parser.add_argument('--fit_data', action='store_true', help='Fit the Broken Power-Law to data')
args = parser.parse_args()

filenames = ["penn_tree","text8","text8_wor","text8_subset","text8_subset_wor","wiki2","wiki2_raw","wiki2_cleaned","wiki19","wiki19_text8","wiki103","wiki103_raw","wiki103_cleaned","wiki_sample_1","wiki_sample_2","wiki_ptb_size_1","wiki_ptb_size_2","wiki_ptb_vocab_1","wiki_ptb_vocab_2","10kGNAD","wiki19_cleaned","wiki_sample_3","wiki_sample_4"]

print("Filenames-> 0: penn_tree, 1: text8, 2: text8_wor, 3: text8_subset, 4: text8_subset_wor, 5: wiki2, 6: wiki2_raw, 7: wiki2_cleaned, 8: wiki19, 9: wiki19_text8, 10: wiki103, 11: wiki103_raw, 12: wiki103_cleaned, 13: wiki_sample_1, 14: wiki_sample_2, 15: wiki_ptb_size_1, 16: wiki_ptb_size_2, 17: wiki_ptb_vocab_1, 18: wiki_ptb_vocab_2, 19: 10kGNAD, 20: wiki19_cleaned, 21: wiki_sample_3, 22: wiki_sample_4")

dataset = args.filename_ID
filename = filenames[dataset]
filename += "_words_10000"

f = open(filename+"_grassberger_logx_mi.dat", "r")
lines = f.readlines()
f.close()

start = 0
end = 0
index = 0

mi = np.zeros([0,1])
Hx = np.zeros([0,1])
Hy = np.zeros([0,1])
Hxy = np.zeros([0,1])
temp = lines[0].split()
if temp[0] == "data:":
	for line in lines:
		temp = line.strip().split(":")
		if temp[0] == "d":
			temp1 = temp[2].split(",")
			mi = np.append(mi,np.zeros(1))
			mi[int(temp[1])-1] = float(temp1[0])
			Hx = np.append(Hx,np.zeros(1))
			Hx[int(temp[1])-1] = float(temp1[1])
			Hy = np.append(Hy,np.zeros(1))
			Hy[int(temp[1])-1] = float(temp1[2])
			Hxy = np.append(Hxy,np.zeros(1))
			Hxy[int(temp[1])-1] = float(temp1[3])
			d = int(temp[1])+1
		index+=1
else:
	print("Not a valid file")

###########################################################################################################################
with plt.style.context(('seaborn')):
	ax = plt.axes()

	if dataset == 0:
		###################################################################################################################
		# PTB
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.4786
		alpha_2 = 0.01
		end_point = 622
		p1 = plt.loglog(np.arange(1,len(data)+1), data, "r-", label="PTB")
		x = np.linspace(0, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+8]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law fit for PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.275
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law fit for PTB")

	elif dataset == 1:
		###################################################################################################################
		# Text8
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.481
		alpha_2 = 0.0153
		end_point = 1208
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="Text8")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+10]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for Text8")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.239
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8")

	elif dataset == 2:
		###################################################################################################################
		# Text8 w/o Rare
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.55
		alpha_2 = 0.0195
		end_point = 1108
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="Text8 (w/o R)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+8]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for Text8 (w/o R)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.2369
		fit_sample = f(x)
		p2 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (w/o R)")

	elif dataset == 3:
		###################################################################################################################
		# Text8 Subset
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.315
		alpha_2 = 0.01
		end_point = 793
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="Text8 (S)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+9]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for Text8 (S)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.1815
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (S)")

	elif dataset == 4:
		###################################################################################################################
		# Text8 Subset w/o Rare
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.42
		alpha_2 = 0.013
		end_point = 585
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="Text8 (w/o R S)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+7]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for Text8 (w/o R S)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.19
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for Text8 (w/o R S)")

	elif dataset == 5:
		###################################################################################################################
		# Wiki2
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.421
		alpha_2 = 0.00281
		end_point = 2203
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.346
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2")

	elif dataset == 6:
		###################################################################################################################
		# Wiki2 Raw
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.34
		alpha_2 = 0.00225
		end_point = 2158
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 Raw")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+10]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 Raw")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.3379
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 Raw")

	elif dataset == 7:
		###################################################################################################################
		# Wiki2 Cleaned
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.38215
		alpha_2 = 0.003
		end_point = 1330
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 (C)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+12]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 (C)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.25
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 (C)")

	elif dataset == 8:
		###################################################################################################################
		# Wiki19
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.61
		alpha_2 = 0.0078
		end_point = 2436
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText19")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText19")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.43
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText19")

	elif dataset == 9:
		###################################################################################################################
		# Wiki19 Text8
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.56
		alpha_2 = 0.012
		end_point = 2170
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText19 Text8")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText19 Text8")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.255
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText19 Text8")

	elif dataset == 10:
		###################################################################################################################
		# Wiki103
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.81
		alpha_2 = 0.0209
		end_point = 2989
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText103")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+10]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText103")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.424
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103")

	elif dataset == 11:
		###################################################################################################################
		# Wiki103 Raw
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.77
		alpha_2 = 0.0198
		end_point = 3020
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText103 Raw")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText103 Raw")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.41
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103 Raw")

	elif dataset == 12:
		###################################################################################################################
		# Wiki103 Cleaned
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.77
		alpha_2 = 0.021
		end_point = 3067
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText103 (C)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText103 (C)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.35
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText103 (C)")

	elif dataset == 13:
		###################################################################################################################
		# Wiki Sample #1
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.382
		alpha_2 = 0.002593
		end_point = 1100
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.338
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 14:
		###################################################################################################################
		# Wiki Sample #2
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.385
		alpha_2 = 0.002358
		end_point = 1159
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.332
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 15:
		###################################################################################################################
		# Wiki PTB Size #1
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.34
		alpha_2 = 0.002890
		end_point = 1288
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.199
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 16:
		###################################################################################################################
		# Wiki PTB Size #2
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.32
		alpha_2 = 0.00285
		end_point = 1253
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.204
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 17:
		###################################################################################################################
		# Wiki PTB Vocab #1
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.4113
		alpha_2 = 0.00363
		end_point = 1860
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.194
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 18:
		###################################################################################################################
		# Wiki PTB Vocab #2
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.4165
		alpha_2 = 0.00365
		end_point = 1319
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText2 PTB")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+16]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText2 PTB")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.184
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText2 PTB")

	elif dataset == 19:
		###################################################################################################################
		# 10kGNAD
		###################################################################################################################
		break_point = 3
		data = mi
		alpha_1 = 0.34
		alpha_2 = 0.002
		end_point = 470
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="10kGNAD")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+8]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law fit for 10kGNAD")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.3
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law fit for 10kGNAD")

	elif dataset == 20:
		###################################################################################################################
		# Wiki19 (C)
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.77
		alpha_2 = 0.021
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText19 (C)")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText19 (C)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.35
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText19 (C)")

	elif dataset == 21:
		###################################################################################################################
		# WikiText Sample 3
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.352
		alpha_2 = 0.002495
		end_point = 1142
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText Sample 3")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText19 (C)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.3415
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText Sample 3")

	elif dataset == 22:
		###################################################################################################################
		# WikiText Sample 4
		###################################################################################################################
		break_point = 4
		data = mi
		alpha_1 = 0.368
		alpha_2 = 0.00203
		end_point = 1314
		p1 = plt.loglog(np.arange(1,len(data)+1), data, label="WikiText Sample 4")
		x = np.linspace(1, len(data), len(data))
		if args.standard_bpl:
			amplitude = mi[break_point+6]
			f = models.BrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
			fit_sample = f(x)
			p2 = plt.loglog(x, fit_sample, label="Broken Power-Law for WikiText19 (C)")
		amplitude = mi[break_point-1]
		f = models.SmoothlyBrokenPowerLaw1D(amplitude=amplitude, x_break=break_point, alpha_1=alpha_1, alpha_2=alpha_2)
		f.delta = 0.31436
		fit_sample = f(x)
		p3 = plt.loglog(x, fit_sample, label="Smoothly Broken Power-Law for WikiText Sample 4")

	###########################################################################################################################

	if args.fit_data:
		[D, p_value] = stats.ks_2samp(data,fit_sample)

		print("Dataset :", filename)
		print("D_inf :", break_point)
		print("c1 :",data[0])
		print("alpha 1 :", alpha_1)
		print("amplitude :", mi[break_point-1])
		print("alpha 2 :", alpha_2)
		print("delta :", f.delta)
		print("D :", D)
		print("p-value :", p_value)
		print("length :", len(data))
		plt.tick_params(labelsize='large', width=5)
		plt.grid(True)
		plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
		plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
		ax.set_xlim(1.0, 10000.0)
		ax.set_xlabel('Distance between words, d', fontsize=15)
		ax.set_ylabel('Mutual Information, I(d)', fontsize=15)
		lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, prop={'size': 15})
		plt.savefig('fit', bbox_extra_artists=(lgd,), bbox_inches='tight')
		plt.show()

	###########################################################################################################################

	if args.compute_LSMR:
		sdds = 0
		ldds = 0

		if args.end_point is not None:
			end_point = args.end_point

		for i in range(break_point):
			sdds += mi[i]

		for i in range(break_point,end_point):
			ldds += mi[i]

		print("Break Point 1:", break_point)
		print("Break Point 2:", end_point)
		print("SDDs", sdds)
		print("LDDs", ldds)
		print("SDDs/LDDs: %f, LDDs/SDDs: %.2f\n" % (sdds/ldds, ldds/sdds))
