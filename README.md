# E7-LRC 
This repository contained codes for the 2nd year experiment *Study of an Oscillating Electrical System Driven into Resonance*. It would import data from csv file and output plotting with phase difference and angle.
## From experiment to this code

### From your RLC circuit

You will need to change the variables from line 13

```python
##### Theoritical value #####

L=18e-3         #Inductance of the inductor in Henry (H)

C=1800e-12      #Capacitance of the capacitor in Faraday (F)

R=820           #Resistance of the resistor in Ohm

```

Note: 18e-3 means 18*10^{-3}

### From your experiment data

I would recommand the arrangement of dataset below in a comma delimiated file. 

| \#frequency(Hz) | peak-to-peak voltage(volt) | unc voltage (volt) | y0   | y1   |
| --------------- | -------------------------- | ------------------ | ---- | ---- |
| 10000           | 2.30                       | 0.05               | 2.30 | 0.50 |

But feel free to change the order of columns, and update it in the code line 28&29. Change the order of variables. 

```python
freq, volt, delta_volt, y0, y1, delta_y = np.loadtxt("low_damp.csv",delimiter=",",unpack=True)   # Change file name and delimiter if required
freq_1, volt_1, delta_volt_1, y0_1, y1_1 = np.loadtxt("high_damp.csv",delimiter=",",unpack=True)
```

