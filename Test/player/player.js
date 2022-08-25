
var get_link=new URLSearchParams(window.location.search);
var mov_name=get_link.get("movie");


$(function () {
    $.getJSON('../movies/'+mov_name+'/data.json', function (data) {
        document.getElementById("title").innerHTML = data.movie_name;
        document.getElementById("year").innerHTML = data.year;
        document.getElementById('yt-trailer').src=data.link;
        for (var key in data.cast_crew) {
            var idiv = document.createElement('div');
            idiv.className = "crew-card";

            var image = document.createElement('img');
            image.src = data.cast_crew[key].img_link;
            image.alt = "cast-crew_image";
            
            var name = document.createElement('p');
            name.className = "cast-name";
            name.innerHTML = data.cast_crew[key].name;

            idiv.appendChild(image);
            idiv.appendChild(name);
            document.getElementById('grid').appendChild(idiv);
        };
    })

});
