import subprocess

# Параметры подключения к базе данных
db_connect = {'host': '172.25.0.2', 'user': 'root', 'password': 'пароль', 'database': 'Inventory'}

# Формирование команды для создания дампа
command = f"mysqldump -h {db_connect['host']} -u {db_connect['user']} -p{db_connect['password']} {db_connect['database']} > dump.sql"

# Выполнение команды
subprocess.run(command, shell=True)