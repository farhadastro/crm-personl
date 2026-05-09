import React, { useState } from 'react';
import axios from 'axios';
import '../styles/glassmorphism.css';

const OrderForm = ({ serviceId }) => {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    tech_stack: '', dataset_size: '', model_type: '', deadline: ''
  });

  const handleSubmit = async () => {
    await axios.post('/api/v1/orders', { ...formData, service_id: serviceId });
    alert('Order submitted successfully');
  };

  return (
    <div className="glass-card" style={{ maxWidth: '600px', margin: 'auto' }}>
      <h2>Submit ML Project Request</h2>
      {step === 1 && (
        <>
          <label>Tech Stack (e.g., PyTorch, TensorFlow)</label>
          <input className="glass-card" type="text" onChange={(e) => setFormData({...formData, tech_stack: e.target.value})} />
          <button onClick={() => setStep(2)}>Next</button>
        </>
      )}
      {step === 2 && (
        <>
          <label>Dataset Size (e.g., 50GB, 1M records)</label>
          <input className="glass-card" type="text" onChange={(e) => setFormData({...formData, dataset_size: e.target.value})} />
          <button onClick={() => setStep(3)}>Next</button>
        </>
      )}
      {step === 3 && (
        <>
          <label>Model Type (e.g., LLM, Computer Vision)</label>
          <input className="glass-card" type="text" onChange={(e) => setFormData({...formData, model_type: e.target.value})} />
          <button onClick={handleSubmit}>Submit Request</button>
        </>
      )}
    </div>
  );
};

export default OrderForm;
