var guessValue = document.getElementById("guess");
var results = document.getElementById("result");
var displayWord = document.getElementById("display");
var displayResult = document.getElementById("container");
var counter = 0;
const submitButton = document.getElementById("submit");

function randomWord() {
    var wordList = ["random1", "random2", "random3"];
    var temp = wordList[Math.floor(Math.random()*3)];
    displayWord.textContent = temp;
}

window.onload = randomWord();

submitButton.addEventListener('click', ()=> {
    checkGuess();
    guessValue.value = "";
})


function checkGuess() {
    var guess = guessValue.value;
    console.log(guess);
    results.textContent = "You guessed " + guess + ".";
    if (guessValue.value === temp) {
        displayResult.textContent = "You guessed correct!";
        alert("You guessed correct!");
    } else {
        displayResult.textContent = "You failed!";
        alert("You failed!");
    }
}
