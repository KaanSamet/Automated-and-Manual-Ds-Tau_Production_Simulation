#author Kaan Samet GULER

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

def p1Getter(rand,p1): #p1 Generator
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

c1 = TCanvas( 'c1', 'canvas title', 20, 20, 1000, 500)
f = TFile( 'my_output.root', 'recreate')

rand = TRandom3()
rand.SetSeed()
u = 6.1

b_inp = 0.8
n_inp = 5
n_sample = 40000000

E_beam = 800

Pt = math.sqrt(1.0/(2.0*b_inp))
#Ps sigma for projection case of b=b_inp
Ps = math.sqrt(1.0/(2.0*b_inp))
P0 = n_sample*0.1
P1 = n_inp

Ene 	= E_beam #Variables for pz
m  	= 0.938 #nucleon mass GeV/c2
mc 	= 1.968 #Ds mass GeV/c2
S  	= math.sqrt(2*m*Ene) #Center of mass system energy
p  	= math.sqrt((S/2)*(S/2)-mc*mc) #Momentum at center of mass system
gamma 	= Ene/S #Gamma factor for center of mass system
beta 	= math.sqrt(1.0-1.0/(gamma*gamma))

#Ds->tau + n_tau
m_tau = 1.777
p1 = 0.182

e1_tau= math.sqrt(m_tau*m_tau + p1*p1)
e1_neu= math.sqrt(p1*p1)

#Define the storable variables
xf_v = []
ptx_v = []
pty_v = []
pt2_v = []
pz_v = []
e_v = []
e_ex_v = []
ax_v = []
ay_v = []
gamma1_v = []
beta1_v = []
p1x_v = []
p1y_v = []
p1z_v = []
ax1_tau_v = []
ay1_tau_v = []
ax1_neu_v = []
ay1_neu_v = []


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

Theta_n2  = TH1F("Theta_n2","Emission angle #theta of #nu2",100,  0.0, 0.2)

ax2_neu_v = []
ay2_neu_v = []
##################################################

XFhistogram = TH1F('XF', "XF of Ds", 100, -1, 1) # XF Histogram
fit = TF1("Fit","[0]*pow((1.-sqrt(x*x)),[1])",-1,1) #XF fit function
PTXhistogram = TH1F("PTX","PTX of Ds",100, -3, 3) # ptx Histogram
PTSQhistogram = TH1F("PT^{2}","PT^{2} of Ds",100, 0, 6) # pt^2 Histogram
PZhistogram = TH1F("PZ","PZ of Ds",100, -10, 10) # pz Histogram
Theta = TH1F("#theta of Ds","Emission angle #theta of Ds",100, 0.0, 0.2) # Ds emission angle Histogram
Theta_tau = TH1F("#theta of #tau","Emission angle #theta of #tau",100,  0.0, 0.2) # Tau emission angle Histogram
Theta_n1  = TH1F("#theta of #nu1","Emission angle #theta of #nu1",100,  0.0, 0.2) # Neutrino emission angle Histogram
Theta_n2  = TH1F("#theta of #nu2","Emission angle #theta of #nu2",100,  0.0, 0.2) # Neutrino2 emission angle Histogram
dsand_kink = TH1F("#theta of Ds","Kink angle #theta of Ds and #tau",100, 0.0, 0.20) # Ds kink angle Histogram
tauand_kink = TH1F("#theta of #tau","Kink angle #theta of #tau",100, 0.0, 0.20) # Tau kink angle Histogram


for i in range(1000000):
	xf 		= XFGen(rand,u)
	xf_v.append(xf)
	XFhistogram.Fill(xf) #Fill XF Histogram #####################
	ptx, pty 	= ptGetter(rand,Pt)
	ptx_v.append(ptx)
	pty_v.append(pty)
	PTXhistogram.Fill(ptx) #Fill ptx Histogram #####################
	pt2 = ptx_v[i]*ptx_v[i] + pty_v[i]*pty_v[i]
	pt2_v.append(pt2)
	PTSQhistogram.Fill(pt2) #Fill pt2 Histogram #####################
	pz  		= p*xf_v[i] #(Ds momentum for z direction)
	pz_v.append(pz)
	e 		= math.sqrt(mc*mc+pt2_v[i]+pz*pz) #(Ds energy in CMS)
	e_v.append(e)
	e_ex 		= gamma * (e + beta*pz)
	e_ex_v.append(e_ex)
	PZhistogram.Fill(pz) #Fill pz Histogram #####################
	pz_ex 		= gamma * (beta*e_v[i] + pz_v[i])
	ax 		= ptx_v[i] / pz_ex
	ax_v.append(ax)
	ay 		= pty_v[i] / pz_ex
	ay_v.append(ay)
	th 		= math.sqrt(ax*ax + ay*ay)
	gamma1 		= e_ex_v[i] /mc #Ds's gamma factor
	gamma1_v.append(gamma1)
	beta1 		= math.sqrt(1.0-1.0/(gamma1*gamma1))
	beta1_v.append(beta1)
	Theta.Fill(th) #Fill Ds emission angle Histogram #####################
	p1x,p1y,p1z 	= p1Getter(rand,p1)
	p1x_v.append(p1x)
	p1y_v.append(p1y)
	p1z_v.append(p1z)
	p1x_ex_tau 	= p1x
	p1y_ex_tau 	= p1y
	p1z_ex_tau 	= gamma1_v[i] * (beta1_v[i] * e1_tau + p1z)
	ax1_tau 	= p1x_ex_tau / p1z_ex_tau
	ax1_tau_v.append(ax1_tau)
	ay1_tau 	= p1y_ex_tau / p1z_ex_tau
	ay1_tau_v.append(ay1_tau)
	th_tau 		= math.sqrt((ax1_tau + ax_v[i])*(ax1_tau + ax_v[i]) + (ay1_tau + ay_v[i]) * (ay1_tau +ay_v[i]))
	Theta_tau.Fill(th_tau) #Fill Tau emission angle Histogram #####################
	p1x_ex_neu 	= -p1x_v[i]
	p1y_ex_neu 	= -p1y_v[i]
	p1z_ex_neu 	= gamma1_v[i] * (beta1_v[i] * e1_neu	-p1z_v[i])
	ax1_neu 	= p1x_ex_neu / p1z_ex_neu
	ax1_neu_v.append(ax1_neu)
	ay1_neu 	= p1y_ex_neu / p1z_ex_neu
	ay1_neu_v.append(ay1_neu)
	th_n1   	= math.sqrt((ax1_neu + ax_v[i])*(ax1_neu + ax_v[i]) + (ay1_neu + ay_v[i])*(ay1_neu + ay_v[i]))
	Theta_n1.Fill(th_n1) #Fill Neu emission angle Histogram #####################
	e1_ex_tau 	= gamma1_v[i] *(e1_tau + beta1_v[i] *p1z_v[i])
	sim_data 	= i % sim_size#
	p2x_ex_neu	= px_nu2[sim_data]
	p2y_ex_neu	= py_nu2[sim_data]
	p2z_ex_neu	= pz_nu2[sim_data] *e1_ex_tau / 100.0
	ax2_neu 	= p2x_ex_neu / p2z_ex_neu
	ax2_neu_v.append(ax2_neu)
	ay2_neu 	= p2y_ex_neu / p2z_ex_neu#
	ay2_neu_v.append(ay2_neu)
	th_n2 		= math.sqrt((ax2_neu + ax_v[i] + ax1_tau_v[i]) * (ax2_neu + ax_v[i] + ax1_tau_v[i]) + (ay2_neu + ay_v[i] + ay1_tau_v[i]) * (ay2_neu + ay_v[i] + ay1_tau_v[i]))
	Theta_n2.Fill(th_n2) #Fill Neu2 emission angle Histogram #####################
	kinkds = math.sqrt((ax1_tau_v[i])*(ax1_tau_v[i]) + (ay1_tau_v[i])*(ay1_tau_v[i]))
	dsand_kink.Fill(kinkds) #Fill Ds kink angle Histogram #####################
	kinktau = math.sqrt((ax2_neu_v[i])*(ax2_neu_v[i]) + (ay2_neu_v[i])*(ay2_neu_v[i]))
	tauand_kink.Fill(kinktau) #Fill Tau kink angle Histogram #####################



c1.Divide(2,2)

c1.cd(1)

gStyle.SetOptFit(1111)
gStyle.SetStatH(0.1)
gStyle.SetStatW(0.2)
gStyle.SetStatFontSize(0.05)

XFhistogram.SetXTitle('XF')
XFhistogram.SetYTitle('Entries')
XFhistogram.SetMinimum(0.0)
XFhistogram.SetFillColor(5)
XFhistogram.Draw()
XFhistogram.Fit("Fit")

c1.cd(2)

PTXhistogram.SetXTitle("Pt_x (GeV/c)")
PTXhistogram.SetYTitle("Entries")
PTXhistogram.SetMinimum(0.0)
PTXhistogram.SetFillColor(5)
PTXhistogram.Draw()

c1.cd(3)

PTSQhistogram.SetXTitle("Pt^{2} (GeV^{2}/c^{2})")
PTSQhistogram.SetYTitle("Entries")
PTSQhistogram.SetMinimum(0.0)
PTSQhistogram.SetFillColor(5)
PTSQhistogram.Draw()
PTSQhistogram.Fit("expo")

c1.cd(4)

PZhistogram.SetXTitle("CMS Pz (GeV/c)")
PZhistogram.SetYTitle("Entries")
PZhistogram.SetMinimum(0.0)
PZhistogram.SetFillColor(5)
PZhistogram.Draw()

c1.Print("phys400.pdf(")
c1.Clear()
c1.Update()

c1.Divide(2,2)

c1.cd(1)

Theta.SetXTitle("#theta (rad)")
Theta.SetYTitle("Entries")
Theta.SetMinimum(0.0)
Theta.SetFillColor(5)
Theta.Draw()

c1.cd(2)

Theta_tau.SetXTitle("#theta (rad)")
Theta_tau.SetYTitle("Entries")
Theta_tau.SetMinimum(0.0)
Theta_tau.SetFillColor(5)
Theta_tau.Draw()

c1.cd(3)

Theta_n1.SetXTitle("#theta (rad)")
Theta_n1.SetYTitle("Entries")
Theta_n1.SetMinimum(0.0)
Theta_n1.SetFillColor(5)
Theta_n1.Draw()

c1.cd(4)

Theta_n2.SetXTitle("#theta (rad)")
Theta_n2.SetYTitle("Entries")
Theta_n2.SetMinimum(0.0)
Theta_n2.SetFillColor(5)
Theta_n2.Draw()

c1.Print("phys400.pdf")
c1.Clear()
c1.Update()

c1.cd(1)

gStyle.SetOptStat(0)

dsand_kink.SetXTitle("kink angle #theta (rad)")
dsand_kink.SetYTitle("Entries")
dsand_kink.SetMinimum(0.0)
dsand_kink.SetFillColorAlpha(kYellow, 0.45)
dsand_kink.Draw()

tauand_kink.SetXTitle("kink angle #theta (rad)")
tauand_kink.SetYTitle("Entries")
tauand_kink.SetMinimum(0.0)
tauand_kink.SetFillColorAlpha(kBlue, 0.25)
tauand_kink.Draw("same")

legend = TLegend(0.7,0.7,0.9,0.9)
legend.SetHeader("Kink Angles","C")
legend.AddEntry("#theta of Ds","Ds kink #theta","f")
legend.AddEntry("#theta of #tau","#tau kink #theta","f")
legend.Draw()


c1.Print("phys400.pdf)") #Print
c1.Clear()
c1.Update()
