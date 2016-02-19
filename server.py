# -*- coding: utf-8 -*-

# 定时检测/tmp/Open-Sesame文件是否存在，
# 如果存在，则向client发送开门指令

import os
import time
from SocketServer import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        i = 0
        print('Got connection from', self.client_address)
        while True:
            time.sleep(1)

            if os.path.isfile("/tmp/Open-Sesame"):
                self.request.send("b") # 开门指令
                os.remove("/tmp/Open-Sesame")
            else:
                if i % 5 == 0:
                	# 保证连接始终有效，keep-alive
                    self.request.send("a")
            i += 1


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


