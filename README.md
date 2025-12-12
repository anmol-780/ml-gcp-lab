# ml-gcp-lab
# ML API Docker Project

This project is a simple Machine Learning API that runs inside a Docker container.  
It loads a trained model (`model.pkl`) and provides a `/predict` endpoint to make predictions.

---

## 👥 Group Members

- **Anmolpreet Kaur**  
- **Harinderjeet Singh**  
- **Gurwinder Kaur**  
- **Harjoban Singh**

## 📦 Project Structure

ml-gcp-lab/
├── api/
│ └── main.py
├── models/
│ └── model.pkl
├── requirements.txt
└── Dockerfile

---

## 🚀 How to Build the Docker Image

Run this command in the terminal:

```bash
docker build -t ml-gcp-app .
docker run -p 8080:8080 ml-gcp-app
* Serving Flask app 'main'
* Running on http://0.0.0.0:8080
Press CTRL+C to quit
 📡 How to Test the API

Open a second terminal and use curl:
curl -X POST -H "Content-Type: application/json" -d '{"input": 5}' http://localhost:8080/predict
responses:
{
    "prediction": 10.0
}
Model

The project includes a simple Linear Regression model stored as models/model.pkl.
This model was trained on small sample data for demonstration purposes.
Technologies Used

Python 3.10

Flask

Scikit-learn

Docker

Notes

Make sure Docker is installed and running.

Do not stop the container when testing the API.

The project is for learning Docker containerization of ML applications.

## Docker Hub Images
- ML App Image: https://hub.docker.com/r/anmol1307preet/mlapp
- MLflow Image: https://hub.docker.com/r/anmol1307preet/mlflow
