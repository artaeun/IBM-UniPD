clc
clear all
close all

%% LOAD DATA
load('ECG.mat')

%% SETTING
Fs=1000; %Hz
time =(0:1/Fs:(length(ECG)-1)/Fs);
time=time';
Durata=time(end);
figure(1)
subplot(211)
plot(time,ECG,'k');
xlabel('Time (secs)')
ylabel('ECG (normalised units)')
title('RAW DATA')
%% Q1) FILTRO
ECG_filtrato = filter([0.25 0.25 0.25 0.25],1,ECG);
subplot(212)
plot(time,ECG_filtrato,'r');

%% Q2) PICCHI R
%Soluzione aritmetica
Np=12; %PARAMETRO DETERMINATO VISIVAMENTE DAL TRACCIATO
temp=ECG_filtrato;
imax=zeros(Np,1);
for i=1:12
    [~ , imax(i)]=max(temp);
    temp(imax(i)-100:imax(i)+100)=0;
end
imax=sort(imax); %I picchi non vengono estratti in ordine
tempo_picchi = time(imax);
ECG_filtrato_picchi = ECG_filtrato(imax);

%Soluzione manuale (ricavando le coordinate dei punti direttamente dal
%grafico)
% tempo_picchi = [0.295, 1.012, 1.711, 2.433, 3.161, 3.848, 4.573, 5.32,6.014, 6.724, 7.453, 8.167];
% ECG_filtrato_picchi = [2.65205, 2.65228, 2.65114, 2.64793, 2.65038, 2.65266, 2.65121, 2.6519, 2.65022, 2.65129, 2.6474, 2.65038];

%Plot picchi R
figure(1)
subplot(212)
hold on
stem(tempo_picchi,ECG_filtrato_picchi)
xlabel('Time (secs)')
ylabel('ECG (normalised units)')
title('FILTERED ECG - RICONOSCIMENTO COMPLESSO R')
legend('ECG','Picco R')

%% Q3) TACOGRAMMA
N = Np-1; %Il tacogramma contiene il numero di intervalli
Tacogramma = zeros(Np-1,1); 
bpm = zeros(size(Tacogramma));

for i=1:length(ECG_filtrato_picchi)-1
    Tacogramma(i) = (tempo_picchi(i+1)-tempo_picchi(i))*1000;   % Tacogramma [ms]
    bpm(i) = (1/(Tacogramma(i)/1000))*60; % BPM
end

tacogramma1 = diff(tempo_picchi)*1000;
bpm1=(1./tacogramma1./1000)*60;
%% Q4) Dal tacogramma costruito, ottenere la misura del battito cardiaco 
% medio e il suo range minimo e massimo
Battito_medio = mean(bpm);
Battito_min = min(bpm);
Battito_max = max(bpm);

%% Salvataggio risultati
save Risultati.mat Durata ECG_filtrato Tacogramma N Battito_medio Battito_min Battito_max
saveas(gcf,'ECG.fig')