
import React, { useState } from 'react';

const MessageInput = ({ onSend, isLoading }) => {
    const [text, setText] = useState('');

    const handleSend = () => {
        if (text.trim() && !isLoading) {
            onSend(text);
            setText('');
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    return (
        <div className="bg-slate-800/90 backdrop-blur-sm p-4 border-t border-slate-700 z-10">
            <div className="flex items-center gap-3 max-w-4xl mx-auto">
                <input
                    type="text"
                    className="flex-1 p-4 bg-slate-900 border border-slate-700 rounded-xl text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500 transition-all shadow-inner"
                    placeholder="Type your message..."
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    onKeyPress={handleKeyPress}
                    disabled={isLoading}
                />
                <button
                    onClick={handleSend}
                    disabled={!text.trim() || isLoading}
                    className={`p-4 rounded-xl font-bold transition-all flex items-center justify-center transform active:scale-95
                        ${!text.trim() || isLoading
                            ? 'bg-slate-800 text-slate-600 cursor-not-allowed border border-slate-700'
                            : 'bg-indigo-600 text-white shadow-[0_4px_0_rgb(55,48,163)] active:shadow-none active:translate-y-1 hover:bg-indigo-500'
                        }`}
                >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
                    </svg>
                </button>
            </div>
        </div>
    );
};

export default MessageInput;
