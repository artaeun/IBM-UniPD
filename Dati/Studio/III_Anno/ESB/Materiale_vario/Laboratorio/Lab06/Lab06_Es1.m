%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 06
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 1
% Calcolare l’uscita del sistema avente h(n)=1 n=0,1,2,....,10 e h(n)=0 altrove 
% in risposta all’ingresso x(n)dove x è l'esponenziale di base 0.5 in (0,10)
% Plottare h, x e y usando il comando stem

n = [0:1:10];
h = ones(size(n));
x = (0.5).^n;

% Uscita del sistema
y = conv(h,x); 
y = filter(h,1,x);

% Rappresentazione grafica dell'uscita del sistema h, del segnale in
% ingresso x e del segnale in uscita y
figure
subplot(3,1,1)
stem(n,h)
xlabel('n')
ylabel('h(n) (u.a.)')
title('h')
subplot(3,1,2)
stem(n,x)
xlabel('n')
ylabel('x(n) (u.a.)')
title('ingresso')
subplot(3,1,3)
stem(n,y(1:length(n))) %È necessario per la conv ridurre l'uscita nell'intervallo dei segnali di input
xlabel('n')
ylabel('y(n) (u.a.)')
title('uscita')


