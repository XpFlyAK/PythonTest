# coding: utf-8

import socket
import ssl

"""
2017/02/16
作业 1


资料:
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')

send 函数的参数和 recv 函数的返回值都是 bytes 类型
其他请参考上课内容, 不懂在群里发问, 不要憋着
"""


# 1
# 补全函数
def protocol_of_url(url):
    protocol = 'http'
    if url[:7] == 'http://':
        protocol = 'http'
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url
    i = u.find('/')
    if i != -1:
        path = u[i:]
        host = u[:i]
    else:
        host = u
        path = '/'
    port_dict = {
        'http': 80,
        'https': 443,
    }
    port = port_dict[protocol]
    if ':' in host:
        port = int(host.split(':')[1])
        host = host.split(':')[0]
    return protocol, host, port, path


def test_protocol_of_url():
    http = 'http'
    https = 'https'
    host = 'g.cn'
    path = '/'
    test_item = [
        ('http://g.cn', (http, host, 80, path)),
        ('http://g.cn/', (http, host, 80, path)),
        ('http://g.cn:90', (http, host, 90, path)),
        ('http://g.cn:90/', (http, host, 90, path)),
        ('https://g.cn', (https, host, 443, path)),
        ('https://g.cn:233/', (https, host, 233, path)),
    ]
    for t in test_item:
        url, excepted = t
        u = protocol_of_url(url)
        e = 'parsed_url ERROR,({}) ({}) ({})'.format(url, u, excepted)
        assert u == excepted, e


# 2
# 补全函数
def host_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表主机的字符串, 比如 'g.cn'
    '''
    pass


# 3
# 补全函数
def port_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表端口的字符串, 比如 '80' 或者 '3000'
    注意, 如上课资料所述, 80 是默认端口
    '''
    pass


# 4
# 补全函数
def path_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表路径的字符串, 比如 '/' 或者 '/search'
    注意, 如上课资料所述, 当没有给出路径的时候, 默认路径是 '/'
    '''
    pass


# 4
# 补全函数
def parsed_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'
    返回一个 tuple, 内容如下 (protocol, host, port, path)
    '''
    pass


# 5
# 把向服务器发送 HTTP 请求并且获得数据这个过程封装成函数
# 定义如下
def get(url, **kwargs):
    protocol, host, port, path = protocol_of_url(url)

    if protocol == 'http':
        s = socket.socket()
    else:
        s = ssl.wrap_socket(socket.socket())
    s.connect((host, port))
    request = 'GET {} HTTP/1.1\r\nhost:{}\r\nConnection:close\r\n\r\n'.format(path, host)
    s.send(request.encode('utf-8'))
    response = b''
    while True:
        rec = s.recv(1024)
        if len(rec) == 0:
            break
        response += rec
    r = response.decode('utf-8')
    head, body = r.split('\r\n\r\n', 1)
    h = head.split('\r\n')
    status_code = int(h[0].split()[1])
    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    if status_code == 301:
        url = headers['Location']
        return get(url)
    return status_code, headers, body


'''
本函数使用上课代码 client.py 中的方式使用 socket 连接服务器
获取服务器返回的数据并返回
注意, 返回的数据类型为 bytes
'''


# 使用
def main():
    url = 'http://movie.douban.com/top250'
    status_code, headers, body = get(url)
    print(status_code, headers, body)


if __name__ == '__main__':
    main()
    # test_protocol_of_url()
