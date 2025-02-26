%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 08
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 2

Fs=1;       % Frequenza di campionamento
Ts=1/Fs;    % Periodo di campionamento
T0=16;      % Periodo segnale
np=2;       % Periodi completi di campionamento

N=np*T0;    % Numero campioni
Nzp=512;    % Zero-padding


% Segnale sinusoidale
t=Ts*(0:1:N-1)';
x=sin(2*pi*t/T0);

subplot(3,1,1)
plot(t,x, 'o-')
xlabel('tempo(sec)')
title('segnale')


%% Spettro del segnale dopo padding di 0 zeri
FTx=fft(x);
S=(abs(FTx).^2)/N;
f_FT=(0:Fs/N:Fs-Fs/N);

f_FT=f_FT(1:N/2);   % Elimino la seconda meta' delle stime
S=S(1:N/2);         % Elimino la seconda meta' delle stime

subplot(3,1,2)
plot(f_FT,S,'o-')
axis([0, Fs/2, 0, max(abs(S))])
title('densità spettrale di potenza dopo padding di 0 zeri')
xlabel('frequenza (Hz)')


%% Spettro del segnale con zero-padding
FTx_zp=fft(x,Nzp);
S_zp=(abs(FTx_zp).^2)/N;
f_FT_zp=(0:Fs/Nzp:Fs-Fs/Nzp);

f_FT_zp=f_FT_zp(1:Nzp/2);   % Elimino la seconda meta' delle stime
S_zp=S_zp(1:Nzp/2);         % Elimino la seconda meta' delle stime

subplot(3,1,3)
plot(f_FT_zp,S_zp,'-o')
axis([0, Fs/2, 0, max(abs(S_zp))])
title('densità spettrale di potenza dopo padding di 480 zeri')
xlabel('frequenza (Hz)')
