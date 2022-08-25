from ctypes import cast
import os
import json
from datetime import date

def write_json(new_data, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["movies"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def create_json(data,filename):
    # Serializing json
    json_object = json.dumps(data, indent=4)
    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)

movie_name=input("Enter Movie Name : ")

movie_year=int(input("Enter Movie Release Year : "))

movie_link=input("Enter Trailer Link Link : ")

json_obj =  { "name":movie_name,"year":movie_year }

json_obj_2={ "movie_name":movie_name,"year":movie_year,"link":movie_link,"cast_crew":[] }

if(len(movie_name)!=0 and len(movie_link)!=0 and movie_year>1900 and movie_year<=int(date.today().year)):
    os.mkdir("./movies/"+movie_name)
    create_json(json_obj_2, './movies/'+movie_name+'/data.json')
    write_json(json_obj, './movies.json')

    

