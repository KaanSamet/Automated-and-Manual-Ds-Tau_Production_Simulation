from ROOT import *
import math
import numpy as np

def XFGen(gen,n): #XF Generator
	m = 1.0/(n+1.0)
	r = gen.Rndm()
	k = r**m
	s = gen.Rndm()
	if(s>0.5): return(1.0-k)
	else: return(k-1.0)

def ptGetter(rand,Pt):
	ptx = Pt * rand.Gaus()
	pty = Pt * rand.Gaus()
	return ptx, pty

def TauMomentumGenerator(rand,p1): #p1 Generator
	m = rand.Rndm()
	cs1 = 2.*(m-0.5)
	if(m>0.5): 
		sn1 = math.sqrt(1.0-cs1*cs1)
	else:
		sn1 = -math.sqrt(1.0-cs1*cs1)
	ph1 = 3.1415*(m) #phi

	#tau neutrino momentum in CMS

	p1z = p1 * cs1
	p1x = p1 * sn1 *math.cos(ph1)
	p1y = p1 * sn1 *math.sin(ph1)

	return p1x, p1y, p1z

def GreetandtakeNinput():
	print("WELCOME to a Toy Monte Carlo Simulation on Ds-Tau Production...\nYou will enter N and b values...\nN value entering rules: \n1) You can enter mX_Slopeimum 4 different n values.\
		\n2) First n value = 6.1 is recommended.\n3) Write stop to stop entries.\n4) Press enter every time you enter a n value.\
		\n5) XF fit line will be drawn for your first n input.")
	# try block to handle the exception
	try:
	    a = []
	     
	    while True:
		a.append(float(input("Enter desired n values here : ")))
		 
	# if the input is not-integer, just print the list
	except:
		print("Your n inputs : ", a)
	return a

def GreetandtakeBinput():
	print("B value entering rules : \n 1) You can enter mX_Slopeimum 4 different values.\
		\n2) First b value = 0.8 is recommended.\n3) Write stop to stop entries.\n4) Press enter every time you enter a b value.\
		\n5) b fit line will be drawn for your first n input.")
	# try block to handle the exception
	try:
	    b = []
	     
	    while True:
		b.append(float(input("Enter desired b values here : ")))
		 
	# if the input is not-integer, just print the list
	except:
		print("Your b inputs : ", b)
	return b
	

def HistogramOpener(n, name, le, re):
	if (n==8):
		histogram1 = TH1F("h1", name, 100, le, re)
		histogram2 = TH1F("h2", name, 100, le, re)
		histogram3 = TH1F("h3", name, 100, le, re)
		histogram4 = TH1F("h4", name, 100, le, re)
		histogram5 = TH1F("h5", name, 100, le, re)
		histogram6 = TH1F("h6", name, 100, le, re)
		histogram7 = TH1F("h7", name, 100, le, re)
		histogram8 = TH1F("h8", name, 100, le, re)
		return (histogram1, histogram2, histogram3, histogram4, histogram5, histogram6, histogram7, histogram8)
	elif (n==6):
		histogram1 = TH1F("h1", name, 100, le, re)
		histogram2 = TH1F("h2", name, 100, le, re)
		histogram3 = TH1F("h3", name, 100, le, re)
		histogram4 = TH1F("h4", name, 100, le, re)
		histogram5 = TH1F("h5", name, 100, le, re)
		histogram6 = TH1F("h6", name, 100, le, re)
		return (histogram1, histogram2, histogram3, histogram4, histogram5, histogram6)
	elif (n==4):
		histogram1 = TH1F("h1", name, 100, le, re)
		histogram2 = TH1F("h2", name, 100, le, re)
		histogram3 = TH1F("h3", name, 100, le, re)
		histogram4 = TH1F("h4", name, 100, le, re)
		return (histogram1, histogram2, histogram3, histogram4)
	elif (n==3):
		histogram1 = TH1F("h1", name, 100, le, re)
		histogram2 = TH1F("h2", name, 100, le, re)
		histogram3 = TH1F("h3", name, 100, le, re)
		return (histogram1, histogram2, histogram3)
	elif (n==2):
		histogram1 = TH1F("h1", name, 100, le, re)
		histogram2 = TH1F("h2", name, 100, le, re)
		return (histogram1, histogram2)
	elif (n==1):
		histogram1 = TH1F("h1", name, 100, le, re)
		return histogram1
	elif (n==0):
		print("You entered no value... Exiting...")
		exit()
	else :
		print("You entered %s values which is more than 4... Exiting..." %len(a))
		exit()

def XFHistogramFiller(a,b,r,loopsize):

	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		histogram4 = b[3]
		XF_1 = []
		XF_2 = []
		XF_3 = []
		XF_4 = []
		for i in range(loopsize):
			xf1 = XFGen(r,a[0]) #Generating Xf and creating different axes for each
			histogram1.Fill(xf1)
			XF_1.append(xf1)
			xf2 = XFGen(r,a[1])
			histogram2.Fill(xf2)
			XF_2.append(xf2)
			xf3 = XFGen(r,a[2])
			histogram3.Fill(xf3)
			XF_3.append(xf3)
			xf4 = XFGen(r,a[3])
			histogram4.Fill(xf4)
			XF_4.append(xf4)
		return (histogram1, histogram2, histogram3, histogram4, XF_1, XF_2, XF_3, XF_4)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		XF_1 = []
		XF_2 = []
		XF_3 = []
		for i in range(loopsize):
			xf1 = XFGen(r,a[0])
			histogram1.Fill(xf1)
			XF_1.append(xf1)
			xf2 = XFGen(r,a[1])
			histogram2.Fill(xf2)
			XF_2.append(xf2)
			xf3 = XFGen(r,a[2])
			histogram3.Fill(xf3)
			XF_3.append(xf3)
		return (histogram1, histogram2, histogram3, XF_1, XF_2, XF_3)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1]
		XF_1 = []
		XF_2 = []
		for i in range(loopsize):
			xf1 = XFGen(r,a[0])
			histogram1.Fill(xf1)
			XF_1.append(xf1)
			xf2 = XFGen(r,a[1])
			histogram2.Fill(xf2)
			XF_2.append(xf2)
		return (histogram1, histogram2, XF_1, XF_2)

	else:
		histogram1 = b
		XF_1 = []
		for i in range(loopsize):
			xf1 = XFGen(r,a[0])
			histogram1.Fill(xf1)
			XF_1.append(xf1)
		return (histogram1, XF_1)

def PTXHistogramFiller(a,b,r,loopsize):

	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		histogram4 = b[3]
		PTX_1 = []
		PTX_2 = []
		PTX_3 = []
		PTX_4 = []
		PTY_1 = []
		PTY_2 = []
		PTY_3 = []
		PTY_4 = []
		for i in range(loopsize):
			ptx1, pty1 = ptGetter(r,math.sqrt(1.0/(2.0*a[0])))
			histogram1.Fill(ptx1)
			PTX_1.append(ptx1)
			PTY_1.append(pty1)
			ptx2, pty2 = ptGetter(r,math.sqrt(1.0/(2.0*a[1])))
			histogram2.Fill(ptx2)
			PTX_2.append(ptx2)
			PTY_2.append(pty2)
			ptx3, pty3 = ptGetter(r,math.sqrt(1.0/(2.0*a[2])))
			histogram3.Fill(ptx3)
			PTX_3.append(ptx3)
			PTY_3.append(pty3)
			ptx4, pty4 = ptGetter(r,math.sqrt(1.0/(2.0*a[3])))
			histogram4.Fill(ptx4)
			PTX_4.append(ptx4)
			PTY_4.append(pty4)
		return (histogram1, histogram2, histogram3, histogram4, PTX_1, PTX_2, PTX_3, PTX_4, PTY_1, PTY_2, PTY_3, PTY_4)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		PTX_1 = []
		PTX_2 = []
		PTX_3 = []
		PTY_1 = []
		PTY_2 = []
		PTY_3 = []
		for i in range(loopsize):
			ptx1, pty1 = ptGetter(r,math.sqrt(1.0/(2.0*a[0])))
			histogram1.Fill(ptx1)
			PTX_1.append(ptx1)
			PTY_1.append(pty1)
			ptx2, pty2 = ptGetter(r,math.sqrt(1.0/(2.0*a[1])))
			histogram2.Fill(ptx2)
			PTX_2.append(ptx2)
			PTY_2.append(pty2)
			ptx3, pty3 = ptGetter(r,math.sqrt(1.0/(2.0*a[2])))
			histogram3.Fill(ptx3)
			PTX_3.append(ptx3)
			PTY_3.append(pty3)
		return (histogram1, histogram2, histogram3, PTX_1, PTX_2, PTX_3, PTY_1, PTY_2, PTY_3)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1] 
		PTX_1 = []
		PTX_2 = []
		PTY_1 = []
		PTY_2 = []
		for i in range(loopsize):
			ptx1, pty1 = ptGetter(r,math.sqrt(1.0/(2.0*a[0])))
			histogram1.Fill(ptx1)
			PTX_1.append(ptx1)
			PTY_1.append(pty1)
			ptx2, pty2 = ptGetter(r,math.sqrt(1.0/(2.0*a[1])))
			histogram2.Fill(ptx2)
			PTX_2.append(ptx2)
			PTY_2.append(pty2)
		return (histogram1, histogram2, PTX_1, PTX_2, PTY_1, PTY_2)

	else:
		histogram1 = b
		PTX_1 = []
		PTY_1 = []
		for i in range(loopsize):
			ptx1, pty1 = ptGetter(r,math.sqrt(1.0/(2.0*a[0])))
			histogram1.Fill(ptx1)
			PTX_1.append(ptx1)
			PTY_1.append(pty1)
		return (histogram1, PTX_1, PTY_1)


def PTSQHistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		ptx1 = args[3]
		pty1 = args[4]
		ptx2 = args[5]
		pty2 = args[6]
		ptx3 = args[7]
		pty3 = args[8]
		ptx4 = args[9]
		pty4 = args[10]
		pt2_1_v = []
		pt2_2_v = []
		pt2_3_v = []
		pt2_4_v = []
		for i in range(loopsize):
			pt2_1 = ptx1[i]*ptx1[i] + pty1[i]*pty1[i]
			pt2_1_v.append(pt2_1)
			histogram1.Fill(pt2_1)
			pt2_2 = ptx2[i]*ptx2[i] + pty2[i]*pty2[i]
			pt2_2_v.append(pt2_2)
			histogram2.Fill(pt2_2)
			pt2_3 = ptx3[i]*ptx3[i] + pty3[i]*pty3[i]
			pt2_3_v.append(pt2_3)
			histogram3.Fill(pt2_3)
			pt2_4 = ptx4[i]*ptx4[i] + pty4[i]*pty4[i]
			pt2_4_v.append(pt2_4)
			histogram4.Fill(pt2_4)
		return (histogram1, histogram2, histogram3, histogram4, pt2_1_v, pt2_2_v, pt2_3_v, pt2_4_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		ptx1 = args[3]
		pty1 = args[4]
		ptx2 = args[5]
		pty2 = args[6]
		ptx3 = args[7]
		pty3 = args[8]
		pt2_1_v = []
		pt2_2_v = []
		pt2_3_v = []
		for i in range(loopsize):
			pt2_1 = ptx1[i]*ptx1[i] + pty1[i]*pty1[i]
			pt2_1_v.append(pt2_1)
			histogram1.Fill(pt2_1)
			pt2_2 = ptx2[i]*ptx2[i] + pty2[i]*pty2[i]
			pt2_2_v.append(pt2_2)
			histogram2.Fill(pt2_2)
			pt2_3 = ptx3[i]*ptx3[i] + pty3[i]*pty3[i]
			pt2_3_v.append(pt2_3)
			histogram3.Fill(pt2_3)
		return (histogram1, histogram2, histogram3, pt2_1_v, pt2_2_v, pt2_3_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1] 
		ptx1 = args[3]
		pty1 = args[4]
		ptx2 = args[5]
		pty2 = args[6]
		pt2_1_v = []
		pt2_2_v = []
		for i in range(loopsize):
			pt2_1 = ptx1[i]*ptx1[i] + pty1[i]*pty1[i]
			pt2_1_v.append(pt2_1)
			histogram1.Fill(pt2_1)
			pt2_2 = ptx2[i]*ptx2[i] + pty2[i]*pty2[i]
			pt2_2_v.append(pt2_2)
			histogram2.Fill(pt2_2)
		return (histogram1, histogram2, pt2_1_v, pt2_2_v)

	else:
		histogram1 = b 
		ptx1 = args[3]
		pty1 = args[4]
		pt2_1_v = []
		for i in range(loopsize):
			pt2_1 = ptx1[i]*ptx1[i] + pty1[i]*pty1[i]
			pt2_1_v.append(pt2_1)
			histogram1.Fill(pt2_1)
		return (histogram1, pt2_1_v)


def PTZHistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	pz1_v = []
	pz2_v = []
	pz3_v = []
	pz4_v = []
	e1_v = []
	e2_v = []
	e3_v = []
	e4_v = []
	e1_ex_v = []
	e2_ex_v = []
	e3_ex_v = []
	e4_ex_v = []
	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		histogram4 = b[3]
		p = args[3]
		xf1 = args[4]
		xf2 = args[5]
		xf3 = args[6]
		xf4 = args[7]
		pt2_1 = args[8]
		pt2_2 = args[9]
		pt2_3 = args[10]
		pt2_4 = args[11]
		for i in range(loopsize):
			pz1 = p*xf1[i]
			pz1_v.append(pz1)
			e1   		= math.sqrt(mc*mc+pt2_1[i]+pz1*pz1)
			e1_v.append(e1)
			e1_ex		= gamma * (e1 + beta*pz1)
			e1_ex_v.append(e1_ex)
			histogram1.Fill(pz1)
			pz2 = p*xf2[i]
			pz2_v.append(pz2)
			e2   		= math.sqrt(mc*mc+pt2_2[i]+pz2*pz2)
			e2_v.append(e2)
			e2_ex		= gamma * (e2 + beta*pz2)
			e2_ex_v.append(e2_ex)
			histogram2.Fill(pz2)
			pz3 = p*xf3[i]
			pz3_v.append(pz3)
			e3   		= math.sqrt(mc*mc+pt2_3[i]+pz3*pz3)
			e3_v.append(e3)
			e3_ex		= gamma * (e3 + beta*pz3)
			e3_ex_v.append(e3_ex)
			histogram3.Fill(pz3)
			pz4 = p*xf4[i]
			pz4_v.append(pz4)
			e4   		= math.sqrt(mc*mc+pt2_4[i]+pz4*pz4)
			e4_v.append(e4)
			e4_ex		= gamma * (e4 + beta*pz4)
			e4_ex_v.append(e4_ex)
			histogram4.Fill(pz4)
		return (histogram1, histogram2, histogram3, histogram4, pz1_v, pz2_v, pz3_v, pz4_v, e1_v, e2_v, e3_v, e4_v, e1_ex_v, e2_ex_v, e3_ex_v, e4_ex_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		p = args[3]
		xf1 = args[4]
		xf2 = args[5]
		xf3 = args[6]
		pt2_1 = args[7]
		pt2_2 = args[8]
		pt2_3 = args[9]
		for i in range(loopsize):
			pz1 = p*xf1[i]
			pz1_v.append(pz1)
			e1   		= math.sqrt(mc*mc+pt2_1[i]+pz1*pz1)
			e1_v.append(e1)
			e1_ex		= gamma * (e1 + beta*pz1)
			e1_ex_v.append(e1_ex)
			histogram1.Fill(pz1)
			pz2 = p*xf2[i]
			pz2_v.append(pz2)
			e2   		= math.sqrt(mc*mc+pt2_2[i]+pz2*pz2)
			e2_v.append(e2)
			e2_ex		= gamma * (e2 + beta*pz2)
			e2_ex_v.append(e2_ex)
			histogram2.Fill(pz2)
			pz3 = p*xf3[i]
			pz3_v.append(pz3)
			e3   		= math.sqrt(mc*mc+pt2_3[i]+pz3*pz3)
			e3_v.append(e3)
			e3_ex		= gamma * (e3 + beta*pz3)
			e3_ex_v.append(e3_ex)
			histogram3.Fill(pz3)
		return (histogram1, histogram2, histogram3, pz1_v, pz2_v, pz3_v, e1_v, e2_v, e3_v, e1_ex_v, e2_ex_v, e3_ex_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1] 
		p = args[3]
		xf1 = args[4]
		xf2 = args[5]
		pt2_1 = args[6]
		pt2_2 = args[7]
		for i in range(loopsize):
			pz1 = p*xf1[i]
			pz1_v.append(pz1)
			e1   		= math.sqrt(mc*mc+pt2_1[i]+pz1*pz1)
			e1_v.append(e1)
			e1_ex		= gamma * (e1 + beta*pz1)
			e1_ex_v.append(e1_ex)
			histogram1.Fill(pz1)
			pz2 = p*xf2[i]
			pz2_v.append(pz2)
			e2   		= math.sqrt(mc*mc+pt2_2[i]+pz2*pz2)
			e2_v.append(e2)
			e2_ex		= gamma * (e2 + beta*pz2)
			e2_ex_v.append(e2_ex)
			histogram2.Fill(pz2)
		return (histogram1, histogram2, pz1_v, pz2_v, e1_v, e2_v, e1_ex_v, e2_ex_v)

	else:
		histogram1 = b
		p = args[3]
		xf1 = args[4]
		pt2_1 = args[5]
		for i in range(loopsize):
			pz1 = p*xf1[i]
			pz1_v.append(pz1)
			e1   		= math.sqrt(mc*mc+pt2_1[i]+pz1*pz1)
			e1_v.append(e1)
			e1_ex		= gamma * (e1 + beta*pz1)
			e1_ex_v.append(e1_ex)
			histogram1.Fill(pz1)
		return (histogram1, pz1_v, e1_v, e1_ex_v)

def Emission_Angle_DsHistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	Theta_Ds_v1 = []
	Theta_Ds_v2 = []
	Theta_Ds_v3 = []
	Theta_Ds_v4 = []
	gamma1_1_v = []
	beta1_1_v = []
	gamma1_2_v = []
	beta1_2_v = []
	gamma1_3_v = []
	beta1_3_v = []
	gamma1_4_v = []
	beta1_4_v = []
	X_Slope1_v = []
	X_Slope2_v = []
	X_Slope3_v = []
	X_Slope4_v = []
	Y_Slope1_v = []
	Y_Slope2_v = []
	Y_Slope3_v = []
	Y_Slope4_v = []
	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		ptx1 = args[3]
		ptx2 = args[4]
		ptx3 = args[5]
		ptx4 = args[6]
		pty1 = args[7]
		pty2 = args[8]
		pty3 = args[9]
		pty4 = args[10]
		ptz1 = args[11]
		ptz2 = args[12]
		ptz3 = args[13]
		ptz4 = args[14]
		e1 = args[15]
		e2 = args[16]
		e3 = args[17]
		e4 = args[18]
		e1_ex = args[19]
		e2_ex = args[20]
		e3_ex = args[21]
		e4_ex = args[22]
		for i in range(loopsize):
			pz1_ex 		= gamma * (beta*e1[i] + ptz1[i])
			gamma1_1 	= e1_ex[i] /mc #Ds's gamma factor
			gamma1_1_v.append(gamma1_1)
			beta1_1 	= math.sqrt(1.0-1.0/(gamma1_1*gamma1_1))
			beta1_1_v.append(beta1_1)
			X_Slope1 		= ptx1[i] / pz1_ex
			X_Slope1_v.append(X_Slope1)
			Y_Slope1 		= pty1[i] / pz1_ex
			Y_Slope1_v.append(Y_Slope1)
			Ds_theta1 	= math.sqrt(X_Slope1*X_Slope1 + Y_Slope1*Y_Slope1)
			Theta_Ds_v1.append(Ds_theta1)
			histogram1.Fill(Ds_theta1)

			pz2_ex 		= gamma * (beta*e2[i] + ptz2[i])
			gamma1_2 	= e2_ex[i] /mc #Ds's gamma factor
			gamma1_2_v.append(gamma1_2)
			beta1_2 	= math.sqrt(1.0-1.0/(gamma1_2*gamma1_2))
			beta1_2_v.append(beta1_2)
			X_Slope2 		= ptx2[i] / pz2_ex
			X_Slope2_v.append(X_Slope2)
			Y_Slope2 		= pty2[i] / pz2_ex
			Y_Slope2_v.append(Y_Slope2)
			Ds_theta2 	= math.sqrt(X_Slope2*X_Slope2 + Y_Slope2*Y_Slope2)
			Theta_Ds_v2.append(Ds_theta2)
			histogram2.Fill(Ds_theta2)

			pz3_ex 		= gamma * (beta*e3[i] + ptz3[i])
			gamma1_3 	= e3_ex[i] /mc #Ds's gamma factor
			gamma1_3_v.append(gamma1_3)
			beta1_3 	= math.sqrt(1.0-1.0/(gamma1_3*gamma1_3))
			beta1_3_v.append(beta1_3)
			X_Slope3 		= ptx3[i] / pz3_ex
			X_Slope3_v.append(X_Slope3)
			Y_Slope3 		= pty3[i] / pz3_ex
			Y_Slope3_v.append(Y_Slope3)
			Ds_theta3 	= math.sqrt(X_Slope3*X_Slope3 + Y_Slope3*Y_Slope3)
			Theta_Ds_v3.append(Ds_theta3)
			histogram3.Fill(Ds_theta3)

			pz4_ex 		= gamma * (beta*e4[i] + ptz4[i])
			gamma1_4 	= e4_ex[i] /mc #Ds's gamma factor
			gamma1_4_v.append(gamma1_4)
			beta1_4 	= math.sqrt(1.0-1.0/(gamma1_4*gamma1_4))
			beta1_4_v.append(beta1_4)
			X_Slope4 		= ptx4[i] / pz4_ex
			X_Slope4_v.append(X_Slope4)
			Y_Slope4 		= pty4[i] / pz4_ex
			Y_Slope4_v.append(Y_Slope4)
			Ds_theta4 	= math.sqrt(X_Slope4*X_Slope4 + Y_Slope4*Y_Slope4)
			Theta_Ds_v4.append(Ds_theta4)
			histogram4.Fill(Ds_theta4)


		return (histogram1, histogram2, histogram3, histogram4, X_Slope1_v, X_Slope2_v, X_Slope3_v, X_Slope4_v, Y_Slope1_v, Y_Slope2_v, Y_Slope3_v, Y_Slope4_v, Theta_Ds_v1, Theta_Ds_v2, Theta_Ds_v3, Theta_Ds_v4, gamma1_1_v, gamma1_2_v, gamma1_3_v, gamma1_4_v, beta1_1_v, beta1_2_v, beta1_3_v, beta1_4_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1] 
		histogram3 = b[2]
		ptx1 = args[3]
		ptx2 = args[4]
		ptx3 = args[5]
		pty1 = args[6]
		pty2 = args[7]
		pty3 = args[8]
		ptz1 = args[9]
		ptz2 = args[10]
		ptz3 = args[11]
		e1 = args[12]
		e2 = args[13]
		e3 = args[14]
		e1_ex = args[15]
		e2_ex = args[16]
		e3_ex = args[17]
		for i in range(loopsize):
			pz1_ex 		= gamma * (beta*e1[i] + ptz1[i])
			gamma1_1 	= e1_ex[i] /mc #Ds's gamma factor
			gamma1_1_v.append(gamma1_1)
			beta1_1 	= math.sqrt(1.0-1.0/(gamma1_1*gamma1_1))
			beta1_1_v.append(beta1_1)
			X_Slope1 		= ptx1[i] / pz1_ex
			X_Slope1_v.append(X_Slope1)
			Y_Slope1 		= pty1[i] / pz1_ex
			Y_Slope1_v.append(Y_Slope1)
			Ds_theta1 	= math.sqrt(X_Slope1*X_Slope1 + Y_Slope1*Y_Slope1)
			Theta_Ds_v1.append(Ds_theta1)
			histogram1.Fill(Ds_theta1)

			pz2_ex 		= gamma * (beta*e2[i] + ptz2[i])
			gamma1_2 	= e2_ex[i] /mc #Ds's gamma factor
			gamma1_2_v.append(gamma1_2)
			beta1_2 	= math.sqrt(1.0-1.0/(gamma1_2*gamma1_2))
			beta1_2_v.append(beta1_2)
			X_Slope2 		= ptx2[i] / pz2_ex
			X_Slope2_v.append(X_Slope2)
			Y_Slope2 		= pty2[i] / pz2_ex
			Y_Slope2_v.append(Y_Slope2)
			Ds_theta2 	= math.sqrt(X_Slope2*X_Slope2 + Y_Slope2*Y_Slope2)
			Theta_Ds_v2.append(Ds_theta2)
			histogram2.Fill(Ds_theta2)

			pz3_ex 		= gamma * (beta*e3[i] + ptz3[i])
			gamma1_3 	= e3_ex[i] /mc #Ds's gamma factor
			gamma1_3_v.append(gamma1_3)
			beta1_3 	= math.sqrt(1.0-1.0/(gamma1_3*gamma1_3))
			beta1_3_v.append(beta1_3)
			X_Slope3 		= ptx3[i] / pz3_ex
			X_Slope3_v.append(X_Slope3)
			Y_Slope3 		= pty3[i] / pz3_ex
			Y_Slope3_v.append(Y_Slope3)
			Ds_theta3 	= math.sqrt(X_Slope3*X_Slope3 + Y_Slope3*Y_Slope3)
			Theta_Ds_v3.append(Ds_theta3)
			histogram3.Fill(Ds_theta3)

		return (histogram1, histogram2, histogram3, X_Slope1_v, X_Slope2_v, X_Slope3_v, Y_Slope1_v, Y_Slope2_v, Y_Slope3_v, Theta_Ds_v1, Theta_Ds_v2, Theta_Ds_v3, gamma1_1_v, gamma1_2_v, gamma1_3_v, beta1_1_v, beta1_2_v, beta1_3_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1] 
		ptx1 = args[3]
		ptx2 = args[4]
		pty1 = args[5]
		pty2 = args[6]
		ptz1 = args[7]
		ptz2 = args[8]
		e1 = args[9]
		e2 = args[10]
		e1_ex = args[11]
		e2_ex = args[12]
		for i in range(loopsize):
			pz1_ex 		= gamma * (beta*e1[i] + ptz1[i])
			gamma1_1 	= e1_ex[i] /mc #Ds's gamma factor
			gamma1_1_v.append(gamma1_1)
			beta1_1 	= math.sqrt(1.0-1.0/(gamma1_1*gamma1_1))
			beta1_1_v.append(beta1_1)
			X_Slope1 		= ptx1[i] / pz1_ex
			X_Slope1_v.append(X_Slope1)
			Y_Slope1 		= pty1[i] / pz1_ex
			Y_Slope1_v.append(Y_Slope1)
			Ds_theta1 	= math.sqrt(X_Slope1*X_Slope1 + Y_Slope1*Y_Slope1)
			Theta_Ds_v1.append(Ds_theta1)
			histogram1.Fill(Ds_theta1)

			pz2_ex 		= gamma * (beta*e2[i] + ptz2[i])
			gamma1_2 	= e2_ex[i] /mc #Ds's gamma factor
			gamma1_2_v.append(gamma1_2)
			beta1_2 	= math.sqrt(1.0-1.0/(gamma1_2*gamma1_2))
			beta1_2_v.append(beta1_2)
			X_Slope2 		= ptx2[i] / pz2_ex
			X_Slope2_v.append(X_Slope2)
			Y_Slope2 		= pty2[i] / pz2_ex
			Y_Slope2_v.append(Y_Slope2)
			Ds_theta2 	= math.sqrt(X_Slope2*X_Slope2 + Y_Slope2*Y_Slope2)
			Theta_Ds_v2.append(Ds_theta2)
			histogram2.Fill(Ds_theta2)

		return (histogram1, histogram2, X_Slope1_v, X_Slope2_v, Y_Slope1_v, Y_Slope2_v, Theta_Ds_v1, Theta_Ds_v2, gamma1_1_v, gamma1_2_v, beta1_1_v, beta1_2_v)

	else:
		histogram1 = b
		ptx1 = args[3]
		pty1 = args[4]
		ptz1 = args[5]
		e1 = args[6]
		e1_ex = args[7]
		for i in range(loopsize):
			pz1_ex 		= gamma * (beta*e1[i] + ptz1[i])
			gamma1_1 	= e1_ex[i] /mc #Ds's gamma factor
			gamma1_1_v.append(gamma1_1)
			beta1_1 	= math.sqrt(1.0-1.0/(gamma1_1*gamma1_1))
			beta1_1_v.append(beta1_1)
			X_Slope1 		= ptx1[i] / pz1_ex
			X_Slope1_v.append(X_Slope1)
			Y_Slope1 		= pty1[i] / pz1_ex
			Y_Slope1_v.append(Y_Slope1)
			Ds_theta1 	= math.sqrt(X_Slope1*X_Slope1 + Y_Slope1*Y_Slope1)
			Theta_Ds_v1.append(Ds_theta1)
			histogram1.Fill(Ds_theta1)

		return (histogram1, X_Slope1_v, Y_Slope1_v, Theta_Ds_v1, gamma1_1_v, beta1_1_v)

def Emission_Angle_TauHistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	rand = args[len(args)-1]
	TauPx_v = []
	TauPy_v = []
	TauPz_v = []
	X_Slope1_Tau_v = []
	X_Slope2_Tau_v = []
	X_Slope3_Tau_v = []
	X_Slope4_Tau_v = []
	Y_Slope1_Tau_v = []
	Y_Slope2_Tau_v = []
	Y_Slope3_Tau_v = []
	Y_Slope4_Tau_v = []
	e1_ex_tau_v = []
	e2_ex_tau_v = []
	e3_ex_tau_v = []
	e4_ex_tau_v = []
	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Gamma1_3 = args[5]
		Gamma1_4 = args[6]
		Beta1_1 = args[7]
		Beta1_2 = args[8]
		Beta1_3 = args[9]
		Beta1_4 = args[10]
		X_Slope_Ds1 = args[11]
		X_Slope_Ds2 = args[12]
		X_Slope_Ds3 = args[13]
		X_Slope_Ds4 = args[14]
		Y_Slope_Ds1 = args[15]
		Y_Slope_Ds2 = args[16]
		Y_Slope_Ds3 = args[17]
		Y_Slope_Ds4 = args[18]

		for i in range(loopsize):
			TauPx,TauPy,TauPz 	= TauMomentumGenerator(rand,p1)

			TauPx_v.append(TauPx)
			TauPy_v.append(TauPy)
			TauPz_v.append(TauPz)
			TauPx_ex 	= TauPx #Experimental X Dir Tau Momentum
			TauPy_ex 	= TauPy #Experimental Y Dir Tau Momentum
			TauPz_ex1 	= Gamma1_1[i] * (Beta1_1[i] * e1_tau + TauPz) #Experimental Z Dir Tau Momentum
			X_Slope1_Tau 	= TauPx_ex / TauPz_ex1
			X_Slope1_Tau_v.append(X_Slope1_Tau)
			Y_Slope1_Tau 	= TauPy_ex / TauPz_ex1
			Y_Slope1_Tau_v.append(Y_Slope1_Tau)
			e1_ex_tau 	= Gamma1_1[i] *(e1_tau + Beta1_1[i] *TauPz)
			e1_ex_tau_v.append(e1_ex_tau)
			Theta_Tau1 		= math.sqrt((X_Slope1_Tau + X_Slope_Ds1[i])*(X_Slope1_Tau + X_Slope_Ds1[i]) + (Y_Slope1_Tau + Y_Slope_Ds1[i]) * (Y_Slope1_Tau +Y_Slope_Ds1[i]))
			histogram1.Fill(Theta_Tau1) #Fill Tau emission angle Histogram

			TauPz_ex2 	= Gamma1_2[i] * (Beta1_2[i] * e1_tau + TauPz)
			X_Slope2_Tau 	= TauPx_ex / TauPz_ex2
			X_Slope2_Tau_v.append(X_Slope2_Tau)
			Y_Slope2_Tau 	= TauPy_ex / TauPz_ex2
			Y_Slope2_Tau_v.append(Y_Slope2_Tau)
			e2_ex_tau 	= Gamma1_2[i] *(e1_tau + Beta1_2[i] *TauPz)
			e2_ex_tau_v.append(e2_ex_tau)
			Theta_Tau2 		= math.sqrt((X_Slope2_Tau + X_Slope_Ds2[i])*(X_Slope2_Tau + X_Slope_Ds2[i]) + (Y_Slope2_Tau + Y_Slope_Ds2[i]) * (Y_Slope2_Tau +Y_Slope_Ds2[i]))
			histogram2.Fill(Theta_Tau2)

			TauPz_ex3 	= Gamma1_3[i] * (Beta1_3[i] * e1_tau + TauPz)
			X_Slope3_Tau 	= TauPx_ex / TauPz_ex3
			X_Slope3_Tau_v.append(X_Slope3_Tau)
			Y_Slope3_Tau 	= TauPy_ex / TauPz_ex3
			Y_Slope3_Tau_v.append(Y_Slope3_Tau)
			e3_ex_tau 	= Gamma1_3[i] *(e1_tau + Beta1_3[i] *TauPz)
			e3_ex_tau_v.append(e3_ex_tau)
			Theta_Tau3 		= math.sqrt((X_Slope3_Tau + X_Slope_Ds3[i])*(X_Slope3_Tau + X_Slope_Ds3[i]) + (Y_Slope3_Tau + Y_Slope_Ds3[i]) * (Y_Slope3_Tau +Y_Slope_Ds3[i]))
			histogram3.Fill(Theta_Tau3)

			TauPz_ex4 	= Gamma1_4[i] * (Beta1_4[i] * e1_tau + TauPz)
			X_Slope4_Tau 	= TauPx_ex / TauPz_ex4
			X_Slope4_Tau_v.append(X_Slope4_Tau)
			Y_Slope4_Tau 	= TauPy_ex / TauPz_ex4
			Y_Slope4_Tau_v.append(Y_Slope4_Tau)
			e4_ex_tau 	= Gamma1_4[i] *(e1_tau + Beta1_4[i] *TauPz)
			e4_ex_tau_v.append(e4_ex_tau)
			Theta_Tau4 		= math.sqrt((X_Slope4_Tau + X_Slope_Ds4[i])*(X_Slope4_Tau + X_Slope_Ds4[i]) + (Y_Slope4_Tau + Y_Slope_Ds4[i]) * (Y_Slope4_Tau +Y_Slope_Ds4[i]))
			histogram4.Fill(Theta_Tau4)

		return (histogram1, histogram2, histogram3, histogram4, TauPx_v, TauPy_v, TauPz_v, X_Slope1_Tau_v, X_Slope2_Tau_v, X_Slope3_Tau_v, X_Slope4_Tau_v, Y_Slope1_Tau_v, Y_Slope2_Tau_v, Y_Slope3_Tau_v, Y_Slope4_Tau_v, e1_ex_tau_v, e2_ex_tau_v, e3_ex_tau_v, e4_ex_tau_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Gamma1_3 = args[5]
		Beta1_1 = args[6]
		Beta1_2 = args[7]
		Beta1_3 = args[8]
		X_Slope_Ds1 = args[9]
		X_Slope_Ds2 = args[10]
		X_Slope_Ds3 = args[11]
		Y_Slope_Ds1 = args[12]
		Y_Slope_Ds2 = args[13]
		Y_Slope_Ds3 = args[14]
		for i in range(loopsize):
			TauPx,TauPy,TauPz 	= TauMomentumGenerator(rand,p1)

			TauPx_v.append(TauPx)
			TauPy_v.append(TauPy)
			TauPz_v.append(TauPz)
			TauPx_ex 	= TauPx #Experimental X Dir Tau Momentum
			TauPy_ex 	= TauPy #Experimental Y Dir Tau Momentum
			TauPz_ex1 	= Gamma1_1[i] * (Beta1_1[i] * e1_tau + TauPz) #Experimental Z Dir Tau Momentum
			X_Slope1_Tau 	= TauPx_ex / TauPz_ex1
			X_Slope1_Tau_v.append(X_Slope1_Tau)
			Y_Slope1_Tau 	= TauPy_ex / TauPz_ex1
			Y_Slope1_Tau_v.append(Y_Slope1_Tau)
			e1_ex_tau 	= Gamma1_1[i] *(e1_tau + Beta1_1[i] *TauPz)
			e1_ex_tau_v.append(e1_ex_tau)
			Theta_Tau1 		= math.sqrt((X_Slope1_Tau + X_Slope_Ds1[i])*(X_Slope1_Tau + X_Slope_Ds1[i]) + (Y_Slope1_Tau + Y_Slope_Ds1[i]) * (Y_Slope1_Tau +Y_Slope_Ds1[i]))
			histogram1.Fill(Theta_Tau1) #Fill Tau emission angle Histogram

			TauPz_ex2 	= Gamma1_2[i] * (Beta1_2[i] * e1_tau + TauPz)
			X_Slope2_Tau 	= TauPx_ex / TauPz_ex2
			X_Slope2_Tau_v.append(X_Slope2_Tau)
			Y_Slope2_Tau 	= TauPy_ex / TauPz_ex2
			Y_Slope2_Tau_v.append(Y_Slope2_Tau)
			e2_ex_tau 	= Gamma1_2[i] *(e1_tau + Beta1_2[i] *TauPz)
			e2_ex_tau_v.append(e2_ex_tau)
			Theta_Tau2 		= math.sqrt((X_Slope2_Tau + X_Slope_Ds2[i])*(X_Slope2_Tau + X_Slope_Ds2[i]) + (Y_Slope2_Tau + Y_Slope_Ds2[i]) * (Y_Slope2_Tau +Y_Slope_Ds2[i]))
			histogram2.Fill(Theta_Tau2)

			TauPz_ex3 	= Gamma1_3[i] * (Beta1_3[i] * e1_tau + TauPz)
			X_Slope3_Tau 	= TauPx_ex / TauPz_ex3
			X_Slope3_Tau_v.append(X_Slope3_Tau)
			Y_Slope3_Tau 	= TauPy_ex / TauPz_ex3
			Y_Slope3_Tau_v.append(Y_Slope3_Tau)
			e3_ex_tau 	= Gamma1_3[i] *(e1_tau + Beta1_3[i] *TauPz)
			e3_ex_tau_v.append(e3_ex_tau)
			Theta_Tau3 		= math.sqrt((X_Slope3_Tau + X_Slope_Ds3[i])*(X_Slope3_Tau + X_Slope_Ds3[i]) + (Y_Slope3_Tau + Y_Slope_Ds3[i]) * (Y_Slope3_Tau +Y_Slope_Ds3[i]))
			histogram3.Fill(Theta_Tau3)

		return (histogram1, histogram2, histogram3, TauPx_v, TauPy_v, TauPz_v, X_Slope1_Tau_v, X_Slope2_Tau_v, X_Slope3_Tau_v, Y_Slope1_Tau_v, Y_Slope2_Tau_v, Y_Slope3_Tau_v, e1_ex_tau_v, e2_ex_tau_v, e3_ex_tau_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Beta1_1 = args[5]
		Beta1_2 = args[6]
		X_Slope_Ds1 = args[7]
		X_Slope_Ds2 = args[8]
		Y_Slope_Ds1 = args[9]
		Y_Slope_Ds2 = args[10]
		for i in range(loopsize):
			TauPx,TauPy,TauPz 	= TauMomentumGenerator(rand,p1)

			TauPx_v.append(TauPx)
			TauPy_v.append(TauPy)
			TauPz_v.append(TauPz)
			TauPx_ex 	= TauPx #Experimental X Dir Tau Momentum
			TauPy_ex 	= TauPy #Experimental Y Dir Tau Momentum
			TauPz_ex1 	= Gamma1_1[i] * (Beta1_1[i] * e1_tau + TauPz) #Experimental Z Dir Tau Momentum
			X_Slope1_Tau 	= TauPx_ex / TauPz_ex1
			X_Slope1_Tau_v.append(X_Slope1_Tau)
			Y_Slope1_Tau 	= TauPy_ex / TauPz_ex1
			Y_Slope1_Tau_v.append(Y_Slope1_Tau)
			e1_ex_tau 	= Gamma1_1[i] *(e1_tau + Beta1_1[i] *TauPz)
			e1_ex_tau_v.append(e1_ex_tau)
			Theta_Tau1 		= math.sqrt((X_Slope1_Tau + X_Slope_Ds1[i])*(X_Slope1_Tau + X_Slope_Ds1[i]) + (Y_Slope1_Tau + Y_Slope_Ds1[i]) * (Y_Slope1_Tau +Y_Slope_Ds1[i]))
			histogram1.Fill(Theta_Tau1) #Fill Tau emission angle Histogram

			TauPz_ex2 	= Gamma1_2[i] * (Beta1_2[i] * e1_tau + TauPz)
			X_Slope2_Tau 	= TauPx_ex / TauPz_ex2
			X_Slope2_Tau_v.append(X_Slope2_Tau)
			Y_Slope2_Tau 	= TauPy_ex / TauPz_ex2
			Y_Slope2_Tau_v.append(Y_Slope2_Tau)
			e2_ex_tau 	= Gamma1_2[i] *(e1_tau + Beta1_2[i] *TauPz)
			e2_ex_tau_v.append(e2_ex_tau)
			Theta_Tau2 		= math.sqrt((X_Slope2_Tau + X_Slope_Ds2[i])*(X_Slope2_Tau + X_Slope_Ds2[i]) + (Y_Slope2_Tau + Y_Slope_Ds2[i]) * (Y_Slope2_Tau +Y_Slope_Ds2[i]))
			histogram2.Fill(Theta_Tau2)

		return (histogram1, histogram2, TauPx_v, TauPy_v, TauPz_v, X_Slope1_Tau_v, X_Slope2_Tau_v, Y_Slope1_Tau_v, Y_Slope2_Tau_v, e1_ex_tau_v, e2_ex_tau_v)

	else:
		histogram1 = b
		Gamma1_1 = args[3]
		Beta1_1 = args[4]
		X_Slope_Ds1 = args[5]
		Y_Slope_Ds1 = args[6]
		for i in range(loopsize):
			TauPx,TauPy,TauPz 	= TauMomentumGenerator(rand,p1)

			TauPx_v.append(TauPx)
			TauPy_v.append(TauPy)
			TauPz_v.append(TauPz)
			TauPx_ex 	= TauPx #Experimental X Dir Tau Momentum
			TauPy_ex 	= TauPy #Experimental Y Dir Tau Momentum
			TauPz_ex1 	= Gamma1_1[i] * (Beta1_1[i] * e1_tau + TauPz) #Experimental Z Dir Tau Momentum
			X_Slope1_Tau 	= TauPx_ex / TauPz_ex1
			X_Slope1_Tau_v.append(X_Slope1_Tau)
			Y_Slope1_Tau 	= TauPy_ex / TauPz_ex1
			Y_Slope1_Tau_v.append(Y_Slope1_Tau)
			e1_ex_tau 	= Gamma1_1[i] *(e1_tau + Beta1_1[i] *TauPz)
			e1_ex_tau_v.append(e1_ex_tau)
			Theta_Tau1 	= math.sqrt((X_Slope1_Tau + X_Slope_Ds1[i])*(X_Slope1_Tau + X_Slope_Ds1[i]) + (Y_Slope1_Tau + Y_Slope_Ds1[i]) * (Y_Slope1_Tau +Y_Slope_Ds1[i]))
			histogram1.Fill(Theta_Tau1) #Fill Tau emission angle Histogram

		return (histogram1, TauPx_v, TauPy_v, TauPz_v, X_Slope1_Tau_v, Y_Slope1_Tau_v, e1_ex_tau_v)


def Emission_Angle_Nu1HistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	rand = args[len(args)-1]
	X_Slope1_Nu1_v = []
	X_Slope2_Nu1_v = []
	X_Slope3_Nu1_v = []
	X_Slope4_Nu1_v = []
	Y_Slope1_Nu1_v = []
	Y_Slope2_Nu1_v = []
	Y_Slope3_Nu1_v = []
	Y_Slope4_Nu1_v = []
	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Gamma1_3 = args[5]
		Gamma1_4 = args[6]
		Beta1_1 = args[7]
		Beta1_2 = args[8]
		Beta1_3 = args[9]
		Beta1_4 = args[10]
		TauPx = args[11]
		TauPy = args[12]
		TauPz = args[13]
		X_Slope_Ds1 = args[14]
		X_Slope_Ds2 = args[15]
		X_Slope_Ds3 = args[16]
		X_Slope_Ds4 = args[17]
		Y_Slope_Ds1 = args[18]
		Y_Slope_Ds2 = args[19]
		Y_Slope_Ds3 = args[20]
		Y_Slope_Ds4 = args[21]

		for i in range(loopsize):
			Nu1Px, Nu1Py, Nu1Pz = -TauPx[i], -TauPy[i], -TauPz[i]

			Nu1Px_ex	= Nu1Px #Experimental X Dir Nu Momentum
			Nu1Py_ex	= Nu1Py #Experimental Y Dir Nu Momentum
			Nu1Pz_ex1	= Gamma1_1[i] * (Beta1_1[i] * e1_neu -Nu1Pz) #Experimental Z Dir Nu Momentum
			X_Slope1_Nu1	= Nu1Px_ex / Nu1Pz_ex1
			X_Slope1_Nu1_v.append(X_Slope1_Nu1)
			Y_Slope1_Nu1	= Nu1Py_ex / Nu1Pz_ex1
			Y_Slope1_Nu1_v.append(Y_Slope1_Nu1)
			Theta_Nu1	= math.sqrt((X_Slope1_Nu1 + X_Slope_Ds1[i])*(X_Slope1_Nu1 + X_Slope_Ds1[i]) + (Y_Slope1_Nu1 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu1 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu1) #Fill Neu emission angle Histogram

			Nu1Pz_ex2	= Gamma1_2[i] * (Beta1_2[i] * e1_neu -Nu1Pz)
			X_Slope2_Nu1	= Nu1Px_ex / Nu1Pz_ex2
			Y_Slope2_Nu1	= Nu1Py_ex / Nu1Pz_ex2
			Theta_Nu2	= math.sqrt((X_Slope2_Nu1 + X_Slope_Ds2[i])*(X_Slope2_Nu1 + X_Slope_Ds2[i]) + (Y_Slope2_Nu1 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu1 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu2)

			Nu1Pz_ex3	= Gamma1_3[i] * (Beta1_3[i] * e1_neu -Nu1Pz)
			X_Slope3_Nu1	= Nu1Px_ex / Nu1Pz_ex3
			Y_Slope3_Nu1	= Nu1Py_ex / Nu1Pz_ex3
			Theta_Nu3	= math.sqrt((X_Slope3_Nu1 + X_Slope_Ds3[i])*(X_Slope3_Nu1 + X_Slope_Ds3[i]) + (Y_Slope3_Nu1 + Y_Slope_Ds3[i]) * (Y_Slope3_Nu1 +Y_Slope_Ds3[i]))

			histogram3.Fill(Theta_Nu3)

			Nu1Pz_ex4	= Gamma1_4[i] * (Beta1_4[i] * e1_neu -Nu1Pz)
			X_Slope4_Nu1	= Nu1Px_ex / Nu1Pz_ex4
			Y_Slope4_Nu1	= Nu1Py_ex / Nu1Pz_ex4
			Theta_Nu4	= math.sqrt((X_Slope4_Nu1 + X_Slope_Ds4[i])*(X_Slope4_Nu1 + X_Slope_Ds4[i]) + (Y_Slope4_Nu1 + Y_Slope_Ds4[i]) * (Y_Slope4_Nu1 +Y_Slope_Ds4[i]))

			histogram4.Fill(Theta_Nu4)

		return (histogram1, histogram2, histogram3, histogram4, X_Slope1_Nu1_v, X_Slope2_Nu1_v, X_Slope3_Nu1_v, X_Slope4_Nu1_v, Y_Slope1_Nu1_v, Y_Slope2_Nu1_v, Y_Slope3_Nu1_v, Y_Slope4_Nu1_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Gamma1_3 = args[5]
		Beta1_1 = args[6]
		Beta1_2 = args[7]
		Beta1_3 = args[8]
		TauPx = args[9]
		TauPy = args[10]
		TauPz = args[11]
		X_Slope_Ds1 = args[12]
		X_Slope_Ds2 = args[13]
		X_Slope_Ds3 = args[14]
		Y_Slope_Ds1 = args[15]
		Y_Slope_Ds2 = args[16]
		Y_Slope_Ds3 = args[17]
		for i in range(loopsize):
			Nu1Px, Nu1Py, Nu1Pz = -TauPx[i], -TauPy[i], -TauPz[i]

			Nu1Px_ex	= Nu1Px #Experimental X Dir Nu Momentum
			Nu1Py_ex	= Nu1Py #Experimental Y Dir Nu Momentum
			Nu1Pz_ex1	= Gamma1_1[i] * (Beta1_1[i] * e1_neu -Nu1Pz) #Experimental Z Dir Nu Momentum
			X_Slope1_Nu1	= Nu1Px_ex / Nu1Pz_ex1
			X_Slope1_Nu1_v.append(X_Slope1_Nu1)
			Y_Slope1_Nu1	= Nu1Py_ex / Nu1Pz_ex1
			Y_Slope1_Nu1_v.append(Y_Slope1_Nu1)
			Theta_Nu1	= math.sqrt((X_Slope1_Nu1 + X_Slope_Ds1[i])*(X_Slope1_Nu1 + X_Slope_Ds1[i]) + (Y_Slope1_Nu1 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu1 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu1) #Fill Neu emission angle Histogram

			Nu1Pz_ex2	= Gamma1_2[i] * (Beta1_2[i] * e1_neu -Nu1Pz)
			X_Slope2_Nu1	= Nu1Px_ex / Nu1Pz_ex2
			Y_Slope2_Nu1	= Nu1Py_ex / Nu1Pz_ex2
			Theta_Nu2	= math.sqrt((X_Slope2_Nu1 + X_Slope_Ds2[i])*(X_Slope2_Nu1 + X_Slope_Ds2[i]) + (Y_Slope2_Nu1 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu1 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu2)

			Nu1Pz_ex3	= Gamma1_3[i] * (Beta1_3[i] * e1_neu -Nu1Pz)
			X_Slope3_Nu1	= Nu1Px_ex / Nu1Pz_ex3
			Y_Slope3_Nu1	= Nu1Py_ex / Nu1Pz_ex3
			Theta_Nu3	= math.sqrt((X_Slope3_Nu1 + X_Slope_Ds3[i])*(X_Slope3_Nu1 + X_Slope_Ds3[i]) + (Y_Slope3_Nu1 + Y_Slope_Ds3[i]) * (Y_Slope3_Nu1 +Y_Slope_Ds3[i]))

			histogram3.Fill(Theta_Nu3)

		return (histogram1, histogram2, histogram3, X_Slope1_Nu1_v, X_Slope2_Nu1_v, X_Slope3_Nu1_v, Y_Slope1_Nu1_v, Y_Slope2_Nu1_v, Y_Slope3_Nu1_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1]
		Gamma1_1 = args[3]
		Gamma1_2 = args[4]
		Beta1_1 = args[5]
		Beta1_2 = args[6]
		TauPx = args[7]
		TauPy = args[8]
		TauPz = args[9]
		X_Slope_Ds1 = args[10]
		X_Slope_Ds2 = args[11]
		Y_Slope_Ds1 = args[12]
		Y_Slope_Ds2 = args[13]
		for i in range(loopsize):
			Nu1Px, Nu1Py, Nu1Pz = -TauPx[i], -TauPy[i], -TauPz[i]

			Nu1Px_ex	= Nu1Px #Experimental X Dir Nu Momentum
			Nu1Py_ex	= Nu1Py #Experimental Y Dir Nu Momentum
			Nu1Pz_ex1	= Gamma1_1[i] * (Beta1_1[i] * e1_neu -Nu1Pz) #Experimental Z Dir Nu Momentum
			X_Slope1_Nu1	= Nu1Px_ex / Nu1Pz_ex1
			X_Slope1_Nu1_v.append(X_Slope1_Nu1)
			Y_Slope1_Nu1	= Nu1Py_ex / Nu1Pz_ex1
			Y_Slope1_Nu1_v.append(Y_Slope1_Nu1)
			Theta_Nu1	= math.sqrt((X_Slope1_Nu1 + X_Slope_Ds1[i])*(X_Slope1_Nu1 + X_Slope_Ds1[i]) + (Y_Slope1_Nu1 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu1 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu1) #Fill Neu emission angle Histogram

			Nu1Pz_ex2	= Gamma1_2[i] * (Beta1_2[i] * e1_neu -Nu1Pz)
			X_Slope2_Nu1	= Nu1Px_ex / Nu1Pz_ex2
			Y_Slope2_Nu1	= Nu1Py_ex / Nu1Pz_ex2
			Theta_Nu2	= math.sqrt((X_Slope2_Nu1 + X_Slope_Ds2[i])*(X_Slope2_Nu1 + X_Slope_Ds2[i]) + (Y_Slope2_Nu1 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu1 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu2)

		return (histogram1, histogram2, X_Slope1_Nu1_v, X_Slope2_Nu1_v, Y_Slope1_Nu1_v, Y_Slope2_Nu1_v)

	else:
		histogram1 = b
		Gamma1_1 = args[3]
		Beta1_1 = args[4]
		TauPx = args[5]
		TauPy = args[6]
		TauPz = args[7]
		X_Slope_Ds1 = args[8]
		Y_Slope_Ds1 = args[9]
		for i in range(loopsize):
			Nu1Px, Nu1Py, Nu1Pz = -TauPx[i], -TauPy[i], -TauPz[i]

			Nu1Px_ex	= Nu1Px #Experimental X Dir Nu Momentum
			Nu1Py_ex	= Nu1Py #Experimental Y Dir Nu Momentum
			Nu1Pz_ex1	= Gamma1_1[i] * (Beta1_1[i] * e1_neu -Nu1Pz) #Experimental Z Dir Nu Momentum
			X_Slope1_Nu1	= Nu1Px_ex / Nu1Pz_ex1
			X_Slope1_Nu1_v.append(X_Slope1_Nu1)
			Y_Slope1_Nu1	= Nu1Py_ex / Nu1Pz_ex1
			Y_Slope1_Nu1_v.append(Y_Slope1_Nu1)
			Theta_Nu1	= math.sqrt((X_Slope1_Nu1 + X_Slope_Ds1[i])*(X_Slope1_Nu1 + X_Slope_Ds1[i]) + (Y_Slope1_Nu1 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu1 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu1) #Fill Neu emission angle Histogram

		return (histogram1, X_Slope1_Nu1_v, Y_Slope1_Nu1_v)


def Emission_Angle_Nu2HistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]
	X_Slope1_Nu2_v = []
	X_Slope2_Nu2_v = []
	X_Slope3_Nu2_v = []
	X_Slope4_Nu2_v = []
	Y_Slope1_Nu2_v = []
	Y_Slope2_Nu2_v = []
	Y_Slope3_Nu2_v = []
	Y_Slope4_Nu2_v = []

	if (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		X_Slope_Ds1 = args[3]
		X_Slope_Ds2 = args[4]
		X_Slope_Ds3 = args[5]
		X_Slope_Ds4 = args[6]
		Y_Slope_Ds1 = args[7]
		Y_Slope_Ds2 = args[8]
		Y_Slope_Ds3 = args[9]
		Y_Slope_Ds4 = args[10]
		e1_ex_tau = args[11] 
		e2_ex_tau = args[12]
		e3_ex_tau = args[13]
		e4_ex_tau = args[14]

		for i in range(loopsize):
			sim_data 	= i % sim_size # Take Momentum data points from file
			Nu2Px_ex	= px_nu2[sim_data] # Momentum in X Dir
			Nu2Py_ex	= py_nu2[sim_data] # Momentum in Y Dir
			Nu2Pz_ex1	= pz_nu2[sim_data] *e1_ex_tau[i] / 100.0 # Momentum in Z Dir
			X_Slope1_Nu2 	= Nu2Px_ex / Nu2Pz_ex1
			X_Slope1_Nu2_v.append(X_Slope1_Nu2)
			Y_Slope1_Nu2 	= Nu2Py_ex / Nu2Pz_ex1
			Y_Slope1_Nu2_v.append(Y_Slope1_Nu2)
			Theta_Nu21 	= math.sqrt((X_Slope1_Nu2 + X_Slope_Ds1[i])*(X_Slope1_Nu2 + X_Slope_Ds1[i]) + (Y_Slope1_Nu2 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu2 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu21) #Fill Neu2 emission angle Histogram

			Nu2Pz_ex2	= pz_nu2[sim_data] *e2_ex_tau[i] / 100.0
			X_Slope2_Nu2 	= Nu2Px_ex / Nu2Pz_ex2
			X_Slope2_Nu2_v.append(X_Slope2_Nu2)
			Y_Slope2_Nu2 	= Nu2Py_ex / Nu2Pz_ex2
			Y_Slope2_Nu2_v.append(Y_Slope2_Nu2)
			Theta_Nu22 	= math.sqrt((X_Slope2_Nu2 + X_Slope_Ds2[i])*(X_Slope2_Nu2 + X_Slope_Ds2[i]) + (Y_Slope2_Nu2 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu2 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu22)

			Nu2Pz_ex3	= pz_nu2[sim_data] *e3_ex_tau[i] / 100.0
			X_Slope3_Nu2 	= Nu2Px_ex / Nu2Pz_ex3
			X_Slope3_Nu2_v.append(X_Slope3_Nu2)
			Y_Slope3_Nu2 	= Nu2Py_ex / Nu2Pz_ex3
			Y_Slope3_Nu2_v.append(Y_Slope3_Nu2)
			Theta_Nu23 	= math.sqrt((X_Slope3_Nu2 + X_Slope_Ds3[i])*(X_Slope3_Nu2 + X_Slope_Ds3[i]) + (Y_Slope3_Nu2 + Y_Slope_Ds3[i]) * (Y_Slope3_Nu2 +Y_Slope_Ds3[i]))

			histogram3.Fill(Theta_Nu23)

			Nu2Pz_ex4	= pz_nu2[sim_data] *e4_ex_tau[i] / 100.0
			X_Slope4_Nu2 	= Nu2Px_ex / Nu2Pz_ex4
			X_Slope4_Nu2_v.append(X_Slope4_Nu2)
			Y_Slope4_Nu2 	= Nu2Py_ex / Nu2Pz_ex4
			Y_Slope4_Nu2_v.append(Y_Slope4_Nu2)
			Theta_Nu24 	= math.sqrt((X_Slope4_Nu2 + X_Slope_Ds4[i])*(X_Slope4_Nu2 + X_Slope_Ds4[i]) + (Y_Slope4_Nu2 + Y_Slope_Ds4[i]) * (Y_Slope4_Nu2 +Y_Slope_Ds4[i]))

			histogram4.Fill(Theta_Nu24)

		return (histogram1, histogram2, histogram3, histogram4, X_Slope1_Nu2_v, X_Slope2_Nu2_v, X_Slope3_Nu2_v, X_Slope4_Nu2_v, Y_Slope1_Nu2_v, Y_Slope2_Nu2_v, Y_Slope3_Nu2_v, Y_Slope4_Nu2_v)

	elif (len(b) == 3):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		X_Slope_Ds1 = args[3]
		X_Slope_Ds2 = args[4]
		X_Slope_Ds3 = args[5]
		Y_Slope_Ds1 = args[6]
		Y_Slope_Ds2 = args[7]
		Y_Slope_Ds3 = args[8]
		e1_ex_tau = args[9] 
		e2_ex_tau = args[10]
		e3_ex_tau = args[11]
		for i in range(loopsize):
			sim_data 	= i % sim_size # Take Momentum data points from file
			Nu2Px_ex	= px_nu2[sim_data] # Momentum in X Dir
			Nu2Py_ex	= py_nu2[sim_data] # Momentum in Y Dir
			Nu2Pz_ex1	= pz_nu2[sim_data] *e1_ex_tau[i] / 100.0 # Momentum in Z Dir
			X_Slope1_Nu2 	= Nu2Px_ex / Nu2Pz_ex1
			X_Slope1_Nu2_v.append(X_Slope1_Nu2)
			Y_Slope1_Nu2 	= Nu2Py_ex / Nu2Pz_ex1
			Y_Slope1_Nu2_v.append(Y_Slope1_Nu2)
			Theta_Nu21 	= math.sqrt((X_Slope1_Nu2 + X_Slope_Ds1[i])*(X_Slope1_Nu2 + X_Slope_Ds1[i]) + (Y_Slope1_Nu2 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu2 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu21) #Fill Neu2 emission angle Histogram

			Nu2Pz_ex2	= pz_nu2[sim_data] *e2_ex_tau[i] / 100.0
			X_Slope2_Nu2 	= Nu2Px_ex / Nu2Pz_ex2
			X_Slope2_Nu2_v.append(X_Slope2_Nu2)
			Y_Slope2_Nu2 	= Nu2Py_ex / Nu2Pz_ex2
			Y_Slope2_Nu2_v.append(Y_Slope2_Nu2)
			Theta_Nu22 	= math.sqrt((X_Slope2_Nu2 + X_Slope_Ds2[i])*(X_Slope2_Nu2 + X_Slope_Ds2[i]) + (Y_Slope2_Nu2 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu2 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu22)

			Nu2Pz_ex3	= pz_nu2[sim_data] *e3_ex_tau[i] / 100.0
			X_Slope3_Nu2 	= Nu2Px_ex / Nu2Pz_ex3
			X_Slope3_Nu2_v.append(X_Slope3_Nu2)
			Y_Slope3_Nu2 	= Nu2Py_ex / Nu2Pz_ex3
			Y_Slope3_Nu2_v.append(Y_Slope3_Nu2)
			Theta_Nu23 	= math.sqrt((X_Slope3_Nu2 + X_Slope_Ds3[i])*(X_Slope3_Nu2 + X_Slope_Ds3[i]) + (Y_Slope3_Nu2 + Y_Slope_Ds3[i]) * (Y_Slope3_Nu2 +Y_Slope_Ds3[i]))

			histogram3.Fill(Theta_Nu23)

		return (histogram1, histogram2, histogram3, X_Slope1_Nu2_v, X_Slope2_Nu2_v, X_Slope3_Nu2_v, Y_Slope1_Nu2_v, Y_Slope2_Nu2_v, Y_Slope3_Nu2_v)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1]
		X_Slope_Ds1 = args[3]
		X_Slope_Ds2 = args[4]
		Y_Slope_Ds1 = args[5]
		Y_Slope_Ds2 = args[6]
		e1_ex_tau = args[7] 
		e2_ex_tau = args[8]
		for i in range(loopsize):
			sim_data 	= i % sim_size # Take Momentum data points from file
			Nu2Px_ex	= px_nu2[sim_data] # Momentum in X Dir
			Nu2Py_ex	= py_nu2[sim_data] # Momentum in Y Dir
			Nu2Pz_ex1	= pz_nu2[sim_data] *e1_ex_tau[i] / 100.0 # Momentum in Z Dir
			X_Slope1_Nu2 	= Nu2Px_ex / Nu2Pz_ex1
			X_Slope1_Nu2_v.append(X_Slope1_Nu2)
			Y_Slope1_Nu2 	= Nu2Py_ex / Nu2Pz_ex1
			Y_Slope1_Nu2_v.append(Y_Slope1_Nu2)
			Theta_Nu21 	= math.sqrt((X_Slope1_Nu2 + X_Slope_Ds1[i])*(X_Slope1_Nu2 + X_Slope_Ds1[i]) + (Y_Slope1_Nu2 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu2 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu21) #Fill Neu2 emission angle Histogram

			Nu2Pz_ex2	= pz_nu2[sim_data] *e2_ex_tau[i] / 100.0
			X_Slope2_Nu2 	= Nu2Px_ex / Nu2Pz_ex2
			X_Slope2_Nu2_v.append(X_Slope2_Nu2)
			Y_Slope2_Nu2 	= Nu2Py_ex / Nu2Pz_ex2
			Y_Slope2_Nu2_v.append(Y_Slope2_Nu2)
			Theta_Nu22 	= math.sqrt((X_Slope2_Nu2 + X_Slope_Ds2[i])*(X_Slope2_Nu2 + X_Slope_Ds2[i]) + (Y_Slope2_Nu2 + Y_Slope_Ds2[i]) * (Y_Slope2_Nu2 +Y_Slope_Ds2[i]))

			histogram2.Fill(Theta_Nu22)

		return (histogram1, histogram2, X_Slope1_Nu2_v, X_Slope2_Nu2_v, Y_Slope1_Nu2_v, Y_Slope2_Nu2_v)

	else:
		histogram1 = b
		X_Slope_Ds1 = args[3]
		Y_Slope_Ds1 = args[4]
		e1_ex_tau = args[5]
		for i in range(loopsize):
			sim_data 	= i % sim_size # Take Momentum data points from file
			Nu2Px_ex	= px_nu2[sim_data] # Momentum in X Dir
			Nu2Py_ex	= py_nu2[sim_data] # Momentum in Y Dir
			Nu2Pz_ex1	= pz_nu2[sim_data] *e1_ex_tau[i] / 100.0 # Momentum in Z Dir
			X_Slope1_Nu2 	= Nu2Px_ex / Nu2Pz_ex1
			X_Slope1_Nu2_v.append(X_Slope1_Nu2)
			Y_Slope1_Nu2 	= Nu2Py_ex / Nu2Pz_ex1
			Y_Slope1_Nu2_v.append(Y_Slope1_Nu2)
			Theta_Nu21 	= math.sqrt((X_Slope1_Nu2 + X_Slope_Ds1[i])*(X_Slope1_Nu2 + X_Slope_Ds1[i]) + (Y_Slope1_Nu2 + Y_Slope_Ds1[i]) * (Y_Slope1_Nu2 +Y_Slope_Ds1[i]))

			histogram1.Fill(Theta_Nu21) #Fill Neu2 emission angle Histogram

		return (histogram1, X_Slope1_Nu2_v, Y_Slope1_Nu2_v)


def Kink_Angle_HistogramFiller(*args):
	a = args[0]
	b = args[1]
	loopsize = args[2]

	if (len(b) == 8):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		histogram5 = b[4]
		histogram6 = b[5]
		histogram7 = b[6]
		histogram8 = b[7]
		
		X_Slope_Tau1 = args[3]
		X_Slope_Tau2 = args[4]
		X_Slope_Tau3 = args[5]
		X_Slope_Tau4 = args[6]
		Y_Slope_Tau1 = args[7]
		Y_Slope_Tau2 = args[8]
		Y_Slope_Tau3 = args[9]
		Y_Slope_Tau4 = args[10]

		X_Slope_Nu21 = args[11]
		X_Slope_Nu22 = args[12]
		X_Slope_Nu23 = args[13]
		X_Slope_Nu24 = args[14]
		Y_Slope_Nu21 = args[15]
		Y_Slope_Nu22 = args[16]
		Y_Slope_Nu23 = args[17]
		Y_Slope_Nu24 = args[18]

		for i in range(loopsize):
			Ds_Kink_Angle1 = math.sqrt((X_Slope_Tau1[i])*(X_Slope_Tau1[i]) + (Y_Slope_Tau1[i])*(Y_Slope_Tau1[i]))
			Tau_Kink_Angle1 = math.sqrt((X_Slope_Nu21[i])*(X_Slope_Nu21[i]) + (Y_Slope_Nu21[i])*(Y_Slope_Nu21[i]))

			histogram1.Fill(Ds_Kink_Angle1) #Fill Ds kink emission angle Histogram
			histogram2.Fill(Tau_Kink_Angle1) #Fill Tau kink emission angle Histogram

			Ds_Kink_Angle2 = math.sqrt((X_Slope_Tau2[i])*(X_Slope_Tau2[i]) + (Y_Slope_Tau2[i])*(Y_Slope_Tau2[i]))
			Tau_Kink_Angle2 = math.sqrt((X_Slope_Nu22[i])*(X_Slope_Nu22[i]) + (Y_Slope_Nu22[i])*(Y_Slope_Nu22[i]))

			histogram3.Fill(Ds_Kink_Angle2)
			histogram4.Fill(Tau_Kink_Angle2)

			Ds_Kink_Angle3 = math.sqrt((X_Slope_Tau3[i])*(X_Slope_Tau3[i]) + (Y_Slope_Tau3[i])*(Y_Slope_Tau3[i]))
			Tau_Kink_Angle3 = math.sqrt((X_Slope_Nu23[i])*(X_Slope_Nu23[i]) + (Y_Slope_Nu23[i])*(Y_Slope_Nu23[i]))

			histogram5.Fill(Ds_Kink_Angle3)
			histogram6.Fill(Tau_Kink_Angle3)

			Ds_Kink_Angle4 = math.sqrt((X_Slope_Tau4[i])*(X_Slope_Tau4[i]) + (Y_Slope_Tau4[i])*(Y_Slope_Tau4[i]))
			Tau_Kink_Angle4 = math.sqrt((X_Slope_Nu24[i])*(X_Slope_Nu24[i]) + (Y_Slope_Nu24[i])*(Y_Slope_Nu24[i]))

			histogram7.Fill(Ds_Kink_Angle4)
			histogram8.Fill(Tau_Kink_Angle4)

		return (histogram1, histogram2, histogram3, histogram4, histogram5, histogram6, histogram7, histogram8)

	elif (len(b) == 6):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		histogram5 = b[4]
		histogram6 = b[5]
		
		X_Slope_Tau1 = args[3]
		X_Slope_Tau2 = args[4]
		X_Slope_Tau3 = args[5]
		Y_Slope_Tau1 = args[6]
		Y_Slope_Tau2 = args[7]
		Y_Slope_Tau3 = args[8]

		X_Slope_Nu21 = args[9]
		X_Slope_Nu22 = args[10]
		X_Slope_Nu23 = args[11]
		Y_Slope_Nu21 = args[12]
		Y_Slope_Nu22 = args[13]
		Y_Slope_Nu23 = args[14]
		for i in range(loopsize):
			Ds_Kink_Angle1 = math.sqrt((X_Slope_Tau1[i])*(X_Slope_Tau1[i]) + (Y_Slope_Tau1[i])*(Y_Slope_Tau1[i]))
			Tau_Kink_Angle1 = math.sqrt((X_Slope_Nu21[i])*(X_Slope_Nu21[i]) + (Y_Slope_Nu21[i])*(Y_Slope_Nu21[i]))

			histogram1.Fill(Ds_Kink_Angle1) #Fill Ds kink emission angle Histogram
			histogram2.Fill(Tau_Kink_Angle1) #Fill Tau kink emission angle Histogram

			Ds_Kink_Angle2 = math.sqrt((X_Slope_Tau2[i])*(X_Slope_Tau2[i]) + (Y_Slope_Tau2[i])*(Y_Slope_Tau2[i]))
			Tau_Kink_Angle2 = math.sqrt((X_Slope_Nu22[i])*(X_Slope_Nu22[i]) + (Y_Slope_Nu22[i])*(Y_Slope_Nu22[i]))

			histogram3.Fill(Ds_Kink_Angle2)
			histogram4.Fill(Tau_Kink_Angle2)

			Ds_Kink_Angle3 = math.sqrt((X_Slope_Tau3[i])*(X_Slope_Tau3[i]) + (Y_Slope_Tau3[i])*(Y_Slope_Tau3[i]))
			Tau_Kink_Angle3 = math.sqrt((X_Slope_Nu23[i])*(X_Slope_Nu23[i]) + (Y_Slope_Nu23[i])*(Y_Slope_Nu23[i]))

			histogram5.Fill(Ds_Kink_Angle3)
			histogram6.Fill(Tau_Kink_Angle3)

		return (histogram1, histogram2, histogram3, histogram4, histogram5, histogram6)

	elif (len(b) == 4):
		histogram1 = b[0]
		histogram2 = b[1]
		histogram3 = b[2]
		histogram4 = b[3]
		
		X_Slope_Tau1 = args[3]
		X_Slope_Tau2 = args[4]
		Y_Slope_Tau1 = args[5]
		Y_Slope_Tau2 = args[6]

		X_Slope_Nu21 = args[7]
		X_Slope_Nu22 = args[8]
		Y_Slope_Nu21 = args[9]
		Y_Slope_Nu22 = args[10]
		for i in range(loopsize):
			Ds_Kink_Angle1 = math.sqrt((X_Slope_Tau1[i])*(X_Slope_Tau1[i]) + (Y_Slope_Tau1[i])*(Y_Slope_Tau1[i]))
			Tau_Kink_Angle1 = math.sqrt((X_Slope_Nu21[i])*(X_Slope_Nu21[i]) + (Y_Slope_Nu21[i])*(Y_Slope_Nu21[i]))

			histogram1.Fill(Ds_Kink_Angle1) #Fill Ds kink emission angle Histogram
			histogram2.Fill(Tau_Kink_Angle1) #Fill Tau kink emission angle Histogram

			Ds_Kink_Angle2 = math.sqrt((X_Slope_Tau2[i])*(X_Slope_Tau2[i]) + (Y_Slope_Tau2[i])*(Y_Slope_Tau2[i]))
			Tau_Kink_Angle2 = math.sqrt((X_Slope_Nu22[i])*(X_Slope_Nu22[i]) + (Y_Slope_Nu22[i])*(Y_Slope_Nu22[i]))

			histogram3.Fill(Ds_Kink_Angle2)
			histogram4.Fill(Tau_Kink_Angle2)

		return (histogram1, histogram2, histogram3, histogram4)

	elif (len(b) == 2):
		histogram1 = b[0]
		histogram2 = b[1]
		
		X_Slope_Tau1 = args[3]
		Y_Slope_Tau1 = args[4]

		X_Slope_Nu21 = args[5]
		Y_Slope_Nu21 = args[6]
		for i in range(loopsize):
			Ds_Kink_Angle1 = math.sqrt((X_Slope_Tau1[i])*(X_Slope_Tau1[i]) + (Y_Slope_Tau1[i])*(Y_Slope_Tau1[i]))
			Tau_Kink_Angle1 = math.sqrt((X_Slope_Nu21[i])*(X_Slope_Nu21[i]) + (Y_Slope_Nu21[i])*(Y_Slope_Nu21[i]))

			histogram1.Fill(Ds_Kink_Angle1) #Fill Ds kink emission angle Histogram
			histogram2.Fill(Tau_Kink_Angle1) #Fill Tau kink emission angle Histogram

		return (histogram1, histogram2)


def HistogramDrawer(*args):
	if (len(args)==5):
		histogram1 = args[0]
		histogram2 = args[1]
		histogram3 = args[2]
		histogram4 = args[3]
		X_title = args[4]
		histogram1.SetXTitle(X_title)
		histogram1.SetYTitle('Entries')
		histogram1.SetMinimum(0.0)
		histogram1.SetFillColorAlpha(kBlue, 0.10)
		histogram1.Draw()
		histogram2.SetFillColorAlpha(kRed, 0.10)
		histogram2.Draw("same")
		histogram3.SetFillColorAlpha(kYellow, 0.10)
		histogram3.Draw("same")
		histogram4.SetFillColorAlpha(kPink, 0.10)	
		histogram4.Draw("same")
		return (histogram1, histogram2, histogram3, histogram4)

	elif (len(args)==4):
		histogram1 = args[0]
		histogram2 = args[1]
		histogram3 = args[2]
		X_title = args[3]
		histogram1.SetXTitle(X_title)
		histogram1.SetYTitle('Entries')
		histogram1.SetMinimum(0.0)
		histogram1.SetFillColorAlpha(kBlue, 0.10)
		histogram1.Draw()
		histogram2.SetFillColorAlpha(kRed, 0.10)
		histogram2.Draw("same")
		histogram3.SetFillColorAlpha(kYellow, 0.10)
		histogram3.Draw("same")
		return (histogram1, histogram2, histogram3)

	elif (len(args)==3):
		histogram1 = args[0]
		histogram2 = args[1]
		X_title = args[2]
		histogram1.SetXTitle(X_title)
		histogram1.SetYTitle('Entries')
		histogram1.SetMinimum(0.0)
		histogram1.SetFillColorAlpha(kBlue, 0.10)
		histogram1.Draw()
		histogram2.SetFillColorAlpha(kRed, 0.10)
		histogram2.Draw("same")
		return (histogram1, histogram2)
		
	elif (len(args)==2):
		histogram1 = args[0]
		X_title = args[1]
		histogram1.SetXTitle(X_title)
		histogram1.SetYTitle('Entries')
		histogram1.SetMinimum(0.0)
		histogram1.SetFillColorAlpha(kBlue, 0.10)
		histogram1.Draw()
		return histogram1


def LegendDrawer(*args):
	if (args[len(args)-1] == "y"):
		if (len(args)==8):
			histogram1 = args[0]
			histogram2 = args[1]
			histogram3 = args[2]
			histogram4 = args[3]
			a = args[4]
			legend = args[5]
			name = args[6]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"n = %s" %a[0],"f")
			legend.AddEntry(histogram2,"n = %s" %a[1],"f")
			legend.AddEntry(histogram3,"n = %s" %a[2],"f")
			legend.AddEntry(histogram4,"n = %s" %a[3],"f")
			legend.Draw()

		elif (len(args)==7):
			histogram1 = args[0]
			histogram2 = args[1]
			histogram3 = args[2]
			a = args[3]
			legend = args[4]
			name = args[5]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"n = %s" %a[0],"f")
			legend.AddEntry(histogram2,"n = %s" %a[1],"f")
			legend.AddEntry(histogram3,"n = %s" %a[2],"f")
			legend.Draw()

		elif (len(args)==6):
			histogram1 = args[0]
			histogram2 = args[1]
			a = args[2]
			legend = args[3]
			name = args[4]
			legend.SetHeader(name,"C") # Legend title
			if (len(a) == 2):
				legend.AddEntry(histogram1,"n = %s" %a[0],"f")
				legend.AddEntry(histogram2,"n = %s" %a[1],"f")
			else:
				legend.AddEntry(histogram1,"n = %s" %a,"f")
				legend.AddEntry(histogram2,"n = %s" %a,"f")
			legend.Draw()
			
		elif (len(args)==5):
			histogram1 = args[0]
			a = args[1]
			legend = args[2]
			name = args[3]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"n = %s" %a,"f")
			legend.Draw


def DoubleLegendDrawer(*args):
	if (args[len(args)-1] == "y"):
		if (len(args)==9):
			histogram1 = args[0]
			histogram2 = args[1]
			histogram3 = args[2]
			histogram4 = args[3]
			a = args[4]
			b = args[5]
			legend = args[6]
			name = args[7]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"N = %s and B = %s" %(a[0], b[0]),"f")
			legend.AddEntry(histogram2,"N = %s and B = %s" %(a[1], b[1]),"f")
			legend.AddEntry(histogram3,"N = %s and B = %s" %(a[2], b[2]),"f")
			legend.AddEntry(histogram4,"N = %s and B = %s" %(a[3], b[3]),"f")
			legend.Draw()

		elif (len(args)==8):
			histogram1 = args[0]
			histogram2 = args[1]
			histogram3 = args[2]
			a = args[3]
			b = args[4]
			legend = args[5]
			name = args[6]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"N = %s and B = %s" %(a[0], b[0]),"f")
			legend.AddEntry(histogram2,"N = %s and B = %s" %(a[1], b[1]),"f")
			legend.AddEntry(histogram3,"N = %s and B = %s" %(a[2], b[2]),"f")
			legend.Draw()

		elif (len(args)==7):
			histogram1 = args[0]
			histogram2 = args[1]
			a = args[2]
			b = args[3]
			legend = args[4]
			name = args[5]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"N = %s and B = %s" %(a[0], b[0]),"f")
			legend.AddEntry(histogram2,"N = %s and B = %s" %(a[1], b[1]),"f")
			legend.Draw()

		elif (len(args)==6):
			histogram1 = args[0]
			a = args[1]
			b = args[2]
			legend = args[3]
			name = args[4]
			legend.SetHeader(name,"C") # Legend title
			legend.AddEntry(histogram1,"N = %s and B = %s" %(a, b),"f")
			legend.Draw()

def KinkLegendDrawer(*args):
	if (args[len(args)-1] == "y"):
		histogram1 = args[0]
		histogram2 = args[1]
		a = args[2]
		b = args[3]
		legend = args[4]
		name = args[5]
		legend.SetHeader(name,"C") # Legend title
		legend.AddEntry(histogram1,"N = %s and B = %s" %(a, b),"f")
		legend.Draw()



Ene 	= 800
m  	= 0.938 #nucleon mass GeV/c2
mc 	= 1.968 #Ds mass GeV/c2
S  	= math.sqrt(2*m*Ene) #Center of mass system energy
gamma 	= Ene/S #Gamma factor for center of mass system
beta 	= math.sqrt(1.0-1.0/(gamma*gamma))

#Ds->tau + n_tau
m_tau = 1.777
p1 = 0.182

e1_tau= math.sqrt(m_tau*m_tau + p1*p1)
e1_neu= math.sqrt(p1*p1)

#Extract Neutrino momentum values###############
f=open("nu_tau_mom.100GeV_tau_decay.dat","r")
lines=f.readlines()
px_nu2=[]
py_nu2=[]
pz_nu2=[]
for x in lines:
    	px_nu2.append(x.split()[3])
	py_nu2.append(x.split()[4])
	pz_nu2.append(x.split()[5])
f.close()

px_nu2 = map(float, px_nu2)
py_nu2 = map(float, py_nu2)
pz_nu2 = map(float, pz_nu2)

sim_size	= np.size(px_nu2)

##################################################
