import pymysql


class Input_Data:

    def input_DB(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='P@ssw0rd',
                                     database='Client_PC_List',
                                     cursorclass=pymysql.cursors.DictCursor)



