// static/script.js


document.addEventListener("DOMContentLoaded", () => {

    const openChat = document.getElementById("openChat");
    const closeChat = document.getElementById("closeChat");
    const chatOverlay = document.getElementById("chatOverlay");

    const chatInput = document.getElementById("chatInput");
    const sendMessage = document.getElementById("sendMessage");
    const chatMessages = document.getElementById("chatMessages");

    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");


    let conversationHistory = [];


    // ----------------------------------------
    // THEME
    // ----------------------------------------

    const savedTheme = localStorage.getItem("portfolio-theme");

    if (savedTheme === "light") {
        document.body.classList.add("light-mode");

        if (themeIcon) {
            themeIcon.textContent = "☀";
        }
    }


    if (themeToggle) {

        themeToggle.addEventListener("click", () => {

            document.body.classList.toggle("light-mode");

            const isLight =
                document.body.classList.contains("light-mode");

            localStorage.setItem(
                "portfolio-theme",
                isLight ? "light" : "dark"
            );

            if (themeIcon) {
                themeIcon.textContent = isLight ? "☀" : "◐";
            }

        });

    }


    // ----------------------------------------
    // CHAT OPEN / CLOSE
    // ----------------------------------------

    function openChatPanel() {

        if (!chatOverlay) {
            return;
        }

        chatOverlay.classList.add("active");

        setTimeout(() => {

            if (chatInput) {
                chatInput.focus();
            }

        }, 250);
    }


    function closeChatPanel() {

        if (!chatOverlay) {
            return;
        }

        chatOverlay.classList.remove("active");
    }


    if (openChat) {
        openChat.addEventListener(
            "click",
            openChatPanel
        );
    }


    if (closeChat) {
        closeChat.addEventListener(
            "click",
            closeChatPanel
        );
    }


    if (chatOverlay) {

        chatOverlay.addEventListener(
            "click",
            (event) => {

                if (event.target === chatOverlay) {
                    closeChatPanel();
                }

            }
        );

    }


    // ----------------------------------------
    // MESSAGE UI
    // ----------------------------------------

    function addMessage(role, text) {

        const message = document.createElement("div");

        message.className =
            `chat-message ${role}`;


        const label = document.createElement("div");

        label.className = "message-label";

        label.textContent =
            role === "user"
                ? "YOU"
                : "ARCHIVE";


        const content = document.createElement("div");

        content.className = "message-content";

        content.textContent = text;


        message.appendChild(label);
        message.appendChild(content);


        chatMessages.appendChild(message);


        chatMessages.scrollTop =
            chatMessages.scrollHeight;

    }


    function addTypingIndicator() {

        const typing = document.createElement("div");

        typing.className =
            "chat-message assistant typing-message";

        typing.id =
            "typingIndicator";


        typing.innerHTML = `
            <div class="message-label">
                ARCHIVE
            </div>

            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;


        chatMessages.appendChild(typing);


        chatMessages.scrollTop =
            chatMessages.scrollHeight;
    }


    function removeTypingIndicator() {

        const typing =
            document.getElementById(
                "typingIndicator"
            );

        if (typing) {
            typing.remove();
        }

    }


    // ----------------------------------------
    // SEND MESSAGE
    // ----------------------------------------

    async function sendChatMessage(customMessage = null) {

        if (!chatInput || !sendMessage) {
            return;
        }


        const message =
            customMessage !== null
                ? customMessage.trim()
                : chatInput.value.trim();


        if (!message) {
            return;
        }


        addMessage(
            "user",
            message
        );


        chatInput.value = "";

        chatInput.style.height =
            "auto";


        sendMessage.disabled = true;


        addTypingIndicator();


        try {

            const response =
                await fetch("/chat", {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        message: message,

                        history:
                            conversationHistory

                    })

                });


            const data =
                await response.json();


            removeTypingIndicator();


            const reply =
                data.response ||
                "I couldn't generate a response right now.";


            addMessage(
                "assistant",
                reply
            );


            conversationHistory.push(
                {
                    role: "user",
                    content: message
                }
            );


            conversationHistory.push(
                {
                    role: "assistant",
                    content: reply
                }
            );


            if (
                conversationHistory.length > 10
            ) {

                conversationHistory =
                    conversationHistory.slice(-10);

            }

        } catch (error) {

            console.error(error);

            removeTypingIndicator();

            addMessage(
                "assistant",
                "Something went wrong while contacting the archive. Try again in a moment."
            );

        }


        sendMessage.disabled = false;

        chatInput.focus();

    }


    if (sendMessage) {

        sendMessage.addEventListener(
            "click",
            () => sendChatMessage()
        );

    }


    if (chatInput) {

        chatInput.addEventListener(
            "keydown",
            (event) => {

                if (
                    event.key === "Enter" &&
                    !event.shiftKey
                ) {

                    event.preventDefault();

                    sendChatMessage();

                }

            }
        );


        chatInput.addEventListener(
            "input",
            () => {

                chatInput.style.height =
                    "auto";

                chatInput.style.height =
                    `${Math.min(
                        chatInput.scrollHeight,
                        140
                    )}px`;

            }
        );

    }


    // ----------------------------------------
    // QUICK PROMPTS
    // ----------------------------------------

    const quickPrompts =
        document.querySelectorAll(
            "[data-prompt]"
        );


    quickPrompts.forEach(
        (button) => {

            button.addEventListener(
                "click",
                () => {

                    const prompt =
                        button.dataset.prompt;

                    openChatPanel();

                    sendChatMessage(prompt);

                }
            );

        }
    );


    // ----------------------------------------
    // ESCAPE TO CLOSE
    // ----------------------------------------

    document.addEventListener(
        "keydown",
        (event) => {

            if (
                event.key === "Escape" &&
                chatOverlay &&
                chatOverlay.classList.contains("active")
            ) {

                closeChatPanel();

            }

        }
    );

});