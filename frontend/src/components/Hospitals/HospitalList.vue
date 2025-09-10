<template>
  <div>
    <div class="flex gap-2 mb-4">
      <input v-model="q" placeholder="Search hospitals..." class="flex-1 p-2 border rounded" />
      <router-link to="/dashboard" class="px-4 py-2 bg-gray-200 rounded">Dashboard</router-link>
    </div>

    <ul class="space-y-3">
      <li v-for="h in filtered" :key="h.id" class="bg-white p-4 rounded shadow">
        <div class="flex justify-between items-center">
          <div>
            <div class="font-semibold">{{ h.name }}</div>
            <div class="text-sm text-gray-600">{{ h.specialization }} • {{ h.address || 'Address not set' }}</div>
          </div>
          <div>
            <button @click="viewDoctors(h.id)" class="px-3 py-1 bg-blue-600 text-white rounded">View Doctors</button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../../api'
import { useRouter } from 'vue-router'

const hospitals = ref([])
const q = ref('')
const router = useRouter()

async function fetch(){
  try{
    const r = await api.get('/hospitals')
    hospitals.value = r.data
  }catch(e){
    console.error(e)
  }
}

onMounted(fetch)

const filtered = computed(()=> {
  if(!q.value) return hospitals.value
  return hospitals.value.filter(h => h.name.toLowerCase().includes(q.value.toLowerCase()) || (h.specialization||'').toLowerCase().includes(q.value.toLowerCase()))
})

function viewDoctors(id){
  router.push(`/hospitals/${id}/doctors`)
}
</script>
