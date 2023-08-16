import React from 'react';

const File = ({ name, onClick }) => (
  <div onClick={onClick}>
    {name}
  </div>
);

export default File;