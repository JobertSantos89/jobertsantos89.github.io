const containerPokemons = document.getElementById("pokemons")
const carregarMaisBtn = document.querySelector(".carregar-mais")
const select = document.getElementById("filtros")

console.log(select)
const BASE_API = "https://pokeapi.co/api/v2";

let offset = 0
let pokemons = [];

select.addEventListener("input", (eventoDeInput) => filtrarPorTipo(eventoDeInput.target.value))

async function pegarTipos() {
    try {
        const resposta = await fetch(`${BASE_API}/type`)
        const dados = await resposta.json()

        dados.results.forEach(tipo => {
            select.innerHTML += `<option value='${tipo.name}'>${tipo.name}</option>`
        })
    } catch (erro) {
        /* o catch  */
        alert(erro.message)
    }
}

async function pegarPokemons(voltarOriginal = false) {
    if (voltarOriginal) {
        offset = 0
        carregarMaisBtn.style.display = 'block'
        containerPokemons.innerHTML = ''
    }

    try {
        /* 
            o bloco TRY serve para testar se aquele trecho de código
            vai funcionar ou não, permitindo que você consiga tratar 
            o erro se acontecer. O TRY geralmente é utilizado somente
            quando o trecho de código está tentando fazer uma conexão
            com alguma ferramenta externa ao código, como o banco de dados
            ou servidor. Havendo erro, ele interrompe o bloco e joga o 
            erro no catch.
        */
        const resposta = await fetch(`${BASE_API}/pokemon?offset=${offset}`)
        const dados = await resposta.json()

        dados.results.forEach(item => {
            pegarPokemon(item.url)
        })

        // if(!dados.pokemon) {
        //     throw new Error("Não tem essa propriedade aqui")
        // }

    } catch (erro) {
        /* o catch  */
        alert(erro.message)
    } finally {
       // alert("rodamos o finally")
    }
}

function carregarMais() {
    offset += 20
    pegarPokemons()
}

function pegarPokemon(urlPokemon) {
    fetch(urlPokemon)
    .then(res => res.json())
    .then(pokemon => {
        pokemons.push(pokemon);

        mostrarNaTela(pokemon)
    })
    .catch((erro) => console.log(erro))
    .finally(() => {})
}

function mostrarNaTela(pokemon) {
    const img = pokemon.sprites.versions['generation-v']['black-white'].animated.front_default ? 
        pokemon.sprites.versions['generation-v']['black-white'].animated.front_default 
        : pokemon.sprites.front_default

    containerPokemons.innerHTML += `
        <div class="pokemon" onclick="irParaDetalhes('${pokemon.name}')">
            <img src="${img}" />
            <h2>${pokemon.name}</h2>

            <div class="types">
                ${pokemon.types.map(item => `<span class="type ${item.type.name}">${item.type.name}</span>`).join(" ")}
            </div>
        </div>
    `
}

async function filtrarPorTipo(nomeTipo) {
    containerPokemons.innerHTML = ''
    carregarMaisBtn.style.display = 'none'

    try {
        const resposta = await fetch(`${BASE_API}/type/${nomeTipo}`)
        const dados = await resposta.json()
    
        dados.pokemon.forEach(item => {
            pegarPokemon(item.pokemon.url)
        })
    } catch (err) {
        console.log(err)
    }

    // fetch(`${BASE_API}/type/${nomeTipo}`)
    // .then(resposta => resposta.json())
    // .then(dados => {
    //     dados.pokemon.forEach(item => {
    //         pegarPokemon(item.pokemon.url)
    //     })
    // })
}

function irParaDetalhes(nomePokemon) {
    localStorage.setItem('pokemon', nomePokemon)

    location = "../detalhes/index.html"
}

function filtrarPorPesquisa() {
    const pesquisa = document.getElementById("pesquisa").value

    if (pesquisa.length === 0) {
        pegarPokemon(true);

        return;
    }

    const pokemonsFiltrados = pokemons.filter(pokemon => pokemon.name.toLowerCase().includes(pesquisa.toLowerCase()) || pokemon.id == pesquisa)
    containerPokemons.innerHTML = ''
    pokemonsFiltrados.forEach(pokemon => mostrarNaTela(pokemon))
}

pegarPokemons() 
pegarTipos()
