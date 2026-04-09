const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/backend';
export const API_ENDPOINTS = {
  LOGIN: `${API_BASE_URL}/api/user/login/`,
  REGISTER: `${API_BASE_URL}/api/user/register/`,
  PREDICT: `${API_BASE_URL}/api/prediction/predict/`,
  DASHBOARD: `${API_BASE_URL}/api/prediction/dashboard-data/`,
  CHAT: `${API_BASE_URL}/api/prediction/chat/`,
};
export default API_BASE_URL;
