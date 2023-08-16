import React, { useState } from 'react';
import Editor from './editor/Editor.js';
import Chat from './chat/Chat.js';

const Chain = () => {
  const [messages, setMessages] = useState([]);

  const handleNewMessage = (newMessage) => {
    setMessages([...messages, newMessage]);
  };

  return (
    <div>
      <Editor onNewMessage={handleNewMessage} />
      <Chat messages={messages} />
    </div>
  );
};

export default Chain;
