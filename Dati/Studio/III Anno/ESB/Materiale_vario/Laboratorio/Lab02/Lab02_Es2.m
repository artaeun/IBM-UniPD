%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 02
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 2
% Caricare il file contenente il segnale EMG
data = xlsread('DATA_Lab05_EMGforce.xlsx');

time = data(:,1); % Time in seconds with sampling rate = 2000 Hz
force = data(:,2); % Force in arbitrary units 
emg = data(:,3); % EMG signal in mV

% Normalizzare il segnale EMG in modo che il minimo sia 0 e il massimo sia
% 100
force_norm= 100*(force-min(force))/(max(force)-min(force));

%% 1) Rappresentare la forza e amplitudine del segnale EMG 
figure(1); 
subplot(2,1,1)
plot(time, force_norm)
axis tight
xlabel('Time (seconds)')
ylabel('Force (%MVC)')
subplot(2,1,2)
plot(time, emg)
axis tight
xlabel('Time (seconds)')
ylabel('EMG amplitude (mV)')
axis tight;

%% 2) Estrapolare una porzione del segnale EMG che corrisponde ad una
% contrazione muscolare volontaria (ad esempio nell'intervallo temporale
% 17-21.48 s) e la corrispettiva forza. Plottare i due segnali in due
% riquadri separati.
time_start_contraction = 17;    % Seconds
time_end_contraction = 21.48;   % Seconds
contraction_force = find((time>time_start_contraction)&(time<time_end_contraction));

figure(2)
subplot(2,1,1)
plot(time(contraction_force),force_norm(contraction_force))
axis tight
xlabel('Time (seconds)')
ylabel('Force (%MVC)')
subplot(2,1,2)
plot(time(contraction_force),emg(contraction_force))
axis tight
xlabel('Time (seconds)')
ylabel('EMG amplitude (mV)')
axis tight
savefig('contrazione_muscolare.fig')

%% 3) Data una soglia di forza di 60 [%MVC], trova dove il segnale e'
% maggiore della soglia. Plottare il segnale originale di forza indicando
% la soglia con una linea orizzontale, e il segnale di forza "sogliato", in
% riquadri diversi
threshold_force = 60;
idx = find(force_norm>threshold_force);
force_thresholded = force_norm;

force_thresholded(idx) = threshold_force;

figure(3); 
subplot(2,1,1)
plot(time, force_norm)
hold on
yline(threshold_force, 'r')
axis tight
xlabel('Time (seconds)')
ylabel('Force (%MVC)')
title('Original force signal')
subplot(2,1,2)
plot(time, force_thresholded)
axis tight
xlabel('Time (seconds)')
ylabel('Force (%MVC)')
title('Thresholded force signal')




