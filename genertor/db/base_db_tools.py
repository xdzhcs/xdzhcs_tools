import cx_Oracle
import genertor.model.table_model as tm

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
        rows = cursor.fetall()
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


