#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cx_Oracle
import genertor.model.table_model as tm
import os
import genertor.util.uitl as sutil
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
class OracleTool:

    def set_db_info(self,host,port,sid,user_name,password):
        self.host = host
        self.port = port
        self.sid = sid
        self.user_name = user_name
        self.passowrd = password


    def get_table_info(self,table_name):
        dsn = cx_Oracle.makedsn(self.host, self.port, self.sid)
        connection = cx_Oracle.connect(self.user_name, self.passowrd, dsn)
        cursor = cx_Oracle.Cursor(connection)  # 返回连接的游标对象
        sql = """select t1.column_name,data_type,data_default,nullable,comments from (
            select table_name,column_name,data_type,data_default,nullable from user_tab_cols where Table_Name='${table_name}'
        )t1
        RIGHT JOIN
        (
            select column_name,comments from user_col_comments where Table_Name='${table_name}'
        )t2
        on t1.column_name=t2.column_name"""
        sql = sql.replace('${table_name}', table_name.upper())
        cursor.execute(sql)
        rows = cursor.fetchall()
        colums=[]
        for row in rows:
            col = tm.ColumInfo()
            col.column_name=row[0]
            col.data_type=row[1]
            col.data_default=row[2]
            col.nullable=row[3]
            col.comments=row[4]
            colums.append(col)

        cursor.close()
        connection.close()
        return colums


def generate_fied(table_name):
    dsn = cx_Oracle.makedsn('127.0.0.1', 1521, 'orcl')
    connection = cx_Oracle.connect('user', 'psw', dsn)
    cursor = cx_Oracle.Cursor(connection)  # 返回连接的游标对象
    sql = """select t1.column_name,data_type,data_default,nullable,comments from (
        select table_name,column_name,data_type,data_default,nullable from user_tab_cols where Table_Name='${table_name}'
    )t1
    RIGHT JOIN
    (
        select column_name,comments from user_col_comments where Table_Name='${table_name}'
    )t2
    on t1.column_name=t2.column_name"""
    sql = sql.replace('${table_name}', table_name.upper())
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        col = tm.ColumInfo()
        col.column_name = row[0]
        col.data_type = row[1]
        col.data_default = row[2]
        col.nullable = row[3]
        col.comments = row[4]
        comments = ''
        if col.comments is not None:
            comments=col.comments
            comments=comments.replace('\n',' ')

        data_type='not_known'

        #字符串
        if col.data_type.upper()=='VARCHAR2' or col.data_type.upper()=='VARCHAR':
            data_type='String'
        elif col.data_type.upper()=='NUMBER':
            data_type='Long'
        elif col.data_type.upper()=='DATE':
            data_type='Date'

        print('private '+data_type+' '+sutil.underline_to_sm_camel(col.column_name)+';    //'+comments)

    cursor.close()
    connection.close()
    pass


if __name__ == '__main__':
    generate_fied('base_user')