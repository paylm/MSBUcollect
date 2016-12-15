import xlwt

def write_execl(fron='font: name Times New Roman, color-index red, bold on',sheet='A Test Sheet',data=None,outfile="example.xls"):

    style0 = xlwt.easyxf(fron)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    row =  0
    for item in data:
        col = 0
        for key in item:
            ws.write(row,col,item[key],style0)
            print item[key]
            col+=1
        row+=1
    wb.save(outfile)

if __name__ == '__main__':
    data =   [{'android': 1008.0, 'id': u'link'},{'project': 'msub', 'id': '111'}]
    write_execl(fron='',sheet="aaa",data=data,outfile='test111.xls')
    for item in data:
        col = 0
        for key in item:
            #ws.write(row,col, 1234.56, style0)
            print key,item[key]
            col+=1
        col+=1