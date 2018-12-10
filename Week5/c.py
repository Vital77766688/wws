# asyncio, tcp клиент
"""
import asyncio

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)
    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = input()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
"""

import socket

with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
    try:
        sock.sendall("put test 10.0 2\n".encode())
    except socket.timeout:
        print("Send data timout")
    except socket.error as ex:
        print("Send data error: ", ex)

    try:
        print(sock.recv(1024).decode())
    except socket.timeout:
        print("Get response timout")
        raise
    except socket.error as ex:
        print("Get response error", ex)
        raise


    try:
        sock.sendall("put test 11.3 2\n".encode())
    except socket.timeout:
        print("Send data timout")
    except socket.error as ex:
        print("Send data error: ", ex)

    print(sock.recv(1024).decode())

    try:
        sock.sendall("get *\n".encode())
    except socket.timeout:
        print("Send data timout")
    except socket.error as ex:
        print("Send data error: ", ex)

    print(sock.recv(1024).decode())

    try:
        sock.sendall("get k2\n".encode())
    except socket.timeout:
        print("Send data timout")
    except socket.error as ex:
        print("Send data error: ", ex)

    print(sock.recv(1024).decode())

    try:
        sock.sendall("get test\n".encode())
    except socket.timeout:
        print("Send data timout")
    except socket.error as ex:
        print("Send data error: ", ex)

    print(sock.recv(1024).decode())