%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 01
%  Prof. Veronese Mattia - UNIPD

%% Opening
clear all
close all
clc

%% ESERCIZIO 1
% Vettore riga v
v = [5, 9, -6, 0, 0.2, 3.6]; % Altrimenti v = [5 9 -6 0 -0.2 3.6];

% Vettore colonna W
w = [0, 0.1, -5, -3, 2.3, 9]'; % Altrimenti v = [0; 0.1; -5; -3; 2.3; 9];

% Salvare in A la somma del vettore riga v e  del vettore colonna w
A = v' + w;

% Salvare in B il prodotto scalare di v per w (usare il commando dot)
B = dot(v',w);

%Salvare in C gli elementi di posto pari di v
C = v(2:2:end);

%Salvare in D cinque copie del vettore v
D = kron(ones(5,1),v);

%Salvare in E gli elementi di posto multiplo di 4 di D
E = D(4:4:end);

%Salvare in F la matrice w*v
F = w*v;

%Salvare in G la matrice costituita dalla seconda fino alla quarta riga di
%F e dalla prima fino alla terza Colonna di F
G = F(2:4,1:3);
