class animal():
    nombre = 'ninguno'
    edad = None

    def haz_ruido(self, fuerte= True):
        if fuerte:
            print('AAAAAAAAAH')
        else:
            print('aaah')



class mamifero():
        vertebrado = True
        pelo = True

        def __init__(alimentacion, altura, peso, progenie=0):
            # Atributos de instancia
            self.alimentacion = alimentacion   # carnívoro, omnívoro, etc
            self.altura = altura #cm
            self.peso = peso #kg
            self.progenie = progenie 
    
    # Cuántos puede tener y cuántos van a sobrevivir    
    def reproducirse(self, max_progenie):
        self.progenie +=  choice(range( max_progenie))
    #...


        
        alimentacion = ''
        tamano = None
        peso = None
        progenie = 0

perro = mamifero()

perro = mamifero("omnívoro", 43, 6.1)