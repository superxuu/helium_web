from faker import Faker
from common.mysql_connect import MysqlDB


def generate_phone():
    fake = Faker(locale='zh_CN')
    res = [1]
    while res:
        phone = fake.phone_number()
        SQL = f"SELECT * FROM user WHERE  phone_number='{phone}'"
        res = MysqlDB().sql_query(SQL)
    return phone


if __name__ == '__main__':
    res = generate_phone()
    print(res)
