#coding:UTF-8

"""
该文件为ace部署该框架的例子
"""

from webFrame import useWsgi

def method(request,response):
    html="""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>欢迎页</title>
            </head>
            <body>
                <p>get参数：{{get}}</p>
                <p>说明：{{text}}</p>
            </body>
        </html>
    """
    html=html.replace("{{get}}",request.GET.get("t",u"没有参数！").encode("UTF-8"))
    html=html.replace("{{text}}","webFrame框架制作！")
    response.write(html)
    return response

def application(environ, start_response):
    return useWsgi(environ,start_response,method)