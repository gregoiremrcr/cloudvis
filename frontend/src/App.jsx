import React, { useState } from 'react';
import UploadForm from './components/UploadForm';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <h1>Accessibilité visuelle : analyse d’image</h1>
      <UploadForm onResult={setResult} />
      {result && (
        <div className="result-box">
          <h2>Description :</h2>
          <p>{result.description}</p>
          <audio controls src={result.audio_url} />
          <img src={result.image_url} alt="Image analysée" />
        </div>
      )}
    </div>
  );
}

export default App;
