from flask import Flask,request
import psycopg2
from psycopg2.extras import RealDictCursor
import json
app = Flask(__name__)

@app.route('/<table_name>',methods = ['POST','GET'])
def home(table_name=None):
    #if username is None or password is None:
        #abort(400) # missing arguments
    return "test successful"
	auth = request.authorization
	user_nam=auth.username
	pass_wrd =auth.password
    con_param="dbname=postgres user="+user_nam+ " password="+pass_wrd
    conn = psycopg2.connect(con_param)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    select_stmnt="select * from " + table_name
    cur.execute(select_stmnt)
    json_result=json.dumps(cur.fetchall(), indent=2)
    conn.close()
    return json_result

if __name__ == '__main__':
    #parser = optparse.OptionParser(usage="python application.py -p ")
    #parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    #(args, _) = parser.parse_args()
    #if args.port == None:
     #   print "Missing required argument: -p/--port"
     #   sys.exit(1)
    app.run(host='0.0.0.0', port=8000, debug=False)

# curl -H "Content-Type: application/json" -X GET -d '{"username":"postgres","password":"postgres123"}' http://localhost:8000/company