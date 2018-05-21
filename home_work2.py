from client_ssl import get


# 2017/02/18
# 作业 2
# ========
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 定义我们的 log 函数
def log(*args, **kwargs):
    print(*args, **kwargs)


# 作业 2.1
#
# 实现函数
def path_with_query(path, query):
    '''
    path 是一个字符串
    query 是一个字典
    返回一个拼接后的 url
    详情请看下方测试函数
    '''
    path_value = path + '?'
    for i in query.keys():
        path_value += i + '=' + str(query[i]) + '&'

    path_value = path_value[:-1]

    log('path_value', path_value)

    return path_value


#
# def test_path_with_query():
#     # 注意 height 是一个数字
#     path = '/'
#     query = {
#         'name': 'gua',
#         'height': 169,
#     }
#     expected = [
#         '/?name=gua&height=169',
#         '/?height=169&name=gua',
#     ]
#     # NOTE, 字典是无序的, 不知道哪个参数在前面, 所以这样测试
#     assert path_with_query(path, query) in expected


# 作业 2.2
#
# 为作业1 的 get 函数增加一个参数 query
# query 是字典
# def get(url, **kwargs):
#     pass


# 作业 2.3
#
# 实现函数
def header_from_dict(headers):
    '''
    headers 是一个字典
    范例如下
    对于
    {
    	'Content-Type': 'text/html',
        'Content-Length': 127,
    }
    返回如下 str
    'Content-Type: text/html\r\nContent-Length: 127\r\n'
    '''
    string = ''
    for a in headers:
        string += a + ': ' + str(headers[a]) + '\r\n'
    log('string', string)
    return string


# 作业 2.4
# 为作业 2.3 写测试
# def test_header_from_dict():
#     d = {
#         'Content-Type': 'text/html',
#         'Content-Length': 127,
#     }
#     exception = 'Content-Type: text/html\r\nContent-Length: 127\r\n'
#     assert header_from_dict(d) in exception


# 作业 2.5
#
"""
豆瓣电影 Top250 页面链接如下
https://movie.douban.com/top250
我们的 client_ssl.py 已经可以获取 https 的内容了
这页一共有 25 个条目

所以现在的程序就只剩下了解析 HTML

请观察页面的规律，解析出
1，电影名
2，分数
3，评价人数
4，引用语（比如第一部肖申克的救赎中的「希望让人自由。」）

解析方式可以用任意手段，如果你没有想法，用字符串查找匹配比较好(find 特征字符串加切片)
"""


def get_header_index(body, find_str):
    return body.find(find_str) + len(find_str)


def parse_body(body):
    sub_body = body[get_header_index(body, '<ol class="grid_view">'):body.find(
        '</ol>')]
    log('sub_body', sub_body)


# 作业 2.6
#
"""
通过在浏览器页面中访问 豆瓣电影 top250 可以发现
1, 每页 25 个条目
2, 下一页的 URL 如下
https://movie.douban.com/top250?start=25

因此可以用循环爬出豆瓣 top250 的所有网页

于是就有了豆瓣电影 top250 的所有网页

由于这 10 个页面都是一样的结构，所以我们只要能解析其中一个页面就能循环得到所有信息

所以现在的程序就只剩下了解析 HTML

请观察规律，解析出
1，电影名
2，分数
3，评价人数
4，引用语（比如第一部肖申克的救赎中的「希望让人自由。」）

解析方式可以用任意手段，如果你没有想法，用字符串查找匹配比较好(find 特征字符串加切片)
"""
if __name__ == '__main__':
    # test_path_with_query()
    # test_header_from_dict()
    dic = get('https://movie.douban.com/top250')
    # log('body', dic[-1])
    parse_body(dic[-1])
