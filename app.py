########################################################################################################################################
# SCRIPT NAME:             app.py                                                                                                      #
# AUTHOR NAME:             NAMAN SINGHAI                                                                                               #
########################################################################################################################################


from flask import Flask, request, jsonify

# CREATE APPLICATION INSTANCE
app = Flask(__name__)

# DUMMY DATA
dummy_data = [
                {
                    "city": "Mumbai",
                    "state": "Maharashtra"
                },
                {
                    "city": "Kolkata",
                    "state": "West Bengal"
                },
                {
                    "city": "Chennai",
                    "state": "Tamil Nadu"
                },
                {
                    "city": "Bangalore",
                    "state": "Karnataka"
                }
            ]

@app.route("/city", methods=["GET", "POST"])
def city():
    if request.method == "GET":
        if len(dummy_data) > 0:
            return jsonify(dummy_data)
        else:
            "NOTHING FOUND", 404
    elif request.method == "POST":
        city = request.form["city"]
        state = request.form["state"]

        new_object = {
            "city": city,
            "state": state
        }

        dummy_data.append(new_object)
        return jsonify(dummy_data), 201

# if __name__ == "__main__":
#     app.run()
