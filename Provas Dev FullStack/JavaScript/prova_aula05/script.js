// Array para armazenar as tarefas
var tarefas = [];

// Função para adicionar uma nova tarefa
function adicionarTarefa() {
    var novaTarefaInput = document.getElementById("novaTarefa");
    var responsavelInput = document.getElementById("responsavel");
    var statusSelect = document.getElementById("status");

    var novaTarefaTexto = novaTarefaInput.value.trim();
    var responsavelTexto = responsavelInput.value.trim();
    var statusSelecionado = statusSelect.value;

    if (novaTarefaTexto !== "") {
        var tarefa = {
            descricao: novaTarefaTexto,
            responsavel: responsavelTexto,
            status: statusSelecionado
        };
        tarefas.push(tarefa);
        atualizarListaTarefas();
        novaTarefaInput.value = "";
        responsavelInput.value = "";
        statusSelect.value = "aguardando";
    } else {
        alert("Por favor, insira uma tarefa válida.");
    }
}

// Função para atualizar a lista de tarefas na página
function atualizarListaTarefas() {
    var listaTarefas = document.getElementById("tarefas");
    listaTarefas.innerHTML = ""; // Limpa a lista antes de atualizar

    // Adiciona cada tarefa à lista
    for (var i = 0; i < tarefas.length; i++) {
        var divTarefa = document.createElement("div");
        divTarefa.classList.add("tarefa");
        var statusClass = tarefas[i].status === "aguardando" ? "aguardando" : "finalizado";
        divTarefa.innerHTML = '<span>' + tarefas[i].descricao + ' - ' + tarefas[i].responsavel + ' - ' + tarefas[i].status + '</span>' +
                              '<button onclick="removerTarefa(' + i + ')">Remover</button>';
        listaTarefas.appendChild(divTarefa);
    }
}

// Função para remover uma tarefa
function removerTarefa(index) {
    tarefas.splice(index, 1);
    atualizarListaTarefas();
}

// Função para limpar todas as tarefas
function limparTarefas() {
    tarefas = [];
    atualizarListaTarefas();
}