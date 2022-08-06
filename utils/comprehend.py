import os
import boto3

class Comprehend:

    def __init__(self):
        self.client = boto3.client('comprehend',
        aws_access_key_id=os.environ.get("ACCESS_KEY", None),
        aws_secret_access_key=os.environ.get("SECRET_KEY", None),
        region_name=os.environ.get("SESSION_TOKEN", None),
        )

    def detectar_sentimento(self, texto):
        result = self.client.detect_sentiment(Text=texto, LanguageCode='en')
        return result

    def detectar_palavra_chave(self, texto):
        result = self.client.detect_key_phrases(Text=texto, LanguageCode='en')
        return result

