#TobeComented

deputados_por_distrito = [16, 3, 19, 3, 4, 9, 3, 9, 4, 10, 47, 2, 39, 9, 18, 6, 5, 9, 5, 6, 2, 2]

partidos = ["PDR - Partido Democratico Republicano",
            "PCP-PEV CDU - Coligacao Democratica Unitaria",
            "PPD/PSD-CDS/PP Portugal a Frente", 
            "MPT Partido da Terra", 
            "L/TDA LIVRE/Tempo de Avancar", 
            "PAN Pessoas-Animais-Natureza", 
            "PTP-MAS Agir",
            "JPP Juntos pelo Povo", 
            "PNR Partido Nacional Renovador",
            "PPM Partido Popular Monarquico",
            "NC Nos, Cidadaos!",
            "PCTP/MRPP Partido Comunista dos Trabalhadores Portugueses",
            "PS Partido Socialista",
            "B.E. Bloco de Esquerda",
            "PURP Partido Unido dos Reformados e Pensionistas"]

def encontra_maior(vector, length):
    maior = 0
    res = 0
    for i in range(length):
        if(vector[i] == maior and maior != 0):
            if(totalVotos[i] < totalVotos[res]):
                maior = vector[i]
                res = i      
        elif(vector[i] > maior):
            maior = vector[i]
            res = i
    return res

def mandatos(nr_mandatos, nr_votos):
    length = len(nr_votos)
    global totalVotos
    totalVotos = list(nr_votos)
    aux_nr_votos = list(nr_votos)
    res = [0] * length
    aux_res = [1] * length
    aux = 0
    while(aux < nr_mandatos):
        temp = encontra_maior(aux_nr_votos, length)
        aux_res[temp] = aux_res[temp] + 1
        aux_nr_votos[temp] = nr_votos[temp] / aux_res[temp]
        res[temp] = res[temp] + 1
        aux = aux + 1
    res_final = tuple(res)
    return res_final

def adicionaListasDoMesmoTamanho(lst1, lst2, length):
    res = [0] * length
    for i in range(length):
        res[i] = lst1[i] + lst2[i]
    return res

#Just for fun
def totalVotosCandidatura(votacoes, nr_mandatos, length):
    res = [0] * length
    i = 0
    while i < nr_mandatos:
        res = adicionaListasDoMesmoTamanho(res, votacoes[i], length)
        i = i + 1
    return res

def assembleia(votacoes):
    nr_mandatos = len(votacoes)
    length = len(votacoes[0])
    res = [0] * length
    for i in range(nr_mandatos):
        res = adicionaListasDoMesmoTamanho(mandatos(deputados_por_distrito[i], votacoes[i]), res, length)
    return res

def max_mandatos(votacoes):
    res = assembleia(votacoes)
    length = len(res)
    return partidos[encontra_maior(res, length)]

#Para testar
votacoes = ((0, 15729, 220408, 1297, 0, 3040, 993, 0, 1354, 1046, 0, 3284, 99652, 19327, 0), 
            (0, 19000, 23173, 255, 0, 532, 201, 0, 306, 232, 0, 1980, 22307, 3890, 0), 
            (0, 23731, 244971, 1959, 0, 2710, 1465, 0, 1094, 1114, 0, 4264, 159476, 20488, 0), 
            (0, 1956, 47716, 282, 0, 0, 175, 0, 165, 247, 0, 417, 19728, 1732, 0), 
            (0, 5384, 52325, 403, 0, 770, 543, 0, 428, 0, 0, 1454, 38317, 4609, 0), 
            (0, 14138, 113419, 662, 0, 2535, 600, 0, 591, 557, 0, 2014, 66199, 13034, 0), 
            (0, 18967, 31260, 237, 0, 649, 216, 0, 168, 207, 0, 1810, 25010, 4225, 0), 
            (0, 17255, 99745, 2076, 0, 3285, 0, 0, 1069, 700, 0, 3160, 46082, 16347, 0), 
            (0, 3299, 53450, 251, 0, 520, 199, 0, 178, 191, 0, 755, 26263, 3114, 0), 
            (0, 12351, 148762, 977, 0, 3029, 633, 0, 595, 453, 0, 2502, 51518, 0, 0), 
            (0, 111661, 560365, 4135, 0, 16913, 2410, 0, 5897, 4270, 0, 14419, 322034, 66874, 0), 
            (0, 7910, 26257, 176, 0, 333, 162, 0, 151, 135, 0, 1031, 19963, 2753, 0), 
            (0, 61832, 488402, 2413, 0, 9072, 3386, 0, 1551, 1525, 0, 9640, 318113, 51002, 0), 
            (0, 21347, 118028, 1454, 0, 2220, 692, 0, 832, 726, 0, 3413, 61194, 13712, 0), 
            (0, 82159, 156444, 1682, 0, 6282, 1133, 0, 1595, 847, 0, 0, 112764, 29667, 0), 
            (0, 6648, 76961, 384, 0, 926, 0, 0, 213, 331, 0, 1473, 35327, 5928, 0), 
            (0, 3656, 71840, 304, 0, 617, 254, 0, 147, 574, 0, 675, 34825, 2784, 0), 
            (0, 5810, 123184, 696, 0, 1229, 465, 0, 266, 626, 0, 1456, 54107, 5786, 0), 
            (0, 2288, 53518, 314, 0, 756, 293, 0, 219, 271, 0, 669, 23189, 3965, 0), 
            (0, 5096, 87597, 2560, 0, 2385, 2992, 0, 617, 538, 0, 1967, 20360, 5568, 0), 
            (0, 803, 6306, 101, 0, 192, 83, 0, 48, 50, 0, 132, 7205, 602, 0), 
            (0, 127, 8938, 87, 0, 0, 0, 0, 64, 47, 0, 52, 2714, 165, 0))



print(mandatos(5, (100, 34, 12, 8)))
print(mandatos(10, (100, 34, 12, 8)))
print(mandatos(20, (100, 34, 12, 8)))
print(mandatos(19, votacoes[2]))
print(mandatos(3, votacoes[3]))
print(assembleia(votacoes))
print(max_mandatos(votacoes))