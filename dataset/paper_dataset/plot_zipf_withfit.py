import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# filenames = [['wiki2_train','wiki2_test_ordered','wiki2_valid_ordered'],['wiki103_train','wiki103_test_ordered','wiki103_valid_ordered'],['ptb_train','ptb_test_ordered','ptb_valid_ordered']]
# filenames = [['wiki2_train','wiki2_test1_ordered','wiki2_test2_ordered','wiki2_valid1_ordered']]
# filenames = [['wiki2Homogenous_trainH1','wiki2Homogenous_testH1_ordered','wiki2Homogenous_validH1_ordered'],['wiki2Homogenous_trainH2','wiki2Homogenous_testH2_ordered','wiki2Homogenous_validH2_ordered'],['wiki2Homogenous_trainCH1','wiki2Homogenous_testCH1_ordered','wiki2Homogenous_validCH1_ordered'],['wiki2Homogenous_trainCH2','wiki2Homogenous_testCH2_ordered','wiki2Homogenous_validCH2_ordered']]
# filenames = [['wiki2Resample_trainR1','wiki2Resample_testR1_ordered','wiki2Resample_validR1_ordered'],['wiki2Resample_trainR2','wiki2Resample_testR2_ordered','wiki2Resample_validR2_ordered'],['wiki2Resample_trainR3','wiki2Resample_testR3_ordered','wiki2Resample_validR3_ordered'],['wiki2Resample_trainR4','wiki2Resample_testR4_ordered','wiki2Resample_validR4_ordered']]
filenames = [[['text8','text8_small','text8_small_wo_r_2','text8_small_wo_r_4'],['wiki103_full','wiki2_full']]]
root = ''

powerlaw = lambda x, amp, index: amp * (x**index)

for group in filenames:
	for file in group:
		with np.load(root+file+'.npz') as arr:
			exec("%s = arr['arr_0']" % (file+"_IDs"))
			exec("%s = arr['arr_1']" % (file+"_frequency"))

ind = 0
amp = 0
index = 0
for group in filenames:
	with plt.style.context(('seaborn')):
		for file in group:
			values = ""
			exec("xdata = np.arange(1,%s_IDs.shape[0]+1)" % (file))
			exec("ydata = %s_frequency" % (file))

			if file.split('_')[1][0:5] == "train":
				yerr = 1 * ydata[0:1000]

				logx = np.log10(xdata[0:1000])
				logy = np.log10(ydata[0:1000])
				logyerr = yerr / ydata[0:1000]

				fitfunc = lambda p, x: p[0] + p[1] * x
				errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

				pinit = [0, -1.0]
				out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)

				pfinal = out[0]
				covar = out[1]
				index = pfinal[1]
				amp = 10.0**pfinal[0]

				indexErr = np.sqrt(covar[1][1])
				ampErr = np.sqrt(covar[0][0])*amp

				values += "="+str(round(index,3))

				# plt.loglog(xdata, powerlaw(xdata.astype(float), amp, index), label=file.split('_')[1]+" : "+r'$\alpha$'+values)

			else:
				yerr = 1 * ydata[0:1000]

				logx = np.log10(xdata[0:1000])
				logy = np.log10(ydata[0:1000])
				logyerr = yerr / ydata[0:1000]

				fitfunc = lambda p, x: p[0] + p[1] * x
				errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

				pinit = [0, index]
				out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)

				pfinal = out[0]
				covar = out[1]
				new_index = pfinal[1]
				new_amp = 10.0**pfinal[0]

				# plt.loglog(xdata, powerlaw(xdata.astype(float), new_amp, new_index), label=file.split('_')[1]+" : "+r'$\alpha$'+values)

				fit_ydata = powerlaw(xdata,new_amp,new_index)
				fit_ydata = fit_ydata.astype(float)
				ydata = ydata.astype(float)
				
				nmse = 0
				nmae = 0
				fit_data_norm = np.std(fit_ydata) #np.sum(fit_ydata)/len(fit_ydata)
				ydata_norm = np.std(ydata) #np.sum(ydata)/len(ydata)

				for i in range(len(fit_ydata)):
					nmse += np.abs(fit_ydata[i]-ydata[i])*np.abs(fit_ydata[i]-ydata[i])/(fit_data_norm*ydata_norm)
					nmae += np.abs(fit_ydata[i]-ydata[i])/(fit_data_norm*ydata_norm)
				nmse = nmse/float(len(fit_ydata))
				nmae = nmae/float(len(fit_ydata))

				values += "="
				values += str(round(new_index,3))
				# values += ", nmae="
				# values += str(round(nmae,3))
				values += ", nmse="
				values += str(round(nmse,3))
			
			ind += 1

			if len(file.split('_')) == 3:
				file = file.split('_')[0]+'_'+file.split('_')[1]

			# labelName = file
			# labelName = file.split('_')[1]
			labelName = file.split('_')[1][0:len(file.split('_')[1])-2]

			plt.loglog(xdata, ydata, label=labelName+" : "+r'$\alpha$'+values)
			
		plt.tick_params(labelsize='large', width=20)
		plt.grid(True)
		plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
		plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
		plt.legend(fontsize='x-large')
		ax = plt.axes()
		ax.set_xlabel('Ordered Rank of Words', fontsize=20)
		ax.set_ylabel('Frequency of Occurence', fontsize=20)
		left, right = plt.xlim()
		plt.xlim((1, right))
		bottom, top = plt.ylim()
		plt.ylim((0, top))

		fname = file.split('_')[0]
		plt.savefig(root+fname+'_zipf')

		plt.show()