<template>
  <div class="p-6 bg-white shadow-lg rounded-xl max-w-4xl mx-auto">
    <h2 class="text-xl font-semibold mb-4">Doctor Dashboard</h2>
    <div class="mb-4">
      <label class="block text-sm font-medium mb-1">Enter Your Doctor ID</label>
      <input v-model="doctorId" type="number" class="border p-2 rounded" />
      <button @click="fetchTokens" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition ml-2">
        Load Tokens
      </button>
    </div>
    <div v-if="tokens.length > 0">
      <h3 class="text-lg font-semibold mb-2">Patient Tokens</h3>
      <ul>
        <li v-for="token in tokens" :key="token.id" class="border p-3 mb-2 rounded flex justify-between items-center">
          <div>
            <p><strong>Token #{{ token.token_number }}</strong></p>
            <p>Patient ID: {{ token.patient_id }}</p>
            <p>Status: {{ token.status }}</p>
          </div>
          <div>
            <button v-if="token.status === 'waiting'" @click="updateStatus(token.id, 'serving')" class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 transition mr-2">
              Start Serving
            </button>
            <button v-if="token.status === 'serving'" @click="updateStatus(token.id, 'completed')" class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 transition mr-2">
              Mark Completed
            </button>
            <button @click="updateStatus(token.id, 'cancelled')" class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 transition">
              Cancel
            </button>
          </div>
        </li>
      </ul>
    </div>
    <p v-else-if="doctorId" class="text-gray-500">No tokens found for this doctor.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../../services/api'

const doctorId = ref('')
const tokens = ref([])

const fetchTokens = async () => {
  if (!doctorId.value) return
  try {
    const res = await API.get(`/doctor/${doctorId.value}/tokens`)
    tokens.value = res.data
  } catch (err) {
    console.error('Error fetching tokens:', err)
  }
}

const updateStatus = async (ticketId, status) => {
  try {
    await API.put(`/tickets/${ticketId}/status`, { status })
    fetchTokens() // Refresh the list
  } catch (err) {
    console.error('Error updating status:', err)
  }
}
</script>
