from experta import *

reposta = lambda x: True if x in ['S','s','sim','Sim','SIM','y', 'Y','yes','Yes','YES'] else False

class ClassificarAnimais(KnowledgeEngine):

    @DefFacts()
    def _initial_features(self):
        yield Fact(animal=True)
        #yield Fact(feature="voa")


    @Rule(NOT(Fact(penas=W())))
    def ask_pena(self):
        self.declare(Fact(penas=reposta(input("Tem pena? "))))

    @Rule(NOT(Fact(voa=W())))
    def ask_voa(self):
        self.declare(Fact(voa=reposta(input("Voa? "))))

    


    @Rule(Fact(penas=True))
    def e_ave(self):
        self.declare(Fact(tipo='ave'))

    @Rule(AND(Fact(voa=True),
              Fact(penas=True)))
    def e_passaro(self):
        print("Passaro")

    @Rule(AND(Fact(voa=False),
              Fact(tipo='ave')))
    def e_pinguim(self):
        print("Pinguim")

