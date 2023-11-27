# Chaabi <br>
First create a virtual environment and install requirements. <br>
Run database.ipynb file to see details of dataset and create a qdrant vector database on their cloud. Please replace api_key in qdrant client to use your own API key for qdrant cluster. <br>
Or, you can use any host with qdrant deployed and use the snapshot of vector db given [here](https://iitgoffice-my.sharepoint.com/:u:/g/personal/s_chivukula_iitg_ac_in/EfiSWjDRp7RFm-g1E0fnmfQBEEyLDjZERXZLNbsYKm7piw?e=QyC7vC) to create your own collecction.<br>

You can now run search.py file and use query function with input your request as a string. You can print it out to clearly see the result obtained. <br>
Now, the work is wrapped in a API using flask and REST for which you can find in flask.py. To request from flask.py you can edit request.py with your own search string.

![image](https://github.com/sai4132/Chaabi/assets/86120933/0ed6f3fe-1635-43b1-938a-3eae33dd4f46)
![image](https://github.com/sai4132/Chaabi/assets/86120933/f4e64336-e767-48bf-98b6-d5618964bc5b)
![image](https://github.com/sai4132/Chaabi/assets/86120933/aa5bed7d-5cbc-464b-86b7-fc81dce4858a)



