%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 05
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 2
% Caricare i dati contenuti in DATA_Lab12_Esercizio2.mat
load DATA_Lab12_Esercizio2

%% 
% 1) Visualizzare il segnale EEG corrispondente alla finestra temporale 20 – 30 s,
% inserendo delle linee verticali di colore diverso in corrispondenza della 
% comparsa di un numero o di una lettera. 

Fs   = 500; % Frequenza di campionamento [Hz]
time = [1/Fs:1/Fs:length(pz)/Fs];

figure(1),
plot(time,pz)
hold on,
plot([time_Frequent_Digit;time_Frequent_Digit],ylim,'g')
hold on,
plot([time_Rare_Letter;time_Rare_Letter],ylim,'r')
xlim([20 30])
xlabel('Time [s]')
ylabel('ERP [\muV]')
title('Segnale Misurato Pz')
legend('Signal','Digit Stimulus','Letter Stimulus')


%%
% 2) Calcolare il numero totale di stimoli (con numeri e lettere) ricevuti
% durante l’esperimento. Crerae un vettore contenente tutti gli stimoli in
% ordine di tempo di comparsa.

points_digit_raw    = int32(time_Frequent_Digit*Fs);        % Stimoli con numero (frequenti)
points_letter_raw   = int32(time_Rare_Letter*Fs);           % Stimoli con lettere (rari)
onsets      = sort([points_digit_raw points_letter_raw]);   % Totale stimoli (con numeri & lettere)
N_tot_onsets = length(onsets);                              % Numero totale di stimoli


%%
% 3) Dividere il segnale in segmenti corrispondenti all’attività registrata dal momento 
% in cui compare lo stimolo fino ad 1 secondo dopo. 

epoch_length    = 1;
points_epoch    = epoch_length*Fs;  % Totale campioni per ogni epoca
time_epoch        = [1/Fs:1/Fs:points_epoch/Fs];
epoch       = zeros(length(onsets),points_epoch);           % Totale epoche

for i = 1:length(onsets)
    current_epoch = pz(onsets(i):onsets(i)+points_epoch-1);
    epoch(i,:)    = current_epoch;
end


%%
% 4) Dai segmenti ricavati dal punto 2), estrapolare quelli corripondenti all'attivita' registrata
% dal momento in cui compare uno stimolo con lettera, calcolare la media
% mobile e plottarla

epoch_letter       = zeros(length(points_letter_raw),points_epoch);           % Totale epoche

for i = 1:length(points_letter_raw)
    current_epoch_letter = pz(points_letter_raw(i):points_letter_raw(i)+points_epoch-1);
    epoch_letter(i,:)    = current_epoch_letter;
end

% figure(2)
% plot(time_erp,epoch_letter)

% Media sincrona
mean_letter = sum(epoch_letter,1)/size(epoch_letter,1);

figure(2)
plot(time_epoch, mean_letter)
xlabel('Time [s]')
ylabel('ERP [\muV]')
title('Media sincrona')

 