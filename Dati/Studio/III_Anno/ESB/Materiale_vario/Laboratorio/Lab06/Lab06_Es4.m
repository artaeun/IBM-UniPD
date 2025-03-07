%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 06
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 4
% Realizzazione sistema MA

% Coefficienti del sistema
B = [1 1 1 1 1];
A = [1];

% Segnale id ingresso
n = [0:1:30]; %Campioni a disposizione
Ts = 0.01;    %Passo di campionamento
f0 = [20, 30, 40];


for i=1:length(f0)

    x = sin(2*pi*f0(i)*n*Ts);
    y = filter(B,A,x);

    % Rappresentazione grafica dei segnali
    figure(i)
    subplot(2,1,1)
    stem(n,x)
    ylabel('x(n) (u.a.)')
    title(['ingresso (f0=' num2str(f0(i)) ')'])
    subplot(2,1,2)
    stem(n,y)
    xlabel('n (u.a.)')
    ylabel('y(n) (u.a.)')
    title('uscita')

end





