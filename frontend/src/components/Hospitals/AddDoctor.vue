<template>
  <div class="p-6 bg-white shadow-lg rounded-xl max-w-md mx-auto">
    <h2 class="text-xl font-semibold mb-4">Add New Doctor</h2>
    <form @submit.prevent="addDoctor">
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Doctor Name</label>
        <input v-model="doctor.name" type="text" required class="border p-2 w-full rounded" />
      </div>
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Specialization</label>
        <input v-model="doctor.specialization" type="text" required class="border p-2 w-full rounded" />
      </div>
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Hospital</label>
        <select v-model="doctor.hospital_id" required class="border p-2 w-full rounded">
          <option value="">Select Hospital</option>
          <option v-for="hospital in hospitals" :key="hospital.id" :value="hospital.id">
            {{ hospital.name }}
          </option>
        </select>
      </div>
      <div class="mb-3">
        <label class="block text-sm font-medium mb-1">Timings</label>
        <input v-model="doctor.timings" type="text" required class="border p-2 w-full rounded" />
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
        Add Doctor
      </button>
    </form>
    <p v-if="message" class="mt-3 text-green-600">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import API from '../../services/api'

const doctor = ref({
  name: '',
  specialization: '',
  hospital_id: '',
  timings: ''
})
const hospitals = ref([])
const message = ref('')

const fetchHospitals = async () => {
  try {
    const res = await API.get('/hospitals')
    hospitals.value = res.data
  } catch (err) {
    console.error('Error fetching hospitals:', err)
  }
}

const addDoctor = async () => {
  try {
    const res = await API.post('/doctors', doctor.value)
    message.value = 'Doctor added successfully!'
    doctor.value = { name: '', specialization: '', hospital_id: '', timings: '' }
  } catch (err) {
    message.value = 'Error adding doctor. Please try again.'
    console.error(err)
  }
}

onMounted(fetchHospitals)
</script>
