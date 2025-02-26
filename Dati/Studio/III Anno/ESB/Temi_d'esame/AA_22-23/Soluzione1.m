clc
clear all
close all

%% OPENING
load TEST01.mat

%setting
N = length(ECG);
Fc = 500;
T = 1/Fc;
t = 0:T:T*(N-1);

%% DOMANDA 1 - CROPPING
tstart = 0.5;
tend = (N-1)*T+0.5; %tcropping 1000 samples
ind = intersect(find(t>=tstart),find(t<=tend)-1);
time = t(ind);
segnale_originale = ECG(ind);

media_segnale_originale = mean(segnale_originale);
min_segnale_originale = min(segnale_originale);
max_segnale_originale = max(segnale_originale);

%% DOMANDA 2 - FILTRAGGIO
% Definisco poli
F = 5;
theta=(2*pi/Fc)*F;
poli = [0.95*exp(1i*theta), 0.95*exp(-1i*theta)];
%Definisco zeri
zeri = [0 1];

b = poly(zeri);
a = poly(poli);
%Imposto guadagno unitario a 250 Hz
G=1/10;
b=b*G;

%filtro
[H,F]=freqz(b,a,2048,Fc);

modulo = abs(H); 
fase = angle(H)*360/(2*pi); %Definita in gradi

%segnale filtrato
segnale_filtrato = filter(b,a,segnale_originale);
media_segnale_filtrato = mean(segnale_filtrato);
min_segnale_filtrato = min(segnale_filtrato);
max_segnale_filtrato = max(segnale_filtrato);

%% DOMANDA 3 - SPETTRO
Ns = 1000; %NO ZERO PADDING
FTx=fft(segnale_originale,Ns); 
S=(abs(FTx).^2)/Ns; 
FTx_filtrato =fft(segnale_filtrato,Ns); 
S_filtrato=(abs(FTx_filtrato).^2)/Ns; 
f_FT=(0:Fc/Ns:Fc-Fc/Ns);

% POWER 0-10Hz
fstart = 0;
fend = 10;
indF = intersect(find(f_FT>=fstart),find(f_FT<=fend));
potenza_originale=mean(S(indF));
potenza_filtrato=mean(S_filtrato(indF));


%% FIGURE
% SEGNALI
plot(time,segnale_originale);
hold on
plot(time,segnale_filtrato,'r')
title('SEGNALI')
xlabel('Tempo (secs)')
ylabel('ECG (mV)')
legend('Segn. Originale','Segn Filtrato')

% ZP figure
figure
zplane(b,a)
title('Diagramma ZERI/POLI');

% Diagramma di Bode del filtro
figure
subplot(2,1,1)
plot(F,modulo)
title('modulo')
xlabel('Hz')
ylabel('mV/Hz')
subplot(2,1,2)
plot(F,fase)
title('fase')
xlabel('Hz')
ylabel('Degree')

%SPETTRO
figure
plot(f_FT(1:Ns/2),S(1:Ns/2))
hold on
plot(f_FT(1:Ns/2),S_filtrato(1:Ns/2),'r')
title('Peridiogramma')
ylabel('PSD [mV^2/Hz]')
xlabel('Hz')
legend('Segn. Originale','Segn Filtrato')