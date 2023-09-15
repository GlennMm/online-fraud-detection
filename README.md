### Online Fraud Detection Project
This repository contains the code for an online fraud detection project.The project uses the following technologies:

- Python - The programming language used to develop the project.
- Sklearn - A machine learning library used to train the AI model.
- TensorFlow - A deep learning library used to train the AI model.
- Django - A web framework used to create the REST API.
- Angular - A web framework used to create the frontend UI.

The project is divided into the following three parts:

- Model training - This part of the project uses Sklearn and TensorFlow to train the AI model. The model is trained on a dataset of fraudulent and non-fraudulent transactions.
- REST API - This part of the project uses Django to create a REST API that exposes the AI model. The REST API can be used to get predictions from the AI model.
- Frontend UI - This part of the project uses Angular to create a frontend UI that consumes the REST API. The frontend UI allows users to input transaction data and get predictions from the AI model.

To get started with the project, you can follow these steps:

Clone the repository to your local machine.
- Train the AI model.
    * `cd notebook`
    * open the notebook in vscode or pycharm
    * experiment with the model and then export the model that produced good results. 
- Run the REST API.
    * `cd api` and run `pip install -r requirements.txt`
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py createsuperuser` ( and follow the prompts also take note you put a secure password )
    * run `python manage.py runserver` to start the rest api
- Run the frontend UI.
    * `cd front` and run `npm install`
    * run `npm start` to start the ui
    
