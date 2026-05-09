import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const ProtectedRoute = ({ role }) => {
  const user = JSON.parse(localStorage.getItem('user')); // Simplified state management

  if (!user) return <Navigate to="/login" />;
  if (role && user.role !== role) return <Navigate to="/unauthorized" />;
  
  return <Outlet />;
};

export default ProtectedRoute;
