document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addTaskButton = document.getElementById('addTaskButton');
    const taskList = document.getElementById('taskList');

    // Função para adicionar uma nova tarefa
    function addTask() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            const listItem = document.createElement('li');
            listItem.className = 'task-item';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.addEventListener('change', () => {
                if (checkbox.checked) {
                    taskSpan.classList.add('completed');
                    listItem.removeChild(deleteButton);
                    const completedText = document.createElement('span');
                    completedText.textContent = 'Concluído';
                    completedText.className = 'completed-text';
                    listItem.appendChild(completedText);
                } else {
                    taskList.removeChild(listItem);
                }
            });

            const taskSpan = document.createElement('span');
            taskSpan.textContent = taskText;
            taskSpan.className = 'task-text';

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Remover';
            deleteButton.addEventListener('click', () => {
                taskList.removeChild(listItem);
            });

            listItem.appendChild(checkbox);
            listItem.appendChild(taskSpan);
            listItem.appendChild(deleteButton);
            taskList.appendChild(listItem);

            // Limpa o campo de entrada de texto
            taskInput.value = '';
        }
    }

    // Adicionar tarefa ao clicar no botão
    addTaskButton.addEventListener('click', addTask);

    // Adicionar tarefa ao pressionar Enter
    taskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addTask();
        }
    });
});
