import { ref } from 'vue'
import api, { setToken } from '../api'

const token = ref(localStorage.getItem('token') || null)
const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

if (token.value) setToken(token.value)

export function useAuth(){
  const login = async (email,password)=>{
    const res = await api.post('/auth/login',{ email, password })
    token.value = res.data.token
    user.value = res.data.user
    localStorage.setItem('token', token.value)
    localStorage.setItem('user', JSON.stringify(user.value))
    setToken(token.value)
    return res
  }
  const register = async (payload)=>{
    const res = await api.post('/auth/register', payload)
    token.value = res.data.token
    user.value = res.data.user
    localStorage.setItem('token', token.value)
    localStorage.setItem('user', JSON.stringify(user.value))
    setToken(token.value)
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
