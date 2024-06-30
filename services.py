from models import Test,Test1
from recommendation_ai import get_book_recommendations,get_recomm_based_on_sentiment

class TestService:
    def check(self, test: Test):
        return get_book_recommendations(test.book,test.allBooks,test.author)

    def check1(self, test1 : Test1):
        return get_recomm_based_on_sentiment(test1.userText,test1.allBooks)
