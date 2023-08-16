import React from 'react';
import ReactDOM from 'react-dom';
import Editor from './editor/Editor';
import Chat from './chat/Chat';

ReactDOM.render(
  <React.StrictMode>
    <Editor />
    <Chat />
  </React.StrictMode>,
  document.getElementById('root')
);
