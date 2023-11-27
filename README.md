# Chaabi <br>
First create a virtual environment and install requirements. <br>
Run database.ipynb file to see details of dataset and create a qdrant vector database on their cloud. Please replace api_key in qdrant client to use your own API key for qdrant cluster. <br>
Or, you can use any host with qdrant deployed and use the snapshot of vector db given [here](https://iitgoffice-my.sharepoint.com/:u:/g/personal/s_chivukula_iitg_ac_in/EfiSWjDRp7RFm-g1E0fnmfQBEEyLDjZERXZLNbsYKm7piw?e=QyC7vC) to create your own collecction.<br>

You can now run search.py file and use query function with input your request as a string. You can print it out to clearly see the result obtained. <br>
Now, the work is wrapped in a API using flask and REST for which you can find in flask.py. To request from flask.py you can edit request.py with your own search string.

![image](https://github.com/sai4132/Chaabi/assets/86120933/ee53804c-3b2e-4813-b939-cfb4d2ab107c)
![image](https://github.com/sai4132/Chaabi/assets/86120933/22dba21b-c598-4e8c-a57a-bd475b0ffd37)
![image](https://github.com/sai4132/Chaabi/assets/86120933/d4901dd8-89cc-4fa2-8ae7-f3f356203382)





