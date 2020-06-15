import mysql.connector
import sys
import subprocess
from .informationgenerator import get_first_name, get_phone_number, get_last_name


class Anonymize:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "toor"
        self.database = "anonymizer"
        self.mysql_connection = self.initialise_database_connection()
        self.cursor = self.mysql_connection.cursor()

    def initialise_database_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )

    def populate_database(self):
        if not len(sys.argv) > 1 or not sys.argv[1].endswith('.sql'):
            print('missing sql dump')
            exit(1)

        self.cursor.execute("drop database if exists {}".format(self.database))
        self.cursor.execute("create database {}".format(self.database))
        self.mysql_connection.commit()
        self.cursor.execute("use {}".format(self.database))

        with open(sys.argv[1], 'r') as f:
            sql_dump = f.read()

        command = subprocess.run(
            ['mysql', '-h', self.host, '-u', self.user, '-p' + self.password, self.database],
            stdout=subprocess.PIPE, input=sql_dump, encoding='utf-8')

        print(command.stdout)

    def export_database(self):
        output_filename = "out.sql"
        command_output = subprocess.check_output(
            ['mysqldump', '-h', self.host, '-u', self.user, '-p' + self.password, self.database])

        with open(output_filename, 'wb') as f:
            f.write(command_output)

    def anonymize_database(self):
        self.cursor.execute("select * from anonymizer.core_users")
        rows = self.cursor.fetchall()

        for row in rows:
            name = get_first_name()
            sql = '''UPDATE anonymizer.core_users SET first_name = %s where id = %s '''
            try:
                self.cursor.execute(sql, (name, row[0]))
            except Exception as e:
                print(e)
        self.mysql_connection.commit()
