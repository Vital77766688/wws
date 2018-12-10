import time
import socket

class Client:

    def __init__(self, host, port, timeout = None):
        self.host = host
        self.port = port
        self.timeout = timeout or 5

    def put(self, key, value, timestamp = None):
        if not timestamp:
            tmstp = str(int(time.time()))
        else:
            tmstp = str(int(timestamp))

        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(bytes("put {} {} {}\n".format(key, str(value), tmstp).encode("utf-8")))
            except socket.timeout:
                print("Send data timeout")
            except socket.error as ex:
                print("Send data error: ", ex)

            a = sock.recv(1024).decode("utf-8").split("\n")

            if a[0] != "ok":
                raise  ClientError

    def get(self, key):
        res = {}
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(bytes("get {}\n".format(key).encode("UTF-8")))
                a = sock.recv(1024).decode("utf-8").split("\n")
            except socket.timeout:
                print("Send data timpout")
            except socket.error as ex:
                print("Send data error: ", ex)

        if a[0] == 'ok':
            for i in range(1, len(a) - 2):
                aa = a[i].split()
                if aa[0] in res:
                    res[aa[0]].append((int(aa[2]), float(aa[1])))
                else:
                    res.update({aa[0] : [(int(aa[2]), float(aa[1]))]})
        else:
            raise ClientError("Ошибка")

        return res

class ClientError(Exception):
    pass

if __name__ == '__main__':
    client = Client("127.0.0.1", 10001, 5)
    client.put("a1", 14.5, str(int(time.time())))
    client.put("a1", 15.5, str(int(time.time())))
    client.put("a2", 14.5, str(int(time.time())))
    print(client.get("a1"))
    print(client.get("*"))