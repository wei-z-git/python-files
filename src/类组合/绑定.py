import settings


class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def func(self):
        print('hello %s' % self.host)

    @classmethod
    def from_conf(cls):
        return cls(settings.HOST, settings.PORT)


conn = MySQL.from_conf()
print(conn.host, conn.port)
