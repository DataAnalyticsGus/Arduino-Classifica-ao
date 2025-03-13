import numpy as np
import time
from pyfirmata import Arduino, util

#Colocar a porta de conexão do Arduino:
porta='COM8'

#Conexão com a placa do Arduino
placa=Arduino(porta)

#Processo de Leitura de Forma Assíncrona
it=util.Iterator(placa)
it.start()

#Definindo os pinos onde os sensores estão ligados no Arduino
sensor01=placa.get_pin('a:0:i')
sensor02=placa.get_pin('a:1:i')

#Inicializando o vetor de armazenamento de dados
Dados=np.array([])
for i in range(5):
    leitura01=sensor01.read()
    leitura02=sensor02.read()
    if leitura01 is not None and leitura02 is not None:
        valor01=int(leitura01*1023)
        valor02=int(leitura02*1023)

        novo_valor=np.array([valor01,valor02])
        Dados=np.append(Dados,novo_valor, axis=0)

        print(f'Dados:{Dados}')
    time.sleep(0.1)
np.savetxt('Dados.csv',Dados,delimiter=',',fmt='%d')

placa.exit()


