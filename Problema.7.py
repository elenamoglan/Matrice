cifrele_zecimale=[0,1,2,3,4,5,6,7,8,9]
Coduri=[['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001'],
        ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101'],
        ['0000', '0001', '0010', '0011', '0100', '1011', '1100', '1101', '1110', '1111'],
        ['0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100'],
        ['0110000 ', '0110001', '0110010', '0110011', '0110100', '0110101', '0110110', '0110111', '0111000', '0111001']]
x=input('Introduceti sistemul de codare:')
if x=='Direct':
    print('Cifrele zecimale in codul Direct: ', Coduri[0])
elif x=='Gray':
    print('Cifrele zecimale in codul Gray: ', Coduri[1])
elif x=='Aiken':
    print('Cifrele zecimale in codul Aiken: ', Coduri[2])
elif x=='Exces 3':
    print('Cifrele zecimale in codul Exces 3: ', Coduri[3])
elif x=='ASCII':
    print('Cifrele zecimale in codul ASCII: ', Coduri[4])
else:
    print('Eroare')
