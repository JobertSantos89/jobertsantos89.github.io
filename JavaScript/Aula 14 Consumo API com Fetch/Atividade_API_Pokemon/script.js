async function buscarPokemon() {
    const pokemonName = document.getElementById('pokemonName').value.toLowerCase().trim();
    const pokemonNome = document.getElementById('pokemonNome');
    const pokemonImagem = document.getElementById('pokemonImagem');
    const pokemonTipos = document.getElementById('pokemonTipos');
    const pokemonHabilidades = document.getElementById('pokemonHabilidades');
    const pokemonInfoDiv = document.getElementById('pokemon-info');

    if (!pokemonName) {
        alert('Por favor, insira o nome ou número do Pokémon.');
        return;
    }

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
        if (!response.ok) {
            throw new Error('Pokémon não encontrado');
        }
        const pokemonData = await response.json();

        pokemonNome.textContent = `Nome: ${pokemonData.name}`;
        pokemonImagem.src = pokemonData.sprites.front_default;
        pokemonImagem.alt = `Imagem do ${pokemonData.name}`;

        const tipos = pokemonData.types.map(typeInfo => typeInfo.type.name).join(', ');
        pokemonTipos.textContent = `Tipos: ${tipos}`;

        const habilidades = pokemonData.abilities.map(abilityInfo => abilityInfo.ability.name).join(', ');
        pokemonHabilidades.textContent = `Habilidades: ${habilidades}`;

        pokemonInfoDiv.style.display = 'block';
    } catch (error) {
        alert(`Erro: ${error.message}`);
        pokemonInfoDiv.style.display = 'none';
    }
}