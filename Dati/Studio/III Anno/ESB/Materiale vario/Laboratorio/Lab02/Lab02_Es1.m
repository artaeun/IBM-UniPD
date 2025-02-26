%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 02
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% ESERCIZIO 1
% Caricare il file ECG.mat
load DATA_Lab05_ECG.mat

% Plot del segnale ECG
figure(1)
plot(ecg, 'LineWidth', 1.5)
xlabel('Campioni Misurati (#)');
ylabel('Ampiezza (mV)')
title('ECG')

% Definisco il vettore tempo associato al segnale
dt = 0.004;         % Periodo di campionamento
N = length(ecg);    % Totale campioni
fc = 1/dt;          % Frequenza di campionamento [Hz]
duration = N*dt;    % [Seconds] durata temporale del segnale

t = linspace(0,duration,N)';

% Plot del segnale ECG con asse temporale
figure(2)
plot(t,ecg, 'LineWidth', 1.5)
axis tight
xlabel('Tempo (s)')
ylabel('Ampiezza (mV)')
title('ECG')

% Valore massimo dell'ECG
[max_ecg, idx_max_ecg] = max(ecg);


% Estrapolare e rappresentare graficamente un complesso PQRS dal segnale ECG
pqrs = ecg(220:420,:);
t_pqrs = t(220:420,:);

% Plot del scomplesso PQRS
figure(3)
plot(t_pqrs, pqrs)
xlabel('Tempo (s)')
ylabel('Ampiezza (mV)')
title('Complesso PQRS')
savefig('complesso_PQRS.fig')



