from experta import *

reposta = lambda x: True if x in ['S','s','sim','Sim','SIM','y', 'Y','yes','Yes','YES'] else False

class ClassificarAnimais(KnowledgeEngine):

    @DefFacts()
    def _initial_features(self):
        yield Fact(animal=True)
        self.encontrou = False
        #yield Fact(feature="voa")


    def Encontrou(self,nome):
        print(nome)
        self.declare(Fact(fim=True))
        self.encontrou = True


    ''' Classe '''
    
    # Amamenta?
    @Rule(AND(Fact(animal=True),NOT(Fact(amamenta=W())),NOT(Fact(tipo=W()))))
    def ask_amamenta(self):
        self.declare(Fact(amamenta=reposta(input("Amamenta? "))))
        

     # Nadadeiras?
    @Rule(AND(Fact(animal=True),NOT(Fact(nadadeiras=W())),NOT(Fact(tipo=W()))))
    def ask_nadadeiras(self):
        self.declare(Fact(nadadeiras=reposta(input("Tem nadadeiras? "))))

     # Répitil?
    @Rule(AND(Fact(animal=True),NOT(Fact(temperatura_constante=W())),NOT(Fact(tipo=W()))))
    def ask_temperatura_constante(self):
        self.declare(Fact(temperatura_constante=reposta(input("Temperatura corporal constante? "))))

     # Penas?
    @Rule(AND(Fact(animal=True),NOT(Fact(penas=W())),NOT(Fact(tipo=W()))))
    def ask_pena(self):
        self.declare(Fact(penas=reposta(input("Tem pena? "))))

    # Anfíbios?
    @Rule(AND(Fact(animal=True),NOT(Fact(pele_umida=W())),NOT(Fact(tipo=W())),Fact(temperatura_constante=False)))
    def ask_pele_umida(self):
        self.declare(Fact(pele_umida=reposta(input("Pele fina e úmida? "))))



    ''' Características '''

    # Voa?
    @Rule(AND(
        NOT(Fact(voa=W())), NOT(Fact(fim=True)),
            OR( Fact(tipo='mamifero'),
                Fact(tipo='ave'))
        ))
    def ask_voa(self):
        self.declare(Fact(voa=reposta(input("Voa? "))))

    # Habitáti Marinho ?
    @Rule(AND(
            NOT(Fact(marinho=W())), NOT(Fact(fim=True)),
            Fact(tipo=W())))
    def ask_marinho(self):
        self.declare(Fact(marinho=reposta(input("Tem habitáti marinho? "))))


    # Cauda longa ?
    @Rule(AND(  NOT(Fact(cauda_longa=W())), NOT(Fact(fim=True)),
                Fact(tipo='anfibio')))
    def ask_cauda_longa(self):
        self.declare(Fact(cauda_longa=reposta(input("Tem a cauda longa? "))))


    # Bípede ?
    @Rule(AND(  NOT(Fact(bipede=W())), NOT(Fact(fim=True)),
                Fact(tipo='mamifero')))
    def ask_bipede(self):
        self.declare(Fact(bipede=reposta(input("É bípede? "))))

    # Onívoro ?
    @Rule(AND(  OR(Fact(tipo='repitil'),Fact(tipo='mamifero')), NOT(Fact(fim=True)),
                NOT(Fact(onivoro=W()))))
    def ask_onivoro(self):
        self.declare(Fact(onivoro=reposta(input("É onívoro? "))))

    # Carnívoro ?
    @Rule(AND(  Fact(tipo='ave'), NOT(Fact(fim=True)),
                NOT(Fact(carnivoro=W()))))
    def ask_carnivoro(self):
        self.declare(Fact(carnivoro=reposta(input("É carnívoro? "))))

    # Muda de cor ?
    @Rule(AND(  Fact(tipo='repitil'), NOT(Fact(fim=True)),
                NOT(Fact(muda_cor=W()))))
    def ask_muda_cor(self):
        self.declare(Fact(muda_cor=reposta(input("Muda de cor? "))))
    
    # Esqueleto cartilaginoso ?
    @Rule(AND(  Fact(tipo='peixe'), NOT(Fact(fim=True)),
                NOT(Fact(esqueleto_cart=W()))))
    def ask_esqueleto_cart(self):
        self.declare(Fact(esqueleto_cart=reposta(input("Tem o esqueleto cartilaginoso ? "))))
    
    # Corpo achatado ?
    @Rule(AND(  Fact(tipo='peixe'), NOT(Fact(fim=True)),
                NOT(Fact(achatado=W()))))
    def ask_achatado(self):
        self.declare(Fact(achatado=reposta(input("O corpo é achatado? "))))

    # Infla  ?
    @Rule(AND(  Fact(tipo='peixe'), NOT(Fact(fim=True)),
                NOT(Fact(infla=W()))))
    def ask_infla(self):
        self.declare(Fact(infla=reposta(input("O corpo infla? "))))

    # Felino ?
    @Rule(AND(  Fact(tipo='mamifero'), NOT(Fact(fim=True)),
                NOT(Fact(felino=W()))))
    def ask_felino(self):
        self.declare(Fact(felino=reposta(input("É um felino (unhas retraem)? "))))




    
    ''' Mamíferos'''

    @Rule(Fact(amamenta=True))
    def e_mamifero(self):
        self.declare(Fact(tipo='mamifero'))
        

    # Baleia
    @Rule(AND(  Fact(tipo='mamifero'),
                NOT(Fact(voa=True)), 
                NOT(Fact(bipede=True)),
                Fact(marinho=True)))
    def e_baleia(self):
        self.Encontrou("Baleia")
        

    # Morgego
    @Rule(AND(  Fact(voa=True),
                NOT(Fact(marinho=True)),
                NOT(Fact(bipede=True)),
                Fact(tipo='mamifero')))
    def e_morcego(self):
        self.Encontrou("Morcego")
        

    # Humano
    @Rule(AND(  Fact(bipede=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=True)),
                Fact(tipo='mamifero')))
    def e_humano(self):
        self.Encontrou("Humano")
        

    # Urso
    @Rule(AND(  Fact(bipede=False),
                Fact(voa=False), 
                Fact(onivoro=True),
                Fact(marinho=False),
                Fact(tipo='mamifero')))
    def e_urso(self):
        self.Encontrou("Urso")
        

    # Cão
    @Rule(AND(  Fact(bipede=False),
                Fact(voa=False), 
                Fact(onivoro=False),
                Fact(marinho=False),
                Fact(tipo='mamifero')))
    def e_cao(self):
        self.Encontrou("Cão")
    

    ''' Peixes '''
    @Rule(Fact(nadadeiras=True))
    def e_peixe(self):
        self.declare(Fact(tipo='peixe'))
        self.declare(Fact(marinho=True))
        

    # Tubarão
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(esqueleto_cart=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_tubarao(self):
        self.Encontrou("Tubarão")
        

    # Arraia
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(achatado=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_arraia(self):
        self.Encontrou("Arraia")
        

     # Baiacu
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(infla=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_baiacu(self):
        self.Encontrou("Baiacu")
        

     # Atum
    @Rule(AND(  Fact(tipo='peixe'),
                Fact(infla=False),
                Fact(achatado=False),
                Fact(esqueleto_cart=False),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_atum(self):
        self.Encontrou("Atum")
        


    ''' Répitil '''
    @Rule(AND(
        Fact(temperatura_constante=False),
        Fact(pele_umida=False)
        ))
    def e_repitil(self):
        self.declare(Fact(tipo='repitil'))
        

    # Jacaré
    @Rule(AND(  Fact(tipo='repitil'),
                Fact(marinho=True),
                Fact(onivoro=False),
                Fact(muda_cor=False)
                ))
    def e_jacare(self):
        self.Encontrou("Jacaré")
        

    # Cobra
    @Rule(AND(  Fact(tipo='repitil'),
                NOT(Fact(voa=True)), 
                Fact(marinho=False),
                Fact(muda_cor=False)
                ))
    def e_cobra(self):
        self.Encontrou("Cobra")
        

     # Tartaruga
    @Rule(AND(  Fact(tipo='repitil'),
                Fact(onivoro=True),  
                NOT(Fact(marinho=False)),
                Fact(muda_cor=False)
                ))
    def e_tartaruga(self):
        self.Encontrou("Tartaruga")
        

     # Camaleão
    @Rule(AND(  Fact(tipo='repitil'),
                Fact(muda_cor=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_camaleao(self):
        self.Encontrou("Camaleão")
        


    ''' Aves '''

    @Rule(Fact(penas=True))
    def e_ave(self):
        self.declare(Fact(tipo='ave'))
        

    # Pinguim
    @Rule(AND(Fact(tipo='ave'),
              Fact(voa=False)))
    def e_pinguim(self):
        self.Encontrou("Pinguim")
        

    # Gavião
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(carnivoro=True),
              Fact(marinho=False)
              ))
    def e_gaviao(self):
        self.Encontrou("Gavião")
        

    # Beija-flor
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(carnivoro=False),
              Fact(marinho=False)
              ))
    def e_beijaflor(self):
        self.Encontrou("Beija-flor")
        
    
    # Gaivota
    @Rule(AND(Fact(tipo='ave'),
              NOT(Fact(voa=False)),
              Fact(marinho=True)
              ))
    def e_gaivota(self):
        self.Encontrou("Gaivota")
        

    
    ''' Anfíbio '''
    @Rule(AND(
        Fact(temperatura_constante=False),
        Fact(pele_umida=True)
        ))
    def e_anfibio(self):
        self.declare(Fact(tipo='anfibio'))
        

    # Sapo
    @Rule(AND(  Fact(tipo='anfibio'),
                Fact(cauda_longa=False),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_sapo(self):
        self.Encontrou("Sapo")
        

    # Salamandra
    @Rule(AND(  Fact(tipo='anfibio'),
                Fact(cauda_longa=True),
                NOT(Fact(voa=True)), 
                NOT(Fact(marinho=False))
                ))
    def e_salamandra(self):
        self.Encontrou("Salamandra")
        





    ''' Leão '''
    # Leão
    @Rule(AND(  Fact(tipo='mamifero'),
                Fact(felino=True),
                NOT(Fact(bipede=True)),
                NOT(Fact(voa=True)), 
                NOT(Fact(onivoro=True)),
                NOT(Fact(marinho=True)),
                ))
    def e_leao(self):
        self.Encontrou("Leão")
           
