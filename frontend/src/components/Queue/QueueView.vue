<template>
  <div>
    <button @click="$router.back()" class="mb-3 text-sm text-gray-600">← Back</button>
    <h2 class="text-xl font-semibold mb-2">Live Queue</h2>
    <div class="bg-white p-4 rounded shadow">
      <div v-if="tickets.length===0" class="text-gray-600">No active waiting tickets</div>
      <ul v-else class="space-y-2">
        <li v-for="t in tickets" :key="t.id" class="flex justify-between items-center">
          <div>Token <span class="font-bold">{{ t.token_number }}</span> — {{ t.status }}</div>
          <div v-if="isPatient(t)">You</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import api from '../../api'
import { createClient } from '@supabase/supabase-js'
import { useRoute } from 'vue-router'

const tickets = ref([])
const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_ANON)

const route = useRoute()
const doctorId = route.params.ticketId || route.params.id

let subscription = null

async function fetchTickets(id){
  try{
    const r = await api.get(`/doctor/${id}/tokens`)
    tickets.value = r.data
  }catch(e){
    console.error(e)
  }
}

onMounted(async ()=>{
  if(doctorId) await fetchTickets(doctorId)
  subscription = supabase.channel('public:tickets')
    .on('postgres_changes', { event: '*', schema: 'public', table: 'tickets' }, ()=>fetchTickets(doctorId))
    .subscribe()
})

onBeforeUnmount(()=>{
  if(subscription) supabase.removeChannel(subscription)
})

function isPatient(t){
  const me = localStorage.getItem('user')
  if(!me) return false
  try{
    const u = JSON.parse(me)
    return u.id === t.patient_id
  }catch{ return false }
}
</script>
