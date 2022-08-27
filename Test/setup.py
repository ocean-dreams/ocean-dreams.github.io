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

movie_link=input("Enter Trailer Video Youtube Id : ")

banner_img_link=input("Enter Banner Image Link : ")

poster_img_link=input("Enter Poster Image Link : ")

json_obj =  { "name":movie_name,"year":movie_year }

json_obj_2={ "movie_name":movie_name,"year":movie_year,"link":"https://www.youtube.com/embed/"+movie_link,"cast_crew":[] }

if(len(banner_img_link)!=0 and len(movie_name)!=0 and len(movie_link)!=0 and movie_year>1900 and movie_year<=int(date.today().year)):
    os.mkdir("./movies/"+movie_name)
    print('curl "'+banner_img_link+'" -o \"./movies/'+ movie_name + '/banner.jpg\"')
    print('curl "'+poster_img_link+'" -o \"./movies/'+ movie_name + '/poster.jpg\"')
    create_json(json_obj_2, './movies/'+movie_name+'/data.json')
    write_json(json_obj, './movies.json')

os.system("pause")    

    

