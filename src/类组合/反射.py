class FtpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = 'xxx'

    def interactie(self):
        while True:
            cmd = input('>>:').strip()
            if not cmd:  # if not (cmd is none)
                continue
            cmd_l = cmd.split()
            print(cmd_l)
            if hasattr(self, cmd_l[0]):  # 判断对象是否有cmd_l的属性
                func = getattr(self, cmd_l[0])
                print(func)
                func()

    def get(self):
        print('getting...')

    def put(self):
        print('putting...')


i = FtpClient('1.1.1.1', 3306)
i.interactie()
