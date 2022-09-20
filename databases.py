import pymysql

# 数据流 连接
db = pymysql.connect(
    host='192.168.1.21',
    user='cwgf',
    password='0Is0z/kvWXFW+5rh',
    port=3306,
    db='spv_commercepv',

)
cursor = db.cursor()
dbs = db.commit()
spv_tyc = "INSERT INTO tyc_info(order_guid,`name`,legal_name,regist_money,regist_address,regist_date,verify_time,create_time)VALUES({},'黑仔外卖','欧啦啦', '欧莱莱','欧内内呢','{}','{}','{}')"