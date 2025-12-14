
import React, { useState } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import { sendMessage } from '../utils/api';

const ChatInterface = () => {
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const handleSendMessage = async (text) => {
        // Add user message
        const userMessage = { role: 'user', text, timestamp: new Date().toISOString() };
        setMessages(prev => [...prev, userMessage]);

        setIsLoading(true);

        try {
            // Call API
            const response = await sendMessage(text);
            setMessages(prev => [...prev, response]);
        } catch (error) {
            console.error("Failed to send message:", error);
            setMessages(prev => [...prev, {
                role: 'bot',
                text: "Sorry, I had trouble connecting. Please try again.",
                timestamp: new Date().toISOString()
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-full bg-slate-900 relative overflow-hidden">
            {/* Ambient Background Glow */}
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[500px] h-[500px] bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

            {/* Header */}
            <header className="bg-slate-800/80 backdrop-blur-md border-b border-slate-700 px-6 py-4 flex items-center justify-center md:justify-start shadow-xl z-10 sticky top-0">
                <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center mr-3 text-white font-bold text-xl shadow-lg transform hover:scale-105 transition-transform duration-200">
                    S
                </div>
                <div>
                    <h1 className="text-xl font-bold text-slate-100 tracking-tight">Scholarship Assistant</h1>
                    <p className="text-xs text-green-400 font-medium flex items-center shadow-green-900/50">
                        <span className="w-2 h-2 bg-green-400 rounded-full mr-1 animate-pulse"></span>
                        Online
                    </p>
                </div>
            </header>

            {/* Messages Area */}
            <MessageList messages={messages} isLoading={isLoading} />

            {/* Input Area */}
            <MessageInput onSend={handleSendMessage} isLoading={isLoading} />
        </div>
    );
};

export default ChatInterface;
