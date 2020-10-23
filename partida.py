class Partida():

    def __init__(self, palabra='', intentos=0, tipo_palabra='',
                 nombre_jugador='', palabra_aciertos=[]):

        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador
        self.palabra_aciertos = palabra_aciertos

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        if type(value) == list:
            self._palabra = value
        else:
            self._palabra = list(value.upper())
        if value == '':
            raise ValueError("No se ingresó ninguna palabra")

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        self._tipo_palabra = value.upper()
        if value == '':
            raise ValueError("No se ingresó el tipo de palabra")

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        self._intentos = value
        if value < 0:
            raise ValueError("Los intentos no pueden ser negativos")

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        self._nombre_jugador = value.upper()
        if value == '':
            raise ValueError("No se ingresó el nombre del jugador")

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        self._palabra_aciertos = value
        if self._palabra_aciertos == []:
            for i in self._palabra:
                self._palabra_aciertos.append(None)
