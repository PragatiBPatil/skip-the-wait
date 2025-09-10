<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded shadow">
    <h2 class="text-2xl mb-4">Login</h2>
    <form @submit.prevent="onSubmit" class="space-y-4">
      <input v-model="email" type="email" placeholder="Email" class="w-full p-2 border rounded" required />
      <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded" required />
      <div class="flex items-center justify-between">
        <button class="px-4 py-2 bg-blue-600 text-white rounded">Login</button>
        <router-link to="/register" class="text-sm text-blue-600">Register</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../../stores/auth'

const email = ref('')
const password = ref('')
const { login } = useAuth()
const router = useRouter()

async function onSubmit(){
  try{
    await login(email.value, password.value)
    router.push('/')
  }catch(e){
    alert('Invalid credentials or server error')
  }
}
</script>
