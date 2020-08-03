#coding=utf8
# 导入xlrd模块
import xlrd

def process():
    #设置文件名和路径
    fname = '/Users/tin/Desktop/git/jp/document/Documents_Renewal/01_要件定義/変更管理簿_リニューアルアプリ.xlsx'
    # 打开文件
    filename = xlrd.open_workbook(fname)
    #获取当前文档的表(得到的是sheet的个数，一个整数）
    sheets=filename.nsheets

    #获取sheet对象，方法有3种：
    # 第一种:#通过sheet名字来获取，当然如果你知道sheet名字了可以直接指定
    # 得到的是一个列表集合[u'etsy_sheet']
    sheet_list = filename.sheet_names()
    sheet=filename.sheet_by_index(0)     #通过sheet索引获得sheet对象
    #获取行数
    nrows = sheet.nrows
    # 获取列数
    ncols = sheet.ncols
    #获取各行数据
    row_list=[]
    for i in range(0,nrows):
        row_datas = sheet.row_values(i)
        row_list.append(row_datas)
    return row_list