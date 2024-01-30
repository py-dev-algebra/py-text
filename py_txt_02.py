# Adresar
# R.br.;Ime;Prezime;Broj telefona

id = 1

while True:
    first_name = input('Upisite Vase ime: ')
    last_name = input('Upisite Vase prezime: ')
    phone = input('Upisite Vas broj telefona: ')

    entry = f'{id};{first_name};{last_name};{phone}\n'

    try:
        with open('novi_adresar/adresar.txt', 'a') as file_writer:
            file_writer.write(entry)
    
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
    
    id += 1
    if input('Zelite li unijeti jos jedan kontakt? (Da/Ne): ').lower() != 'da':
        break


# Nema with open sintaksu pa se ne koristi toliko cesto!!!
# while True:
#     first_name = input('Upisite Vase ime: ')
#     last_name = input('Upisite Vase prezime: ')
#     phone = input('Upisite Vas broj telefona: ')

#     entry = f'{id};{first_name};{last_name};{phone}\n'

#     try:
#         file_writer = open('adresar/adresar.txt', 'a')
#         file_writer.write(entry)
#     except Exception as ex:
#         print(f'Dogodila se greska: {ex}')
#     finally:
#         file_writer.close()

#     id += 1
#     if input('Zelite li unijeti jos jedan kontakt? (Da/Ne): ').lower() != 'da':
#         break