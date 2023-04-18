// script that fetches title

$(document).ready(function() {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
      const movies = data.results;
      const list = $('#list_movies');
      for (const movie of movies) {
        list.append('<li>' + movie.title + '</li>');
      }
    });
  });
  