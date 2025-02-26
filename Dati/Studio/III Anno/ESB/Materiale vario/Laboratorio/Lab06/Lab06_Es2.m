%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 06
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 2

n = [0:1:10];
% Risposta h(n)
h = (0.5).^n;
% Ingresso x(n)
x = 1.2*ones(size(n));
% Uscita
y = conv(h,x);

% Rappresentazione del segnale h, x e y
figure
subplot(3,1,1)
stem(n,h)
xlabel('n')
ylabel('h(n) (u.a.)')
title('Risposta Impulsiva')
axis([0 25 0 3])
subplot(3,1,2)
stem(n,x)
xlabel('n')
ylabel('x(n) (u.a.)')
title('INGRESSO')
axis([0 25 0 3])
subplot(3,1,3)
stem(n,y(1:length(n)))
xlabel('n')
ylabel('y(n) (u.a.)')
title('USCITA')
axis([0 25 0 3])

