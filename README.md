# LFyA
Consideraciones:
• La entrada al algoritmo es la siguiente:
(a) La primera l ́ınea contiene el alfabeto, separando cada s ́ımbolo
por un espacio.
(b) La segunda l ́ınea contiene el conjunto de estados, separando
cada estado por un espacio.
(c) La tercera l ́ınea contiene el estado inicial.
(d) La cuarta l ́ınea el conjunto de estados finales, separados por
un espacio.

(e) Las siguientes n l ́ıneas, donde n es el n ́umero de estados, con-
tienen las filas de la tabla de transiciones. Se usar ́a la letra V ,

para indicar que el aut ́omata no se mueve a ning ́un estado.
(f) La siguiente l ́ınea contiene el n ́umero de palabras m que ser ́an
procesadas por el aut ́omata. Finalmente, las  ́ultimas m l ́ıneas
contienen las palabras a procesar.
• La salida del programa es la siguiente: m l ́ıneas donde cada l ́ınea
indique si la palabra w es o no parte del lenguaje del aut ́omata.

1

0 1
→ ∗q0 q1 q1
q1 q0 q0

Considere el automata de arriba, la entrada al programa sera la siguiente:
0 1
q0 q1
q0
q0
q1 q1
q0 q0
5
0101
1000
111
0
La salida del programa debe ser:
0101 pertenece al lenguaje
1000 pertenece al lenguaje
pertenece al lenguaje
111 no pertenece al lenguaje
0 no pertenece al lenguaje

2

0 1
→ q0 {q0, q1} {q0}
q1 ∅ {q2}
∗q2 ∅ ∅
