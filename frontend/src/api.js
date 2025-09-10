import axios from 'axios'
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'
const api = axios.create({ baseURL: API_BASE })

export function setToken(token){
  api.defaults.headers.common['Authorization'] = token ? `Bearer ${token}` : undefined
}
export default api
