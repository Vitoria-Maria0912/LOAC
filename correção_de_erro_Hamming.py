def calcular_paridade(bits):
    paridade = [0, 0, 0]
    paridade[0] = bits[0] ^ bits[1] ^ bits[3]
    paridade[1] = bits[0] ^ bits[2] ^ bits[3]
    paridade[2] = bits[1] ^ bits[2] ^ bits[3]
    return paridade

def adicionar_paridade(bits):
    paridade = calcular_paridade(bits)
    bits_com_paridade = bits + paridade
    return bits_com_paridade

def corrigir_erro(bits_com_paridade):
    paridade_calculada = calcular_paridade(bits_com_paridade[:-3])
    paridade_recebida = bits_com_paridade[-3:]

    erro = 0
    for i in range(3):
        if paridade_calculada[i] != paridade_recebida[i]:
            erro += 2 ** i

    if erro == 0:
        return bits_com_paridade[:-3]
    else:
        bits_com_paridade[erro - 1] = 1 - bits_com_paridade[erro - 1]
        return bits_com_paridade[:-3]

# Exemplo de uso
bits_originais = [1, 0, 1, 1]  # Bits de dados originais (4 bits)
bits_com_paridade = adicionar_paridade(bits_originais)  # Adiciona bits de paridade (7 bits)
print("Bits originais:", bits_originais)
print("Bits com paridade:", bits_com_paridade)

bits_com_erro = bits_com_paridade.copy()
bits_com_erro[2] = 1 - bits_com_erro[2]  # Introduz erro nos bits

bits_corrigidos = corrigir_erro(bits_com_erro)
print("Bits com erro:", bits_com_erro)
print("Bits corrigidos:", bits_corrigidos)
