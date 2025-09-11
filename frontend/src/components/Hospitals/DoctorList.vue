<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <button @click="$router.back()" class="mb-6 text-sm text-gray-600 hover:text-blue-600 transition-colors">← Back</button>
    <h2 class="text-2xl font-semibold mb-6 text-gray-900">Doctors</h2>

    <div v-if="loading" class="flex justify-center items-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-green-600"></div>
      <span class="ml-3 text-gray-600">Loading doctors...</span>
    </div>

    <div v-else-if="error" class="text-center py-20">
      <div class="text-red-500 text-6xl mb-4">⚠️</div>
      <h3 class="text-xl font-semibold text-gray-900 mb-2">Failed to load doctors</h3>
      <p class="text-gray-600 mb-4">{{ error }}</p>
      <button
        @click="fetchDoctors"
        class="px-6 py-3 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-colors"
      >
        Try Again
      </button>
    </div>

    <ul v-else class="space-y-4">
      <li v-for="d in doctors" :key="d.id" class="bg-white p-6 rounded-2xl shadow flex justify-between items-center">
        <div>
          <div class="font-semibold text-lg text-gray-900">{{ d.name }}</div>
          <div class="text-sm text-gray-600">{{ d.specialization }} • {{ d.timings }}</div>
        </div>
        <div class="flex gap-3">
          <button
            @click="book(d.id)"
            class="px-4 py-2 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 transition-colors"
          >
            Book Token
          </button>
          <router-link
            :to="`/queue/${d.id}`"
            class="px-4 py-2 bg-gray-200 rounded-xl font-semibold hover:bg-gray-300 transition-colors"
          >
            Live Queue
          </router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import API from '../../services/api'
import { useRoute } from 'vue-router'
import { useNotifications } from '../../stores/notifications'

const route = useRoute()
const doctors = ref([])
const loading = ref(false)
const error = ref('')
const { success, error: showError } = useNotifications()

async function fetchDoctors(){
  loading.value = true
  error.value = ''
  try{
    const r = await API.get(`/doctors/${route.params.id}`)
    doctors.value = r.data
  }catch(e){
    error.value = e.response?.data?.error || 'Failed to load doctors'
    console.error(e)
  }finally{
    loading.value = false
  }
}

onMounted(fetchDoctors)

async function book(doctorId){
  try{
    const r = await API.post('/tickets', { doctor_id: doctorId })
    success(
      'Appointment Booked!',
      `Token ${r.data.ticket_id} booked. Estimated wait: ${r.data.estimated_wait_minutes ?? 'N/A'} minutes`
    )
  }catch(e){
    showError('Booking Failed', 'Please make sure you are logged in and try again.')
  }
}
</script>
