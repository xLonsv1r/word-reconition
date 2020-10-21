import random
import os
from flask import Flask, request, jsonify
from keyword_spotting_service import Keyword_Spotting_Service


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
	

	
	audio_file = request.files["file"]
	file_name = str(random.randint(0, 100000))
	audio_file.save(file_name)

	
	kss = Keyword_Spotting_Service()
	predicted_keyword = kss.predict(file_name)

	
	os.remove(file_name)

	
	result = {"keyword": predicted_keyword}
	return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)
