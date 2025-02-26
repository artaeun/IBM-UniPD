%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 01
%  Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% ESRECIZIO 2

% 1) Caricare il file DATA_Lab02_Es02.xlsx
data = xlsread ('DATA_Lab03_Es02.xlsx');

% 2) Craere due matrici, una per gli uomini e una per le donne, contenenti la
% loro temperatura corporea e il battito cardiaco

% Matrice uomni
male = 0;
idx_male = find(data(:,2)==0);
N_male = length(idx_male);
data_male = zeros(N_male,2);
data_male(:,1) = data(idx_male,1);
data_male(:,2) = data(idx_male,3);

% Matrice donne
female = 1;
idx_female = find(data(:,2)==1);
N_female = length(idx_female);
data_female = zeros(N_female,2);
data_female(:,1) = data(idx_female,1);
data_female(:,2) = data(idx_female,3);

% 3) Plot
subplot(2,1,1)
plot(data_male(:,1), data_male(:,2))
xlabel('Body Temperature [F]')
ylabel('Heart Rate [BPM]')
title('Male')
subplot(2,1,2)
plot(data_female(:,1), data_female(:,2))
xlabel('Body Temperature [F]')
ylabel('Heart Rate [BPM]')
title('Female')


