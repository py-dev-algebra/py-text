# Adresar
# R.br.;Ime;Prezime;Broj telefona


while True:
    id = 1
    first_name = input('Upisite Vase ime: ')
    last_name = input('Upisite Vase prezime: ')
    phone = input('Upisite Vas broj telefona: ')

    entry = f'{id};{first_name};{last_name};{phone}\n'

    try:
        file_writer = open('adresar/adresar.txt', 'a')
        file_writer.write(entry)
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
    finally:
        file_writer.close()


    if input('Zelite li unijeti jos jedan kontakt? (Da/Ne): ').lower() != 'da':
        break