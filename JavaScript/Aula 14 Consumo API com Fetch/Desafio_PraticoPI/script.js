const API_KEY = 'SUA_CHAVE_API_AQUI'; // Substitua pela sua chave API do TMDb
const API_URL = 'https://api.themoviedb.org/3';
const IMG_URL = 'https://image.tmdb.org/t/p/w500';

async function buscarFilmesPopulares() {
    try {
        const response = await fetch(`${API_URL}/movie/popular?api_key=${API_KEY}&language=pt-BR`);
        const data = await response.json();
        exibirFilmes(data.results, 'filmesPopulares');
    } catch (error) {
        alert('Erro ao buscar filmes populares');
    }
}

async function buscarFilmes() {
    const termoBusca = document.getElementById('searchInput').value;
    if (!termoBusca) return;

    try {
        const response = await fetch(`${API_URL}/search/movie?api_key=${API_KEY}&query=${termoBusca}&language=pt-BR`);
        const data = await response.json();
        exibirFilmes(data.results, 'resultadosBusca');
    } catch (error) {
        alert('Erro ao buscar filmes');
    }
}

function exibirFilmes(filmes, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    filmes.forEach(filme => {
        const filmeCard = document.createElement('div');
        filmeCard.classList.add('filme-card');
        filmeCard.innerHTML = `
            <img src="${IMG_URL}${filme.poster_path}" alt="${filme.title}">
            <h3>${filme.title}</h3>
            <button onclick="verDetalhes(${filme.id})">Detalhes</button>
        `;
        container.appendChild(filmeCard);
    });
}

async function verDetalhes(filmeId) {
    try {
        const response = await fetch(`${API_URL}/movie/${filmeId}?api_key=${API_KEY}&language=pt-BR&append_to_response=credits`);
        const filme = await response.json();

        document.getElementById('tituloFilme').textContent = filme.title;
        document.getElementById('sinopseFilme').textContent = `Sinopse: ${filme.overview}`;
        document.getElementById('anoFilme').textContent = `Ano: ${filme.release_date.split('-')[0]}`;
        document.getElementById('generoFilme').textContent = `Gênero: ${filme.genres.map(g => g.name).join(', ')}`;
        document.getElementById('avaliacaoFilme').textContent = `Avaliação: ${filme.vote_average}`;
        document.getElementById('elencoFilme').textContent = `Elenco: ${filme.credits.cast.slice(0, 5).map(a => a.name).join(', ')}`;

        document.getElementById('detalhesFilme').style.display = 'block';
        document.getElementById('filmesPopulares').style.display = 'none';
        document.getElementById('resultadosBusca').style.display = 'none';
    } catch (error) {
        alert('Erro ao buscar detalhes do filme');
    }
}

function fecharDetalhes() {
    document.getElementById('detalhesFilme').style.display = 'none';
    document.getElementById('filmesPopulares').style.display = 'flex';
    document.getElementById('resultadosBusca').style.display = 'flex';
}

// Inicialização
