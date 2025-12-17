
// ----------------------------------------------------------------------
// CONFIGURATION
// ----------------------------------------------------------------------

// REPLACE THIS with your running FastAPI URL
const API_URL = "http://127.0.0.1:8000/agent/run";

// ----------------------------------------------------------------------

/**
 * Sends a message to the backend API.
 * 
 * @param {string} message - The message sent by the user.
 * @returns {Promise<object>} - A promise that resolves to the bot's response.
 */
export const sendMessage = async (message) => {
    try {
        console.log(`[API] Sending message to ${API_URL}:`, message);

        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            // Adjust the payload key ('query', 'message', 'text') to match your Pydantic model
            body: JSON.stringify({ query: message }),   
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.statusText}`);
        }

        const data = await response.json();

        // Expecting the backend to return { "response": "..." } or similar
        // Adjust 'data.response' to match your actual API response structure
        const botText = data.answer;

        return {
            role: 'bot',
            text: botText,
            timestamp: new Date().toISOString()
        };

    } catch (error) {
        console.error("API Call Failed, falling back to mock response:", error);

        // FALLBACK: Return a mock response if the backend is down
        return mockFallback(message);
    }
};

/**
 * Fallback response if backend is not connected.
 */
const mockFallback = async (message) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            let responseText = "I see the backend is not connected yet! Check 'src/utils/api.js' to configure your FastAPI URL.";

            if (message.toLowerCase().includes("hello")) {
                responseText = "Hello! Connect me to FastAPI to make me smart.";
            }

            resolve({
                role: 'bot',
                text: responseText,
                timestamp: new Date().toISOString()
            });
        }, 1000);
    });
};
