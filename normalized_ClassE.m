%plot Figure 7.14 in the book by Cripps
clear;clc;close all;
phi=50:10:180; %conduction angle
%phi=125; %conduction angle
phi_rad=phi/180*pi;
m=sqrt(1+power((2*pi+sin(phi_rad)-phi_rad)./(1-cos(phi_rad)),2));  
alpha1=acos(-1./m);  alpha2=phi_rad-alpha1;
vci=-(m.*(power(sin(alpha1),2)-power(sin(alpha2),2))+2*(cos(alpha2)-cos(alpha1)))./(2*pi*m);
vcq=m.*(m.*(sin(alpha1)+sin(alpha2))+0.5*(sin(2*alpha1)-sin(2*alpha2))+2*sin(alpha2).*cos(alpha1))/(2*pi);
vdc=m.*(m.*(power(sin(alpha1),2)-power(sin(alpha2),2))+2*(cos(alpha2)-cos(alpha1)))/4/pi;
ipk=1+m;
RL=-vci;  %?-vci/m
XL=vcq./m;
%figure;hold;
plot(phi,RL,'r-','Displayname','RL'); hold;grid;
plot(phi,XL,'b-.','Displayname','XL'); legend('show');
ax1=gca;
ax2=axes('position',get(ax1,'position'),'Color','none','YAxisLocation','right');
line(phi,ipk,'Color','g','LineStyle',':','Displayname','IPK','Parent',ax2);
line(phi,vdc,'Color','m','LineStyle','-.','Displayname','VDC','Parent',ax2);legend('show')
%xx=[phi',RL',XL',vdc',ipk']