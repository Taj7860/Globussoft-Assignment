from fastapi import FastAPI

app = FastAPI()

tourist_place = {
                    'india' : ['Charminar', 'Kerala', 'Manali'],
                    'france': ['Eiffel Tower', 'france museum'],
                    'japan' : [ 'Mount fuji', 'Osaka']

}

@app.get("/hello/{country}")
def hello(country: str):
    return tourist_place.get(country.lower(),["Data not found"])