from ahorcado import Ahorcado


class App():
    def singleplayer(self):
        Ahorcado().un_jugador()

    def multiplayer(self):
        Ahorcado().dos_jugadores()


if __name__ == "__main__":
    while True:
        app = App()
        print("1. Un Jugador")
        print("2. Dos Jugadores")
        print("3. Salir")
        op = int(input("Ingrese el modo de juego: "))
        if op == 1:
            print("Ha seleccionado 'Un Jugador'")
            app.singleplayer()
        if op == 2:
            print("Ha seleccionado 'Dos Jugadores'")
            app.multiplayer()
        if op == 3:
            print("Ha seleccionado 'Salir'")
            print("Saliendo del juego...")
            break
