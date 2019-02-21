import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("result.xlsx")
sheet = book.sheet_by_name("Sheet1")
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='airport',
        port=3306,
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into airport_tbl (name,otp,operations,country,subregion,starrating) values (%s, %s, %s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
      # uuid      =sheet.cell(r,1).value
      name      = sheet.cell(r,1).value
      otp       = sheet.cell(r,2).value
      operations          = sheet.cell(r,3).value
      country     = sheet.cell(r,4).value
      subregion       = sheet.cell(r,5).value
      starrating = sheet.cell(r,6).value
      values = (name,otp,operations,country,subregion,starrating)
      # 执行sql语句
      cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")



