
from flask import Flask, jsonify, request,render_template
from werkzeug.wrappers import Request, Response
from flask_restful import Api, Resource
import os, json


webapp = Flask(__name__,template_folder='.')
api = Api(webapp)


class test(Resource):
    def get(self):
        try:
            print('Success')
        except Exception as er:
            return('Error')
        finally:
            return render_template('index.html')
            #  return('Working')


api.add_resource(test,'/')


            
if __name__ == '__main__':
    # webapp.run()
    webapp.secret_key = os.urandom(24)
    port = int(os.environ.get('PORT', 6000))
    webapp.run(host='0.0.0.0', port=port, debug=False , threaded=True)
    # webapp.run(host='192.168.2.13', port=port, debug=True, threaded=True)


