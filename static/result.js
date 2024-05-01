// document.addEventListener("DOMContentLoaded", function() {
//     // Function to handle button click event
//     function redirectToHome() {
//         window.location.href = "/home"; // Redirect to the "/home" page
//     }

//     // Retrieve user choices from sessionStorage
//     var userChoices = {};
//     for (var i = 1; i <= quiz_answers.length; i++) {
//         userChoices[i] = sessionStorage.getItem("selectedChoice_" + i);
//     }

//     // Calculate score and match answers
//     var correctAnswers = quiz_answers; // Assuming quiz_answers is an array of correct answers
//     var score = 0;
//     var resultContainer = document.getElementById("result");
//     var resultHTML = "<h2>Quiz Results</h2><ul style='list-style: none; padding: 0; margin: 0;'>";
//     for (var i = 0; i < correctAnswers.length; i++) {
//         resultHTML += "<li style='margin-bottom: 10px; font-size: large;'>Question " + (i + 1) + ": ";
//         if (userChoices[i + 1] === correctAnswers[i]) {
//             resultHTML += "Correct";
//             score++;
//         } else {
//             resultHTML += "Incorrect. Correct answer is: " + correctAnswers[i];
//         }
//         resultHTML += "</li>";
//     }
//     resultHTML += "</ul><p>Score: " + score + "/" + correctAnswers.length + "</p>";
//     resultContainer.innerHTML = resultHTML;

//     // Add event listener to the "Restart" button
//     var restartButton = document.querySelector(".continue-btn");
//     restartButton.addEventListener("click", redirectToHome);
// });
document.addEventListener("DOMContentLoaded", function() {
    // Function to handle button click event
    function redirectToHome() {
        window.location.href = "/home"; // Redirect to the "/home" page
    }

    // Retrieve user choices from sessionStorage
    var userChoices = {};
    for (var i = 1; i <= quiz_answers.length; i++) {
        userChoices[i] = sessionStorage.getItem("selectedChoice_" + i);
    }

    // Calculate score and match answers
    var correctAnswers = quiz_answers; // Assuming quiz_answers is an array of correct answers
    var score = 0;

    // Create the result table HTML
    var resultContainer = document.getElementById("result");
    var resultHTML = "<h2>Quiz Results</h2><h3>Score: " + score + "/" + correctAnswers.length + "</h3><table><thead><tr><th>Question</th><th>Result</th><th>Correct Answer</th></tr></thead><tbody>";

    for (var i = 0; i < correctAnswers.length; i++) {
        resultHTML += "<tr class='" + (userChoices[i + 1] === correctAnswers[i] ? 'correct' : 'incorrect') + "'>";
        resultHTML += "<td>Question " + (i + 1) + "</td>";
        resultHTML += "<td>";
        if (userChoices[i + 1] === correctAnswers[i]) {
            resultHTML += "Correct";
            score++;
        } else {
            resultHTML += "Incorrect";
        }
        resultHTML += "</td>";
        resultHTML += "<td>" + correctAnswers[i] + "</td>";
        resultHTML += "</tr>";
    }

    resultHTML += "</tbody></table>";

    // Set the result HTML to the container
    resultContainer.innerHTML = resultHTML;

    // Add centering styles to the result container
    resultContainer.style.margin = "0 auto"; // Center horizontally

    // Add event listener to the "Restart" button
    var restartButton = document.querySelector(".continue-btn");
    restartButton.addEventListener("click", redirectToHome);
});

