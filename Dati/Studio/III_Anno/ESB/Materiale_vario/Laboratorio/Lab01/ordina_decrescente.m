function [ M ] = ordina_decrescente( M, r, c )
 %ordina_decrescente funzione che implementa l'algoritmo del selection sort
%   La funzione accetta 3 parametri (la matrice, l'indice della riga da
%   ordinare e il numero di colonne) e restituisce la matrice con la
%   r-esima riga ordinata in modo decrescente
 
    for i = 1 : c-1
        i_max = i;
        j = i+1;
        for j = j : c
            if M(r, j) > M(r, i_max)
                i_max = j;
             end
        end
 
        temp = M(r, i);
        M(r, i) = M(r, i_max);
        M(r, i_max) = temp;
    end
end