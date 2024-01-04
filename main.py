from src import Gmaps
import requests

def get_query_parameter(parameter_name):
  request = requests.get("http://localhost:8080/")
  query_parameters = request.args
  return query_parameters.get(parameter_name)

query_parameter_value = get_query_parameter("query")
print(query_parameter_value)


#queries = [
#   "web developers in austin texas"
#]

#Gmaps.places(queries, max=5)
