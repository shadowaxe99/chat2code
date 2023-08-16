import React, { Component } from 'react';

class Editor extends Component {
  render() {
    return (
      <div className='editor'>
        <input type='text' onKeyPress={event => {
          if (event.key === 'Enter') {
            onMessageSend(event.target.value);
            event.target.value = '';
          }
        }} />
        {/* Editor content goes here */}
      </div>
    );
  }
}

export default Editor;
