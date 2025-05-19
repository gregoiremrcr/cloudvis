import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState(null);
  const [description, setDescription] = useState('');
  const [audioUrl, setAudioUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setImage(e.target.files[0]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:5000/analyze', formData);
      setDescription(res.data.description);
      setAudioUrl(`http://localhost:5000${res.data.audio_url}`);
    } catch (error) {
      console.error('Erreur :', error);
      alert('Échec de l’analyse.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Analyse d’image pour accessibilité</h1>

      <form onSubmit={handleSubmit} className="flex flex-col items-center gap-4">
        <input type="file" onChange={handleFileChange} accept="image/*" required />
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
        >
          Analyser
        </button>
      </form>

      {loading && <p className="mt-4 text-gray-600">Analyse en cours...</p>}

      {description && (
        <div className="mt-8 max-w-xl text-center">
          <h2 className="text-xl font-semibold text-gray-700 mb-2">Description :</h2>
          <p className="text-gray-800 whitespace-pre-line">{description}</p>

          <h3 className="mt-6 text-lg font-medium text-gray-700">Audio :</h3>
          <audio controls className="mt-2">
            <source src={audioUrl} type="audio/mpeg" />
            Votre navigateur ne supporte pas la lecture audio.
          </audio>
        </div>
      )}
    </div>
  );
}

export default App;
