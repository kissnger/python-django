from django.shortcuts import render
from django.http import HttpResponse    # 引用HttpResponse类
from sign import spider
from sign import readDoc
from sign import svnTools
# Create your views here. 
def index(request): 
    dic = spider.process()
    dataList = []
    if dic == None or dic == {}:
        pass
    else:
        dataList = dic['result']
    if dataList == None or dataList == []:
        dataList = []
    return render(request, 'index.html', {'dataList': dataList})
    # return HttpResponse(spider.process())

def readExcel(request):
    rowList = readDoc.process()
    return render(request, 'readDoc.html', {'rowList': rowList})

def callMySelf():
        print('callMySelf')
        
    # 接收请求数据
def svnPath(request):  
    request.encoding='utf-8'
    local_path = 'local_path'
    print(request.GET)
    if local_path in request.GET:
        if request.GET[local_path]:
            return render(request, 'local_path.html', {'message': request.GET[local_path], 'callMySelf': callMySelf})
        else :
            return render(request, 'local_path.html', {'message': '', 'empty': '请输入内容'})
    else:
        return render(request, 'local_path.html')
