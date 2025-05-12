%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 07
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 1 - CHALLENGE
% Progettare un filtro con uno zero in -1, un polo in 0.9, una coppia di 
% zeri e poli complessi coniugati a 30 Hz e un’altra a 60 Hz.
% Gli zeri siano sul cerchio di raggio unitario e i poli all’interno del
% cerchio unitario (ad es. modulo 0.9).

Fs = 1000;
F1 = 60;
theta1 = (2*pi/Fs)*F1;
F2 = 30;
theta2 = (2*pi/Fs)*F2;

zeri=[exp(1i*theta1), exp(-1i*theta1) exp(1i*theta2), exp(-1i*theta2) -1 ];
coeff=0.9;
poli=[coeff*exp(1i*theta1), coeff*exp(-1i*theta1), coeff*exp(1i*theta2), coeff*exp(-1i*theta2) coeff];

b=poly(zeri);
a=poly(poli);

G=polyval(b,1)/polyval(a,1);
b=b/G;
[H,F]=freqz(b,a,2048,Fs);

% Diagramma di Bode del filtro
figure
subplot(2,1,1)
plot(F,20*log10(abs(H)))
title('modulo')
xlabel('Hz')
subplot(2,1,2)
plot(F,angle(H)*360/(2*pi))
title('fase')
xlabel('Hz')

% Diagramma zeri-poli
figure
zplane(b,a)


%% FILTRARE IL SEGNALE

% Load ECG data
load segnale_bioelettrico.mat

dati = segnale;
N = length(dati);
t = [0:1/Fs:(N-1)/Fs];
y = filter(b,a,dati);

figure
plot(t, dati, 'b')
hold on
plot(t, y, 'r')
xlabel('time')
ylabel('u.a.')
legend('Segnale originale', 'Segnale filtrato')



