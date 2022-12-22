import mysql.connector as mysql_con
import cx_Oracle


class OracleData():
    """
    cred ={
        'user':user,
        'password': password,
        'host':'10.0.0.0',
        'port':1521,
        'service':"adva",
        'views':['t1',t2]
    }
    """

    def __init__(self, cred=None):
        self.conn = None
        if not cred:
            return False

        self.cred = cred
        self.views = cred['views']
        dsn = cx_Oracle.makedsn(cred['host'], cred['port'],
                                service_name=cred['service'])
        try:
            self.conn = cx_Oracle.connect(
                user=cred['user'], password=cred['password'], dsn=dsn, encoding="UTF-8")
            print(cred["area"], "Successfully connected with :", cx_Oracle.clientversion())
        except Exception as e:
            print(e)
            self.conn = None

    def getdata(self):
        data_store = None
        if self.conn:
            data_store = []
            for view in self.views:
                sql_string = f"SELECT * FROM {view}"
                with self.conn.cursor() as cursor:
                    cursor.execute(sql_string)
                    # print(cursor.description)
                    data = cursor.fetchall()

                    if data:
                        colnames = [column_header[0] for column_header in cursor.description]
                        new_data = []
                        for row in data:                            
                            dict_row={}
                            for idx, key_name in enumerate(colnames):
                                # print(idx, name, row[idx])
                                dict_row[key_name] = row[idx]

                            new_data.append(dict_row)
                        
                        data_store.extend(new_data)

        return data_store

    def __del__(self):
        if self.conn:
            try:
                self.conn.commit()
                self.conn.close()
                print(self.cred["area"], 'Connection terminated.')
            except Exception as e:
                print(e)
        print("Delete object")


class MysqlData():
    """
    cred ={
        'user':admin,
        'password': admin,
        'host':'10.30.10.7',
        'port':3306, 
        'database':'pm_pulp2_wait',       
        'views':['t_pm_pulp2']
    }
    """

    def __init__(self, cred=None):
        if not cred:
            return False

        self.views = cred['views']

        try:
            self.conn = mysql_con.connect(
                user=cred['user'], password=cred['password'], host=cred['host'], database=cred['database'])
            print("Successfully connected to Mysql database")
        except Exception as e:
            print(e)
            self.conn = None

    def getdata(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        data_store = None
        if self.conn:
            data_store = []
            for view in self.views:
                # SELECT json_object('id', id, 'quality', quality, 'tag', tag,'value', FORMAT(value,3), 
                # 'tstamp', reg_date,'description',tag_desc) FROM t_pm_pulp2
                sql_string = f"SELECT * FROM {view}"
                with self.conn.cursor() as cursor:
                    cursor.execute(sql_string)
                    data = cursor.fetchall()
                    # if data:
                    #     data_store.extend(data)
                    if data:
                        colnames = [column_header[0] for column_header in cursor.description]
                        new_data = []
                        for row in data:                            
                            dict_row={}
                            for idx, name in enumerate(colnames):
                                # print(idx, name, row[idx])
                                dict_row[name] = row[idx]
                            new_data.append(dict_row)
                        # print(newdata)
                        data_store.extend(new_data)

        return data_store

    def __del__(self):
        if self.conn:
            try:
                self.conn.commit()
                self.conn.close()
                print('Mysql Connection is Closed.')
            except Exception as e:
                print(e)
        print("Delete object")
