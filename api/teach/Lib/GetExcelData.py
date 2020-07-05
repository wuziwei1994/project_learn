# author：xintian   
# time:2020-06-19
#-*- coding: utf-8 -*-
import xlrd#读取库
def get_excelData(sheetName,startRow,endRow,bodyCol,repsCol):
    '''
    :param sheetName: 表名
    :param startRow: 开始行数
    :param endRow: 结束函数
    :param bodyCol: 请求体列数
    :param repsCol: 响应体列数
    :return: [(请求体，响应体),(请求体，响应体)]
    '''
    excelDir = '../data/1.test.xls'
    workBook = xlrd.open_workbook(excelDir)#保存原样--样式
    #2- 操作对应的用例表
    workSheet = workBook.sheet_by_name(sheetName)#通过表名获取
    dataList = []
    for cnt in range(startRow-1,endRow):
        cellData = workSheet.cell_value(cnt,bodyCol)#字符串类型  请求体
        repsCellData = workSheet.cell_value(cnt, repsCol)  # 字符串类型  预期结果
        # dataList.append(cellData)
        dataList.append((cellData,repsCellData))
    return dataList#列表


