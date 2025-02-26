%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 04
% Prof. Veronese Mattia - UNIPD


%% OPENING
clear all
close all
clc

%% Definizione del segnale sinusoidale

A = 1.5;                % Ampiezza [V]
T = 100;                % Periodo del segnale [s]
Fc = 1;                 % Frequenza di campionamento [Hz]
time = [0:1/Fc:150];    % Time [s]

% Segnale sinusoidale
y = A*sin(2*pi*1/T*time);

%% Definizione del quantizzatore ad arrotondamento e troncamento

n_bit = 4;                          % Numero di bit
range_y = [min(y), max(y)];         % Range del segnale sinusoidale
N_livelli = 2^n_bit-1;              % Numero di livelli per la codifica
q = max(abs(range_y))*2/N_livelli;         % Passo di quantizzazione - ATTENZIONE PERCHÈ CODIFICA CON SEGNO È SIMMETRICA

% PROBLEMA: IL NUMERO DI LIVELLI DI yq_arr è effettivamente superiore a N_livelli

% Quantizzatore ad arrotondamento
% yq_arr = q * round(y/q);
yq_arr = q * sign(y).*min(abs(round(y/q)),(N_livelli-1)/2);

% Errore di quantizzazione
e_arr = yq_arr - y;

% Quantizzatore a troncamento
% yq_trunc = q * fix(y/q);
yq_trunc = q * sign(y).*min(abs(fix(y/q)),(N_livelli-1)/2);

% Errore di quantizzazione
e_trunc = yq_trunc - y;

% Rappresentazione del segnali sinusoidale originale e dei segnali
% quantizzati sovrapposti
figure
plot(time,y)
xlabel('Time [sec]')
ylabel('Segnale')
hold on
stem(time,yq_arr, 'rx')
stem(time,yq_trunc, 'g.')

%% Salvataggio dei risultati in una struttura
quant(1).data = yq_arr;
quant(1).err = e_arr;
quant(2).data = yq_trunc;
quant(2).err = e_trunc;

save Resultati_Lab10_esercizio_1 quant


% Rappresentazione degli errori di arrotondamento
figure
plot(time,e_arr, 'r')
hold on
plot(time,e_trunc, 'g')
xlabel('Time [sec]')
ylabel('QUANTIZ. ERROR')

