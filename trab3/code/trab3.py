from ClassificarAnimais import ClassificarAnimais

reposta = lambda x: True if x in ['S','s','sim','Sim','SIM','y', 'Y','yes','Yes','YES'] else False

while reposta(input("\nOlá! Vamos identificar um animal (S/N)? ")):
    engine = ClassificarAnimais()
    engine.reset()
    engine.run()
    if not engine.encontrou:
        print('Não foi possível identificar um animal com essas características!')

