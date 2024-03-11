# 1. import the library
import uvicorn
from fastapi import FastAPI

# 2. Create the app project
app = FastAPI()

# 3. Index route, open automatically on http://127.0.0.1:8000
@app.get('/')
# @app it based on the object name in step 2 app = FastAPI() if you change 
# app to application the it will be @application
def index():
    return {'message': 'Hello World'}

# 4. Route with a single parameter, returns the parameter with a message
# Located at: http://127.0.0.1:8000/AnyNameHere

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to Marwah Portfolio':f'{name}'}

# 5. Run the API with uvicorn
# Will run on the http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 8000)

# to run the app run the following in command line: uvicorn main:app --reload
# to send message next to the local host add /the message
# other commane: next to the local host add /docs
# other commane: next to the local host add /redoc