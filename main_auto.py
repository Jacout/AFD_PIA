class automata():
    def __init__(self):
        self.cadena =  ""
        self.estado_actual = 0
        
        """Clase llamada a automata con dos atributos que es la cadena y estado_actual
        que es el estado inicial 0, que tiene una funcion para leer la cadena,
        por default esta la cadena vacia posterior cada estado que se encuentra
        actualmente lo imprime y el simbolo que se consume, posterior envia el numero de la posicion
        de la cadena a la funcion para poder usar el simbolo en la transicion
        Posterior llama a estatus para ver si es aceptada o no
        """
    def leer(self):
        self.cadena = input("Ingrese una cadena de 0 y 1: \n")
        for i in range(len(self.cadena)):
            print(f"Estado actual q{self.estado_actual}")
            print(f"Simbolo a consumir {self.cadena[i]}")
            self.estados(i)
        
        self.estatus()
        
        """Funcion que verifica los estados que se encuentra y el simbolo que se va a consumir de la cadena
        y llama a la funcion de transicion para determinar el siguiente estado, ejemplo del primero que es
        estado q0 y consume 0 se mantiene, en caso de consumir 1 cambia a estado q1
        """
    def estados(self,numero):
        if(self.estado_actual == 0 and self.cadena[numero] == '0'):
            self.estado_actual = 0
        elif(self.estado_actual == 0 and self.cadena[numero] == '1'):
            self.estado_actual = 1
        elif(self.estado_actual == 1 and self.cadena[numero] == '0'):
            self.estado_actual = 0
        elif(self.estado_actual == 1 and self.cadena[numero] == '1'):
            self.estado_actual = 2
        elif(self.estado_actual == 2 and self.cadena[numero] == '0'):
            self.estado_actual = 4
        elif(self.estado_actual == 2 and self.cadena[numero] == '1'):
            self.estado_actual = 3
        elif(self.estado_actual == 3 and self.cadena[numero] == '0'):
            self.estado_actual = 3
        elif(self.estado_actual == 3 and self.cadena[numero] == '1'):
            self.estado_actual = 3
        elif(self.estado_actual == 4 and self.cadena[numero] == '0'):
            self.estado_actual = 4
        elif(self.estado_actual == 4 and self.cadena[numero] == '1'):
            self.estado_actual = 5
        elif(self.estado_actual == 5 and self.cadena[numero] == '0'):
            self.estado_actual = 4
        elif(self.estado_actual == 5 and self.cadena[numero] == '1'):
            self.estado_actual = 3
        
        """Funcion que compara y ve si la cadena es aceptada,
        dependiendo el estado que se encuentre
        """
    def estatus(self):
        if(self.estado_actual == 0):
            print("Cadena aceptada")
        elif(self.estado_actual == 1):
            print("Cadena aceptada")
        elif(self.estado_actual == 2):
            print("Cadena aceptada")
        elif(self.estado_actual == 3):
            print("Cadena no aceptada")
        elif(self.estado_actual == 4):
            print("Cadena aceptada")
        elif(self.estado_actual == 5):
            print("Cadena aceptada")
            
            
#Se inicializa la clase del automata y se manda a llamar a leer para empezar
a = automata()
a.leer()