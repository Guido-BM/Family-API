from flask import Flask, request, jsonify
from datastructure import Family

app = Flask(__name__)
jackson_family = Family('Jackson')

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200


@app.route('/', methods=['GET'])
def home():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    member = request.get_json()
    jackson_family.add_member(member)
    return jsonify({}), 200

@app.route('/member/<string:member_id>', methods=['PUT'])
def update_member(member_id):
    member = request.get_json()
    updated_member = jackson_family.update_member(member_id, member)
    if updated_member:
        return jsonify(updated_member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(debug=True)