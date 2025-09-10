<script setup>
import { ref, onMounted } from "vue";
import API from "../services/api";

const tickets = ref([]);

const fetchTickets = async () => {
  try {
    const res = await API.get("/tickets/mine");
    tickets.value = res.data;
  } catch (err) {
    console.error("Error fetching tickets:", err);
  }
};

onMounted(fetchTickets);
</script>

<template>
  <div class="p-6 bg-white shadow-lg rounded-xl max-w-2xl mx-auto">
    <h2 class="text-xl font-semibold mb-4">My Tickets</h2>
    <ul>
      <li v-for="t in tickets" :key="t.id" class="border p-3 mb-2 rounded">
        🎟 Ticket #{{ t.token_number }} — Status: 
        <span class="font-semibold">{{ t.status }}</span> 
        | ⏳ Wait: {{ t.estimated_wait_minutes }} mins
      </li>
    </ul>
  </div>
</template>
