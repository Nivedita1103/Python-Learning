import mysql.connector as ctor
dbcon=ctor.connet(host="localhost",user="larner",password="",database="items")
cursor=dbcon.cursor()
sql1="DELETE FROM catagory WHERE name='%s'"
data1=("Stockable",)
cursor.execute(sql1,data1)
dbcon.commit()
print("Rows affected:",cursor.rowcount)
dbcon.close()
