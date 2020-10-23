from palabrasRepo import Repository
from partida import Partida
import random


class ServicesPartidas():

    def get_random_palabra(self):
        repo = Repository.repo_ran
        indice = random.choice(repo)
        palabra = {'palabra': indice[1], 'tipo_palabra': indice[0]}
        return palabra

    def iniciar_partida(self, nombre, dificultad, palabra='', tipo_palabra=''):
        repo = Repository.repo_ran
        if palabra == '':
            indice = random.choice(repo)
            palabra = indice[1]
        if tipo_palabra == '':
            tipo_palabra = indice[0]
        if dificultad < 1 or dificultad > 10:
            raise ValueError("La dificultad ingresada no esta entre 1-10")
        intentos = (dificultad * len(palabra))
        partida = Partida(palabra, intentos, tipo_palabra, nombre)
        return partida

    def intentar_letra(self, partida, letra):
        if partida._intentos == 0:
            raise ValueError
        while partida._intentos > 0:
            if letra in partida._palabra:  #Verifica si la letra esta en la palabra
                for i in partida._palabra:  #Busca el indice de la letra y la coloca en palabra_aciertos
                    if letra == i:              
                        ind = partida._palabra.index(letra)
                        partida.palabra_aciertos[ind] = letra
                partida._intentos -= 1
            if letra not in partida._palabra:
                partida._intentos -= 1
            if (partida._intentos == 0 or partida._palabra_aciertos ==
               partida._palabra):
                break
            return 'Continua'
        if partida.palabra_aciertos == partida.palabra:
            partida.palabra_aciertos.clear()
            return 'Gano'
        if partida.palabra_aciertos != partida.palabra:
            partida.palabra_aciertos.clear()
            return 'Perdio'
