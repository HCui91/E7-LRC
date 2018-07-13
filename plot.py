#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

##### Reset variables #####
#Expected natural frequency
omega_0=0
omega=0
#2 experiment data sets
freq, volt, delta_volt, y0, y1, delta_y=[0,0,0,0,0,0]
freq_1, volt_1, delta_volt_1, y0_1, y1_1=[0,0,0,0,0]

##### Theoritical value #####
L=18e-3         #Inductance of the inductor in Henry (H)
C=1800e-12      #Capacitance of the capacitor in Faraday (F)
R=820           #Resistance of the resistor in Ohm

##### Theoritical natural frequency #####
omega_0=1/(np.sqrt(L*C))         # Theoretical natural ANGULAR frequency
omega=np.sqrt(omega_0**2-(R**2/(2*L**2)))      # Theoretical natural frequency 
plt.plot((omega,omega), (0, 4), 'k--',label="Theoretical amplitude resonance")    # Plot a vertical line at the natural frequency
print("Theoretical amplitude resonance is ",omega,"radian per second, or",omega/(2*np.pi),"Hz")

##### Import data #####
# CSV in form: frequency(Hz)	peak-to-peak voltage(volt)	unc voltage (volt)	y0 (volt)	y1 (volt)
# There are 2 sets of data corresponding to high damping and low damping. 
# where y0 and y1 are the Lissajous Figures on the oscilliscope.
freq, volt, delta_volt, y0, y1, delta_y = np.loadtxt("low_damp.csv",delimiter="	",unpack=True)   # Change file name and delimiter if required
freq_1, volt_1, delta_volt_1, y0_1, y1_1 = np.loadtxt("high_damp.csv",delimiter="	",unpack=True)

##### Data modification #####
freq=2*np.pi*freq     # Convert to angular frequency
volt=volt/2           # From peak-to-peak voltage to amplitude
phase=np.arcsin(y1/y0) # Phase calculation
# Same treatment to the other dataset
freq_1=2*np.pi*freq_1
volt_1=volt_1/2
phase_1=np.arcsin(y1_1/y0_1)

##### Uncertainty propagation #####
delta_y1y0=np.sqrt((delta_volt/y1)**2+(delta_volt/y0)**2)*(y1/y0)  #1 Uncertainty of the measurement
delta_phase = delta_y1y0/np.sqrt(1-(y1/y0)**2)                     #2 Uncertainty of phase calculation
# Same treatment to the other dataset
delta_y1y0_1=np.sqrt((delta_volt_1/y1_1)**2+(delta_volt_1/y0_1)**2)*(y1_1/y0_1)
delta_phase_1 = delta_y1y0_1/np.sqrt(1-(y1_1/y0_1)**2)

##### Correction to phase angles #####
#Reset counters
x=0
y=0
for x in range(0,36):
    if freq[x] >= 28e3*2*np.pi:
        phase[x]=np.pi-phase[x]
for y in range(0,34):
    if freq_1[y] >= 28e3*2*np.pi:
        phase_1[y]=np.pi-phase_1[y]

##### Output to angular frequency and amplitude to csv file #####
# If you want to investigate more about angular frequency and amplitude, uncomment it.
#np.savetxt("output0.csv",(freq,volt,delta_volt,phase,delta_phase), delimiter=",")
#np.savetxt("output1.csv",(freq_1,volt_1,delta_volt_1,phase_1,delta_phase_1), delimiter=",")

##### Amplitude graph #####
#Decide size of the output plot
plt.figure(1,figsize=(10,9))
plt.errorbar(freq,volt,yerr=delta_volt,fmt='o',label="Low damping")         # Plot with errorbar
plt.errorbar(freq_1,volt_1,yerr=delta_volt_1,fmt='D',label="High damping")
#Graph configuration
plt.title("Plot of Voltage resonance data")
plt.xlabel("Angular frequence(radian per second)")
plt.ylabel("Amplitude of Voltage(volt)")
plt.legend(loc="best")
plt.xlim(6e4-1000,26e4+1000)          # Modify it with your frequency range
plt.ylim(0.5,4)
plt.grid()
#plt.show()                           # Uncomment it if you are using command line tools
#Save graph  
plt.savefig("E7_amplitude")

##### Phase angle graph #####
plt.figure(2,figsize=(10,7))     # Generate another canvas
plt.errorbar(freq,phase,yerr=delta_phase,fmt='o',label="Low damping")       # Plot with errorbar
plt.errorbar(freq_1,phase_1,yerr=delta_phase_1,fmt='D',label="High damping")
plt.plot((50000,280000),(np.pi/2,np.pi/2),'--',label="Phase angle=pi/2")    # A reference line at the phase angle where should have resonance
plt.title("Plot of phase resonance data")
plt.xlabel("Angular frequence(radian per second)")
plt.ylabel("Phase angle(radian)")
plt.legend(loc="best")
plt.ylim(0,np.pi)
plt.xlim(np.min(freq)-1000,np.max(freq)+1000)
plt.grid()
#plt.show()
plt.savefig("E7_phase")

