function [ M ] = ordina_crescente( M, r, c )
%ordina_crescente funzione che implementa l'algoritmo del selection sort
%   La funzione accetta 3 parametri (la matrice, l'indice della riga da
%   ordinare e il numero di colonne) e restituisce la matrice con la
%   r-esima riga ordinata in modo crescente
 
    for i = 1 : c-1
        i_min = i;
        j = i+1;
        for j = j : c
            if M(r, j) < M(r, i_min)
                % Se vero, aggiorno l'indice dell'elemento minimo
                i_min = j;
             end
         end
 
        % Blocco di codice relativo allo scambio
        temp = M(r, i);
        M(r, i) = M(r, i_min);
        M(r, i_min) = temp;
    end
end