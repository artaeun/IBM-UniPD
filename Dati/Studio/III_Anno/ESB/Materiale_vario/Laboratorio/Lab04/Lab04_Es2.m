%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 04
% Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc


%% Esercizio 2

%Creazione del segnale
n=11;
z=linspace(0, pi, n);
x = 5*cos(z) ;
y = 1./(1+ x.^2);

%Plot data
figure
plot(x ,y ,'og')

%Calcolo interpolazione
m = 100;
interpx = linspace(-5, 5 , m);
interpy_linear= interp1 (x, y, interpx, 'linear');
interpy_spline= interp1 (x, y, interpx, 'spline');

hold on
plot (interpx, interpy_linear, 'r')
plot (interpx, interpy_spline, 'b')
legend ('dati', 'Interpolazione Lineare','Interpolazione Spline')
xlabel('x (u.a.)')
ylabel('y (u.a.)')