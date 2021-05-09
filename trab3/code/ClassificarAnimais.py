from experta import *

reposta = lambda x: True if x in ['S','s','sim','Sim','SIM','y', 'Y','yes','Yes','YES'] else False

class ClassificarAnimais(KnowledgeEngine):

    @DefFacts()
    def _initial_features(self):
        yield Fact(animal=True)
        #yield Fact(feature="voa")

    
    # Amamenta?
    @Rule(NOT(Fact(amamenta=W())))
    def ask_amamenta(self):
        self.declare(Fact(amamenta=reposta(input("Amamenta? "))))

     # Penas?
    @Rule(NOT(Fact(penas=W())))
    def ask_pena(self):
        self.declare(Fact(penas=reposta(input("Tem pena? "))))


    # Habitáti Marinho ?
    @Rule(NOT(Fact(marinho=W())))
    def ask_marinho(self):
        self.declare(Fact(marinho=reposta(input("Tem habitáti marinho? "))))

    # Bípede ?
    @Rule(NOT(Fact(bipede=W())))
    def ask_bipede(self):
        self.declare(Fact(bipede=reposta(input("É bípede? "))))

    # Onívoro ?
    @Rule(NOT(Fact(onivoro=W())))
    def ask_onivoro(self):
        self.declare(Fact(onivoro=reposta(input("É onívoro? "))))


   

    # Voa?
    @Rule(NOT(Fact(voa=W())))
    def ask_voa(self):
        self.declare(Fact(voa=reposta(input("Voa? "))))

    


    ## Aves ##

    @Rule(Fact(penas=True))
    def e_ave(self):
        self.declare(Fact(tipo='ave'))

    @Rule(AND(Fact(voa=True),
              Fact(penas=True)))
    def e_passaro(self):
        print("Passaro")

    # Pinguim
    @Rule(AND(Fact(voa=False),
              Fact(tipo='ave')))
    def e_pinguim(self):
        print("Pinguim")

    
    ## Mamíferos ##

    @Rule(Fact(amamenta=True))
    def e_ave(self):
        self.declare(Fact(tipo='mamifero'))

    # Baleia
    @Rule(AND(  Fact(tipo='mamifero'),
                Fact(voa=False), 
                Fact(bipede=False),
                Fact(marinho=True)))
    def e_baleia(self):
        print("Baleia")

    # Morgego
    @Rule(AND(  Fact(voa=True),
                Fact(marinho=False),
                Fact(bipede=False),
                Fact(tipo='mamifero')))
    def e_morcego(self):
        print("Morcego")

    # Humano
    @Rule(AND(  Fact(bipede=True),
                Fact(voa=False), 
                Fact(marinho=False),
                Fact(tipo='mamifero')))
    def e_humano(self):
        print("Humano")

    # Urso
    @Rule(AND(  Fact(bipede=False),
                Fact(voa=False), 
                Fact(onivoro=True),
                Fact(marinho=False),
                Fact(tipo='mamifero')))
    def e_urso(self):
        print("Urso")

    # Cão
    @Rule(AND(  Fact(bipede=False),
                Fact(voa=False), 
                Fact(onivoro=True),
                Fact(marinho=False),
                Fact(tipo='mamifero')))
    def e_cao(self):
        print("Cão")
    

    

