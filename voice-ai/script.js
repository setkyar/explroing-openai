const message = document.querySelector("#message");
const result = document.querySelector("#result");

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
const grammar = "#JSGF V1.0;";

const recognition = new SpeechRecognition();

const speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;

recognition.lang = "en-US";
recognition.interimResults = false;

recognition.addEventListener("result", async function (event) {
  const last = event.results.length - 1;
  const command = event.results[last][0].transcript;

  message.textContent = "Recognised speech: " + command;

  try {
    // send the command to the server and get the response
    const response = await sendCommand(command);
    // update the result element with the response from the server
    result.textContent = "Answer: " + response;

    // text to speach
    var msg = new SpeechSynthesisUtterance(response);
    window.speechSynthesis.speak(msg);

  } catch (error) {
    // handle any errors that may occur
    result.textContent = "Error: " + error.message;
  }
});

recognition.onspeechend = function () {
  recognition.stop();
};

recognition.onerror = function (event) {
  message.textContent = "Error occurred in recognition: " + event.error;
};

document.querySelector("#command-button").addEventListener("click", function () {
  recognition.start();
});

// send command to server using request
async function sendCommand(command) {
  const url = "http://localhost:5000/answer/" + command;
  try {
    // make the HTTP request
    const response = await fetch(url);
    // parse the response as JSON
    const data = await response.text();
    // return the data from the server
    return data.trim()
  } catch (error) {
    console.log(error);
    // throw an error if something went wrong
    throw new Error("Failed to send command to server");
  }
}
