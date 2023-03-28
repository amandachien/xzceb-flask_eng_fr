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

authenticator = IAMAuthenticator('q83hgme1vXuGAubDp5z8EdW9_mGywZuoLeNU_XSOBHuJ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/7fee2882-9338-4e0b-9821-b7b6c5dc5825')

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
