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

def evaluacion(estados):
    for estado in estados:
        if estado in estados_fnales:
            return("Pertenece al lenguaje")

    return("No pertenece al lenguaje")



def automata(palabra):
    estados_actuales = [estado_inicial]
    for i,letra in enumerate(palabra):
        pos_alf = alfabeto.index(letra)
        pos_est = []
        for est in estados_actuales:
            if len(est) > 1 and type(est) == list:
                for el in est:
                    aux_est=estados.index(el)
                    pos_est.append(aux_est)
            else:
                if type(est) == list:
                    aux_est = estados.index(est[0])
                else:
                    aux_est = estados.index(est)
                pos_est.append(aux_est)

        aux_estados_actuales = []
        for pos in pos_est:
            change=transiciones[pos][pos_alf]
            if change == 'V':
                pass
            else:
                aux_estados_actuales.append(change)
        
        estados_actuales = []
        for est in aux_estados_actuales:
            estados_actuales.append(est.split())

        aux2=[]
        for est in estados_actuales:
            if len(est) > 1:
                for el in est:
                    aux2.append(el)
            else:
                aux2.append(est[0])

        estados_actuales = aux2
    return(evaluacion(estados_actuales))



if __name__=='__main__':
    alfabeto = [i for i in input().split()]
    estados = [i for i in input().split()]
    estado_inicial = [i for i in input().split()]
    estados_fnales = [i for i in input().split()]
    transiciones = []
    for i in range(len(estados)):
        transiciones.append([i for i in input().split(', ')])
    num_palabras = int(input())
    for i in range(num_palabras):
        palabra = input()
        print(palabra,automata(palabra))