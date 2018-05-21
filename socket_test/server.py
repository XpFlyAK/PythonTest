# -*- coding: UTF-8 -*-
import socket


def log(*key, **kwargs):
    print('log==', *key, **kwargs)


def parse_address(address):
    address_bottle = {
        '/': route_home,
        '/login': route_login,
        # '/register': route_register,
    }
    web_response = address_bottle.get(address, not_found)
    return web_response()


def not_found():
    e = {
        '404': 'HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\n'
    }
    error_response = e.get('404') + '\r\n' + '<h1>404 Not Found</h1>'
    return error_response


def route_login():
    with open('login.html', 'r') as f:
        return f.read()


def route_home():
    headers = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n'
    body = '<h1>Welcome HomePage</h1>'
    response = headers + '\r\n' + body
    return response


def get_url(body):
    pass


def run(host='', port=3000):
    s = socket.socket()
    s.bind((host, port))
    while True:
        s.listen(5)

        connect, address = s.accept()
        request = connect.recv(1024).decode('utf-8')
        log('request===' + request)
        url = get_url(request)

        # response = parse_address()
        headers = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n'
        body = '<h1>Welcome HomePage</h1>'
        response = headers + '\r\n' + body
        connect.sendall(response.encode('utf-8'))
        connect.close()


if __name__ == '__main__':
    home = dict(host='', port=3000)

    run(**home)
