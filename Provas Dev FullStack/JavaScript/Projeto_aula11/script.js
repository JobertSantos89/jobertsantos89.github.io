const questions = [
    'Quem pintou a Mona Lisa?',
    'Qual é a fórmula química da água?',
    'Quem foi o primeiro presidente dos Estados Unidos?',
    'Qual é a capital da Austrália?',
    'Qual é a maior montanha do mundo?',
    'Em que ano o homem pisou na Lua pela primeira vez?',
    'Qual é o menor país do mundo?',
    'Quem escreveu "Dom Quixote"?',
    'Qual é o planeta mais próximo do sol?',
    'Quantos estados há no Brasil?'
];

const options = [
    ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    ["H2O", "CO2", "O2", "N2"],
    ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
    ["Sydney", "Melbourne", "Canberra", "Brisbane"],
    ["Monte Everest", "K2", "Kangchenjunga", "Lhotse"],
    ["1965", "1969", "1971", "1973"],
    ["Vaticano", "Mônaco", "Nauru", "San Marino"],
    ["William Shakespeare", "Miguel de Cervantes", "Homer", "Dante Alighieri"],
    ["Mercúrio", "Vênus", "Terra", "Marte"],
    ["24", "26", "27", "29"]
];

const correctAnswers = [0, 0, 1, 2, 0, 1, 0, 1, 0, 2];

const explanations = [
    "Leonardo da Vinci pintou a Mona Lisa, uma das pinturas mais famosas do mundo.",
    "A fórmula química da água é H2O, composta por dois átomos de hidrogênio e um de oxigênio.",
    "George Washington foi o primeiro presidente dos Estados Unidos, servindo de 1789 a 1797.",
    "Canberra é a capital da Austrália, escolhida como um compromisso entre Sydney e Melbourne.",
    "O Monte Everest, com 8.848 metros, é a montanha mais alta do mundo.",
    "O homem pisou na Lua pela primeira vez em 1969, durante a missão Apollo 11.",
    "O Vaticano é o menor país do mundo, tanto em área quanto em população.",
    "Miguel de Cervantes escreveu 'Dom Quixote', uma das obras mais importantes da literatura ocidental.",
    "Mercúrio é o planeta mais próximo do sol em nosso sistema solar.",
    "O Brasil possui 26 estados e um Distrito Federal, totalizando 27 unidades federativas."
];

let reloadButton = document.getElementById('reload');
reloadButton.style.display = "none";
let nowQuestion = Math.floor(Math.random() * questions.length);

generateQuestions();
selectButton();

function generateQuestions() {
    document.getElementById("question").innerHTML = questions[nowQuestion];
    
    const optionsContainer = document.querySelectorAll('button.alternative');
    optionsContainer.forEach((element, index) => {
        element.textContent = options[nowQuestion][index];
    });
}

function selectButton() {
    const alternatives = document.querySelectorAll('.alternative');

    alternatives.forEach(button => {
        button.addEventListener('click', () => {
            const answer = button.value;
            checkAnswer(answer);
        });
    });
}

function checkAnswer(answer) {
    answer = parseInt(answer);
    let statusAnswer = document.getElementById("statusAnswer");
    if (answer === correctAnswers[nowQuestion]) {
        statusAnswer.innerHTML = `Acertou!!! ${explanations[nowQuestion]}`;
    } else {
        statusAnswer.innerHTML = `Errou! Resposta correta: ${options[nowQuestion][correctAnswers[nowQuestion]]}. ${explanations[nowQuestion]}`;
    }
    reloadButton.style.display = "block";
}

document.getElementById('reload').addEventListener('click', () => location.reload());
