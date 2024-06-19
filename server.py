import socket
import threading

def simple_parse_request(request):
    return request.split("\n")

class Server:
    def __init__(self, address):
        self.address = address
        self.ip = address[0]
        self.port = address[1]

    def create_socket(self):
        self.s = socket.socket()
    
    def binding(self):
        self.s.bind(self.address)
        print(f"binding: {self.address}")
    
    def listen(self, number):
        self.s.listen(number)
    
    def accept(self):
        return self.s.accept()

    def connected(self, connection, address):
        request = connection.recv(1024).decode('utf-8')
        
        print("Connected to ", address)
        # print(simple_parse_request(request)[0].split(" ")[1])

        message = ("HTTP/1.1 OK\n"
                   "Content-type: text/html\n"
                   "Connection: close\n\n"
                   "<b>Selamat datang</b>")
        
        connection.send(message.encode('utf-8'))
        connection.close()

def main():
    wifi_ipv4 = "192.168.100.106" # get from my wifi
    server = Server((wifi_ipv4, 80))
    server.create_socket()
    server.binding()

    server.listen(5)
    while True:
        t = threading.Thread(target=server.connected, args=server.accept())
        t.start()

if __name__ == "__main__":
    main()