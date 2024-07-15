async function buscarCEP() {
    const cep = document.getElementById('cep').value.replace(/\D/g, '');
    const logradouro = document.getElementById('logradouro');
    const bairro = document.getElementById('bairro');
    const cidade = document.getElementById('cidade');
    const estado = document.getElementById('estado');
    const enderecoInfoDiv = document.getElementById('endereco-info');

    if (!cep) {
        alert('Por favor, insira um CEP.');
        return;
    }

    try {
        const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        if (!response.ok) {
            throw new Error('CEP não encontrado');
        }
        const enderecoData = await response.json();

        if (enderecoData.erro) {
            throw new Error('CEP não encontrado');
        }

        logradouro.textContent = `Logradouro: ${enderecoData.logradouro || 'Não disponível'}`;
        bairro.textContent = `Bairro: ${enderecoData.bairro || 'Não disponível'}`;
        cidade.textContent = `Cidade: ${enderecoData.localidade || 'Não disponível'}`;
        estado.textContent = `Estado: ${enderecoData.uf || 'Não disponível'}`;
        enderecoInfoDiv.style.display = 'block';
    } catch (error) {
        alert(`Erro: ${error.message}`);
        enderecoInfoDiv.style.display = 'none';
    }
}

