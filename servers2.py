import socket
import threading
import sqlite3


def update_sql(array):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    login = array[0]
    pb_key = array[1]
    cur.execute("UPDATE users SET pb_key= ? WHERE login=? ", (pb_key, login))
    con.commit()
    con.close()
    print("add")


def get():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users ")
    rows = cur.fetchall()
    print(rows)
    return rows


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())
sock.bind((ip, 2247))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(data)
    try:
        list = data.decode()
        if list == '^^^':
            print(1)
            datas = get()
            print(datas)
            datas = str(datas)
            sock.sendto(datas.encode(), addres)
        else:
            opendata = list.split('>')
            update_sql(opendata)
            print('done')
    except:
        if addres not in client:
            client.append(addres)  # Если такого клиента нету , то добавить
        for clients in client:
            if clients == addres:
                continue  # Не отправлять данные клиенту, который их прислал
            sock.sendto(data, clients)


potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    mensahe = input()
    sor.sendto(('[' + alias + ']' + mensahe).encode('utf-8'), server)
