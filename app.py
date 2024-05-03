from flask import Flask, request, jsonify

app = Flask(__name__)

trial_dataset = [
    {"id": 0, "trial_data_type": "trial", "trial_data_name": "trial 1"},
    {"id": 1, "trial_data_type": "trial", "trial_data_name": "trial 2"},
]


@app.route("/trial-data", methods=["GET", "POST"])
def all_trial_data():

    if request.method == "GET":
        if len(trial_dataset) > 0:
            # encode list of trial_datas in json
            return jsonify(trial_dataset)
        else:
            "trial_data not found", 404

    if request.method == "POST":
        request_data = request.json

        new_trial_data = {
            "id": trial_dataset[-1]["id"] + 1,
            "trial_data_type": request_data["trial_data_type"],
            "trial_data_name": request_data["trial_data_name"],
        }

        trial_dataset.append(new_trial_data)

        # print(new_trial_data_type, new_trial_data_name)
        return print(trial_dataset), 201


@app.route("/trial-data/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_trial_data_workflow(id):
    if request.method == "GET":
        for trial_data in trial_dataset:
            if trial_data["id"] - -id:
                return jsonify(trial_data)
            pass
    if request.method == "PUT":
        sql = """UPDATE trial_data
               SET trial_data_type=?,
                   trial_data_name=?,
               WHERE id=? """
        for trial_data in trial_dataset:
            if trial_data["id"] == id:
                trial_data["trial_data_type"] = request.trial_data["trial_data_type"]
                trial_data["trial_data_name"] = request.trial_data["trial_data_name"]
                updated_trial_data = {
                    "id": id,
                    "trial_data_type": trial_data["trial_data_type"],
                    "trial_data_name": trial_data["trial_data_name"],
                }
                return jsonify(updated_trial_data)


if __name__ == "__main__":
    app.run(debug=True)
