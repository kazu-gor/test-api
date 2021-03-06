
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask, jsonify, abort, make_response
import peewee

class User(peewee.Model):
    user_input = peewee.IntegerField()
    
app = Flask(__name__)

@app.route('/')
def test():
    try:
        total
    except NameError:
        total = 0
    try:
        total += 3
    except User.DoesNotExist:
        abort(404)
        
    result = {
        "data": {
            "output": total,
        }
    }
    return result

# @app.errorhandler(404)
# def not_found(error):
#     # return make_response(jsonify({'error': 'Not found'}), 404)
#     return {'error': 'Not found'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]