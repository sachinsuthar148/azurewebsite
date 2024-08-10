from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Simulate Azure Function

#home route
@app.route("/")
def home():
    return "<h1> Server is working very well.</br> Check How_To_Run.txt file in folder and check the APIs in POST method </h1>"

# This function represents a service that processes input data and returns a result.
def simulate_function(input_data):
    # Process the input data (e.g., perform some computation or transformation)
    return {"result": f"Processed: {input_data}"}

# Define an endpoint to simulate the Azure Function
@app.route('/simulate-function', methods=['POST'])
def simulate_function_endpoint():
    # Extract JSON data from the incoming request
    data = request.json
    
    # Check if 'input' is provided in the request data
    if not data or 'input' not in data:
        # Return an error response if 'input' is missing
        return jsonify({"error": "No input provided"}), 400
    
    # Retrieve the 'input' value from the request data
    input_data = data['input']
    
    # Call the simulate_function to process the input data
    result = simulate_function(input_data)
    
    # Return the processed result as JSON response
    return jsonify(result)

# Simulate Azure Logic Apps
# This function represents a service that handles workflows based on triggers.
def simulate_logic_app(data):
    # Check if the 'trigger' key is present in the data
    if "trigger" in data:
        # Return a response indicating the workflow was triggered
        return {"status": "Triggered"}
    else:
        # Return a response indicating the workflow was not triggered
        return {"status": "Not Triggered"}

# Define an endpoint to simulate Azure Logic Apps
@app.route('/simulate-logic-app', methods=['POST'])
def simulate_logic_app_endpoint():
    # Extract JSON data from the incoming request
    data = request.json
    
    # Call the simulate_logic_app function to handle the workflow
    result = simulate_logic_app(data)
    
    # Return the workflow status as JSON response
    return jsonify(result)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)



# -->>>>>>> For test open How_To_Run.txt file