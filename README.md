# **AI BookWise - FastAPI**
This FastAPI application is a component of the AI BookWise system, designed to connect with the OpenAI model. Based on inputs from the Spring Boot application, it provides book recommendations and bibliotherapy to assist users during challenging times.

# **Purpose**
The primary purpose of this application is twofold:

**Book Recommendations:**

When a user returns a book, the Spring Boot application sends this data to the FastAPI application.
The FastAPI application uses the OpenAI model to recommend three books based on the returned book.

**Sentiment Analysis:**

The Spring Boot application sends user thoughts to the FastAPI application.
After performing sentiment analysis, the FastAPI application uses OpenAI to recommend books that can improve the user's mood and provide comfort.

# **To run the FastAPI application, follow these steps:**

Clone the repository into your local system:

Navigate to the project directory

**Install the required dependencies:**

pip install -r requirements.txt

**Start the FastAPI server:**

uvicorn main:app --reload

# **Configuration**
Ensure that the FastAPI application is configured correctly to connect to the OpenAI model. You may need to set up environment variables or configuration files with the necessary API keys and settings.

**Please change the OpenAI key with your OpenAI key; otherwise, it won't work.**

# **Additional Information**
For more detailed instructions and information about the overall AI BookWise system, please refer to the main **GitHub repository :** https://github.com/sbera717/Library


