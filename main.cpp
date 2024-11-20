#include <iostream>

using namespace std;

// clase de automata el cual tiene atributos de la cadena y estado el cual es el inicial 0
class automata{
private:
    char cadena[50];
    int estado = 0;
//metodos los cuales son leer la cadena, estados para las transiciones y estatus para ver el estado y aceptar o no la cadena
public:
    void leerCadena();
    void estados();
    void estatus();
};

//funcion para leer la cadena, despues manda a llamar a estados y estatus, imprime el estado final
void automata::leerCadena(){
    cout << "Ingrese la cadena de 0 y 1" << "\n";
    cin.getline(cadena,50);

    estados();
    cout << "Estado final Q" << estado << "\n";
    estatus();


}
//funcion para en base al estado, posterior el simbolo consumido realizar una transciccion hacia otro
//se imprime el estado actual y el simbolo a consumir
void automata::estados(){

    for(int i = 0; cadena[i] != '\0';++i){
        cout << "Estado actual q" << estado << "\n";
        cout << "Simbolo a consumir " << cadena[i] << "\n";
        switch(estado){
        case 0:
            if(cadena[i] == '0'){
                estado = 0;
            }
            else if (cadena[i] == '1'){
                estado = 1;
            }
            break;
        case 1:
            if(cadena[i] == '0'){
                    estado = 0;
            }
            else if (cadena[i] == '1'){
                estado = 2;
            }
            break;

        case 2:
            if(cadena[i] == '0'){
                estado = 4;
            }
            else if (cadena[i] == '1'){
                estado = 3;
            }
            break;

        case 3:
            if(cadena[i] == '0'){
                estado = 3;
            }
            else if (cadena[i] == '1'){
                estado = 3;
            }
            break;

        case 4:
            if(cadena[i] == '0'){
                estado = 4;
            }
            else if(cadena[i] == '1'){
                estado = 5;
                }
            break;
        case 5:
            if(cadena[i] == '0'){
                estado = 4;
            }
            else if(cadena[i] == '1'){
                estado = 3;
                }
            break;
        default:
            continue;

        }
    }



}
//en base al estado que termina al momento mandarlo a llamar, se determina si es aceptada o no la cadena
void automata::estatus(){
    switch(estado){
    case 0: cout << "La cadena es aceptada";
    break;
    case 1: cout << "La cadena es aceptada";
    break;
    case 2: cout << "La cadena es aceptada";
    break;
    case 3: cout << "La cadena no es aceptada";
    break;
    case 4: cout << "La cadena es aceptada";
    break;
    case 5: cout << "La cadena es aceptada";
    break;
    default:
        cout << "Sepa que ingresaste bro";

    }
}

//funcion principal que inicializa la clase o se define, para asi llamar a la clase automata y sus funciones
//y asi empezar las funciones mencionadas arriba
int main()
{
    automata automata1;
    automata1.leerCadena();
    return 0;
}
