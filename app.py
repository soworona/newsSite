from flask import Flask, request, render_template 
import pickle

app = Flask(__name__)


#model = pickle.load(open ("finalized_model.pkl","rb"))



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():

      return render_template("predict.html")


if __name__ == "__main__": app.run()

