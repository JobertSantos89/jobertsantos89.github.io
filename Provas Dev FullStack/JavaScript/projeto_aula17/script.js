const apiKey = '2deac8aced7e6e4dc2e0a6bbcc0f2197'; // Substitua com sua chave da API
const apiUrl = 'https://api.themoviedb.org/3';

async function fetchMovies() {
    try {
        const response = await fetch(`${apiUrl}/movie/popular?api_key=${apiKey}`);
        const data = await response.json();
        displayMovies(data.results);
    } catch (error) {
        console.error('Erro ao buscar filmes:', error);
    }
}

async function fetchGenres() {
    try {
        const response = await fetch(`${apiUrl}/genre/movie/list?api_key=${apiKey}`);
        const data = await response.json();
        displayGenres(data.genres);
    } catch (error) {
        console.error('Erro ao buscar gêneros:', error);
    }
}

function displayGenres(genres) {
    const genreList = document.getElementById('genres');
    genreList.innerHTML = '';

    genres.forEach(genre => {
        const genreElement = document.createElement('div');
        genreElement.className = 'genre';
        genreElement.dataset.id = genre.id;
        genreElement.textContent = genre.name;

        genreElement.addEventListener('click', () => {
            fetchMoviesByGenre(genre.id);
        });
        genreList.appendChild(genreElement);
    });
}

async function fetchMoviesByGenre(genreId) {
    try {
        const response = await fetch(`${apiUrl}/discover/movie?api_key=${apiKey}&with_genres=${genreId}`);
        const data = await response.json();
        displayMovies(data.results);
        document.getElementById('home').style.display = 'block';
        document.getElementById('genres').style.display = 'none';
    } catch (error) {
        console.error('Erro ao buscar filmes por gênero:', error);
    }
}

function displayMovies(movies) {
    const movieList = document.getElementById('movie-list');
    movieList.innerHTML = '';

    movies.forEach(movie => {
        const movieElement = document.createElement('div');
        movieElement.className = 'movie';
        movieElement.dataset.id = movie.id;

        const movieImage = document.createElement('img');
        movieImage.src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
        movieImage.alt = movie.title;

        const movieTitle = document.createElement('div');
        movieTitle.className = 'movie-title';
        movieTitle.textContent = movie.title;

        movieElement.appendChild(movieImage);
        movieElement.appendChild(movieTitle);
        movieList.appendChild(movieElement);
    });

    document.querySelectorAll('.movie').forEach(movieElement => {
        movieElement.addEventListener('click', () => showMovieDetails(movieElement.dataset.id));
    });
}

async function showMovieDetails(movieId) {
    try {
        const response = await fetch(`${apiUrl}/movie/${movieId}?api_key=${apiKey}`);
        const movie = await response.json();

        document.getElementById('movie-title').textContent = movie.title;
        document.getElementById('movie-poster').src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
        document.getElementById('movie-overview').textContent = movie.overview;
        document.getElementById('movie-details').style.display = 'block';
    } catch (error) {
        console.error('Erro ao buscar detalhes do filme:', error);
    }
}

document.getElementById('close-details').addEventListener('click', () => {
    document.getElementById('movie-details').style.display = 'none';
});

async function searchMovies(query) {
    try {
        const response = await fetch(`${apiUrl}/search/movie?api_key=${apiKey}&query=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayMovies(data.results);
    } catch (error) {
        console.error('Erro ao buscar filmes:', error);
    }
}

document.getElementById('search-button').addEventListener('click', () => {
    const query = document.getElementById('search-input').value;
    if (query) {
        searchMovies(query);
    }
});

document.getElementById('home-link').addEventListener('click', () => {
    document.getElementById('home').style.display = 'block';
    document.getElementById('genres').style.display = 'none';
    fetchMovies(); // Carregar filmes na página inicial
});

document.getElementById('genres-link').addEventListener('click', () => {
    document.getElementById('home').style.display = 'none';
    document.getElementById('genres').style.display = 'flex';
    fetchGenres(); // Carregar gêneros ao clicar no link
});

document.addEventListener('DOMContentLoaded', fetchMovies);
