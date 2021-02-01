# !/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Fernando Rodrigo Aguilar Javier
# Author email: faguilar@comunidad.unam.mx
# Detalles del codigo
# La primera l ́ınea contiene el alfabeto, separando cada s ́ımbolo por un espacio.
# La segunda l ́ınea contiene el conjunto de estados, separando cada estado por un espacio.
# La tercera l ́ınea contiene el estado inicial.
# La cuarta l ́ınea el conjunto de estados finales, separados por un espacio.
# Las siguientes n l ́ıneas, donde n es el n ́umero de estados, contienen las filas de la tabla de transiciones. Se usar ́a la letra V ,
# para indicar que el aut ́omata no se mueve a ning ́un estado.
# La siguiente l ́ınea contiene el n ́umero de palabras m que ser ́anprocesadas por el aut ́omata. Finalmente, las  ́ultimas m l ́ıneas
# contienen las palabras a procesar.

def evaluacion(estado):
    if estado in estados_fnales:
        return ("Pertenece al lenguaje")
    else:
        return("No Pertenece al lenguaje")

def automata(palabra):
    estado_actual = estado_inicial
    palabra = [i for i in palabra]
    for i in range(len(palabra)):
        try:
            pos_alf = alfabeto.index(palabra[i]) # posición del simbolo en el alfabeto
            pos_est = estados.index(estado_actual) # En que estado nos econtramos
        except:
            print("WARNING: Un elemento de tu palabra no se encuentra en el alfabeto \n")
            estado_actual = "Se murio la linea de ejecucion\n"
            break
        
        estado_actual = transiciones[pos_est][pos_alf] # actualizar estado actual
        
    return(evaluacion(estado_actual))


if __name__=="__main__":
    # Inputs
    alfabeto = [i for i in input().split()] # Elementos de alfabeto
    estados = [i for i in input().split()] # Estados que pertenecen al A
    estado_inicial = input() # Estado inicial 
    estados_fnales = [i for i in input().split()] # estados finales
    ##########################################################
    transiciones = [] # Función de transición
    for i in range(len(estados)):
        transiciones.append([i for i in input().split()])
    ##########################################################
    num_palabras = int(input()) # Palabras 
    for i in range(num_palabras):
        palabra = input()
        print(palabra, automata(palabra))
