<template>
  <div>
    <button @click="$router.back()" class="mb-3 text-sm text-gray-600">← Back</button>
    <h2 class="text-xl font-semibold mb-2">Doctors</h2>
    <ul class="space-y-3">
      <li v-for="d in doctors" :key="d.id" class="bg-white p-4 rounded shadow flex justify-between items-center">
        <div>
          <div class="font-medium">{{ d.name }}</div>
          <div class="text-sm text-gray-600">{{ d.specialization }} • {{ d.consultation_time_minutes }} min</div>
        </div>
        <div class="flex gap-2">
          <button @click="book(d.id)" class="px-3 py-1 bg-green-600 text-white rounded">Book Token</button>
          <router-link :to="`/queue/${d.id}`" class="px-3 py-1 bg-gray-200 rounded">Live Queue</router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../../api'
import { useRoute } from 'vue-router'

const route = useRoute()
const doctors = ref([])

async function fetchDoctors(){
  try{
    const r = await api.get(`/hospitals/${route.params.id}/doctors`)
    doctors.value = r.data
  }catch(e){
    console.error(e)
  }
}

onMounted(fetchDoctors)

async function book(doctorId){
  try{
    const r = await api.post('/book', { doctor_id: doctorId, hospital_id: route.params.id })
    alert(`Booked token ${r.data.ticket.token_number}. Est wait ~${r.data.ticket.estimated_wait_minutes ?? 'N/A'} min`)
  }catch(e){
    alert('Booking failed. Are you logged in?')
  }
}
</script>
