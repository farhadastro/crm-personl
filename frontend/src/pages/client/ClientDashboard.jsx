import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/glassmorphism.css';

const ClientDashboard = () => {
  const [orders, setOrders] = useState([]);
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    // Fetch orders and projects for the current client
    axios.get('/api/v1/orders').then(res => setOrders(res.data));
    axios.get('/api/v1/projects').then(res => setProjects(res.data));
  }, []);

  return (
    <div style={{ padding: '40px' }}>
      <h1>Client Dashboard</h1>
      
      <section>
        <h2>Active Projects</h2>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          {projects.map(p => (
            <div key={p.id} className="glass-card">
              <h3>{p.name}</h3>
              <p>Status: {p.status.toUpperCase()}</p>
              <div className="progress-bar" style={{ background: '#333', height: '10px', borderRadius: '5px' }}>
                <div style={{ width: '60%', height: '100%', background: '#4f46e5', borderRadius: '5px' }} />
              </div>
            </div>
          ))}
        </div>
      </section>

      <section style={{ marginTop: '40px' }}>
        <h2>Order History</h2>
        {orders.map(o => (
          <div key={o.id} className="glass-card" style={{ marginBottom: '10px' }}>
            <span>Order #{o.id} - {o.model_type} - {o.status}</span>
          </div>
        ))}
      </section>
    </div>
  );
};

export default ClientDashboard;
