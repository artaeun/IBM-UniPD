%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 07
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 3

% 2) Determinare poli e zeri della funzione di trasferimento e farne il
% grafico nel piano di Gauss
% H(z) = (1-z^(-2))/(1+0.81z^(-1))

% Coefficienti del numeratore e denominatore
a = [1 0.81];
b = [1 0 -1];

% Zeri e poli
z = roots(b);
p = roots(a);

%%
% 3) Visualizzare la risposta in frequenza del filtro, in modulo e fase, e il
% diagramma zeri-poli
Fc = 1000;
Np = 2048;

[H, F] = freqz(b,a,Np,Fc);

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



