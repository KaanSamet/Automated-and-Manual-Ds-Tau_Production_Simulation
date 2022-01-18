from ROOT import *
import math
import numpy as np
import MyFunctions

#################
f = TFile( 'my_output.root', 'recreate')

rand = TRandom3()
rand.SetSeed()

a = MyFunctions.GreetandtakeNinput() # Greets the user and takes a n input as a list.
b = MyFunctions.GreetandtakeBinput()

c1 = TCanvas( 'c1', 'canvas title', 20, 20, 1000, 500) # Opens the canvas

entries = 1000000

E_beam = 800

n_sample = 40000000
P0 = n_sample*0.1
#P1 = n_inp

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

#################
#Histogram opener parameters
XF_Histogram_Name = "XF of Ds"
XF_has_legend = "y"
XF_XTitle = "XF"
XF_Legend_Name = "N values"
XF_le = -1
XF_re = 1

PTX_Histogram_Name = "PTX of Ds"
PTX_has_legend = "y"
PTX_XTitle = "Pt_x (GeV/c)"
PTX_Legend_Name = "B values"
PTX_le = -3
PTX_re = 3

PTSQ_Histogram_Name = "PT^{2} of Ds"
PTSQ_has_legend = "y"
PTSQ_XTitle = "Pt^{2} (GeV^{2}/c^{2})"
PTSQ_Legend_Name = "B values"
PTSQ_le = 0
PTSQ_re = 6

PTZ_Histogram_Name = "PZ of Ds"
PTZ_has_legend = "y"
PTZ_XTitle = "Pt^{2} (GeV^{2}/c^{2})"
PTZ_Legend_Name = "N values"
PTZ_le = -10
PTZ_re = 10

Emission_Angle_Ds_Histogram_Name = "Emission angle #theta of Ds"
Emission_Angle_Ds_has_legend = "y"
Emission_Angle_Ds_XTitle = "#theta (rad)"
Emission_Angle_Ds_Legend_Name = "Values"
Emission_Angle_Ds_le = 0.0
Emission_Angle_Ds_re = 0.2

Emission_Angle_Tau_Histogram_Name = "Emission angle #theta of #tau"
Emission_Angle_Tau_has_legend = "y"
Emission_Angle_Tau_XTitle = "#theta (rad)"
Emission_Angle_Tau_Legend_Name = "Values"
Emission_Angle_Tau_le = 0.0
Emission_Angle_Tau_re = 0.2

Emission_Angle_Nu1_Histogram_Name = "Emission angle #theta of #nu1"
Emission_Angle_Nu1_has_legend = "y"
Emission_Angle_Nu1_XTitle = "#theta (rad)"
Emission_Angle_Nu1_Legend_Name = "Values"
Emission_Angle_Nu1_le = 0.0
Emission_Angle_Nu1_re = 0.2

Emission_Angle_Nu2_Histogram_Name = "Emission angle #theta of #nu2"
Emission_Angle_Nu2_has_legend = "y"
Emission_Angle_Nu2_XTitle = "#theta (rad)"
Emission_Angle_Nu2_Legend_Name = "Values"
Emission_Angle_Nu2_le = 0.0
Emission_Angle_Nu2_re = 0.2

Kink_Angle_Histogram_Name = "Kink angle #theta of Ds and #tau"
Kink_Angle_has_legend = "y"
Kink_Angle_XTitle = "#theta (rad)"
Kink_Angle_Legend_Name = "Values"
Kink_Angle_le = 0.0
Kink_Angle_re = 0.1


# First Step : Opens the required amount of histograms using entered input count. Name changes the histogram name, le is the left end and re is the right end of the histogram. All histograms are opened here and stored as objects.
XF_Histograms = MyFunctions.HistogramOpener(len(a), XF_Histogram_Name, XF_le, XF_re) #XF Histogram
fit1 = TF1("fit_XF","[0]*pow((1.-sqrt(x*x)),[1])",-1,1) #XF fit function

PTX_Histograms = MyFunctions.HistogramOpener(len(b), PTX_Histogram_Name, PTX_le, PTX_re) #PTX Histogram

PTSQ_Histograms = MyFunctions.HistogramOpener(len(b), PTSQ_Histogram_Name, PTSQ_le, PTSQ_re) #PTSQ Histogram

PTZ_Histograms = MyFunctions.HistogramOpener(len(a), PTZ_Histogram_Name, PTZ_le, PTZ_re) #PTZ Histogram

Emission_Angle_Ds_Histograms = MyFunctions.HistogramOpener(len(a), Emission_Angle_Ds_Histogram_Name, Emission_Angle_Ds_le, Emission_Angle_Ds_re) #Theta Ds

Emission_Angle_Tau_Histograms = MyFunctions.HistogramOpener(len(a), Emission_Angle_Tau_Histogram_Name, Emission_Angle_Tau_le, Emission_Angle_Tau_re) #Theta Tau

Emission_Angle_Nu1_Histograms = MyFunctions.HistogramOpener(len(a), Emission_Angle_Nu1_Histogram_Name, Emission_Angle_Nu1_le, Emission_Angle_Nu1_re) #Theta Nu1

Emission_Angle_Nu2_Histograms = MyFunctions.HistogramOpener(len(a), Emission_Angle_Nu2_Histogram_Name, Emission_Angle_Nu2_le, Emission_Angle_Nu2_re) #Theta Nu2

Kink_Angle_Histograms = MyFunctions.HistogramOpener(2*len(a), Kink_Angle_Histogram_Name, Kink_Angle_le, Kink_Angle_re) #Theta Kink


# Fills the histogram with input values and accepts the corresponding histograms and parameters. Then, returns filled histograms.
print("Filling the XF Graph... Thank you for waiting...")
XF_Filled_Histograms = MyFunctions.XFHistogramFiller(a, XF_Histograms, rand, entries) # Fills the XF histogram with the required calculations of the XF value.
print("Filling the PTX Graph... Thank you for waiting...")
PTX_Filled_Histograms = MyFunctions.PTXHistogramFiller(b, PTX_Histograms, rand, entries) # Fills the PTX histogram with the required calculations of the PTX value.

c1.Divide(2,2)

# Draw XF Graphs
c1.cd(1)

#Arange Canvas
#gStyle.SetOptStat(0)
gStyle.SetOptFit(1111)
gStyle.SetStatH(0.1)
gStyle.SetStatW(0.2)
gStyle.SetStatFontSize(0.05)
legend1 = TLegend(0.1,0.6,0.3,0.9)
#Fills the XF histograms with the calculated XF values, returns the needed values and stores them as vectors.
if (len(XF_Filled_Histograms)==2):
	XF_Drawn_Histograms = MyFunctions.HistogramDrawer(XF_Filled_Histograms[0], XF_XTitle)
	XF_1 = XF_Filled_Histograms[1]

elif (len(XF_Filled_Histograms)==4):
	XF_Drawn_Histograms = MyFunctions.HistogramDrawer(XF_Filled_Histograms[0], XF_Filled_Histograms[1], XF_XTitle)
	XF_1 = XF_Filled_Histograms[2]
	XF_2 = XF_Filled_Histograms[3]
		
elif (len(XF_Filled_Histograms)==6):
	XF_Drawn_Histograms = MyFunctions.HistogramDrawer(XF_Filled_Histograms[0], XF_Filled_Histograms[1], XF_Filled_Histograms[2], XF_XTitle)
	XF_1 = XF_Filled_Histograms[3]
	XF_2 = XF_Filled_Histograms[4]
	XF_3 = XF_Filled_Histograms[5]

elif (len(XF_Filled_Histograms)==8):
	XF_Drawn_Histograms = MyFunctions.HistogramDrawer(XF_Filled_Histograms[0], XF_Filled_Histograms[1], XF_Filled_Histograms[2], XF_Filled_Histograms[3], XF_XTitle)
	XF_1 = XF_Filled_Histograms[4]
	XF_2 = XF_Filled_Histograms[5]
	XF_3 = XF_Filled_Histograms[6]
	XF_4 = XF_Filled_Histograms[7]

#Fit line of XF Graph
if (len(XF_Filled_Histograms)==1) :
	XFhistogram1 = XF_Filled_Histograms
else:
	XFhistogram1 = XF_Filled_Histograms[0]
XFhistogram1.Fit("fit_XF")
legend1.AddEntry("fit_XF","Fit line of n = %s" %a[0],"l")
#End of Fit line of XF Graph

# Seperates the drawn histogram object to histograms and draws them
if (len(XF_Drawn_Histograms)==2):
	MyFunctions.LegendDrawer(XF_Drawn_Histograms[0], XF_Drawn_Histograms[1], a, legend1, XF_Legend_Name, XF_has_legend)
elif (len(XF_Drawn_Histograms)==3):
	MyFunctions.LegendDrawer(XF_Drawn_Histograms[0], XF_Drawn_Histograms[1], XF_Drawn_Histograms[2], a, legend1, XF_Legend_Name, XF_has_legend)
elif (len(XF_Drawn_Histograms)==4):
	MyFunctions.LegendDrawer(XF_Drawn_Histograms[0], XF_Drawn_Histograms[1], XF_Drawn_Histograms[2], XF_Drawn_Histograms[3], a, legend1, XF_Legend_Name, XF_has_legend)
else:
	MyFunctions.LegendDrawer(XF_Drawn_Histograms, a, legend1, XF_Legend_Name, XF_has_legend)
#End of Draw XF Graphs

#Draw PTX Graphs
c1.cd(2)
legend2 = TLegend(0.1,0.6,0.3,0.9)

if (len(PTX_Filled_Histograms)==3):
	PTX_Drawn_Histograms = MyFunctions.HistogramDrawer(PTX_Filled_Histograms[0], PTX_XTitle)
	PTX_1 = PTX_Filled_Histograms[1]
	PTY_1 = PTX_Filled_Histograms[2]

elif (len(PTX_Filled_Histograms)==6):
	PTX_Drawn_Histograms = MyFunctions.HistogramDrawer(PTX_Filled_Histograms[0], PTX_Filled_Histograms[1], PTX_XTitle)
	PTX_1 = PTX_Filled_Histograms[2]
	PTX_2 = PTX_Filled_Histograms[3]
	PTY_1 = PTX_Filled_Histograms[4]
	PTY_2 = PTX_Filled_Histograms[5]

elif (len(PTX_Filled_Histograms)==9):
	PTX_Drawn_Histograms = MyFunctions.HistogramDrawer(PTX_Filled_Histograms[0], PTX_Filled_Histograms[1], PTX_Filled_Histograms[2], PTX_XTitle)
	PTX_1 = PTX_Filled_Histograms[3]
	PTX_2 = PTX_Filled_Histograms[4]
	PTX_3 = PTX_Filled_Histograms[5]
	PTY_1 = PTX_Filled_Histograms[6]
	PTY_2 = PTX_Filled_Histograms[7]
	PTY_3 = PTX_Filled_Histograms[8]

elif (len(PTX_Filled_Histograms)==12):
	PTX_Drawn_Histograms = MyFunctions.HistogramDrawer(PTX_Filled_Histograms[0], PTX_Filled_Histograms[1], PTX_Filled_Histograms[2], PTX_Filled_Histograms[3], PTX_XTitle)
	PTX_1 = PTX_Filled_Histograms[4]
	PTX_2 = PTX_Filled_Histograms[5]
	PTX_3 = PTX_Filled_Histograms[6]
	PTX_4 = PTX_Filled_Histograms[7]
	PTY_1 = PTX_Filled_Histograms[8]
	PTY_2 = PTX_Filled_Histograms[9]
	PTY_3 = PTX_Filled_Histograms[10]
	PTY_4 = PTX_Filled_Histograms[11]


if (len(PTX_Drawn_Histograms)==2):
	MyFunctions.LegendDrawer(PTX_Drawn_Histograms[0], PTX_Drawn_Histograms[1], b, legend2, PTX_Legend_Name, PTX_has_legend)
elif (len(PTX_Drawn_Histograms)==3):
	MyFunctions.LegendDrawer(PTX_Drawn_Histograms[0], PTX_Drawn_Histograms[1], PTX_Drawn_Histograms[2], b, legend2, PTX_Legend_Name, PTX_has_legend)
elif (len(PTX_Drawn_Histograms)==4):
	MyFunctions.LegendDrawer(PTX_Drawn_Histograms[0], PTX_Drawn_Histograms[1], PTX_Drawn_Histograms[2], PTX_Drawn_Histograms[3], b, legend2, PTX_Legend_Name, PTX_has_legend)
else:
	MyFunctions.LegendDrawer(PTX_Drawn_Histograms, b, legend2, PTX_Legend_Name, PTX_has_legend)
# End of Draw PTX Graphs

# PTSQ histogram filler
print("Filling the PTSQ Graph... Thank you for waiting...")
if (len(PTSQ_Histograms) == 4):
	PTSQ_Filled_Histograms = MyFunctions.PTSQHistogramFiller(b, PTSQ_Histograms, entries, PTX_1, PTY_1, PTX_2, PTY_2, PTX_3, PTY_3, PTX_4, PTY_4)
elif (len(PTSQ_Histograms) == 3):
	PTSQ_Filled_Histograms = MyFunctions.PTSQHistogramFiller(b, PTSQ_Histograms, entries, PTX_1, PTY_1, PTX_2, PTY_2, PTX_3, PTY_3)
elif (len(PTSQ_Histograms) == 2):
	PTSQ_Filled_Histograms = MyFunctions.PTSQHistogramFiller(b, PTSQ_Histograms, entries, PTX_1, PTY_1, PTX_2, PTY_2)
else:
	PTSQ_Filled_Histograms = MyFunctions.PTSQHistogramFiller(b, PTSQ_Histograms, entries, PTX_1, PTY_1)


# Draw PTSQ Graphs
c1.cd(3)
legend3 = TLegend(0.3,0.6,0.6,0.9)

if (len(PTSQ_Filled_Histograms)==2):
	PTSQ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTSQ_Filled_Histograms[0], PTSQ_XTitle)
	PTSQ_1 = PTSQ_Filled_Histograms[1]

elif (len(PTSQ_Filled_Histograms)==4):
	PTSQ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTSQ_Filled_Histograms[0], PTSQ_Filled_Histograms[1], PTSQ_XTitle)
	PTSQ_1 = PTSQ_Filled_Histograms[2]
	PTSQ_2 = PTSQ_Filled_Histograms[3]

elif (len(PTSQ_Filled_Histograms)==6):
	PTSQ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTSQ_Filled_Histograms[0], PTSQ_Filled_Histograms[1], PTSQ_Filled_Histograms[2], PTSQ_XTitle)
	PTSQ_1 = PTSQ_Filled_Histograms[3]
	PTSQ_2 = PTSQ_Filled_Histograms[4]
	PTSQ_3 = PTSQ_Filled_Histograms[5]

elif (len(PTSQ_Filled_Histograms)==8):
	PTSQ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTSQ_Filled_Histograms[0], PTSQ_Filled_Histograms[1], PTSQ_Filled_Histograms[2], PTSQ_Filled_Histograms[3], PTSQ_XTitle)
	PTSQ_1 = PTSQ_Filled_Histograms[4]
	PTSQ_2 = PTSQ_Filled_Histograms[5]
	PTSQ_3 = PTSQ_Filled_Histograms[6]
	PTSQ_4 = PTSQ_Filled_Histograms[7]


if (len(PTSQ_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(PTSQ_Drawn_Histograms[0], PTSQ_Drawn_Histograms[1], a, b, legend3, PTSQ_Legend_Name, PTSQ_has_legend)
elif (len(PTSQ_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(PTSQ_Drawn_Histograms[0], PTSQ_Drawn_Histograms[1], PTSQ_Drawn_Histograms[2], a, b, legend3, PTSQ_Legend_Name, PTSQ_has_legend)
elif (len(PTSQ_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(PTSQ_Drawn_Histograms[0], PTSQ_Drawn_Histograms[1], PTSQ_Drawn_Histograms[2], PTSQ_Drawn_Histograms[3], a, b, legend3, PTSQ_Legend_Name, PTSQ_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(PTSQ_Drawn_Histograms, a, b, legend3, PTSQ_Legend_Name, PTSQ_has_legend)

PTSQhistogram1 = PTSQ_Filled_Histograms[0]
PTSQhistogram1.Fit("fit_PTSQ")
legend3.AddEntry("fit_PTSQ","Expo. Fit line","l")
PTSQhistogram1.Fit("expo")
# End of Draw PTSQ Graphs

#PTZ Histogram Filler
print("Filling the PTZ Graph... Thank you for waiting...")
if (len(PTZ_Histograms) == 4):
	PTZ_Filled_Histograms = MyFunctions.PTZHistogramFiller(a, PTZ_Histograms, entries, p, XF_1, XF_2, XF_3, XF_4, PTSQ_1, PTSQ_2, PTSQ_3, PTSQ_4)
elif (len(PTZ_Histograms) == 3):
	PTZ_Filled_Histograms = MyFunctions.PTZHistogramFiller(a, PTZ_Histograms, entries, p, XF_1, XF_2, XF_3, PTSQ_1, PTSQ_2, PTSQ_3)
elif (len(PTZ_Histograms) == 2):
	PTZ_Filled_Histograms = MyFunctions.PTZHistogramFiller(a, PTZ_Histograms, entries, p, XF_1, XF_2, PTSQ_1, PTSQ_2)
else:
	PTZ_Filled_Histograms = MyFunctions.PTZHistogramFiller(a, PTZ_Histograms, entries, p, XF_1, PTSQ_1)


# Draw PTZ Graphs
c1.cd(4)
legend4 = TLegend(0.1,0.6,0.3,0.9)

if (len(PTZ_Filled_Histograms)==4):
	PTZ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTZ_Filled_Histograms[0], PTZ_XTitle)
	PTZ_1 = PTZ_Filled_Histograms[1]
	e1_v = PTZ_Filled_Histograms[2]
	e1_ex_v = PTZ_Filled_Histograms[3]

elif (len(PTZ_Filled_Histograms)==8):
	PTZ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTZ_Filled_Histograms[0], PTZ_Filled_Histograms[1], PTZ_XTitle)
	PTZ_1 = PTZ_Filled_Histograms[2]
	PTZ_2 = PTZ_Filled_Histograms[3]
	e1_v = PTZ_Filled_Histograms[4]
	e2_v = PTZ_Filled_Histograms[5]
	e1_ex_v = PTZ_Filled_Histograms[6]
	e2_ex_v = PTZ_Filled_Histograms[7]

elif (len(PTZ_Filled_Histograms)==12):
	PTZ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTZ_Filled_Histograms[0], PTZ_Filled_Histograms[1], PTZ_Filled_Histograms[2], PTZ_XTitle)
	PTZ_1 = PTZ_Filled_Histograms[3]
	PTZ_2 = PTZ_Filled_Histograms[4]
	PTZ_3 = PTZ_Filled_Histograms[5]
	e1_v = PTZ_Filled_Histograms[6]
	e2_v = PTZ_Filled_Histograms[7]
	e3_v = PTZ_Filled_Histograms[8]
	e1_ex_v = PTZ_Filled_Histograms[9]
	e2_ex_v = PTZ_Filled_Histograms[10]
	e3_ex_v = PTZ_Filled_Histograms[11]

elif (len(PTZ_Filled_Histograms)==16):
	PTZ_Drawn_Histograms = MyFunctions.HistogramDrawer(PTZ_Filled_Histograms[0], PTZ_Filled_Histograms[1], PTZ_Filled_Histograms[2], PTZ_Filled_Histograms[3], PTZ_XTitle)
	PTZ_1 = PTZ_Filled_Histograms[4]
	PTZ_2 = PTZ_Filled_Histograms[5]
	PTZ_3 = PTZ_Filled_Histograms[6]
	PTZ_4 = PTZ_Filled_Histograms[7]
	e1_v = PTZ_Filled_Histograms[8]
	e2_v = PTZ_Filled_Histograms[9]
	e3_v = PTZ_Filled_Histograms[10]
	e4_v = PTZ_Filled_Histograms[11]
	e1_ex_v = PTZ_Filled_Histograms[12]
	e2_ex_v = PTZ_Filled_Histograms[13]
	e3_ex_v = PTZ_Filled_Histograms[14]
	e4_ex_v = PTZ_Filled_Histograms[15]


if (len(PTZ_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(PTZ_Drawn_Histograms[0], PTZ_Drawn_Histograms[1], a, b, legend4, PTZ_Legend_Name, PTZ_has_legend)
elif (len(PTZ_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(PTZ_Drawn_Histograms[0], PTZ_Drawn_Histograms[1], PTZ_Drawn_Histograms[2], a, b, legend4, PTZ_Legend_Name, PTZ_has_legend)
elif (len(PTSQ_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(PTZ_Drawn_Histograms[0], PTZ_Drawn_Histograms[1], PTZ_Drawn_Histograms[2], PTZ_Drawn_Histograms[3], a, b, legend4, PTZ_Legend_Name, PTZ_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(PTZ_Drawn_Histograms, a, b, legend4, PTZ_Legend_Name, PTZ_has_legend)
# End of Draw PTZ Graphs

c1.Print("test.pdf(")
c1.Clear()
c1.Update()

#Emission_Angle_Ds Histogram Filler
print("Filling the Ds Emission Angle #Theta Graph... Thank you for waiting...")
if (len(Emission_Angle_Ds_Histograms) == 4):
	Emission_Angle_Ds_Filled_Histograms = MyFunctions.Emission_Angle_DsHistogramFiller(a, Emission_Angle_Ds_Histograms, entries, PTX_1, PTX_2, PTX_3, PTX_4, PTY_1, PTY_2, PTY_3, PTY_4, PTZ_1, PTZ_2, PTZ_3, PTZ_4, e1_v, e2_v, e3_v, e4_v, e1_ex_v, e2_ex_v, e3_ex_v, e4_ex_v)
elif (len(Emission_Angle_Ds_Histograms) == 3):
	Emission_Angle_Ds_Filled_Histograms = MyFunctions.Emission_Angle_DsHistogramFiller(a, Emission_Angle_Ds_Histograms, entries, PTX_1, PTX_2, PTX_3, PTY_1, PTY_2, PTY_3, PTZ_1, PTZ_2, PTZ_3, e1_v, e2_v, e3_v, e1_ex_v, e2_ex_v, e3_ex_v)
elif (len(Emission_Angle_Ds_Histograms) == 2):
	Emission_Angle_Ds_Filled_Histograms = MyFunctions.Emission_Angle_DsHistogramFiller(a, Emission_Angle_Ds_Histograms, entries, PTX_1, PTX_2, PTY_1, PTY_2, PTZ_1, PTZ_2, e1_v, e2_v, e1_ex_v, e2_ex_v)
else:
	Emission_Angle_Ds_Filled_Histograms = MyFunctions.Emission_Angle_DsHistogramFiller(a, Emission_Angle_Ds_Histograms, entries, PTX_1, PTY_1, PTZ_1, e1_v, e1_ex_v)

c1.Divide(2,2)

# Draw Emission_Angle_Ds Graphs
c1.cd(1)
legend5 = TLegend(0.3,0.6,0.6,0.9)

if (len(Emission_Angle_Ds_Filled_Histograms)==6):
	Emission_Angle_Ds_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Ds_Filled_Histograms[0], Emission_Angle_Ds_XTitle)
	X_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[1]
	Y_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[2]
	THETA_DS1 = Emission_Angle_Ds_Filled_Histograms[3]
	Gamma1_1 = Emission_Angle_Ds_Filled_Histograms[4]
	Beta1_1 = Emission_Angle_Ds_Filled_Histograms[5]

elif (len(Emission_Angle_Ds_Filled_Histograms)==12):
	Emission_Angle_Ds_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Ds_Filled_Histograms[0], Emission_Angle_Ds_Filled_Histograms[1], Emission_Angle_Ds_XTitle)
	X_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[2]
	X_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[3]
	Y_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[4]
	Y_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[5]
	THETA_DS1 = Emission_Angle_Ds_Filled_Histograms[6]
	THETA_DS2 = Emission_Angle_Ds_Filled_Histograms[7]
	Gamma1_1 = Emission_Angle_Ds_Filled_Histograms[8]
	Gamma1_2 = Emission_Angle_Ds_Filled_Histograms[9]
	Beta1_1 = Emission_Angle_Ds_Filled_Histograms[10]
	Beta1_2 = Emission_Angle_Ds_Filled_Histograms[11]

elif (len(Emission_Angle_Ds_Filled_Histograms)==18):
	Emission_Angle_Ds_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Ds_Filled_Histograms[0], Emission_Angle_Ds_Filled_Histograms[1], Emission_Angle_Ds_Filled_Histograms[2], Emission_Angle_Ds_XTitle)
	X_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[3]
	X_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[4]
	X_Slope_Ds_3 = Emission_Angle_Ds_Filled_Histograms[5]
	Y_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[6]
	Y_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[7]
	Y_Slope_Ds_3 = Emission_Angle_Ds_Filled_Histograms[8]
	THETA_DS1 = Emission_Angle_Ds_Filled_Histograms[9]
	THETA_DS2 = Emission_Angle_Ds_Filled_Histograms[10]
	THETA_DS3 = Emission_Angle_Ds_Filled_Histograms[11]
	Gamma1_1 = Emission_Angle_Ds_Filled_Histograms[12]
	Gamma1_2 = Emission_Angle_Ds_Filled_Histograms[13]
	Gamma1_3 = Emission_Angle_Ds_Filled_Histograms[14]
	Beta1_1 = Emission_Angle_Ds_Filled_Histograms[15]
	Beta1_2 = Emission_Angle_Ds_Filled_Histograms[16]
	Beta1_3 = Emission_Angle_Ds_Filled_Histograms[17]

elif (len(Emission_Angle_Ds_Filled_Histograms)==24):
	Emission_Angle_Ds_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Ds_Filled_Histograms[0], Emission_Angle_Ds_Filled_Histograms[1], Emission_Angle_Ds_Filled_Histograms[2], Emission_Angle_Ds_Filled_Histograms[3], Emission_Angle_Ds_XTitle)
	X_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[4]
	X_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[5]
	X_Slope_Ds_3 = Emission_Angle_Ds_Filled_Histograms[6]
	X_Slope_Ds_4 = Emission_Angle_Ds_Filled_Histograms[7]
	Y_Slope_Ds_1 = Emission_Angle_Ds_Filled_Histograms[8]
	Y_Slope_Ds_2 = Emission_Angle_Ds_Filled_Histograms[9]
	Y_Slope_Ds_3 = Emission_Angle_Ds_Filled_Histograms[10]
	Y_Slope_Ds_4 = Emission_Angle_Ds_Filled_Histograms[11]
	THETA_DS1 = Emission_Angle_Ds_Filled_Histograms[12]
	THETA_DS2 = Emission_Angle_Ds_Filled_Histograms[13]
	THETA_DS3 = Emission_Angle_Ds_Filled_Histograms[14]
	THETA_DS4 = Emission_Angle_Ds_Filled_Histograms[15]
	Gamma1_1 = Emission_Angle_Ds_Filled_Histograms[16]
	Gamma1_2 = Emission_Angle_Ds_Filled_Histograms[17]
	Gamma1_3 = Emission_Angle_Ds_Filled_Histograms[18]
	Gamma1_4 = Emission_Angle_Ds_Filled_Histograms[19]
	Beta1_1 = Emission_Angle_Ds_Filled_Histograms[20]
	Beta1_2 = Emission_Angle_Ds_Filled_Histograms[21]
	Beta1_3 = Emission_Angle_Ds_Filled_Histograms[22]
	Beta1_4 = Emission_Angle_Ds_Filled_Histograms[23]


if (len(Emission_Angle_Ds_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Ds_Drawn_Histograms[0], Emission_Angle_Ds_Drawn_Histograms[1], a, b, legend5, Emission_Angle_Ds_Legend_Name, Emission_Angle_Ds_has_legend)
elif (len(Emission_Angle_Ds_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Ds_Drawn_Histograms[0], Emission_Angle_Ds_Drawn_Histograms[1], Emission_Angle_Ds_Drawn_Histograms[2], a, b, legend5, Emission_Angle_Ds_Legend_Name, Emission_Angle_Ds_has_legend)
elif (len(Emission_Angle_Ds_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Ds_Drawn_Histograms[0], Emission_Angle_Ds_Drawn_Histograms[1], Emission_Angle_Ds_Drawn_Histograms[2], Emission_Angle_Ds_Drawn_Histograms[3], a, b, legend5, Emission_Angle_Ds_Legend_Name, Emission_Angle_Ds_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Ds_Drawn_Histograms, a, b, legend5, Emission_Angle_Ds_Legend_Name, Emission_Angle_Ds_has_legend)
# End of Draw Emission_Angle_Ds Graphs


#Emission_Angle_Tau Histogram Filler
print("Filling the #tau Emission Angle #Theta Graph... Thank you for waiting...")
if (len(Emission_Angle_Tau_Histograms) == 4):
	Emission_Angle_Tau_Filled_Histograms = MyFunctions.Emission_Angle_TauHistogramFiller(a, Emission_Angle_Tau_Histograms, entries, Gamma1_1, Gamma1_2, Gamma1_3, Gamma1_4, Beta1_1, Beta1_2, Beta1_3, Beta1_4, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, X_Slope_Ds_4, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3, Y_Slope_Ds_4, rand)
elif (len(Emission_Angle_Tau_Histograms) == 3):
	Emission_Angle_Tau_Filled_Histograms = MyFunctions.Emission_Angle_TauHistogramFiller(a, Emission_Angle_Tau_Histograms, entries, Gamma1_1, Gamma1_2, Gamma1_3, Beta1_1, Beta1_2, Beta1_3, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3, rand)
elif (len(Emission_Angle_Tau_Histograms) == 2):
	Emission_Angle_Tau_Filled_Histograms = MyFunctions.Emission_Angle_TauHistogramFiller(a, Emission_Angle_Tau_Histograms, entries, Gamma1_1, Gamma1_2, Beta1_1, Beta1_2, X_Slope_Ds_1, X_Slope_Ds_2, Y_Slope_Ds_1, Y_Slope_Ds_2, rand)
else:
	Emission_Angle_Tau_Filled_Histograms = MyFunctions.Emission_Angle_TauHistogramFiller(a, Emission_Angle_Tau_Histograms, entries, Gamma1_1, Beta1_1, X_Slope_Ds_1, Y_Slope_Ds_1, rand)

# Draw Emission_Angle_Tau Graphs
c1.cd(2)
legend6 = TLegend(0.3,0.6,0.6,0.9)

if (len(Emission_Angle_Tau_Filled_Histograms)==7):
	Emission_Angle_Tau_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Tau_Filled_Histograms[0], Emission_Angle_Tau_XTitle)
	Tau_Px = Emission_Angle_Tau_Filled_Histograms[1]
	Tau_Py = Emission_Angle_Tau_Filled_Histograms[2]
	Tau_Pz = Emission_Angle_Tau_Filled_Histograms[3]
	X_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[4]
	Y_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[5]
	E1_ex_Tau = Emission_Angle_Tau_Filled_Histograms[6]

elif (len(Emission_Angle_Tau_Filled_Histograms)==11):
	Emission_Angle_Tau_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Tau_Filled_Histograms[0], Emission_Angle_Tau_Filled_Histograms[1], Emission_Angle_Tau_XTitle)
	Tau_Px = Emission_Angle_Tau_Filled_Histograms[2]
	Tau_Py = Emission_Angle_Tau_Filled_Histograms[3]
	Tau_Pz = Emission_Angle_Tau_Filled_Histograms[4]
	X_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[5]
	X_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[6]
	Y_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[7]
	Y_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[8]
	E1_ex_Tau = Emission_Angle_Tau_Filled_Histograms[9]
	E2_ex_Tau = Emission_Angle_Tau_Filled_Histograms[10]

elif (len(Emission_Angle_Tau_Filled_Histograms)==15):
	Emission_Angle_Tau_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Tau_Filled_Histograms[0], Emission_Angle_Tau_Filled_Histograms[1], Emission_Angle_Tau_Filled_Histograms[2], Emission_Angle_Tau_XTitle)
	Tau_Px = Emission_Angle_Tau_Filled_Histograms[3]
	Tau_Py = Emission_Angle_Tau_Filled_Histograms[4]
	Tau_Pz = Emission_Angle_Tau_Filled_Histograms[5]
	X_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[6]
	X_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[7]
	X_Slope_Tau_3 = Emission_Angle_Tau_Filled_Histograms[8]
	Y_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[9]
	Y_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[10]
	Y_Slope_Tau_3 = Emission_Angle_Tau_Filled_Histograms[11]
	E1_ex_Tau = Emission_Angle_Tau_Filled_Histograms[12]
	E2_ex_Tau = Emission_Angle_Tau_Filled_Histograms[13]
	E3_ex_Tau = Emission_Angle_Tau_Filled_Histograms[14]

elif (len(Emission_Angle_Tau_Filled_Histograms)==19):
	Emission_Angle_Tau_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Tau_Filled_Histograms[0], Emission_Angle_Tau_Filled_Histograms[1], Emission_Angle_Tau_Filled_Histograms[2], Emission_Angle_Tau_Filled_Histograms[3], Emission_Angle_Tau_XTitle)
	Tau_Px = Emission_Angle_Tau_Filled_Histograms[4]
	Tau_Py = Emission_Angle_Tau_Filled_Histograms[5]
	Tau_Pz = Emission_Angle_Tau_Filled_Histograms[6]
	X_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[7]
	X_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[8]
	X_Slope_Tau_3 = Emission_Angle_Tau_Filled_Histograms[9]
	X_Slope_Tau_4 = Emission_Angle_Tau_Filled_Histograms[10]
	Y_Slope_Tau_1 = Emission_Angle_Tau_Filled_Histograms[11]
	Y_Slope_Tau_2 = Emission_Angle_Tau_Filled_Histograms[12]
	Y_Slope_Tau_3 = Emission_Angle_Tau_Filled_Histograms[13]
	Y_Slope_Tau_4 = Emission_Angle_Tau_Filled_Histograms[14]
	E1_ex_Tau = Emission_Angle_Tau_Filled_Histograms[15]
	E2_ex_Tau = Emission_Angle_Tau_Filled_Histograms[16]
	E3_ex_Tau = Emission_Angle_Tau_Filled_Histograms[17]
	E4_ex_Tau = Emission_Angle_Tau_Filled_Histograms[18]

if (len(Emission_Angle_Tau_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Tau_Drawn_Histograms[0], Emission_Angle_Tau_Drawn_Histograms[1], a, b, legend6, Emission_Angle_Tau_Legend_Name, Emission_Angle_Tau_has_legend)
elif (len(Emission_Angle_Tau_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Tau_Drawn_Histograms[0], Emission_Angle_Tau_Drawn_Histograms[1], Emission_Angle_Tau_Drawn_Histograms[2], a, b, legend6, Emission_Angle_Tau_Legend_Name, Emission_Angle_Tau_has_legend)
elif (len(Emission_Angle_Tau_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Tau_Drawn_Histograms[0], Emission_Angle_Tau_Drawn_Histograms[1], Emission_Angle_Tau_Drawn_Histograms[2], Emission_Angle_Tau_Drawn_Histograms[3], a, b, legend6, Emission_Angle_Tau_Legend_Name, Emission_Angle_Tau_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Tau_Drawn_Histograms, a, b, legend6, Emission_Angle_Tau_Legend_Name, Emission_Angle_Tau_has_legend)
# End of Draw Emission_Angle_Tau Graphs


#Emission_Angle_Nu1 Histogram Filler
print("Filling the #nu1 Emission Angle #Theta Graph... Thank you for waiting...")
if (len(Emission_Angle_Nu1_Histograms) == 4):
	Emission_Angle_Nu1_Filled_Histograms = MyFunctions.Emission_Angle_Nu1HistogramFiller(a, Emission_Angle_Nu1_Histograms, entries, Gamma1_1, Gamma1_2, Gamma1_3, Gamma1_4, Beta1_1, Beta1_2, Beta1_3, Beta1_4, Tau_Px, Tau_Py, Tau_Pz, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, X_Slope_Ds_4, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3, Y_Slope_Ds_4)
elif (len(Emission_Angle_Nu1_Histograms) == 3):
	Emission_Angle_Nu1_Filled_Histograms = MyFunctions.Emission_Angle_Nu1HistogramFiller(a, Emission_Angle_Nu1_Histograms, entries, Gamma1_1, Gamma1_2, Gamma1_3, Beta1_1, Beta1_2, Beta1_3, Tau_Px, Tau_Py, Tau_Pz, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3)
elif (len(Emission_Angle_Nu1_Histograms) == 2):
	Emission_Angle_Nu1_Filled_Histograms = MyFunctions.Emission_Angle_Nu1HistogramFiller(a, Emission_Angle_Nu1_Histograms, entries, Gamma1_1, Gamma1_2, Beta1_1, Beta1_2, Tau_Px, Tau_Py, Tau_Pz, X_Slope_Ds_1, X_Slope_Ds_2, Y_Slope_Ds_1, Y_Slope_Ds_2)
else:
	Emission_Angle_Nu1_Filled_Histograms = MyFunctions.Emission_Angle_Nu1HistogramFiller(a, Emission_Angle_Nu1_Histograms, entries, Gamma1_1, Beta1_1, Tau_Px, Tau_Py, Tau_Pz, X_Slope_Ds_1, Y_Slope_Ds_1)


# Draw Emission_Angle_Nu1 Graphs
c1.cd(3)
legend7 = TLegend(0.3,0.6,0.6,0.9)

if (len(Emission_Angle_Nu1_Filled_Histograms)==3):
	Emission_Angle_Nu1_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu1_Filled_Histograms[0], Emission_Angle_Nu1_XTitle)
	X_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[1]
	Y_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[2]

elif (len(Emission_Angle_Nu1_Filled_Histograms)==6):
	Emission_Angle_Nu1_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu1_Filled_Histograms[0], Emission_Angle_Nu1_Filled_Histograms[1], Emission_Angle_Nu1_XTitle)
	X_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[2]
	X_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[3]
	Y_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[4]
	Y_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[5]

elif (len(Emission_Angle_Nu1_Filled_Histograms)==9):
	Emission_Angle_Nu1_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu1_Filled_Histograms[0], Emission_Angle_Nu1_Filled_Histograms[1], Emission_Angle_Nu1_Filled_Histograms[2], Emission_Angle_Nu1_XTitle)
	X_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[3]
	X_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[4]
	X_Slope_Nu1_3 = Emission_Angle_Nu1_Filled_Histograms[5]
	Y_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[6]
	Y_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[7]
	Y_Slope_Nu1_3 = Emission_Angle_Nu1_Filled_Histograms[8]

elif (len(Emission_Angle_Nu1_Filled_Histograms)==12):
	Emission_Angle_Nu1_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu1_Filled_Histograms[0], Emission_Angle_Nu1_Filled_Histograms[1], Emission_Angle_Nu1_Filled_Histograms[2], Emission_Angle_Nu1_Filled_Histograms[3], Emission_Angle_Nu1_XTitle)
	X_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[4]
	X_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[5]
	X_Slope_Nu1_3 = Emission_Angle_Nu1_Filled_Histograms[6]
	X_Slope_Nu1_4 = Emission_Angle_Nu1_Filled_Histograms[7]
	Y_Slope_Nu1_1 = Emission_Angle_Nu1_Filled_Histograms[8]
	Y_Slope_Nu1_2 = Emission_Angle_Nu1_Filled_Histograms[9]
	Y_Slope_Nu1_3 = Emission_Angle_Nu1_Filled_Histograms[10]
	Y_Slope_Nu1_4 = Emission_Angle_Nu1_Filled_Histograms[11]


if (len(Emission_Angle_Nu1_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu1_Drawn_Histograms[0], Emission_Angle_Nu1_Drawn_Histograms[1], a, b, legend7, Emission_Angle_Nu1_Legend_Name, Emission_Angle_Nu1_has_legend)
elif (len(Emission_Angle_Nu1_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu1_Drawn_Histograms[0], Emission_Angle_Nu1_Drawn_Histograms[1], Emission_Angle_Nu1_Drawn_Histograms[2], a, b, legend7, Emission_Angle_Nu1_Legend_Name, Emission_Angle_Nu1_has_legend)
elif (len(Emission_Angle_Nu1_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu1_Drawn_Histograms[0], Emission_Angle_Nu1_Drawn_Histograms[1], Emission_Angle_Nu1_Drawn_Histograms[2], Emission_Angle_Nu1_Drawn_Histograms[3], a, b, legend7, Emission_Angle_Nu1_Legend_Name, Emission_Angle_Nu1_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu1_Drawn_Histograms, a, b, legend7, Emission_Angle_Nu1_Legend_Name, Emission_Angle_Nu1_has_legend)
# End of Draw Emission_Angle_Nu1 Graphs

#Emission_Angle_Nu2 Histogram Filler
print("Filling the #nu2 Emission Angle #Theta Graph... Thank you for waiting...")
if (len(Emission_Angle_Nu2_Histograms) == 4):
	Emission_Angle_Nu2_Filled_Histograms = MyFunctions.Emission_Angle_Nu2HistogramFiller(a, Emission_Angle_Nu2_Histograms, entries, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, X_Slope_Ds_4, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3, Y_Slope_Ds_4, E1_ex_Tau, E2_ex_Tau, E3_ex_Tau, E4_ex_Tau)
elif (len(Emission_Angle_Nu2_Histograms) == 3):
	Emission_Angle_Nu2_Filled_Histograms = MyFunctions.Emission_Angle_Nu2HistogramFiller(a, Emission_Angle_Nu2_Histograms, entries, X_Slope_Ds_1, X_Slope_Ds_2, X_Slope_Ds_3, Y_Slope_Ds_1, Y_Slope_Ds_2, Y_Slope_Ds_3, E1_ex_Tau, E2_ex_Tau, E3_ex_Tau)
elif (len(Emission_Angle_Nu2_Histograms) == 2):
	Emission_Angle_Nu2_Filled_Histograms = MyFunctions.Emission_Angle_Nu2HistogramFiller(a, Emission_Angle_Nu2_Histograms, entries, X_Slope_Ds_1, X_Slope_Ds_2, Y_Slope_Ds_1, Y_Slope_Ds_2, E1_ex_Tau, E2_ex_Tau)
else:
	Emission_Angle_Nu2_Filled_Histograms = MyFunctions.Emission_Angle_Nu2HistogramFiller(a, Emission_Angle_Nu2_Histograms, entries, X_Slope_Ds_1, Y_Slope_Ds_1, E1_ex_Tau)


# Draw Emission_Angle_Nu2 Graphs
c1.cd(4)
legend8 = TLegend(0.3,0.6,0.6,0.9)

if (len(Emission_Angle_Nu2_Filled_Histograms)==3):
	Emission_Angle_Nu2_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu2_Filled_Histograms[0], Emission_Angle_Nu2_XTitle)
	X_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[1]
	Y_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[2]

elif (len(Emission_Angle_Nu2_Filled_Histograms)==6):
	Emission_Angle_Nu2_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu2_Filled_Histograms[0], Emission_Angle_Nu2_Filled_Histograms[1], Emission_Angle_Nu2_XTitle)
	X_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[2]
	X_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[3]
	Y_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[4]
	Y_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[5]

elif (len(Emission_Angle_Nu2_Filled_Histograms)==9):
	Emission_Angle_Nu2_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu2_Filled_Histograms[0], Emission_Angle_Nu2_Filled_Histograms[1], Emission_Angle_Nu2_Filled_Histograms[2], Emission_Angle_Nu2_XTitle)
	X_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[3]
	X_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[4]
	X_Slope_Nu2_3 = Emission_Angle_Nu2_Filled_Histograms[5]
	Y_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[6]
	Y_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[7]
	Y_Slope_Nu2_3 = Emission_Angle_Nu2_Filled_Histograms[8]

elif (len(Emission_Angle_Nu2_Filled_Histograms)==12):
	Emission_Angle_Nu2_Drawn_Histograms = MyFunctions.HistogramDrawer(Emission_Angle_Nu2_Filled_Histograms[0], Emission_Angle_Nu2_Filled_Histograms[1], Emission_Angle_Nu2_Filled_Histograms[2], Emission_Angle_Nu2_Filled_Histograms[3], Emission_Angle_Nu2_XTitle)
	X_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[4]
	X_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[5]
	X_Slope_Nu2_3 = Emission_Angle_Nu2_Filled_Histograms[6]
	X_Slope_Nu2_4 = Emission_Angle_Nu2_Filled_Histograms[7]
	Y_Slope_Nu2_1 = Emission_Angle_Nu2_Filled_Histograms[8]
	Y_Slope_Nu2_2 = Emission_Angle_Nu2_Filled_Histograms[9]
	Y_Slope_Nu2_3 = Emission_Angle_Nu2_Filled_Histograms[10]
	Y_Slope_Nu2_4 = Emission_Angle_Nu2_Filled_Histograms[11]


if (len(Emission_Angle_Nu2_Drawn_Histograms)==2):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu2_Drawn_Histograms[0], Emission_Angle_Nu2_Drawn_Histograms[1], a, b, legend8, Emission_Angle_Nu2_Legend_Name, Emission_Angle_Nu2_has_legend)
elif (len(Emission_Angle_Nu2_Drawn_Histograms)==3):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu2_Drawn_Histograms[0], Emission_Angle_Nu2_Drawn_Histograms[1], Emission_Angle_Nu2_Drawn_Histograms[2], a, b, legend8, Emission_Angle_Nu2_Legend_Name, Emission_Angle_Nu2_has_legend)
elif (len(Emission_Angle_Nu2_Drawn_Histograms)==4):
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu2_Drawn_Histograms[0], Emission_Angle_Nu2_Drawn_Histograms[1], Emission_Angle_Nu2_Drawn_Histograms[2], Emission_Angle_Nu2_Drawn_Histograms[3], a, b, legend8, Emission_Angle_Nu2_Legend_Name, Emission_Angle_Nu2_has_legend)
else:
	MyFunctions.DoubleLegendDrawer(Emission_Angle_Nu2_Drawn_Histograms, a, b, legend8, Emission_Angle_Nu2_Legend_Name, Emission_Angle_Nu2_has_legend)
# End of Draw Emission_Angle_Nu2 Graphs

c1.Print("test.pdf")
c1.Clear()
c1.Update()

#Kink_Angle Filler
print("Filling the Kink angle #theta of Ds and #tau Graph... Thank you for waiting...")
if (len(Kink_Angle_Histograms) == 8):
	Kink_Angle_Filled_Histograms = MyFunctions.Kink_Angle_HistogramFiller(a, Kink_Angle_Histograms, entries, X_Slope_Tau_1, X_Slope_Tau_2, X_Slope_Tau_3, X_Slope_Tau_4, Y_Slope_Tau_1, Y_Slope_Tau_2, Y_Slope_Tau_3, Y_Slope_Tau_4, X_Slope_Nu2_1, X_Slope_Nu2_2, X_Slope_Nu2_3, X_Slope_Nu2_4, Y_Slope_Nu2_1, Y_Slope_Nu2_2, Y_Slope_Nu2_3, Y_Slope_Nu2_4)
elif (len(Kink_Angle_Histograms) == 6):
	Kink_Angle_Filled_Histograms = MyFunctions.Kink_Angle_HistogramFiller(a, Kink_Angle_Histograms, entries, X_Slope_Tau_1, X_Slope_Tau_2, X_Slope_Tau_3, Y_Slope_Tau_1, Y_Slope_Tau_2, Y_Slope_Tau_3, X_Slope_Nu2_1, X_Slope_Nu2_2, X_Slope_Nu2_3, Y_Slope_Nu2_1, Y_Slope_Nu2_2, Y_Slope_Nu2_3)
elif (len(Kink_Angle_Histograms) == 4):
	Kink_Angle_Filled_Histograms = MyFunctions.Kink_Angle_HistogramFiller(a, Kink_Angle_Histograms, entries, X_Slope_Tau_1, X_Slope_Tau_2, Y_Slope_Tau_1, Y_Slope_Tau_2, X_Slope_Nu2_1, X_Slope_Nu2_2, Y_Slope_Nu2_1, Y_Slope_Nu2_2)
elif (len(Kink_Angle_Histograms) == 2):
	Kink_Angle_Filled_Histograms = MyFunctions.Kink_Angle_HistogramFiller(a, Kink_Angle_Histograms, entries, X_Slope_Tau_1, Y_Slope_Tau_1, X_Slope_Nu2_1, Y_Slope_Nu2_1)


c1.Divide(2,2)
# Draw Kink_Angle Graphs

if (len(Kink_Angle_Filled_Histograms)==2):
	c1.cd(1)
	legend9 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], a[0], b[0], legend9, Kink_Angle_Legend_Name, Kink_Angle_has_legend)

elif (len(Kink_Angle_Filled_Histograms)==4):
	c1.cd(1)
	legend9 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], a[0], b[0], legend9, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(2)
	legend10 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], a[1], b[1], legend10, Kink_Angle_Legend_Name, Kink_Angle_has_legend)

elif (len(Kink_Angle_Filled_Histograms)==6):
	c1.cd(1)
	legend9 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], a[0], b[0], legend9, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(2)
	legend10 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], a[1], b[1], legend10, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(3)
	legend11 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[4], Kink_Angle_Filled_Histograms[5], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[4], Kink_Angle_Filled_Histograms[5], a[2], b[2], legend11, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
elif (len(Kink_Angle_Filled_Histograms)==8):
	c1.cd(1)
	legend9 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[0], Kink_Angle_Filled_Histograms[1], a[0], b[0], legend9, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(2)
	legend10 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[2], Kink_Angle_Filled_Histograms[3], a[1], b[1], legend10, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(3)
	legend11 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[4], Kink_Angle_Filled_Histograms[5], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[4], Kink_Angle_Filled_Histograms[5], a[2], b[2], legend11, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
	c1.cd(4)
	legend12 = TLegend(0.3,0.6,0.6,0.9)
	Kink_Angle_Drawn_Histograms = MyFunctions.HistogramDrawer(Kink_Angle_Filled_Histograms[6], Kink_Angle_Filled_Histograms[7], Kink_Angle_XTitle)
	MyFunctions.KinkLegendDrawer(Kink_Angle_Filled_Histograms[6], Kink_Angle_Filled_Histograms[7], a[3], b[3], legend12, Kink_Angle_Legend_Name, Kink_Angle_has_legend)
# End of Kink_Angle Graphs

c1.Print("test.pdf)")
