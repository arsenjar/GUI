from flask import Flask, jsonify
import json

# App initialization
app = Flask(__name__)

try:
    with open('status.json', 'r') as file:
        data = json.load(file)

    # print(data)
    print(f"left: {data['left']}")
except FileNotFoundError:
    print("No status.json file")

def check_robot_direction(status):
    # Attempt to get robot's status
    return data[f'{status}']

def change_directions(status):
    #loading file:
    try:
        with open('status.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No status.json file")
    # Flip status
    if data[f'{status}'] == True:
        data[f'{status}'] = False
        with open('status.json', 'w') as file:
            json.dump(data, file)
    else:
        data[f'{status}'] = True
        with open('status.json', 'w') as file:
            json.dump(data, file)

    return data[f'{status}']


@app.route('/check_status/<status>', methods=['GET'])
def get_motor_position(status):
    # Returns motor's position
    print(status)
    is_active = check_robot_direction(status)
    return jsonify({"status - ": is_active})
@app.route('/')
def hello_world():
    # Basic home page
    return 'Hello World'
@app.route('/change_status/<status>', methods=['GET'])
def change_motor_position(status):
    # Changes value in status json file, controlling robot's movement.
    print(status)
    Status = change_directions(status)
    return jsonify({"status - ": Status})


if __name__ == '__main__':
    app.run(debug=True)