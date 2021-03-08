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
                func = getattr(self, cmd_list[0]) #判断是否有属性
                print(func)
                func()

    def get(self):
        print('getting...')

    def put(self):
        print('putting...')


i = FtpClient('1.1.1.1', 3306)
i.interactie()

""" 
反射的目的：
应该就是为了在函数内部判断时，不用写一堆判断
 """