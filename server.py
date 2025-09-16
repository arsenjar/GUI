from flask import Flask, jsonify
import json
app = Flask(__name__)

try:
    with open('status.json', 'r') as file:
        data = json.load(file)

    # print(data)
    print(f"left: {data['left']}")

except FileNotFoundError:
    print("No status.json file")
# A function that returns a boolean value
# def check_user_status(status):
#     return user_id == 123

def check_robot_diraction(status):
    return data[f'{status}']

@app.route('/check_status/<status>', methods=['GET'])
def get_motor_position(status):
    print(status)
    is_active = check_robot_diraction(status)

    return jsonify({"status - ": is_active})


# @app.route('/check_status/<int:user_id>', methods=['GET'])
# def get_user_status(user_id):
#     # Call the function and get the boolean result
#     is_active = check_user_status(user_id)
#
#     # Return the boolean as a JSON response
#     return jsonify({"is_active": is_active})


if __name__ == '__main__':
    app.run(debug=True)