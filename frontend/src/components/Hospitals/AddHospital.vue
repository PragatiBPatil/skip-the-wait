<template>
  <div class="p-6 bg-white shadow-lg rounded-xl max-w-md mx-auto">
    <h2 class="text-xl font-semibold mb-4">Add New Hospital</h2>
    <form @submit.prevent="addHospital">
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Hospital Name</label>
        <input v-model="hospital.name" type="text" required class="border p-2 w-full rounded" />
      </div>
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Address</label>
        <input v-model="hospital.address" type="text" required class="border p-2 w-full rounded" />
      </div>
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Specialization</label>
        <input v-model="hospital.specialization" type="text" required class="border p-2 w-full rounded" />
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
        Add Hospital
      </button>
    </form>
    <p v-if="message" class="mt-3 text-green-600">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../../services/api'

const hospital = ref({
  name: '',
  address: '',
  specialization: ''
})
const message = ref('')

const addHospital = async () => {
  try {
    const res = await API.post('/hospitals', hospital.value)
    message.value = 'Hospital added successfully!'
    hospital.value = { name: '', address: '', specialization: '' }
  } catch (err) {
    message.value = 'Error adding hospital. Please try again.'
    console.error(err)
  }
}
</script>
