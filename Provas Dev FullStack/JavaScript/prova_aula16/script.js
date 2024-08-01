document.addEventListener('DOMContentLoaded', () => {
    const API_URL_LIST = 'https://dog.ceo/api/breeds/list/all';
    const API_URL_IMAGES = 'https://dog.ceo/api/breed/{breed}/images/random/4';
    
    const listaRacasContainer = document.getElementById('listaRacas');
    const imagensRacaContainer = document.getElementById('imagensRaca');
    const loadingContainer = document.createElement('div');
    loadingContainer.id = 'loading';
    loadingContainer.textContent = 'Carregando...';
    document.body.appendChild(loadingContainer);

    async function obterListaRacas() {
        showLoading(true);
        try {
            const response = await fetch(API_URL_LIST);
            if (!response.ok) {
                throw new Error('Falha ao buscar a lista de raças');
            }
            const data = await response.json();
            exibirListaRacas(data.message);
        } catch (error) {
            showError('Erro ao obter a lista de raças.');
        } finally {
            showLoading(false);
        }
    }
    
    function exibirListaRacas(racas) {
        listaRacasContainer.innerHTML = '';
        for (const raca in racas) {
            const botaoRaca = document.createElement('button');
            botaoRaca.textContent = raca;
            botaoRaca.onclick = () => exibirImagensRaca(raca);
            listaRacasContainer.appendChild(botaoRaca);
        }
    }
    
    async function exibirImagensRaca(raca) {
        showLoading(true);
        try {
            const response = await fetch(API_URL_IMAGES.replace('{breed}', raca));
            if (!response.ok) {
                throw new Error('Falha ao buscar as imagens da raça');
            }
            const data = await response.json();
            exibirImagens(data.message);
        } catch (error) {
            showError('Erro ao obter as imagens da raça.');
        } finally {
            showLoading(false);
        }
    }
    
    function exibirImagens(imagens) {
        imagensRacaContainer.innerHTML = '';
        imagens.forEach(url => {
            const img = document.createElement('img');
            img.src = url;
            imagensRacaContainer.appendChild(img);
        });
    }

    function showLoading(show) {
        loadingContainer.style.display = show ? 'block' : 'none';
    }

    function showError(message) {
        alert(message); // Você pode melhorar o tratamento de erros exibindo uma mensagem no HTML
    }

    obterListaRacas();
});


