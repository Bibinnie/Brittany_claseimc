class Persona:

    #precondiciones + postcondiciones de los casos
    #atributos: encapsulacion 

    __peso=0
    __altura=0.0
    __imc=0.0 

    #metodos: 1 metodo por cada caso de uso
    #def nombreCasodeUso(self,parametros)(precondiciones separadas con comas):

    def calcularIndicedeMasaCorporal(self,peso,altura):
        self.__peso= peso
        self.__altura= altura
        self.__imc= (self.__peso/(self.__altura*self.__altura))
        return self.__imc
    
    def clasificarIMC(self):
        if self.__imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= self.__imc < 24.9:
            return "Peso normal"
        elif 25 <= self.__imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad" 
    