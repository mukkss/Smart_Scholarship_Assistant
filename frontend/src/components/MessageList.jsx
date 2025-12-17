
import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';

const MessageList = ({ messages, isLoading }) => {
    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages, isLoading]);

    return (
        <div className="flex-1 overflow-y-auto p-4 md:p-6 space-y-4 z-0 scroller">
            <div className="max-w-4xl mx-auto flex flex-col h-full justify-end min-h-0">
                {/* Wrapper to push content down if few messages */}
                <div className="flex-1"></div>

                {messages.length === 0 && (
                    <div className="absolute inset-0 flex flex-col items-center justify-center text-center p-8 animate-fade-in pointer-events-none opacity-80">
                        <p className="text-5xl md:text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500 tracking-tight leading-tight mb-4 drop-shadow-sm">
                            Smart Scholarship<br />Assistant
                        </p>
                        <p className="text-xl md:text-2xl text-slate-400 font-light max-w-lg">
                            Ask me anything about scholarships, deadlines, and requirements.
                        </p>
                    </div>
                )}

                {messages.map((msg, index) => (
                    <MessageBubble key={index} message={msg} />
                ))}

                {isLoading && (
                    <div className="flex justify-start w-full mb-4 px-1">
                        <div className="bg-slate-800 p-4 rounded-2xl rounded-bl-none shadow-lg border border-slate-700 flex items-center space-x-2">
                            <div className="w-2 h-2 bg-indigo-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                            <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                            <div className="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                        </div>
                    </div>
                )}

                <div ref={bottomRef} />
            </div>
        </div>
    );
};

export default MessageList;
