%edge ( (0,2), (0,3) ).
%edge ( (0,3), (0,2) ).

% 1. All edges must form a single, linear loop. No crossing or branching is allowed.
%%%%%%%%%%%%%%%%%%%% 2. The loop must pass through all numbered circles.  
% 3. White circles must be passed through in a straight line.
% 4. Black circles must always be in the corner of a turn.
% 5. The number in each circle must be the sum of the lengths of the 2 straight lines segments going out of that circle. antes de aqui el numero nos la pela

row(0..N-1) :- size(N).
col(0..N-1):- size(N).
point( (X,Y) ) :- row(X), col(Y).

adj( (X,Y), (X,Y+1)) :- row(X), col(Y), col(Y+1). %x es adyacente a y, y no es la ultima
adj( (X,Y), (X+1,Y)) :- row(X), col(Y), row(X+1). %lo mismo verticalmente
%adj(Q,P) :- adj(P,Q).

{edge(P,Q)} :- adj(P,Q).
edge(Q,P) :- edge(P,Q).

used(P) :- edge(P,_). % el primer argumento de un edge siempre es un used
:- used(P), #count{Q: edge(P,Q)}!=2. %no puede ser que si cuento el numero de q tiene que adr 2

%TODO: se necesita una restriccion que se llame conectado, si está usado se ha de poder llegar
% reach((X,Y),(X',Y')) si dos puntos son usados se ha de llegar de una al otro

%clingo --text imprime el programa. El truco está en exprimir reach, hay muchos pares de puntos y andar mirando caminos recursivos es una barbaridad. Usa el mismo truco que en hamiltonian
% se fija un punto raiz y se mira si alguien es accesible desde ese punto raiz. Que punto se puede tomar como raiz? Una de las bolas (SIEMPRE ESTÁ EN EL LOOP) #min sobre las bolas, el predicado reach
% dice si puedes llegar desde la bola mínima o no, se trazan caminos desde una sola bola


ball(B) :- number(B,N), N!=0.
:- ball(B), not used(B).

%TODO: si es blanca, tienen que estar alineadas, si es negra, una vertical y otra horizontal

%aligned(B, P):- ball(B), edge(B,P). %el punto está en linea recta desde la bola, como reach pero solo en linea recta, este es el caso base
%si tengo una arista alineada a una alineada, tambien está alineada. Si hago un count de todas las P que cumplen align (B,P) el numero ha de ser el de la bola en valor absoluto


seg(P,Q) :- edge(P,Q), P < Q.
% que genere al menos 100
%:- #count {P,Q: seg(P,Q)}<100.