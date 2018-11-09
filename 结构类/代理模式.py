#!/user/bin/env python
# -*- coding: utf-8 -*-


#构建一个服务器，该服务器接受如下格式数据，addr代表地址，content代表接收的信息内容
info_struct=dict()
info_struct["addr"]=10000
info_struct["content"]=""
class Server:
    content=""
    def recv(self,info):
        pass
    def send(self,info):
        pass
    def show(self):
        pass
class infoServer(Server):
    def recv(self,info):
        self.content=info
        return "recv OK!"
    def send(self,info):
        pass
    def show(self):
        print("SHOW:%s"%self.content)

"""
infoServer有接收和发送的功能，发送功能由于暂时用不到，保留。
另外新加一个接口show，用来展示服务器接收的内容。
接收的数据格式必须如info_struct所示，服务器仅接受info_struct的content字段。
那么，如何给这个服务器设置一个白名单，使得只有白名单里的地址可以访问服务器呢？
修改Server结构是个方法，但这显然不符合软件设计原则中的单一职责原则。
在此基础之上，使用代理，是个不错的方法。代理配置如下
"""


class serverProxy:
    pass
class infoServerProxy(serverProxy):
    server=""
    def __init__(self,server):
        self.server=server
    def recv(self,info):
        return self.server.recv(info)
    def show(self):
        self.server.show()

class whiteInfoServerProxy(infoServerProxy):
    white_list=[]
    def recv(self,info):
        try:
            assert type(info)==dict
        except:
            return "info structure is not correct"
        addr=info.get("addr",0)
        if not addr in self.white_list:
            return "Your address is not in the white list."
        else:
            content=info.get("content","")
            return self.server.recv(content)
    def addWhite(self,addr):
        self.white_list.append(addr)
    def rmvWhite(self,addr):
        self.white_list.remove(addr)
    def clearWhite(self):
        self.white_list=[]

"""
代理中有一个server字段，控制代理的服务器对象，infoServerProxy充当Server的直接接口代理，
而whiteInfoServerProxy直接继承了infoServerProxy对象，同时加入了white_list和对白名单的操作。
这样，在场景中通过对白名单代理的访问，就可以实现服务器的白名单访问了。
"""

if  __name__=="__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = infoServer()
    info_server_proxy = whiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()

"""    
代理模式定义如下：
为某对象提供一个代理，以控制对此对象的访问和控制。
代理模式在使用过程中，应尽量对抽象主题类进行代理，
而尽量不要对加过修饰和方法的子类代理。
如上例中，如果有一个xServer继承了Server，并新加了方法xMethod，
xServer的代理应以Server为主题进行设计，而尽量不要以xServer为主题，
以xServer为主题的代理可以从ServerProxy继承并添加对应的方法。
"""