from src import Gmaps

queries = [
   "web developers in austin texas"
]

Gmaps.places(queries, max=5)
