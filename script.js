// Store the options
const choices = { "rock": 0, "paper": 1, "scissors": 2 };
const reverseChoices = { 0: "Rock", 1: "Paper", 2: "Scissors" };

// Function to play the game
function playGame(playerChoice) {
    const computerChoice = Math.floor(Math.random() * 3);  // Random choice for the computer
    const player = choices[playerChoice];

    const resultText = `
        <p>You chose <strong>${reverseChoices[player]}</strong></p>
        <p>Computer chose <strong>${reverseChoices[computerChoice]}</strong></p>
        <p><strong>${getResult(player, computerChoice)}</strong></p>
    `;

    document.getElementById("result").innerHTML = resultText;
}

// Determine the result
function getResult(player, computer) {
    if (player === computer) {
        return "It's a draw!";
    }
    if (
        (player === 0 && computer === 2) || 
        (player === 1 && computer === 0) || 
        (player === 2 && computer === 1)
    ) {
        return "You win!";
    }
    return "You lose!";
}

// Event listeners for buttons
document.getElementById("rock").addEventListener("click", () => playGame("rock"));
document.getElementById("paper").addEventListener("click", () => playGame("paper"));
document.getElementById("scissors").addEventListener("click", () => playGame("scissors"));
