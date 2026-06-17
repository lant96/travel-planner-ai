import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:8000';

export default function App() {
  const [formData, setFormData] = useState({
    origin: 'Athens',
    destination: 'Copenhagen',
    departure_date: '2026-07-01',
    return_date: '2026-07-10',
    budget: 2000,
    interests: ['design', 'food'],
    adults: 1
  });

  const [destinations, setDestinations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOptions = async () => {
      try {
        const res = await axios.get(`${API_BASE_URL}/destinations`);
        setDestinations(res.data.destinations);
      } catch (err) {
        console.error('Failed to fetch destinations:', err);
      }
    };
    fetchOptions();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'budget' || name === 'adults' ? parseFloat(value) : value
    }));
  };

  const handleInterestToggle = (interest) => {
    setFormData(prev => ({
      ...prev,
      interests: prev.interests.includes(interest)
        ? prev.interests.filter(i => i !== interest)
        : [...prev.interests, interest]
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/plan-trip`, formData);
      
      if (response.data.status === 'success') {
        setResult(response.data);
      } else {
        setError(response.data.message || 'Failed to plan trip');
      }
    } catch (err) {
      setError('Error connecting to server. Make sure backend is running on port 8000');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>✈️ AI Travel Planner</h1>
        <p>Powered by Groq LLM</p>
      </header>

      <main className="main-container">
        <section className="form-section">
          <h2>Plan Your Trip</h2>
          <form onSubmit={handleSubmit} className="trip-form">
            <div className="form-group">
              <label>From</label>
              <select name="origin" value={formData.origin} onChange={handleInputChange}>
                {destinations.map(dest => (
                  <option key={dest} value={dest}>{dest}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>To</label>
              <select name="destination" value={formData.destination} onChange={handleInputChange}>
                {destinations.map(dest => (
                  <option key={dest} value={dest}>{dest}</option>
                ))}
              </select>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Departure</label>
                <input type="date" name="departure_date" value={formData.departure_date} onChange={handleInputChange}/>
              </div>
              <div className="form-group">
                <label>Return</label>
                <input type="date" name="return_date" value={formData.return_date} onChange={handleInputChange}/>
              </div>
            </div>

            <div className="form-group">
              <label>Budget (€)</label>
              <input type="number" name="budget" value={formData.budget} onChange={handleInputChange} min="500"/>
            </div>

            <div className="form-group">
              <label>Interests</label>
              <div className="interests-grid">
                {['cultural', 'food', 'architecture', 'design', 'nature', 'nightlife', 'history', 'art'].map(interest => (
                  <label key={interest} className="interest-checkbox">
                    <input 
                      type="checkbox" 
                      checked={formData.interests.includes(interest)}
                      onChange={() => handleInterestToggle(interest)}
                    />
                    <span>{interest}</span>
                  </label>
                ))}
              </div>
            </div>

            <button type="submit" disabled={loading} className="submit-button">
              {loading ? 'Planning...' : 'Get AI Travel Plan'}
            </button>
          </form>
        </section>

        {error && <section className="error-section"><p>{error}</p></section>}

        {result && (
          <section className="result-section">
            <h2>🎉 Your AI Travel Plan</h2>
            <div className="recommendation-box">
              <pre>{result.recommendation}</pre>
            </div>
          </section>
        )}
      </main>
    </div>
  );
}
