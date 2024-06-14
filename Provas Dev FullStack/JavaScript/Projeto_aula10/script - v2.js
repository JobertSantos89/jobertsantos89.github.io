const formulario = document.querySelector("form")
const containerTarefas = document.querySelector(".tarefas")
const concluidas = document.querySelector(".concluidas")

formulario.addEventListener("submit", adicionarTarefa)
//formulario.removeEventListener("submit", adicionarTarefa)

let tarefas = []

function adicionarTarefa(eventoDeSubmit) {
    eventoDeSubmit.preventDefault()

    const nomeTarefa = formulario.nome.value

    tarefas.push(nomeTarefa)

    mostrarNaTela()
}

function mostrarNaTela() {
    containerTarefas.innerHTML = ''

    for (let tarefa of tarefas) {
        const containerTarefa = document.createElement("div")
        containerTarefa.classList.add("tarefa")

        const input = document.createElement("input")
        input.type = "checkbox"
        input.addEventListener("input", contabilizarConcluidas)

        const p = document.createElement("p")
        p.innerHTML = tarefa

        const containerBotoes = document.createElement("div")

        const botaoEditar = document.createElement("button")
        botaoEditar.innerText = "Editar"
        botaoEditar.addEventListener("click", () => editarTarefa(tarefa))

        const botaoApagar = document.createElement("button")
        botaoApagar.innerText = "Apagar"
        botaoApagar.addEventListener("click", () => apagarTarefa(tarefa))

        containerBotoes.append(botaoEditar, botaoApagar)
        containerTarefa.append(input, p, containerBotoes)

        containerTarefas.appendChild(containerTarefa)
    }
}

function contabilizarConcluidas() {
    const inputsConcluidas = document.querySelectorAll("input[type=checkbox]:checked")

    concluidas.innerHTML = inputsConcluidas.length
}

function editarTarefa(nomeTarefa) {
    const novoNome = prompt("Digite o novo nome da tarefa")

    if (!novoNome /* novoNome == "" */) {
        return;
    }

    const index = tarefas.indexOf(nomeTarefa)
    
    if (index === -1) {
        alert("A tarefa não foi encontrada")
        return
    }

    tarefas[index] = novoNome


    /* for (let i = 0; i < tarefas.length; i++) {
        if (tarefas[i] === nomeTarefa) {
            tarefas[i] = novoNome

            break
        }
    } */

    mostrarNaTela()
}

function apagarTarefa(nomeTarefa) {
    //containerTarefas.removeChild(container)

    /* const index = tarefas.indexOf(nomeTarefa)
    
    if (index === -1) {
        alert("A tarefa não foi encontrada")
        return
    }

    tarefas.splice(index, 1) */

    //splice ou for

    let novoArray = []

    for (let tarefa of tarefas) {
        if (tarefa !== nomeTarefa) {
            novoArray.push(tarefa)
        }
    }

    tarefas = novoArray

    mostrarNaTela()
}