# echo-server.py

import socket

# хост на котором будет слушать сервер
HOST = "127.0.0.1"
# и порт. Непривилегированные порты > 1024
PORT = 65432

address = (HOST, PORT)

# чтобы не вызывать socket.close(), оборачиваем в with
# 1-й параметр socket.AF_INET - константа указания семейства адресов =
# семейство интернет адресов IPv4
# 2-й параметр socket.SOCK_STREAM - тип протокола
# SOCK_STREAM = TCP, SOCK_DGRAM = UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() -> связывание сокета с хостом и портом
    # хост может быть - хостом (localhost, etc), IP адресом или пустой строкой
    # если будет пустая строка, то коннект будет на свободный адрес машины
    # порт может быть от 1 до 65535
    s.bind(address)
    # listen() -> "слушаем" соединения
    # можно указать параметр __backlog -
    # максимальное кол-ов одновременных подключений
    # по умолчанию = cat /proc/sys/net/core/somaxconn = 4096
    s.listen()
    # accept() -> блокируем выполнение и ожидаем входящего соединения
    # метод возвращает новый объект сокета и свой адрес
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # recv() -> получаем данные с нового сокета
            data = s.recv(1024)
            if not data:
                break
            # sendall() -> отправляем все данные которые отправил нам клиент
            conn.sendall(data)