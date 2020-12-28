from pony.orm import *
from common.config import *


# db = Database()
# class USER(db.Entity):
#     pass
#     username=Required(str)
#
# db.bind(provider=db_provider, host=db_host,port=port, user=user, passwd=passwd, db=db_name)
# db.generate_mapping(check_tables=True, create_tables=False)


class MysqlDB(object):
    def __init__(self):
        self.db = Database()
        self.db.bind(provider=db_provider, host=db_host, port=port, user=user, passwd=passwd, db=db_name)
        self.db.generate_mapping(check_tables=True, create_tables=False)

    @db_session
    def query(self, table, condition='1'):
        res = self.db.select(f"select * from {table} where {condition}")
        return res

    @db_session
    def sql_query(self, sql):
        res = self.db.select(sql)
        return res

if __name__ == '__main__':
    a = MysqlDB().query('user', 'id<=3433890743304388611')
    print(type(a))
    print(a)
    print(len(a))
