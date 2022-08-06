from os import getenv
import boto3

class Comprehend:

    def __init__(self):
        self.client = boto3.client('comprehend',
        aws_access_key_id=getenv("ACCESS_KEY"),
        aws_secret_access_key=getenv("SECRET_KEY"),
        aws_session_token=getenv("SESSION_TOKEN")
        )

    def detectar_sentimento(self, texto):
        result = self.client.detect_sentiment(Text=texto, LanguageCode='en')
        return result

    def detectar_palavra_chave(self, texto):
        result = self.client.detect_key_phrases(Text=texto, LanguageCode='en')
        return result

