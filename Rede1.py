import pandas as pd
import warnings #para esconder os erros
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/Samuel/Downloads/admission_dataset.csv')
#print(df)
y = df['Chance of Admit ']
x = df.drop('Chance of Admit ', axis = 1)

x_treino, x_teste = x[0:2], x[2:4] #[0:300] [300:]
y_treino, y_teste = y[0:2], y[2:4] #[0:300] [300:]

#print(x_treino.shape)

from keras.models import Sequential #Para criar uma camada após a outra em modo sequencial
from keras.layers import Dense

# Criando a arquitetura da rede neural
modelo = Sequential()
#vvv 1ª camada oculta vvv qtd neuronios
modelo.add(Dense(units=3, activation='relu', input_dim=x_treino.shape[1]))
modelo.add(Dense(units=3, activation='relu'))

#vvvv neuronio de saida deixei uma representação gráfica na raiz do projeto
modelo.add(Dense(units=1, activation='linear'))

#Treinamento de rede neural:
#              vvv função de custo mse vai calcular o quadrado do erro evaiu tentar minimizar os erros,
modelo.compile(loss='mse', optimizer='adam', metrics=['mae'])
#                                   erro medio absoluto ^^^          vv nao e obrigadorio porem ele valida a performance do aprendizado.
resultado = modelo.fit(x_treino, y_treino, epochs=1000, batch_size=32, validation_data=(x_teste,y_teste))
# qts epocas de treinamento completo eu quero ^^^^^      ^^^^^é quantas linhas do nosso dataset ele vai treinar para cada ajuste dos pesos e baias da rede neural 32 e op padrão
#                                                        ^^^^ vai varrer de 32 a 32 linhas  e quando terminar as 400 linhas ele vai terminar a epoca ou ephocs
#print(resultado)

# Gerar as previsões da rede neural com os dados de teste
y_previsto = modelo.predict(x_teste)

# Criar um DataFrame para comparar os valores reais com as previsões
resultado_comparacao = pd.DataFrame({
    'Valor Real': y_teste,
    'Valor Previsto': y_previsto.flatten()  # Usamos .flatten() para garantir que os valores sejam uma lista de uma dimensão
})

# Imprimir a comparação
print(resultado_comparacao)
sds = 3

import matplotlib.pyplot as plt

plt.plot(resultado.history['loss'])
plt.plot(resultado.history['val_loss'])
plt.title('Histórico de Treinamento')
plt.ylabel('Função de custo')
plt.xlabel('Épocas de trienamento')
plt.legend(['Erro de treinamneto', 'Erro teste'])
plt.show()