
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# Instantiating the class without storing the instance
# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)



# Without instantiating, it will throw an error, missing argument 'self'
# Instantiate the class: The self parameter is only passed to methods if called on an object.
# That said, you can fix the error by instantiating the class and calling the method on the object instance.
# programs = GetPrograms.get_programs()

# class GetPrograms:

#   @staticmethod
#   def get_programs():
#     URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

#     response = requests.get(URL)
#     return response.content



# programs = GetPrograms.get_programs()
