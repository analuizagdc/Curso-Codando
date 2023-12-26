import socket as ss
from threading import Thread

class Server:
    def __init__(self):
        self.routes = {
            '/batata': {'data_type': 'text', 'data': 'batata'},
            '/batatinhas': {'data_type': 'html', 'data': '<h2> Oi lipe seu lindo <3 <h2>'}
        }
        
        self.server_socket = self.init_socket()
        self.allow_clients()
        
    def get_data(self, client: ss.socket) -> str:
        while True: 
            package = client.recv(1026)
            if not package:
                break
            return package.decode('utf-8')
            
    def send_data(self, client: ss.socket, data_type: str, data: str):
        if data_type == 'html':
            message = f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{data}'
        elif data_type == 'text':
            message = f'HTTP/1.1 200 OK\r\n\r\n{data}'
            
        client.send(message.encode('utf-8'))
        
    def manage_client(self, client: ss.socket, address: tuple[str, int]):
        print(f'Client {address[0]} connected!')
        
        request = self.get_data(client)
        route = self.handle_request(request)
        
        if route in self.routes.keys():
            data_type = self.routes[route]['data_type']
            data = self.routes[route]['data']
            self.send_data(client, data_type, data)
        else:
            self.send_data(client, 'text', 'The route was not found!')
            
    def handle_request(self, request: str) -> str:
        ex_route = request.index('HTTP/1.1')
        return request[4:ex_route]
    
    def allow_clients(self):
        while True:
            client, address = self.server_socket.accept()
            Thread(target=self.manage_client, args=(client, address)).start()
            
    def init_socket(self):
        server_socket = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        ip_address = ss.gethostbyname(ss.gethostname())
        server_socket.bind((ip_address, 46026))
        print(f'Server started! HostIp: {ip_address}')
        server_socket.listen(5)
        return server_socket
    
server = Server()
