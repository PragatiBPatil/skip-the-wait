<template>
  <div>
    <h2 class="text-xl font-semibold mb-4">My Tickets</h2>
    <div v-if="tickets.length===0" class="text-gray-600">You have no bookings yet.</div>
    <ul class="space-y-3">
      <li v-for="t in tickets" :key="t.id" class="bg-white p-4 rounded shadow flex justify-between items-center">
        <div>
          <div class="font-medium">Token {{ t.token_number }} — {{ t.status }}</div>
          <div class="text-sm text-gray-600">Est wait: {{ t.estimated_wait_minutes ?? 'N/A' }} min</div>
        </div>
        <div>
          <router-link :to="`/queue/${t.id}`" class="px-3 py-1 bg-gray-200 rounded">View</router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../../api'

const tickets = ref([])

async function fetch(){
  try{
    const r = await api.get('/tickets/mine')
    tickets.value = r.data
  }catch(e){
    console.error(e)
  }
}

onMounted(fetch)
</script>
