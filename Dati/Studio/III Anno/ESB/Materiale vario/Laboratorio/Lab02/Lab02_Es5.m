%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 02
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 3
% 1) Caricare il file contenente i dati
load DATA_Lab05_es5.mat

%% 2) Rappresentare il segnale glicemico in funzione del tempo,
% indicando la soglia di valori normali (70-250 mg/dl) con due linee rosse

low_level_glucose = 70;       % mg/dl    
upper_level_glucose = 250;    % mg/dl   

% Durata di acqusizione del segnale glicemico
t_c = 5;    % Tempo di campionamento [minuti]
CGM_values = CGM.value;
N=length(CGM_values); % Numero di campioni
duration = t_c*N/60;    % Tempo totale di acquisizione [ore]
time = linspace(0, duration, N);

figure(1)
plot(time, CGM_values )
yline(upper_level_glucose,'-r')
yline(low_level_glucose,'-r')
xlabel('Time (hours)')
ylabel('Glucose (mg/dl)')
title('CGM signal')


%% 3) Identificare gli eventi di ipoglicemia ed iperglicemia e
% calcolare la loro durata nel corso di tutto il tracciato 

% Indici eventi ipoglicemici e iperglicemici
idx_eventi_ipoglicemici = find(CGM_values <low_level_glucose);
idx_eventi_iperglicemici = find(CGM_values >upper_level_glucose);

% Corrispettivi tempi degli eventi ipoglicemici e iperglicemici
t_eventi_ipoglicemici = time(idx_eventi_ipoglicemici);
t_eventi_iperglicemici = time (idx_eventi_iperglicemici);

% Calcola la differenza tra gli indici successivi
diff_ipoglicemia = diff(idx_eventi_ipoglicemici);
diff_iperglicemia = diff(idx_eventi_iperglicemici);

% Trova gli indici degli eventi che terminano
idx_end_eventi_ipoglicemia = find(diff_ipoglicemia > 1);
idx_end_eventi_iperglicemia = find(diff_iperglicemia > 1);

% Numero totale di eventi ipoglicemici e iperglicemici
N_eventi_ipoglicemia = length(idx_end_eventi_ipoglicemia)+1; % +1 per quello finale 
N_eventi_iperglicemia = length(idx_end_eventi_iperglicemia)+1;

% Vettori dove inserire la durata degli eventi ipoglicemici e iperglicemici
durata_eventi_ipoglicemia = zeros(N_eventi_ipoglicemia,1);
durata_eventi_iperglicemia = zeros(N_eventi_iperglicemia,1);

% Calcolo della durata degli eventi ipoglicemici 
start = 1;
for i=1:N_eventi_ipoglicemia
    
    if i == N_eventi_ipoglicemia
            durata_eventi_ipoglicemia(i,:) = t_eventi_ipoglicemici(end)- t_eventi_ipoglicemici(start);
    else
        durata_eventi_ipoglicemia(i,:) = t_eventi_ipoglicemici(idx_end_eventi_ipoglicemia(i))-t_eventi_ipoglicemici(start);
        start = idx_end_eventi_ipoglicemia(i) + 1;
    end % end if
    
end % for

% Calcolo della durata degli eventi iperglicemici
start = 1;
for i=1:N_eventi_iperglicemia
    
    if i == N_eventi_iperglicemia
            durata_eventi_iperglicemia(i,:) = t_eventi_iperglicemici(end)- t_eventi_iperglicemici(start);
    else
        durata_eventi_iperglicemia(i,:) = t_eventi_iperglicemici(idx_end_eventi_iperglicemia(i))-t_eventi_iperglicemici(start);
        start = idx_end_eventi_iperglicemia(i) + 1;
    end % end if
    
end % for
