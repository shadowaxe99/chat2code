import React from 'react';
import File from '../Filesystem/File';

const AgentLogFilesList = ({ logFiles, onFileClick }) => (
  <div>
    {logFiles.map((file, index) => (
      <File key={index} name={file} onClick={() => onFileClick(file)} />
    ))}
  </div>
);

export default AgentLogFilesList;