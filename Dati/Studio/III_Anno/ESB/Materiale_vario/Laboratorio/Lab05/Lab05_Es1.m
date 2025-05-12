%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 05
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% INIZIALIZZAZIONE DATI e VARIABILI

% Load cortical evoked potentials related to electrical stimulation of the esophagus
% Data courtesy of Dr. M.V. Kamath,
% McMaster University, Hamilton, ON, Canada.
load DATA_Lab12_Esercizio1

%Inizializzazione dati
d(:,1) = PE.E11;
d(:,2) = PE.E22;
d(:,3) = PE.E33;
d(:,4) = PE.E44;
d(:,5) = PE.E55;


% Parameters of the data acquisition
fs = 1000;     % sampling rate
T = 1/fs;    % sampling interval in seconds
N = size(d,1); % number of samples in each signal
tend = (N-1)*T;
time = linspace(0, tend, N);

%% Synchronous average (MEDIA SINCRONA)

% Compute the average of the trials
y = mean(d,2);

%% PLOT

% Plot multiple ERPs in the same figure
k_min = 1;              % first signal to be plotted
k_max = size(d,2);      % last signal to be plotted

figure(1);

for k = k_min:k_max+1
    
    % Extract the current signal from the matrix
    if k <= k_max
        
        % Signal of trial k
        y_k = d(:,k);
        
        % Plot the current signal in the proper subplot
        subplot(k_max+1, 1, k);
        plot(time, d(:,k), 'k-');
        title(['ERP #',num2str(k)]);
        xlabel('Time (secs)');
        ylabel('ERP*10000 (V)');
        axis tight;
        
    else
        
        % Plot the average of the trials in the proper subplot
        subplot(k_max+1, 1, k);
        plot(time, y, 'k-');
        title('Synchronous Average 5 sweeps')
        xlabel('Time (secs)');
        ylabel('ERP*10000 (V)');
        axis tight;
        
    end
    
end





