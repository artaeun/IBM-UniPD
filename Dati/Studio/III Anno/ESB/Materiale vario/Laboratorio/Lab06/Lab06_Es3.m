%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 06
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 3
% Calcolare l’uscita del sistema
% y(n) = x(n)+ x(n-1) + x(n-2) + x(n-3) + x(n-4)
% in risposta all ingresso x, l'esponenziale di base 0.5 definito
% nell'intervallo di tempo (0,10) con tc=0.1 secondi
A = [1];
B = [1 1 1 1 1];
tc = 0.1; %secondi
time = [0:tc:10]; %secondi
x = (0.5).^time;  %ingresso


% Uscita del sistema
y = filter(B,A,x);


% Plottare i segnali ingresso x e uscita y rispetto al tempo 
figure
subplot(2,1,1)
stem(time,x)
xlabel('Time [secondi]')
ylabel('x(t)')
title('Ingresso')
subplot(2,1,2)
stem(time,y)
xlabel('Time [secondi]')
ylabel('y(t)')
title('Uscita')


