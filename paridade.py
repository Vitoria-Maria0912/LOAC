def calcular_paridade(bits):
    count_ones = sum(bit for bit in bits)  # Conta o número de bits '1'
    paridade = count_ones % 2  # Calcula a paridade (0 se par, 1 se ímpar)
    return paridade


def adicionar_paridade(bits):
    paridade = calcular_paridade(bits)
    bits_com_paridade = bits + [paridade]
    return bits_com_paridade


def verificar_paridade(bits_com_paridade):
    paridade_calculada = calcular_paridade(bits_com_paridade[:-1])  # Calcula paridade sem o último bit
    paridade_recebida = bits_com_paridade[-1]  # Último bit é a paridade recebida
    if paridade_calculada == paridade_recebida:
        return "Sem erros de paridade."
    else:
        return "Erro de paridade detectado."

# Exemplo de uso
bits_originais = [1, 0, 1, 1, 0]  # Bits de dados originais
bits_com_paridade = adicionar_paridade(bits_originais)  # Adiciona bit de paridade
print("Bits originais:", bits_originais)
print("Bits com paridade:", bits_com_paridade)
print(verificar_paridade(bits_com_paridade))
