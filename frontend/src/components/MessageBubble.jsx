
import React from 'react';

const MessageBubble = ({ message }) => {
    const isUser = message.role === 'user';

    return (
        <div className={`flex w-full mb-4 ${isUser ? 'justify-end' : 'justify-start'} animate-slide-in`}>
            <div
                className={`max-w-[70%] p-3 md:p-4 rounded-2xl text-sm md:text-base leading-relaxed break-words shadow-lg transition-transform hover:scale-[1.01]
                    ${isUser
                        ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-br-sm shadow-blue-500/20'
                        : 'bg-slate-800 text-slate-100 border border-slate-700 rounded-bl-sm shadow-black/20'
                    }`}
            >
                {message.text}
            </div>
        </div>
    );
};

export default MessageBubble;
