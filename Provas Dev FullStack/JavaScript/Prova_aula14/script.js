document.addEventListener('DOMContentLoaded', () => {
    const API_URL_LIST = 'https://dog.ceo/api/breeds/list/all';
    const API_URL_IMAGES = 'https://dog.ceo/api/breed/{breed}/images/random/4';
    
    const listaRacasContainer = document.getElementById('listaRacas');
    const imagensRacaContainer = document.getElementById('imagensRaca');
    
    async function obterListaRacas() {
        try {
            const response = await fetch(API_URL_LIST);
            const data = await response.json();
            exibirListaRacas(data.message);
        } catch (error) {
            alert('Erro ao obter a lista de raças.');
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
        try {
            const response = await fetch(API_URL_IMAGES.replace('{breed}', raca));
            const data = await response.json();
            exibirImagens(data.message);
        } catch (error) {
            alert('Erro ao obter as imagens da raça.');
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
    
    obterListaRacas();
});

