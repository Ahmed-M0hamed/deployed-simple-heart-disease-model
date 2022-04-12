# deployed-iris_dataset-model
we will deploy simple model with docker and fast api 
to follow along you should make sure to get docker installed 

## The model 
we made simple randomforest model you can see in model.ipynb and we loaded it into 
pickle file and we conveted our test data to json file curl -X POST http://localhost:81/predict -d @./data/test.json -H "Content-Type: application/json"
    