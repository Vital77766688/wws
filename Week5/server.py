import asyncio

class ServerException(Exception):
    pass

class Server:

    dict = {}

    def put_data(self, values):
        key, value, timestamp = values.split()
        #if key not in self.dict:
        #    self.dict[key] = []
        #self.dict[key].append((int(timestamp), float(value)))
        if key not in self.dict:
            self.dict[key] = {}
        self.dict[key][int(timestamp)] = float(value)

        return "ok\n\n"

    def get_data(self, values):
        key = values.strip()

        if key == "*":
            return "ok\n" + "\n".join(key + " " + str(val) + " " + str(tmstp) for key, item in self.dict.items() for tmstp, val in item.items()) + "\n\n"
            #return "ok\n" + "\n".join(key + " " + str(i[1]) + " "+ str(i[0]) for key, item in self.dict.items() for i in item) + "\n\n"
        elif key not in self.dict:
            return "ok\n\n"
        else:
            return  "ok\n" + "\n".join(key + " " + str(val) + " " + str(tmstp) for tmstp, val in self.dict[key].items()) + "\n\n"
            #return "ok\n" + "\n".join(key + " " + str(i[1]) + " " + str(i[0]) for i in self.dict[key]) + "\n\n"

    def process_data(self, data):

        method, values = data.split(" ", 1)
        if method == "put":
            return self.put_data(values)
        elif method == "get":
            return self.get_data(values)
        else:
            raise ServerException("error\nwrong command\n\n")


class ServerProtocol(asyncio.Protocol):

    def __init__(self):
        self._server = Server()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            resp = self._server.process_data(data.decode())
            self.transport.write(resp.encode())
        except ServerException as se:
            err = se.args[0].encode()
            self.transport.write(err)




def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ServerProtocol, host, port)

    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()

    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server("127.0.0.1", 10001)