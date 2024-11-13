document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    // Function to add a message to the chat container
    function addMessage(role, content) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', role);
        messageElement.innerText = content;
        chatContainer.appendChild(messageElement);
    }

    // Event listener for the send button
    sendBtn.addEventListener('click', function() {
        const userMessage = userInput.value.trim();

        if (userMessage !== '') {
            // Add user message to chat container
            addMessage('user', userMessage);

            // Send user message to Flask backend for processing
            fetch('/send-message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: userMessage
                })
            })
            .then(response => {
                // Check if response is valid JSON
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Check if response contains expected data
                if (data && data.response) {
                    // Add chatbot response to chat container
                    addMessage('chatbot', data.response);
                } else {
                    throw new Error('Invalid response data');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage('chatbot', 'An error occurred while processing your request.');
            });

            // Clear user input field
            userInput.value = '';
        }
    });
});
