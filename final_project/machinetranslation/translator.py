"""
Import ibm watson LanguageTranslatorV3 to start translation
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('TDzST_QJMLGSk4VfqVBsm1JHMwLaUvBpTXwqnZb3wrbE')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/71f754af-208f-4009-8a44-cb7bac98416b')

def english_to_french(english_text):
    #write the code here
    """
    This function translates English to French and return the French text.
    """
    french_translation = language_translator.translate(
        text=english_text,
        model_id="en-fr").get_result()
    french_text=french_translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    """
    This function translates French to English and return the English text.
    """
    english_translation = language_translator.translate(
        text=french_text,
        model_id="fr-en").get_result()
    english_text=english_translation['translations'][0]['translation']
    return english_text
