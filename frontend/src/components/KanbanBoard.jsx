import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/glassmorphism.css';

const KanbanBoard = () => {
  const [projects, setProjects] = useState([]);
  const columns = ['backlog', 'in_progress', 'review', 'done'];

  useEffect(() => {
    axios.get('/api/v1/projects').then(res => setProjects(res.data));
  }, []);

  const onDrop = async (projectId, newStatus) => {
    await axios.patch(`/api/v1/projects/${projectId}/status`, { status: newStatus });
    setProjects(prev => prev.map(p => p.id === projectId ? { ...p, status: newStatus } : p));
  };

  return (
    <div style={{ display: 'flex', gap: '20px', padding: '20px' }}>
      {columns.map(col => (
        <div key={col} className="glass-card" style={{ width: '250px', minHeight: '500px' }}>
          <h3>{col.toUpperCase().replace('_', ' ')}</h3>
          {projects.filter(p => p.status === col).map(p => (
            <div key={p.id} className="glass-card" draggable onDragStart={(e) => e.dataTransfer.setData('id', p.id)}>
              {p.name}
            </div>
          ))}
          <div onDragOver={(e) => e.preventDefault()} onDrop={(e) => onDrop(e.dataTransfer.getData('id'), col)} style={{ height: '100%' }}>
            Drop here
          </div>
        </div>
      ))}
    </div>
  );
};

export default KanbanBoard;
