# Ds-Tau_Production_Simulation
Performs Ds-Tau Production simulation with randomly generated numbers that makes sense physically (Using meaningful probability distributions for quantum-level particles)

You need Cern Root framework in your basrc and python in order to run the code. I used ubuntu 18.04 because of its stability and newest cern root version 6. Automated version is Main.py and it imports MyFunctions.py. Also nu_tau_mom.100GeV_tau_decay.dat file needs to be in the same directory with them since they import experimental tau neutrino data points. The normal code that is with n = 6.1 and b = 0.8 values can be directly drawn from Hardcoded.py. The equation below is used for the calculations ;

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x = \frac{d^{2}\sigma}{dx_{F}dp_{T}^{2}} = Ae^{bp_{T}^{2}}(1-|x_{F}|)^{n}" title="\Large x = \frac{d^{2}\sigma}{dx_{F}dp_{T}^{2}} = Ae^{bp_{T}^{2}}(1-|x_{F}|)^{n}" />

Experiment mainly simulates decay of a Ds particle to tau and tau neutrino particles. Since this experiment could not be performed fastly with instruments because of the background noise and tiny kink angle, we generate the experiment with this code. Code mainly generates probability distribution of a Ds particle and calculates its momentum. It also calculates Tau and Tau Neutrino momentums and kink angles. We then compare Ds and Tau kink angles and see why it is too hard to detect Ds particles.

Code requires N and B values as inputs from the user. Then generates graphs accordingly. Code allows maximum of 4 entered N and B values. N and B input count must be equal or code will return an error. Each input is paired with its corresponding input. For example, first N input and first B input is paired and calculated together to draw 1st histogram. This applies to 2nd 3rd and 4th. User can enter one, two, three or four N and B values but not more than that. It is not meaningful to draw more than 4 histograms in one section since it becomes quickly messy.

Each output histogram is experimentally verified using DONuT experiment conclusions.
