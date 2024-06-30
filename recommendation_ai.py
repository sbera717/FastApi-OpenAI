import os
import ast
import json
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

model = "gpt-3.5-turbo"
temperature = 0.7
max_tokens = 500

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key="sk-proj-HC4Q9Ma6V3PQB4e1MgbKT3BlbkFJbTuKR4KxnzyZM983g1uQ",
    )

def get_book_recommendations(book_title, book_dict, author):

    try:

        #prompts
        system_message = """
        You are an experienced literary curator and librarian at a prestigious book club. 
        Your task is to provide personalized book recommendations based on the preferences and themes of a given book.

        """
        prompt = f"""
        As a literary curator serving as a librarian at a prestigious book club, your role is to recommend top books similar to {book_title} by {author} strictly from the {book_dict}. 
        Your task is to select the top four books that closely align with {book_title} while ensuring all recommendations are from the {book_dict} only without including the given book itself. 
        Output should be a JSON where the keys are of recommended book title and the values are their author.
        constraint : Don't Recommend anything out of the {book_dict}.

        List of books:
        {', '.join(book_dict)}
        """
        
        # print("system_message :: ", system_message)
        # print("prompt :: ", prompt)
        messages = [
            {"role":"system", "content":system_message},
            {"role":"user","content":prompt}
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        return {"The function get_book_recommendations gave out the error : ": str(e)}   


def get_recomm_based_on_sentiment(user_text, book_dict):

    try:
        system_message = """ You are an emotion classifier and a book recommendation assistant.
        Given a text input, your task is to categorize the text into one of the six basic moods: Happy, Sad, Angry, Fearful, Surprised, or Disgusted. 
        Consider the emotional context and overall sentiment of the text when making your decision.
        Then Given a text input that has been categorized into one of the six basic moods—Happy, Sad, Angry, Fearful, Surprised, or Disgusted—your task is to recommend a book from the provided list of books that best matches the mood. 
        Each book in the list has an associated mood, and your recommendations should align with the emotional context of the input.
        """

        prompt = f""" Categorize the {user_text} into one of the six basic moods: Happy, Sad, Angry, Fearful, Surprised, or Disgusted.
            Then, recommend a book from the {book_dict} that matches the identified mood.
            Output Format: Python dict :: Mood : The categorized mood,
                            Recommended Book : The recommended book by author"
        """

        messages = [
            {"role":"system", "content":system_message},
            {"role":"user","content":prompt}
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        ) 
        return ast.literal_eval(completion.choices[0].message.content)
        
    except Exception as e:
        return {"The function get_recomm_based_on_sentiment gave out the error : ": str(e)} 


# -------------------------- INPUT ----------------------------------
# book_title = "To Kill a Mockingbird"
# book_author = "Harper Lee"
# books_dict = {
#     "1984": "George Orwell",
#     "Pride and Prejudice": "Jane Austen",
#     "The Catcher in the Rye": "J.D. Salinger",
#     "The Great Gatsby": "F. Scott Fitzgerald",
#     "The Grapes of Wrath": "John Steinbeck",
#     "Moby Dick": "Herman Melville",
#     "Brave New World": "Aldous Huxley",
#     "Lord of the Flies": "William Golding",
#     "Jane Eyre": "Charlotte Brontë",
#     "Animal Farm": "George Orwell"
# }

# print(get_book_recommendations(book_title, books_dict, book_author))

# user_text = "hello i had a breakup today and i am feeling very sad can you suggest some book which can give me relief"
# print(get_recomm_based_on_sentiment(user_text,books_dict))

# ------------------------- OUTPUT -------------------------------- 
# {
#     "1": "The Grapes of Wrath",
#     "2": "Lord of the Flies",
#     "3": "Animal Farm"
# }
