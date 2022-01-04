# pastebin_api_clone

simple api to post and get your code from server just like pastebin,but api only

## How to use 
The api hosted at : https://pastebincloneapi.pythonanywhere.com/api/v1/paste
##### Endpoint
1. Get all code  
   `api/v1/paste`  : return all codes
2. Get code by unique_id  
   `GET api/v1/paste/:unique_id` : return a code select by unique id,you will get unique id when add code
3. Add new code  
    `POST api/v1/paste` : return a unique id of added code if success
## How to run locally 
1. git clone this repository 
   ```bash
   git clone https://github.com/AlphaBeta1906/pastebin_api_clone/
   ```
3. make and activate virtualenv
   ```bash
   virtualenv venv
   . venv/bin/activate
   ```
4. Install dependency 
   ```bash
   pip install requirements.txt
   ```
5. Run server
   ```bash
   python app.py
   ```
   
