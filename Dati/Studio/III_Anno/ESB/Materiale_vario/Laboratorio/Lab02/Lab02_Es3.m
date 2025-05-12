%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 02
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 1: RR interval time series from two healthy subjects - Holter
% monitoring for 24h
% Dataset available at https://physionet.org/content/rr-interval-healthy-subjects/1.0.0/

%% Primo soggetto (ID: 4040)
data_Sbj1 = importdata('DATA_Lab05_Subject1.txt');

figure(1)
plot(data_Sbj1)
axis tight
xlabel('Numero di battiti cardiaci')
ylabel('Intervallo RR (ms)')
title('Soggetto ID 4040')

%% Calcolare i battiti per minuto e la frequenza cardiaca per ogni intervall RR

bpm_Sbj1 = zeros(size(data_Sbj1));   % Battiti per minuto

F_sbj1 = zeros(size(data_Sbj1));     % Frequenza cardiaca

for i=1:size(data_Sbj1,1)
   F_sbj1(i) = 1/(data_Sbj1(i)/1000);
   bpm_Sbj1(i) = F_sbj1(i)*60;
end

% Battito cardiaco medio
mean_HR_Sbj1 = mean(bpm_Sbj1);


%% Secondo soggetto (ID: 10)
data_Sbj2 = importdata('DATA_Lab05_Subject2.txt');

figure(2)
plot(data_Sbj2)
axis tight
xlabel('Numero di battiti cardiaci')
ylabel('Intervallo RR (ms)')
title('Soggetto ID 10')

% Calcolare i battiti per minuto e la frequenza cardiaca per ogni intervall RR
bpm_Sbj2 = zeros(size(data_Sbj2));   % Battiti per minuto

F_sbj2 = zeros(size(data_Sbj2));     % Frequenza cardiaca

for i=1:size(data_Sbj2,1)
   F_sbj2(i) = 1/(data_Sbj2(i)/1000);
   bpm_Sbj2(i) = F_sbj2(i)*60;
end

% Battito cardiaco medio
mean_HR_Sbj2 = mean(bpm_Sbj2);
