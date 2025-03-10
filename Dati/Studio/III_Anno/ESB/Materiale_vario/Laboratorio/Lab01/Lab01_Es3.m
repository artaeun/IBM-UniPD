%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 01
%  Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 3
% 1) Scrivere un M-file che disegni con una linea continua rossa
%   la funzione f(t)=2e(-0.05t) nell’intervallo [0,100] (rappresentare f(t) mediante 500 punti equispaziati).
% 2)Rappresentare f(t) nel riquadro superiore di una figura a due riquadri (suggerimento: usare subplot).
%   Nel riquadro inferiore rappresentare di nuovo la stessa funzione con sovrapposti, rappresentati da cerchietti blu, 
%   dei suoi campioni rumorosi generati artificialmente ai tempi (0, 5, 10, 15, …100).
%   Per generare i campioni considerare rumore gaussiano additivo a media nulla e standard deviation 0.03.
%   Intitolare i grafici rispettivamente con ‘Esponenziale decrescente’ ed ‘Esponenziale decrescente con campioni rumorosi (SD=0.03)’.

t = linspace(0,100,500);
f = 2*exp(-0.05*t);
subplot(2,1,1)
plot(t, f, 'r')
title('Esponenziale decrescente')

ts = [0:5:100]';
fs = 2*exp(-0.05*ts);
vs = 0.03*randn(length(fs),1);  % Rumore gaussiano additivo
ys = fs + vs;                   % Campioni rumorosi

subplot(2,1,2)
plot(t, f, 'r')
hold on
plot(ts, ys, 'ob')
title('Esponenziale decrescente con campioni rumorosi (SD=0.03)')

% 3) Acquisire da tastiera (suggerimento: usare l’istruzione input) un valore positivo
%   (suggerimento: usare una struttura while … end per controllare che l’utente immetta un valore SD strettamente positivo)
%   da usare come standard deviation del rumore additivo da usare nella generazione dei campioni rumorosi di f(t).
%   Intitolare i grafici dei due riquadri rispettivamente con “Esponenziale decrescente” e “Esponenziale decrescente con campioni rumorosi (SD=__)”
%   (far apparire nel titolo del secondo riquadro il valore della SD immesso da tastiera, suggerimento: usare num2str)

sd = input('Inserisci un valore di SD: ');
while sd <= 0
    
    sd = input('Dammi un valore positivo di SD: ');

end % while

ts = [0:5:100];
fs = 2*exp(-0.05*ts);
vs = sd*randn(length(fs),1);
ys = fs + vs;

subplot(2,1,2)
plot(t, f, 'r',ts, ys, 'ob')
title(['Esponenziale decrescente con campioni rumorosi (SD='+convertCharsToStrings(num2str(sd))+')'])


