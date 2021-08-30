#This script was written by Huang Junjie on July 9, 2021
import math
def bayesian(ALogP,nHeavyAtom,nN,nO,BCUTc,nHBAcc2,nRotBt,PSA,mw):

	if ALogP >= -5 and ALogP < -4:
		s1=0.6448
	elif ALogP >= -4 and ALogP < -3:
		s1=0.7420
	elif ALogP >= -3 and ALogP < -2:
		s1=0.6895
	elif ALogP >= -2 and ALogP < -1:
		s1=0.7648
	elif ALogP >= -1 and ALogP < 0:
		s1=0.9507
	elif ALogP >= 0 and ALogP < 1:
		s1=1.3775
	elif ALogP >= 1 and ALogP < 2:
		s1=1.7351
	elif ALogP >= 2 and ALogP < 3:
		s1=0.6529
	elif ALogP >= 3 and ALogP < 4:
		s1=0.1990
	elif ALogP >= 4 and ALogP < 5:
		s1=0.0001
	elif ALogP >= 5 and ALogP < 6:
		s1=0
	else:
		s1=0
		s1=float(s1)


	if nHeavyAtom >= 3 and nHeavyAtom < 5:
		s2=78.2269
	elif nHeavyAtom >= 5 and nHeavyAtom < 7:
		s2=58.1656
	elif nHeavyAtom >= 7 and nHeavyAtom < 9:
		s2=5.2476
	elif nHeavyAtom >= 9 and nHeavyAtom < 11:
		s2=1.535
	elif nHeavyAtom >= 11 and nHeavyAtom < 13:
		s2=0.6317
	elif nHeavyAtom >= 13 and nHeavyAtom < 15:
		s2=0.2640
	elif nHeavyAtom >= 15 and nHeavyAtom < 17:
		s2=3.2526
	elif nHeavyAtom >= 17 and nHeavyAtom < 19:
		s2=1.0917
	elif nHeavyAtom >= 19 and nHeavyAtom < 21:
		s2=1.0457
	elif nHeavyAtom >= 21 and nHeavyAtom < 23:
		s2=1.0084
	else:
		s2=0
		s2=float(s2)

	if nN == 0:
		s3=1.7856
	elif nN == 1:
		s3=1.3128
	elif nN == 2:
		s3=1.0351
	elif nN == 3:
		s3=0.3875
	elif nN == 4:
		s3=0.1408
	elif nN == 5:
		s3=0.0214
	elif nN == 6:
		s3=0.0001
	elif nN == 7:
		s3=0.00001
	elif nN == 8:
		s3=0.00001
	elif nN == 9:
		s3=0.000001
	else:
		s3=0
		s3=float(s3)


	if nO == 0:
		s4=1.4078
	elif nO == 1:
		s4=2.0969
	elif nO == 2:
		s4=1.0129
	elif nO == 3:
		s4=0.5148
	elif nO == 4:
		s4=0.001
	elif nO == 5:
		s4=0.0001
	elif nO == 6:
		s4=0.00001
	elif nO == 7:
		s4=0.000001
	else:
		s4=0
		s4=float(s4)


	if BCUTc >= 0 and BCUTc < 0.05:
		s5=4.5990
	elif BCUTc >= 0.05 and BCUTc < 0.1:
		s5=4.3132
	elif BCUTc >= 0.1 and BCUTc < 0.15:
		s5=1.3673
	elif BCUTc >= 0.15 and BCUTc < 0.2:
		s5=0.8657
	elif BCUTc >= 0.2 and BCUTc < 0.25:
		s5=0.9385
	elif BCUTc >= 0.25 and BCUTc < 0.3:
		s5=0.4445
	elif BCUTc >= 0.3 and BCUTc < 0.35:
		s5=0.5386
	elif BCUTc >= 0.35 and BCUTc < 0.4:
		s5=0.8412
	elif BCUTc >= 0.4 and BCUTc < 0.45:
		s5=1.6678
	elif BCUTc >= 0.45 and BCUTc < 0.5:
		s5=0.28125
	elif BCUTc >= 0.5 and BCUTc < 6:
		s5=0.01
	else:
		s5=0
		s5=float(s5)


	if nHBAcc2 == 0:
		s6=7.6017
	elif nHBAcc2 == 1:
		s6=4.0239
	elif nHBAcc2 == 2:
		s6=4.1777
	elif nHBAcc2 == 3:
		s6=0.9385
	elif nHBAcc2 == 4:
		s6=0.1528
	elif nHBAcc2 == 5:
		s6=0.0662
	elif nHBAcc2 == 6:
		s6=0.0294
	elif nHBAcc2 == 7:
		s6=0.0507
	elif nHBAcc2 == 8:
		s6=0.001
	elif nHBAcc2 == 9:
		s6=0.0001
	else:
		s6=0
		s6=float(s6)


	if nRotBt == 0:
		s7=3.2607
	elif nRotBt == 1:
		s7=2.1327
	elif nRotBt == 2:
		s7=1.7312
	elif nRotBt == 3:
		s7=1.3250
	elif nRotBt == 4:
		s7=1.5968
	elif nRotBt == 5:
		s7=1.2856
	elif nRotBt == 6:
		s7=0.6090
	elif nRotBt == 7:
		s7=0.3101
	elif nRotBt == 8:
		s7=0.1398
	elif nRotBt == 9:
		s7=0.0339
	elif nRotBt == 10:
		s7=0.0181
	elif nRotBt == 11:
		s7=0.001
	elif nRotBt == 12:
		s7=0.0001
	elif nRotBt == 13:
		s7=0.00001
	else:
		s7=0
		s7=float(s7)


	if PSA >= 0 and PSA < 10:
		s8=6.3826
	elif PSA >= 10 and PSA < 20:
		s8=4.5930
	elif PSA >= 20 and PSA < 30:
		s8=4.8832
	elif PSA >= 30 and PSA < 40:
		s8=3.9130
	elif PSA >= 40 and PSA < 50:
		s8=2.0945
	elif PSA >= 50 and PSA < 60:
		s8=0.7219
	elif PSA >= 60 and PSA < 70:
		s8=0.0559
	elif PSA >= 70 and PSA < 80:
		s8=0.001
	elif PSA >= 80 and PSA < 90:
		s8 = 0.0001
	elif PSA >= 90 and PSA < 100:
		s8 = 0.00001
	elif PSA >= 100 and PSA < 120:
		s8 = 0.000001
	elif PSA >= 120 and PSA < 150:
		s8 = 0.0000001
	elif PSA >= 150 and PSA < 160:
		s8 = 0.00000001
	else:
		s8=0
		s8=float(s8)


	if mw >= 0 and mw < 30:
		s9=2
	elif mw >= 30 and mw < 60:
		s9=68.505
	elif mw >= 60 and mw < 90:
		s9=152.139
	elif mw >= 90 and mw < 120:
		s9=8.3734
	elif mw >= 120 and mw < 150:
		s9=2.0678
	elif mw >= 150 and mw < 180:
		s9=0.6398
	elif mw >= 180 and mw < 210:
		s9=0.2389
	elif mw >= 210 and mw < 240:
		s9=1.17
	elif mw >= 240 and mw < 270:
		s9=1.0739
	elif mw >= 270 and mw < 300:
		s9=1.03352
	else:
		s9=0
		s9=float(s9)

	if s1>0 and s2>0 and s3>0 and s4>0 and s5>0 and s6>0 and s7>0 and s8>0 and s9>0 :
		D=math.log(s1)+math.log(s2)+math.log(s3)+math.log(s4)+math.log(s5)+math.log(s6)+math.log(s7)+math.log(s8)+math.log(s9)
		RFL=math.exp(float(D)/9)
	else:
		RFL=0
	return RFL

