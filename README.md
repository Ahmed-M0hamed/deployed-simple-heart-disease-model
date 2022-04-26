# deployed-iris_dataset-model
we will deploy simple model with docker and fast api 
to follow along you should make sure to get docker installed 

## The model 
we made simple randomforest model you can see in model.ipynb and we loaded it into 
pickle file and we conveted our test data to json file 

## main.py 
this include the fast api server and some funcions to run the app 
this app accept batch json data and you can change it  

## run the app 
to run the app open your bash shell first type 
```bash 
docker build -t my_app . 
``` 
you build the image from the docker file which you can take look at 
-t => flag to choose name 

after that you can run your container so type 
```bash 
docker run --rm -p 81:80 my_app 
``` 
--rm => to remove the container when it,s stopped 
-p => choose the port 

and to get predictions you should have json file with the data like test.json 
and you type 
```bash 
curl -X POST http://localhost:81/predict \
    -d @./data/test.json \
    -H "Content-Type: application/json"
``` 

finally you should stop the container after you finish 

```bash
docker stop 'name or id'
```
