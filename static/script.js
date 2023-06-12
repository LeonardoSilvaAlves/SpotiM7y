// Lógica JavaScript para interagir com o back-end

// Função para fazer uma chamada AJAX ao endpoint de pesquisa
function searchMusic() {
    var searchQuery = document.getElementById('search_query').value;
  
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/search', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var searchResults = document.getElementById('search-results');
        searchResults.innerHTML = xhr.responseText;
      }
    };
    xhr.send('search_query=' + encodeURIComponent(searchQuery));
  }
  
  // Adicione os eventos aos elementos do formulário
  var searchForm = document.getElementById('search-form');
  if (searchForm) {
    searchForm.addEventListener('submit', function(event) {
      event.preventDefault();
      searchMusic();
    });
  }
  