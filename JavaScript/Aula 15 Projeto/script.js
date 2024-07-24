document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const contactList = document.getElementById('contact-list');

    let contacts = [];
    let editIndex = -1;  // Para armazenar o índice do contato em edição

    const addContact = (name, phone, email) => {
        contacts.push({ name, phone, email });
        renderContacts();
    };

    const editContact = (index, name, phone, email) => {
        contacts[index] = { name, phone, email };
        renderContacts();
    };

    const deleteContact = (index) => {
        contacts.splice(index, 1);
        renderContacts();
    };

    const renderContacts = () => {
        contactList.innerHTML = '';
        contacts.forEach((contact, index) => {
            const contactItem = document.createElement('li');
            contactItem.innerHTML = `
                <form>
                    <input type="text" value="${contact.name}" readonly>
                    <input type="text" value="${contact.phone}" readonly>
                    <input type="email" value="${contact.email}" readonly>
                    <div class="buttons">
                        <button type="button" class="edit-btn">Editar</button>
                        <button type="button" class="delete-btn">Excluir</button>
                    </div>
                </form>
            `;
            
            // Event listener para o botão Editar
            contactItem.querySelector('.edit-btn').addEventListener('click', () => startEditContact(index));
            
            // Event listener para o botão Excluir
            contactItem.querySelector('.delete-btn').addEventListener('click', () => deleteContact(index));
            
            contactList.appendChild(contactItem);
        });
    };

    const startEditContact = (index) => {
        const contact = contacts[index];
        document.getElementById('name').value = contact.name;
        document.getElementById('phone').value = contact.phone;
        document.getElementById('email').value = contact.email;
        editIndex = index;
    };

    const addNewContact = (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;

        if (editIndex >= 0) {
            editContact(editIndex, name, phone, email);
            editIndex = -1;  // Resetar o índice de edição após a edição ser concluída
        } else {
            addContact(name, phone, email);
        }

        contactForm.reset();
    };

    // Impede a digitação de caracteres não numéricos no campo telefone
    document.getElementById('phone').addEventListener('input', (e) => {
        e.target.value = e.target.value.replace(/\D/g, '');
    });

    contactForm.onsubmit = addNewContact;
});
