import matplotlib.pyplot as plt

resultado = 1
resultados = 1

plt.plot(resultado)
plt.plot(resultados)
plt.title('Histórico de Treinamento')
plt.ylabel('Função de custo')
plt.xlabel('Épocas de trienamento')
plt.legend('Erro de treinamneto', 'Erro teste')
plt.show()