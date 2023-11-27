# Chaabi <br>

![image](https://github.com/sai4132/Chaabi/assets/86120933/d1cc7cd5-f040-44ae-8e41-feb1d54870f5)
![image](https://github.com/sai4132/Chaabi/assets/86120933/25141b88-2edc-4df8-8625-eca0bf26ea23)
![image](https://github.com/sai4132/Chaabi/assets/86120933/22f9c861-1278-48f4-9c4e-b40d98a0cdd1)

First create a virtual environment and install requirements. <br>
Run database.ipynb file to see details of dataset and create a qdrant vector database on their cloud. Please replace api_key in qdrant client to use your own API key for qdrant cluster. <br>
Or, you can use any host with qdrant deployed and use the snapshot of vector db given to create your own collecction.<br>

You can now run search.py file and use query function with input your request as a string. You can print it out to clearly see the result obtained. <br>
Now, the work is wrapped in a API using flask and REST for which you can find in flask.py. To request from flask.py you can edit request.py with your own search string.
