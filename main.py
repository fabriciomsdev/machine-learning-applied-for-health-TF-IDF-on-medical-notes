
import os
from dotenv import load_dotenv
import requests

from dtos import ResultElement, UMLSSearchResponse, UMLSSearchResponseResult

load_dotenv()

class Config:
    class Providers:
        UMLS_api_key = os.getenv("UMLS_API_KEY")



class MedicalNotesStorage:
    storage_root = './data/medical_notes'

    def load_notes(self):
        pass

class UMLSClient:
    @property
    def search_url(self):
        return "https://uts-ws.nlm.nih.gov/search/current?string="
    
    def __init__(self, key = Config().Providers.UMLS_api_key):
        self.key = key

    def find_medical_term(self, term: str):
        url = self.search_url + term + '&apiKey=' + self.key
        reponse = requests.get(self.search_url + term)

        if reponse.status_code == 200:
            json = reponse.json()
            return UMLSSearchResponse(
                pageSize=json.get("pageSize"),
                pageNumber=json.get("pageNumber"),
                result=[
                    UMLSSearchResponseResult(
                        classType=result.get("classType"),
                        results=[
                            ResultElement(
                                ui=result.get("ui"),
                                rootSource=result.get("rootSource"),
                                uri=result.get("uri"),
                                name=result.get("name")
                            )
                            for result in json.get("result")
                        ],
                        recCount=json.get("recCount")
                    )
                    for result in json.get("result")
                ]
            )
        

