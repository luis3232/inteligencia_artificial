% Aluno: Luís Aurelio Campos
% RA: 2017207390
% Universidade Tuiuti do Paraná
% Ciências da Computação     
          
% EXERCICIO NUMERO 1, LISTAR ELEMENTOS REPETIDOS
elem_repetidos([],[]).
elem_repetidos([X|XsP],YsP) :- partition(=(X),XsP,Es,Xs), (Es=[] -> YsP=Ys; YsP=[X|Ys]), elem_repetidos(Xs,Ys).   
          
% EXERCICIO NUMERO 2, INTERCALADA
intercalada(L, [], L):- !.
intercalada([], L, L):- !.
intercalada([X|LIST1], [Y|LIST2], [X,Y|LIST3]):- intercalada(LIST1, LIST2, LIST3).

% EXERCICIO NUMERO 4, ONDERNACAO DE LISTA
distribuir_listas([],[],[]).
distribuir_listas([X],[X],[]).
distribuir_listas([X,Y|Z],[X|A],[Y|B]) :- distribuir_listas(Z,A,B). 

intercalar_listas([],L,L).
intercalar_listas(M,[],M).
intercalar_listas([X|M],[Y|L],[Y|C]) :- X > Y, intercalar_listas([X|M],L,C).
intercalar_listas([X|M],[Y|L],[X|C]) :- X =< Y, intercalar_listas(M,[Y|L],C).

ordenada([],[]).
ordenada([X],[X]).
ordenada([X,Y|Z],S) :- distribuir_listas([X,Y|Z],A,B), ordenada(A,As), ordenada(B,Bs), intercalar_listas(As,Bs,S).

% EXERCICIO NUMERO 3, ONDERNACAO DE LISTA COM INSERÇÃO
insercao_ord(N, X, S) :- append([N], X, M), ordenada(M, S).
