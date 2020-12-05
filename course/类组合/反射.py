class FtpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = 'xxx'

    def interactie(self):
        while True:
            cmd = input('>>:').strip()
            if not cmd:  # if not (cmd is none)
                continue  # 为了防止输入空字符

            cmd_list = cmd.split()
            print(cmd_list)
            if hasattr(self, cmd_list[0]):  # 判断对象是否有cmd_list的属性
                func = getattr(self, cmd_list[0])
                print(func)
                func()

    def get(self):
        print('getting...')

    def put(self):
        print('putting...')


i = FtpClient('1.1.1.1', 3306)
i.interactie()
