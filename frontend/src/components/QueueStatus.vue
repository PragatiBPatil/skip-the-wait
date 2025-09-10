<script setup>
import { ref } from "vue";
import API from "../services/api";

const doctorId = ref("");
const status = ref(null);

const fetchQueue = async () => {
  try {
    const res = await API.get(`/queue/${doctorId.value}`);
    status.value = res.data;
  } catch (err) {
    console.error("Error fetching queue:", err);
  }
};
</script>

<template>
  <div class="p-6 bg-gray-100 shadow-md rounded-xl max-w-md mx-auto">
    <h2 class="text-lg font-semibold mb-3">Queue Status</h2>
    <input v-model="doctorId" placeholder="Enter Doctor ID" class="border p-2 w-full mb-3 rounded" />
    <button @click="fetchQueue" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">
      Check Queue
    </button>

    <div v-if="status" class="mt-4 bg-white p-3 rounded shadow">
      <p>👨‍⚕️ Doctor ID: {{ status.doctor_id }}</p>
      <p>Now Serving: {{ status.now_serving }}</p>
      <p>Waiting Count: {{ status.waiting_count }}</p>
      <p>Average Wait: {{ status.average_wait_time }} mins</p>
    </div>
  </div>
</template>
