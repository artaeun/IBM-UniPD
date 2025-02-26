%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 07
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 2
% Progettare un filtro in modo che la funzione di trasferimento H(z) abbia:
% Uno zero in z=0 e un polo in p=0.8
Fc = 1000;
zeri = 0;
poli = 0.8;
b = poly(zeri);
a = poly(poli);

figure
zplane(b,a)
[H,F]=freqz(b,a,2048,Fc);


% Uno zero in 0.5 e una coppia di poli complessi coniugati in -0.6±j0.3
Fc = 1000;
zeri = 0.5;
poli = [-0.6+0.3j -0.6-0.3j];
b = poly(zeri);
a = poly(poli);

figure
zplane(b,a)
[H,F]=freqz(b,a,2048,Fc);


% Uno zero in 0.5 e una coppia di poli complessi coniugati a 60Hz dentro al
% cerchio unitario
Fc = 1000;
F = 60;
theta=(2*pi/Fc)*F;
zeri = 0.5;
poli = [0.9*exp(1i*theta), 0.9*exp(-1i*theta)];
b = poly(zeri);
a = poly(poli);

figure
zplane(b,a)
[H,F]=freqz(b,a,2048,Fc);

