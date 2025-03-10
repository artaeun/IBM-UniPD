%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 08
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 1
% Calcolare lo spettro del segnale ecg contenuto nel file ecg_60.mat,
% campionato a 200Hz.

load ecg_60.mat

N = length(t);  % Totale campioni
Fs = 200;       % Frequenza di campionamento
x = ecg_60;     % segnale

% figure(1)
figure('units','normalized','outerposition',[0 0 1 1])  % Create a full-screen figure
subplot(3,1,1)
plot(t,x,'k')
xlabel('Tempo [Sec]')
title('Segnale ecg')

% Calcolo spettro del segnale
FTx = fft(x,N);
S = (abs(FTx).^2)/N;
f_FT = (0:Fs/N:Fs-Fs/N);
subplot(3,1,2)
plot(f_FT(1:N/2),S(1:N/2),'k')
xlabel('Frequenza [Hz]')
title('Densita spettrale di potenza')
subplot(3,1,3)
semilogy(f_FT(1:N/2),S(1:N/2),'k')
xlabel('Frequenza [Hz]')
title('Densita spettrale di potenza (scala semi-logaritmica)')

% Densita' spettrale di potenza media nell'intervallo [0,50] e [50,100] Hz
% Intervallo [0,50]Hz
f_start_first_interval = 0;
f_end_first_interval = 50;
ind = intersect(find(f_FT>=f_start_first_interval),find(f_FT<=f_end_first_interval));
% In alternativa, si può usare il seguente comando con operatore logico:
% ind = find(f_FT>=f_start_first_interval & f_FT<=f_end_first_interval);
mean_power_first_interval = mean(S(ind));

% Intervallo [50,100]Hz
f_start_second_interval = 50;
f_end_second_interval = 100;
ind = intersect(find(f_FT>=f_start_second_interval),find(f_FT<=f_end_second_interval));
mean_power_second_interval = mean(S(ind));

