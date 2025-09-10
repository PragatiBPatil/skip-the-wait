import { ref } from 'vue'
import api, { setToken } from '../api'

const token = ref(localStorage.getItem('token') || null)
const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

if (token.value) setToken(token.value)

export function useAuth(){
  const login = async (email,password)=>{
    const res = await api.post('/auth/login',{ email, password })
    token.value = res.data.access_token
    user.value = { role: res.data.role } // backend returns role separately, no user object
    localStorage.setItem('token', token.value)
    localStorage.setItem('user', JSON.stringify(user.value))
    setToken(token.value)
    return res
  }
  const register = async (payload)=>{
    const res = await api.post('/auth/register', payload)
    // backend register returns message only, no token or user
    // so no token or user to set here
    return res
  }
  const logout = ()=>{
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    setToken(null)
  }
  return { token, user, login, register, logout }
}
