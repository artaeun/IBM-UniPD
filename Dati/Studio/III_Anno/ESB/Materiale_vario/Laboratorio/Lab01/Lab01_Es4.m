%% Elaborazione Segnali Biomedici - Soluzione Laboratorio 01
%  Prof. Veronese Mattia - UNIPD

%% OPENING
clear all
close all
clc

%% Esercizio 4
% Input la dimensione righe della matrice A
flag=true;
while flag==true
    m = input('Inserisci numero di righe per la matrice A:');
    flag = m<=0;
end

% Input la dimensione colonne della matrice A
flag=true;
while flag==true
    n = input('Inserisci numero di colonne per la matrice A:');
    flag = n<=0;
end

% Input gli elementi della matrice A
disp('Inserisci i valori della matrice A (scrivi un valore e premi invio)')
A=[];
for i=1:m
    for j=1:n
        A(i,j)=input('');
    end
end

% Creo la matrice B esattamente uguale alla matrice A
B = A;
 
for i = 1 : m
    if mod(i,2)==0
        % Caso riga pari
        B = ordina_crescente(B, i, n);
    else
        % Caso riga dispari
        B = ordina_decrescente(B, i, n);
    end
end
disp('MATRICE A:') 
disp(A)
disp('MATRICE B:') 
disp(B);