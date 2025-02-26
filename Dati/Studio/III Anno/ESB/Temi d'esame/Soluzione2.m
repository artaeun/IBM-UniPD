clc
clear all
close all

%% OPENING
%load data
load TEST02.mat

%setting
N = length(EMG);
Fc = 500;
T = 1/Fc;
time = 0:T:T*(N-1);
segnale_originale=EMG;

%% DOMANDA 1 - CROPPING SEGNALE ORIGINALE
tTaglio= [2,6, 10, 14, 18]; %secondi
durata = 2; %secondi
Nepoche = length(tTaglio);

%analisi epoche originali
for i=1:Nepoche
    tStart = tTaglio(i);
    tEnd = tStart + durata;
    ind = intersect(find(time>=tStart),find(time<=tEnd));
    epoche(i).ind = ind;
    epoche(i).segnale = segnale_originale(ind)';
end
media_segnale_originale = mean([epoche.segnale]);
min_segnale_originale = min([epoche.segnale]);
max_segnale_originale = max([epoche.segnale]);

%% DOMANDA 2 - FILTRAGGIO
% Definisco poli
F = 50;
theta=(2*pi/Fc)*F;
poli = [0.95*exp(1i*theta), 0.95*exp(-1i*theta) 0.95];
%Definisco zeri
zeri = [+1i -1i -1];

%Progetto il filtro e definisco il guadagno
b = poly(zeri);
a = poly(poli);
G=polyval(b,1)/polyval(a,1);
b=b/G;
segnale_filtrato = filter(b,a,segnale_originale);


%% DOMANDA 3 - SPETTRO
FTx=fft(segnale_originale,N); 
S=(abs(FTx).^2)/N; 
P_segnale_originale = S(1:N/2);
FTx_filtrato =fft(segnale_filtrato,N); 
S_filtrato=(abs(FTx_filtrato).^2)/N; 
P_segnale_filtrato = S_filtrato(1:N/2);
f_FT=(0:Fc/N:Fc-Fc/N);

% POWER 0-50Hz
fstart = 0;
fend = 50;
indF = intersect(find(f_FT>=fstart),find(f_FT<=fend));
potenza_originale=mean(S(indF));
potenza_filtrato=mean(S_filtrato(indF));



%% FIGURE

% SEGNALI
figure
plot(time,EMG);
hold on
plot(time,segnale_filtrato,'r')
xlabel('Time (secs)')
ylabel('EMG (mV)')
title('CONFRONTO SEGNALI')
legend('Segnale Originale','Segnale Filtrato')

% ZP figure
figure
zplane(b,a)

% Diagramma di Bode del filtro
figure
[H,F]=freqz(b,a,2048,Fc);
subplot(2,1,1)
plot(F,abs(H))
title('modulo')
xlabel('Hz')
subplot(2,1,2)
plot(F,angle(H))
title('fase')
xlabel('Hz')

%PSD
figure
plot(f_FT(1:N/2),S(1:N/2))
hold on
plot(f_FT(1:N/2),S_filtrato(1:N/2),'r')
xlabel('Hz')
ylabel('PSD')
title('Power Spectral Density [0-250Hz]')
legend('Segnale Originale','Segnale Filtrato')
