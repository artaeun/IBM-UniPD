%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 03
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio BIOPAC

% 1) Caricare e plottare il segnale EMG
load EMG_bothArm_crescente.mat

dt = 0.002;                                 % Tempo di campionamento [s]
N_campioni = size(data,1);                  % Numero totale di campioni
duration = (N_campioni-1)*dt;                 % Durata di acquisizione del segnale
time = linspace(0,duration,N_campioni);   % Vettore tempo

figure(1)
subplot(2,1,1)
% plot(time, data(:,1))
plot(data(:,1))
xlabel('Time [s]')
ylabel('mV')
title('EMG')
subplot(2,1,2)
plot(time, data(:,2))
xlabel('Time s[]')
ylabel('mV')
title('Integrated EMG')

%% 2) Creare matrice contenente, valore medio, valore massimo, valore minimio e picco-to-picco per ogni singola contrazione del braccio dominante
ind_contractions_arm1 = [979,2001;2951,4051;4993,5993;6922,8022;8887,10087;11090,11990;12890,13990;15010,16210];

tot_contractions_arm1 = size(ind_contractions_arm1, 1);
stats_arm1 = zeros(tot_contractions_arm1, 4);

for i=1:tot_contractions_arm1
    contractions_arm1 = data(ind_contractions_arm1(i,1):ind_contractions_arm1(i,2),1);
    stats_arm1(i, 1) = mean(contractions_arm1);
    stats_arm1(i, 2) = max(contractions_arm1);
    stats_arm1(i, 3) = min(contractions_arm1);
    stats_arm1(i, 4) = stats_arm1(i, 2) - stats_arm1(i, 3);
    
end     % for


% Creare matrice contenente, valore medio, valore massimo, valore minimio e picco-to-picco per ogni singola contrazione del braccio NON dominante
times_contractions_arm2 = [17980,18930;19960,21000;21980,22980;23970,24980;25940,27030;27940,29080;30010,30910;31940,32900];

tot_contractions_2 = size(times_contractions_arm2, 1);
stats_arm2 = zeros(tot_contractions_2, 4);

for i=1:tot_contractions_2
    contractions_arm2 = data(times_contractions_arm2(i,1):times_contractions_arm2(i,2),1);
    stats_arm2(i, 1) = mean(contractions_arm2);
    stats_arm2(i, 2) = max(contractions_arm2);
    stats_arm2(i, 3) = min(contractions_arm2);
    stats_arm2(i, 4) = stats_arm2(i, 2) - stats_arm2(i, 3);
end     % for

disp('VERIFICA LE VARIABILI stats_arm* PER LE SOLUZIONI ESERCIZIO - PARTE 2')

%% 3) Per ogni parametro rilevato (mean, max, …) per le 5 misurazioni a forza massima calcolare media e SD 
stats_arm1_max_contractions = zeros(2, 4);
stats_arm2_max_contractions = zeros(2, 4);

for i=1:4
    % Braccio dominante
    stats_arm1_max_contractions(1,i) = mean(stats_arm1(4:end,i));
    stats_arm1_max_contractions(2,i) = std(stats_arm1(4:end,i));
    % Braccio non dominante
    stats_arm2_max_contractions(1,i) = mean(stats_arm2(4:end,i));
    stats_arm2_max_contractions(2,i) = std(stats_arm2(4:end,i));
    
end


% 4) Per ogni parametro rilevato (mean, min, max, P-P) confrontare la media ottenuta 
% al passo precedente con il valore relativo al gruppo di dati a forza minima 
% e determinare l’aumento percentuale nelle due diverse situazioni
% Aumento percentuale del braccio dominante
aumento_perc_arm1 = zeros(1,4);
for i=1:size(aumento_perc_arm1, 2)
    aumento_perc_arm1(:,i) = (stats_arm1_max_contractions(1,i)-stats_arm1(1,i))/stats_arm1(1,i)*100;
end     % for

% Aumento percentuale del braccio NON dominante
aumento_perc_arm2 = zeros(1,4);
for i=1:size(aumento_perc_arm2, 2)
    aumento_perc_arm2(:,i) = (stats_arm2_max_contractions(1,i)-stats_arm2(1,i))/stats_arm2(1,i)*100;
end     % for

disp('VERIFICA LE VARIABILI aumento_perc_arm* PER LE SOLUZIONI ESERCIZIO - PARTE 3')

