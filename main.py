from fastapi import FastAPI
from models import Test,Test1
from services import TestService

# Instantiate the FastAPI app
app = FastAPI()

# Instantiate the TestService
test_service = TestService()

# Define the POST endpoint
@app.post("/allbooks")
async def get_books(test: Test):
   return test_service.check(test)  # Call the check method


@app.post("/user")
async def get_response(test1: Test1):
   return test_service.check1(test1)  # Call the check method

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
