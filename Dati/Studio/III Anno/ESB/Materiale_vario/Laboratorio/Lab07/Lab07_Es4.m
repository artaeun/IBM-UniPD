%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 07
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 4
% Progettare un filtro passa-basso con 2 poli reali coincidenti in 0.8 e
% 2 zeri nell' origine, in modo che abbia guadagno unitario per ω=0 
% |H(ω=0)|= |H(1)|= 1
% Visualizzare la risposta in frequenza del filtro, in modulo e fase, 
% e il diagramma zeri-poli.


Fc = 1000;
poli = [0.8, 0.8];
zeri = [0, 0];
b = poly(zeri);
a = poly(poli);

G = polyval(b,1)/polyval(a,1);
b = b/G;

% Filtro
[H, F] = freqz(b,a,2048,Fc);

figure
subplot(2,1,1)
plot(F,20*log10(abs(H)))		% Disegna il modulo
title('modulo')
xlabel('Hz')
subplot(2,1,2)
plot(F,angle(H)*360/(2*pi))	    % Disegna la fase 
title('fase')
xlabel('Hz')

% Diagramma zeri-poli
figure
zplane(b,a) 
