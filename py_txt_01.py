from datetime import datetime as dt


first_name = input("Upisite Vase ime: ")
file_name_date = dt.now().strftime('%Y-%m')


# 1. korak - otvori konekciju prema datoteci
file_writer = open(f'files/{file_name_date}.txt', 'w') # 'w' -> (over)write ili 'a' -> append
# 2. korak - zapisi podatke u datoteku
file_writer.write(first_name)
# 3. korak - zatvori konekciju prema datoteci
file_writer.close()

# 1. korak - otvori konekciju prema datoteci
file_reader = open(f'files\{file_name_date}.txt', 'r') # 'r' -> read
# 2. korak - zapisi podatke u datoteku
file_data = file_reader.read()
# 3. korak - zatvori konekciju prema datoteci
file_reader.close()

print(f'Sadrzaj datoteke je {file_data}')
