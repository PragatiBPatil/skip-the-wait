<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded shadow">
    <h2 class="text-2xl mb-4">Register</h2>
    <form @submit.prevent="onSubmit" class="space-y-4">
      <input v-model="full_name" placeholder="Full name" class="w-full p-2 border rounded" required />
      <input v-model="email" type="email" placeholder="Email" class="w-full p-2 border rounded" required />
      <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded" required />
      <div>
        <select v-model="role" class="w-full p-2 border rounded">
          <option value="patient">Patient</option>
          <option value="doctor">Doctor</option>
          <option value="admin">Admin</option>
        </select>
      </div>
      <button class="px-4 py-2 bg-green-600 text-white rounded">Create account</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../../stores/auth'

const full_name = ref('')
const email = ref('')
const password = ref('')
const role = ref('patient')
const { register } = useAuth()
const router = useRouter()

async function onSubmit(){
  try{
    await register({ name: full_name.value, email: email.value, password: password.value, role: role.value })
    router.push('/')
  }catch(e){
    alert('Registration failed')
  }
}
</script>
