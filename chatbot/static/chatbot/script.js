const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");

const leadForm = document.getElementById("lead-form");
const leadResult = document.getElementById("lead-result");

function addMessage(text, className) {
    const messageDiv = document.createElement("div");
    messageDiv.className = className;
    messageDiv.textContent = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const userMessage = messageInput.value.trim();

    if (!userMessage) {
        addMessage("Please type a question first.", "bot-message");
        return;
    }

    addMessage(userMessage, "user-message");
    messageInput.value = "";

    fetch(`/chat/?message=${encodeURIComponent(userMessage)}`)
        .then(response => response.json())
        .then(data => {
            addMessage(data.bot_reply, "bot-message");
        })
        .catch(error => {
            addMessage("Sorry, something went wrong. Please try again.", "bot-message");
        });
});

leadForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(leadForm);

    fetch("/submit-lead/", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                leadResult.textContent = data.message;
                leadResult.className = "lead-result success";
                leadForm.reset();
            } else {
                leadResult.textContent = "Please check the form. Name, contact, requirement, and message are required.";
                leadResult.className = "lead-result error";
            }
        })
        .catch(error => {
            leadResult.textContent = "Sorry, something went wrong. Please try again.";
            leadResult.className = "lead-result error";
        });
});