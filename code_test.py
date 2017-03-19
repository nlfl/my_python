#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 08:06:19 2017

@author: zhaolu
"""

#
# -*- coding: utf-8 -*-

"""
Created on Sun Jan 29 10:12:07 2017

@author: zhaolu

qq：115792703
"""
import ibm_db
conn1 = ibm_db.connect("DATABASE=cbs;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=zxw6142083;", "", "") 


def area_insert(pro, city, code):
    pro1 = pro
    city1 = city
    code1 = code
    # 插入记录
    sql_desc = "INSERT INTO \"NULLID\".\"AREA_LIST\" (AREA_PROVINCE,AREA_CITY,AREA_CODE) values('" + pro1 + "','" + city1 + "','" + code1 + "')"
    print sql_desc
    ibm_db.exec_immediate(conn1,sql_desc)

#    pgdb_conn.commit()
#    pg_cursor.close()
#    pgdb_conn.close()


def bank_insert(bank_name, bank_code):
    name1 = bank_name
    code1 = bank_code
    # 插入记录
    sql_desc = "INSERT INTO \"NULLID\".\"BANK_LIST\" (BANK_NAME,BANK_CODE) values('" + \
        name1 + "','" + code1 + "')"

    ibm_db.exec_immediate(conn1,sql_desc)

#    pgdb_conn.commit()
#    pg_cursor.close()
#    pgdb_conn.close()


def cnaps_insert(area_code, bank_code, bank_name, cnaps_code):
    code1 = area_code
    code2 = bank_code
    name1 = bank_name
    cnaps1 = cnaps_code

    # 插入记录
    sql_desc = "INSERT INTO \"NULLID\".\"CNAPS_LIST\" (AREA_CODE,BANK_CODE,BANK_NAME,CNAPS_CODE) values ('" + \
        code1 + "','" + code2 + "','" + name1 + "','" + cnaps1 + "')"
    print sql_desc
    sql_u = sql_desc.decode('utf-8')
    print sql_u
    ibm_db.exec_immediate(conn1,sql_u)
#    pgdb_conn.commit()
#    pg_cursor.close()
#    pgdb_conn.close()


def area_data():
    fp = open("./AREACODE.TXT", 'r')
    for line in fp:
        num1 = [word for word in line.split("|")]
        area_insert(unicode(num1[0],"gb2312"), unicode(num1[1],"gb2312"), unicode(num1[2],"gb2312"))
    fp.close()


def bank_data():
    fp = open("./OTHERBANKCODE.TXT", 'r')
    for line in fp:
        num1 = [word for word in line.split("|")]
        bank_insert(unicode(num1[0],"gb2312"), unicode(num1[1],"gb2312"))
    fp.close()


def cnaps_data():
    fp = open("./111.txt", 'r')
    for line in fp:
        num1 = [word for word in line.split("|")]
        cnaps_insert(unicode(num1[1],"gb2312"), unicode(num1[0],"gb2312"), unicode(num1[2],"gb2312"),unicode(num1[3],"gb2312"))
        #cnaps_insert(num1[1], num1[0], num1[2],num1[3])
    fp.close()


if __name__ == '__main__':
    area_data()
    bank_data()
    cnaps_data()

   