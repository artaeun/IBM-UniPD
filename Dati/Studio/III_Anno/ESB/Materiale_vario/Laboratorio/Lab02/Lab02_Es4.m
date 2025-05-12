%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 02
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 3

% Caricare il file DATA_Lab06_TestFisiologico.xlsx
data = xlsread('DATA_Lab05_TestFisiologico.xlsx');

label_signali = ["EMG", "GSR", "THE", "HR"];
tot_signali = size(data,2)-1;

figure
% Plot dei segnali
for i=1:tot_signali
    
    subplot(tot_signali,1,i)
    plot(data(:,1),data(:,i+1))
    title(label_signali(i))
    
end % for

% Creare una struttura array per i signali, che contenga i nomi dei
% segnali, i dati dei segnali, il vettore tempo e un cell array 'stat' 1x2
% contenente una matrice con il valore minimo e massimo di ciascun segnale,
% e un vettore con la standard deviation di ciascun segnale
segnali = struct('nome_segnale', label_signali);

segnali.dati = data(:,2:tot_signali+1);
segnali.tempo = data(:,1);

max_min_signali = zeros(tot_signali,2);
std_signali = zeros(tot_signali,1);

for i=1:tot_signali
    
    max_min_signali(i,1) = max(data(:,i+1));
    max_min_signali(i,2) = min(data(:,i+1));
    std_signali(i,1) = std(data(:,i+1));

end % for

segnali.stat = {max_min_signali, std_signali};

