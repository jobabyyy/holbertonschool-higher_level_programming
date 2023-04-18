// fetches and displays value of Hello
// fetches from tag DIV#hello

$(function() {
    $.ajax({
      url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
      type: 'GET',
      dataType: 'text',
      success: function(data) {
        const matches = data.match(/<div class="hello">(.+)<\/div>/);
        $('#hello').text(matches[1]);
      }
    });
  });
  