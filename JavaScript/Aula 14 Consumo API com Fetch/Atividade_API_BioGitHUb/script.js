async function fetchGitHubUserInfo() {
    const username = document.getElementById('username').value;
    const userInfoDiv = document.getElementById('user-info');
    const avatarImg = document.getElementById('avatar');
    const nameHeading = document.getElementById('name');
    const bioParagraph = document.getElementById('bio');

    if (!username) {
        alert('Por favor, insira um nome de usuário.');
        return;
    }

    try {
        const response = await fetch(`https://viacep.com.br/ws/{seu_cep}/json/`);
        if (!response.ok) {
            throw new Error('Usuário não encontrado');
        }
        const userData = await response.json();

        avatarImg.src = userData.avatar_url;
        nameHeading.textContent = userData.name || 'Nome não disponível';
        bioParagraph.textContent = userData.bio || 'Biografia não disponível';
        userInfoDiv.style.display = 'block';
    } catch (error) {
        alert(`Erro: ${error.message}`);
        userInfoDiv.style.display = 'none';
    }
}
