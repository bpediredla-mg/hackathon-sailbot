# hackathon-sailbot
Hackathon attempt to create a Sailthru chatbot from the publicly available Sailthru documentation

Note: Most of the code generated in this is via ChatGPT

#Prerequisites:
Download the Tinybloke language model and place it in the models directory. Refer to models/tinyllama-gguf/README.txt
This code assumes we're using tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf, change it it llm_backend.py accordingly

To run scraper to create the output file, run the following
```
cd backend
python scraper.py
```

To run frontend, navigate to frontend folder and run the following

```
cd frontend
python3 -m http.server 3000
```

To run backend, navigate to backend folder and run the following. If running for the first time create the new python virtual environment (commented out below)
```
cd backend
#python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
