import math

input = 0 #entrada

output_desire = 0 # saida desejada

input_weight = 0.5 #peso inicial

learnig_rate = 0.01 # taxa de aprendizado  POSSO ALTERAR

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print('entrada', input, 'desejado', output_desire)

error = math.inf #deixamos o erro como infinito mas e comio se fosse o contador
interation = 0

bias = 1 # neuronio virtual q e sempre 1 por conta do erro de se eu deixar o input 0 e a saida desejada 0 também
bias_wheight = 0.5

while not error == 0:

    interation += 1
    print('Interação: ', interation)
    print('peso', input_weight)
            #neuronio real            neuronio virtual
    sum = (input * input_weight) + (bias * bias_wheight) #soma

    output =  activation(sum) #saida

    print('saida', output)

    error = output_desire - output # erro para ter acerto tem que dar 0

    print('erro', error)

    if not error == 0:
        input_weight = input_weight + learnig_rate * input * error
        bias_wheight = bias_wheight + (learnig_rate * bias * error)

print('PARABÉNS A REDE APRENDEU')