document.addEventListener("DOMContentLoaded", function () {
    // Function to redirect to next quiz
    function redirectToNextQuiz(selectedChoice) {
        // Store the selected choice and current quiz ID in sessionStorage
        sessionStorage.setItem("selectedChoice_" + id, selectedChoice);

        if(parseInt(id) < quiz_questions.length){
            // Redirect to the next quiz
            window.location.href = (parseInt(id) + 1);
        } else {
            // Redirect to the results page
            window.location.href = "/result";
        }
    }

    // Select the element where you want to display the question
    var questionElement = document.getElementById("title");
    // Set the question text
    questionElement.innerText = "Question " + id + ": " + quiz_questions[parseInt(id)-1].questions;

    // Set the image source
    var questionImageElement = document.getElementById("questionImage");
    questionImageElement.src =quiz_questions[parseInt(id)-1].imageURL;


    // Select the element where you want to display the choices
    var choicesElement = document.getElementById("contents");

    // Loop through the choices and create HTML elements to display them
    for (var i = 0; i < quiz_questions[parseInt(id)-1].choices.length; i++) {
        var choice = quiz_questions[parseInt(id)-1].choices[i];

        // Create a div element for each choice
        var choiceDiv = document.createElement("div");
        choiceDiv.classList.add("block", "choice");

        // Create a radio button for each choice
        var radioBtn = document.createElement("input");
        radioBtn.type = "radio";
        radioBtn.name = "choice";
        radioBtn.value = choice;

        // Create a label for the radio button
        var label = document.createElement("label");
        label.appendChild(radioBtn);
        label.appendChild(document.createTextNode(choice));

        // Append the label to the choices element
        choiceDiv.appendChild(label);

        // Append the choice div to the choices element
        choicesElement.appendChild(choiceDiv);
    }

    // Create submit button
    var submitButton = document.createElement("button");
    submitButton.textContent = "Continue";
    submitButton.classList.add("btn", "continue-btn");
    submitButton.addEventListener("click", function () {
        // Find the selected choice
        var selectedChoice = document.querySelector('input[name="choice"]:checked');

        // Check if any choice is selected
        if (selectedChoice) {
            // Redirect to the next quiz
            redirectToNextQuiz(selectedChoice.value);
        } else {
            // If no choice is selected, alert the user to select a choice
            alert("Please select an answer!");
        }
    });

    // Append the submit button to the choices element
    choicesElement.appendChild(submitButton);
});
