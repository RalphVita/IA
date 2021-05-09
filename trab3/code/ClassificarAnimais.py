from experta import *

reposta = lambda x: True if x in ['S','s','sim','Sim','SIM','y', 'Y','yes','Yes','YES'] else False

class ClassificarAnimais(KnowledgeEngine):

    @DefFacts()
    def _initial_features(self):
        yield Fact(animal=True)
        #yield Fact(feature="voa")


    ''' Classe '''
    
    # Amamenta?
    @Rule(NOT(Fact(amamenta=W())))
    def ask_amamenta(self):
        self.declare(Fact(amamenta=reposta(input("Amamenta? "))))
        #nadadeiras = temperatura_constante = penas = pele_umida = False


     # Nadadeiras?
    @Rule(NOT(Fact(nadadeiras=W())))
    def ask_nadadeiras(self):
        self.declare(Fact(nadadeiras=reposta(input("Tem nadadeiras? "))))

     # Répitil?
    @Rule(NOT(Fact(temperatura_constante=W())))
    def ask_temperatura_constante(self):
        self.declare(Fact(temperatura_constante=reposta(input("Temperatura corporal constante? "))))

     # Penas?
    @Rule(NOT(Fact(penas=W())))
    def ask_pena(self):
        self.declare(Fact(penas=reposta(input("Tem pena? "))))

    # Anfíbios?
    @Rule(NOT(Fact(pele_umida=W())))
    def ask_pele_umida(self):
        self.declare(Fact(pele_umida=reposta(input("Pele fina e úmida? "))))



    ''' Características '''

    # Voa?
    @Rule(AND(
        NOT(Fact(voa=W())),
            OR( Fact(tipo='mamifero'),
                Fact(tipo='ave'))
        ))
    def ask_voa(self):
        self.declare(Fact(voa=reposta(input("Voa? "))))

    # Habitáti Marinho ?
    @Rule(NOT(Fact(marinho=W())))
    def ask_marinho(self):
        self.declare(Fact(marinho=reposta(input("Tem habitáti marinho? "))))


    # Cauda longa ?
    @Rule(NOT(Fact(cauda_longa=W())))
    def ask_cauda_longa(self):
        self.declare(Fact(cauda_longa=reposta(input("Tem a cauda longa? "))))


    # Bípede ?
    @Rule(NOT(Fact(bipede=W())))
    def ask_bipede(self):
        self.declare(Fact(bipede=reposta(input("É bípede? "))))

    # Onívoro ?
    @Rule(NOT(Fact(onivoro=W())))
    def ask_onivoro(self):
        self.declare(Fact(onivoro=reposta(input("É onívoro? "))))

    # Carnívoro ?
    @Rule(NOT(Fact(carnivoro=W())))
    def ask_carnivoro(self):
        self.declare(Fact(carnivoro=reposta(input("É carnívoro? "))))

    # Onívoro ?
    @Rule(NOT(Fact(muda_cor=W())))
    def ask_muda_cor(self):
        self.declare(Fact(muda_cor=reposta(input("Muda de cor? "))))
    
    # Esqueleto cartilaginoso ?
    @Rule(NOT(Fact(esqueleto_cart=W())))
    def ask_esqueleto_cart(self):
        self.declare(Fact(esqueleto_cart=reposta(input("Tem o esqueleto cartilaginoso ? "))))
    
    # Corpo achatado ?
    @Rule(NOT(Fact(achatado=W())))
    def ask_achatado(self):
        self.declare(Fact(achatado=reposta(input("O corpo é achatado? "))))

    # Infla  ?
    @Rule(NOT(Fact(infla=W())))
    def ask_infla(self):
        self.declare(Fact(infla=reposta(input("O corpo infla? "))))

    # Felino ?
    @Rule(NOT(Fact(felino=W())))
    def ask_felino(self):
        self.declare(Fact(felino=reposta(input("É um felino (unhas retraem)? "))))




    
    ''' Mamíferos'''

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
    

    ''' Peixes '''
    @Rule(Fact(nadadeiras=True))
    def e_ave(self):
        self.declare(Fact(tipo='peixe'))

    # Tubarão
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(esqueleto_cart=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_tubarao(self):
        print("Tubarão")

    # Arraia
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(achatado=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_arraia(self):
        print("Arraia")

     # Baiacu
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(infla=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_baiacu(self):
        print("Baiacu")

     # Atum
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(infla=False),
                Fact(achatado=False),
                Fact(esqueleto_cart=False),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_atum(self):
        print("Atum")


    ''' Répitil '''
    @Rule(AND(
        Fact(temperatura_constante=False),
        Fact(pele_umida=False)
        ))
    def e_ave(self):
        self.declare(Fact(tipo='repitil'))

    # Jacaré
    @Rule(AND(  Fact(tipo='repitil'),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_jacare(self):
        print("Jacaré")

    # Cobra
    @Rule(AND(  Fact(tipo='repitil'),
                NOT(Fact(voa=True)), 
                Fact(marinho=False)
                ))
    def e_cobra(self):
        print("Cobra")

     # Tartaruga
    @Rule(AND(  Fact(tipo='repitil'),
                Fact(onivoro=True), 
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_tartaruga(self):
        print("Tartaruga")

     # Camaleão
    @Rule(AND(  Fact(tipo='repitil'),
                Fact(muda_cor=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_camaleao(self):
        print("Camaleão")


    ''' Aves '''

    @Rule(Fact(penas=True))
    def e_ave(self):
        self.declare(Fact(tipo='ave'))

    # Pinguim
    @Rule(AND(Fact(tipo='ave'),
              Fact(voa=False)))
    def e_pinguim(self):
        print("Pinguim")

    # Gavião
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(carnivoro=True)
              ))
    def e_gaviao(self):
        print("Gavião")

    # Beija-flor
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(carnivoro=False)
              ))
    def e_beijaflor(self):
        print("Beija-flor")
    
    # Gaivota
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(marinho=True)
              ))
    def e_gaivota(self):
        print("Gaivota")

    
    ''' Anfíbio '''
    @Rule(AND(
        Fact(temperatura_constante=False),
        Fact(pele_umida=True)
        ))
    def e_ave(self):
        self.declare(Fact(tipo='anfibio'))

    # Sapo
    @Rule(AND(  Fact(tipo='anfibio'),
                Fact(cauda_longa=False),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_sapo(self):
        print("Sapo")

    # Salamandra
    @Rule(AND(  Fact(tipo='anfibio'),
                Fact(cauda_longa=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_salamandra(self):
        print("Salamandra")





    ''' Leão '''
    # Leão
    @Rule(AND(  Fact(tipo='mamifero'),
                Fact(felino=True)
                ))
    def e_leao(self):
        print("Leão")        
