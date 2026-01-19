let questions = [
    {
        "question": "Who is the Prime Minister of India?",
        "options": ["Narendra Modi", "Rahul Gandhi"]
    },
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus"]
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": ["Rabindranath Tagore", "Bankim Chandra"]
    },
    {
        "question": "Which language is mainly used for web development?",
        "options": ["JavaScript", "C++"]
    }
];
let i = 0;

function dispaly_question(number){
    document.getElementById('span-quesno').innerHTML = number + 1;
    document.getElementById('h6-question').innerHTML = `<span style="margin-right: 15px;">${number + 1}.</span>${questions[number].question}`;
    document.getElementById('label-opt1').innerHTML = questions[number].options[0];
    document.getElementById('label-opt2').innerHTML = questions[number].options[1];
}

function Next(){
    if(i < questions.length)
        dispaly_question(i++);
    else{
        alert('End of Quiz!');
    }
}

window.onload = Next();