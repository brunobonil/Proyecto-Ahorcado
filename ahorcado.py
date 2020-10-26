from servicesPartidas import ServicesPartidas


class Ahorcado():

    def un_jugador(self):
        nombre = str(input("Ingrese el nombre del jugador: "))
        dificultad = int(input("Seleccione la dificultad entre 1-10: "))
        partida = ServicesPartidas().iniciar_partida(nombre, dificultad)
        while True:
            letra = input(str("Ingrese la letra a intentar: "))
            if letra == 'salir':
                break
            resultado = ServicesPartidas().intentar_letra(partida, letra)
            if resultado == 'Gano':
                print("Has Ganado!")
                break
            if resultado == 'Perdio':
                print("Has Perdido")
                break
        return True

    def dos_jugadores(self):
        nombre1 = str(input("Ingrese el nombre del primer jugador: "))
        dificultad1 = int(input("Ingrese la dificultad (1-10): "))
        palabra_adivinar1 = str(input("""Jugador 2, ingrese la palabra a
                                      adivinar por el jugador 1: """))
        tipo_palabra_adivinar1 = str(input("""Jugador 2, ingrese el tipo de
                                           palabra: """))
        partida = ServicesPartidas().iniciar_partida(nombre1, dificultad1,
                                                     palabra_adivinar1,
                                                     tipo_palabra_adivinar1)
        while True:
            letra = input(str("Jugador 1, ingrese la letra a intentar: "))
            if letra == 'salir':
                break
            resultado1 = ServicesPartidas().intentar_letra(partida, letra)
            if resultado1 == 'Gano':
                break
            if resultado1 == 'Perdio':
                break
        nombre2 = str(input("Ingrese el nombre del segundo jugador: "))
        dificultad2 = int(input("Ingrese la dificultad (1-10): "))
        palabra_adivinar2 = str(input("""Jugador 1, ingrese la palabra a
        adivinar por el jugador 2: """))
        tipo_palabra_adivinar2 = str(input("""Jugador 1, ingrese el tipo de
        palabra: """))
        partida = ServicesPartidas().iniciar_partida(nombre2, dificultad2,
                                                     palabra_adivinar2,
                                                     tipo_palabra_adivinar2)
        while True:
            letra = input(str("Jugador 2, ingrese la letra a intentar: "))
            letra.upper()
            if letra == 'salir':
                break
            resultado2 = ServicesPartidas().intentar_letra(partida, letra)
            if resultado2 == 'Gano':
                break
            if resultado2 == 'Perdio':
                break
        hist = dict()
        hist['JUGADOR 1'] = {'NOMBRE': nombre1, 'PALABRA':
                             palabra_adivinar1.upper(),
                             'RESULTADO': resultado1}
        hist['JUGADOR 2'] = {'NOMBRE': nombre2, 'PALABRA':
                             palabra_adivinar2.upper(),
                             'RESULTADO': resultado2}
        for i in hist:
            print(hist[i])
        return True
