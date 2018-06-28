#calculate the matching parameters of ideal Class E PA
# by myota,  @2018.5
import math

#modify the following 5 parameters#
phi=180;  #conduction angle
vsup=5;  #power supply
Imax=2;  #peak current allowed by power MOS
freq=130e3;  #switch frequency
Q=20;  #required Q value of load impedence
##
phi_rad=phi/180.0*math.pi
pi2=2*math.pi
m=math.sqrt(1.0+math.pow((pi2+math.sin(phi_rad)-phi_rad)/(1.0-math.cos(phi_rad)),2))
alpha1=math.acos(-1/m); alpha2=phi_rad-alpha1
vci=-(m*(math.pow(math.sin(alpha1),2)-math.pow(math.sin(alpha2),2))+2*(math.cos(alpha2)-math.cos(alpha1)))/pi2/m
vcq=m*(m*(math.sin(alpha1)+math.sin(alpha2))+0.5*(math.sin(2*alpha1)-math.sin(2*alpha2))+2*math.sin(alpha2)*math.cos(alpha1))/pi2
vdc=m*(m*(math.pow(math.sin(alpha1),2)-math.pow(math.sin(alpha2),2))+2*(math.cos(alpha2)-math.cos(alpha1)))/2/pi2;
ipk=1.0+m
RL=-vci; XL=vcq/m;
##
scale=(vsup*1.0/vdc)/(Imax*1.0/ipk)
Cp=1/scale/pi2/freq
Req=RL*scale; Xeq=XL*scale; Lx=Xeq/pi2/freq;
Ls=Q*Req/pi2/freq-Lx;
Cs=1/math.pow(pi2*freq,2)/Ls
print("Cp=%g nF   #shunt Cap at drain" % (Cp*1.0e9))
print("RL=%g         #Real of required impedence" % Req)
print("Lx=%g uH    #Imag of required impedence" % (Lx*1.0e6))
print("Ls=%g uH    #inductor for serial resonator" % (Ls*1.0e6))
print("Cs=%g nF    #capacitor for serial resonator" % (Cs*1.0e9))
Idc=Imax*1.0/(1+m)
print("Idc=%g" % Idc)
print("Irf=%g" % (Imax-Idc))
