(function() {

  // Globals
  var url = '../parts-of-speech/',
      taret = document.querySelector('#target');

  // HTTP fetcher
  function get(url, handleSuccess) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (xmlhttp.readyState == XMLHttpRequest.DONE) {
        if (xmlhttp.status === 200) {
          if (handleSuccess) handleSuccess(JSON.parse(xmlhttp.responseText))
        } else {
          if (handleErr) handleErr(xmlhttp)
        }
      };
    };
    xmlhttp.open('GET', url, true);
    xmlhttp.send();
  };

  // Select a random element from an array
  function select(arr) {
    return arr[ parseInt(Math.random() * arr.length) ];
  }

  // Get the madlib content to write to the DOM
  function madLib(noun1, noun2, adjective, verb) {
    return 'The ' + noun1 + ' and the ' + adjective + ' ' + noun2 +
      ' did not ' + verb + ' together, despite popular opinion.';
  }

  // MAIN
  get(url + 'nouns.json', function(nouns) {
    get(url + 'adjectives.json', function(adjectives) {
      get(url + 'verbs.json', function(verbs) {
        target.innerHTML = madLib( select(nouns), select(nouns), select(adjectives), select(verbs) )
      })
    })
  })
})()