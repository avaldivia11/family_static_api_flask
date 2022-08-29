"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def one_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member),200


@app.route('/member', methods=['POST'])
def create_member():
    member=request.get_json()
    first_name = request.json.get("first_name")
    age = request.json.get("age")
    """ if first_name == "":return jsonify({"msg":"debes ingresar tu nombre"}),400
    if age == null:return jsonify({"msg":"debes ingresar tu edad"}),400 """
    add_to_list = jackson_family.add_member(member)
    return jsonify({"msg":"El registro fue exitoso"}),200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.delete_member(id)
    return jsonify({"done":True}),200

@app.route('/update_member/<int:id>', methods=['PUT'])
def update_member(id):
    member = request.get_json()
    """ if first_name == "":return jsonify({"msg":"debes ingresar tu nombre"}),400
    if age == null:return jsonify({"msg":"debes ingresar tu edad"}),400 """
    new_member = jackson_family.update_member(id,member)
    return jsonify(new_member,{"msg":"usuario actualizado"}),200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
