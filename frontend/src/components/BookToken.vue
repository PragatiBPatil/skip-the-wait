<script setup>
import { ref, onMounted } from "vue";
import API from "../services/api";

const hospitalId = ref("");
const doctorId = ref("");
const hospitals = ref([]);
const doctors = ref([]);
const responseMsg = ref("");

const fetchHospitals = async () => {
  try {
    const res = await API.get("/hospitals");
    hospitals.value = res.data;
  } catch (err) {
    console.error("Error fetching hospitals:", err);
  }
};

const fetchDoctors = async () => {
  if (!hospitalId.value) return;
  try {
    const res = await API.get(`/doctors/${hospitalId.value}`);
    doctors.value = res.data;
  } catch (err) {
    console.error("Error fetching doctors:", err);
  }
};

const bookToken = async () => {
  if (!doctorId.value) {
    responseMsg.value = "❌ Please select a doctor!";
    return;
  }
  try {
    const res = await API.post("/tickets", { doctor_id: doctorId.value });
    responseMsg.value = `✅ ${res.data.message} | Ticket ID: ${res.data.ticket_id}`;
  } catch (err) {
    responseMsg.value = "❌ You must be logged in to book a token!";
    console.error(err);
  }
};

onMounted(fetchHospitals);
</script>

<template>
  <div class="p-6 bg-white shadow-lg rounded-xl max-w-md mx-auto">
    <h2 class="text-xl font-semibold mb-4">Book Token</h2>
    <select v-model="hospitalId" @change="fetchDoctors" class="border p-2 w-full mb-3 rounded">
      <option value="">Select Hospital</option>
      <option v-for="hospital in hospitals" :key="hospital.id" :value="hospital.id">
        {{ hospital.name }} - {{ hospital.specialization }}
      </option>
    </select>
    <select v-model="doctorId" class="border p-2 w-full mb-3 rounded" :disabled="!hospitalId">
      <option value="">Select Doctor</option>
      <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">
        {{ doctor.name }} - {{ doctor.specialization }}
      </option>
    </select>
    <button @click="bookToken" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition" :disabled="!doctorId">
      Book
    </button>
    <p class="mt-3 text-green-600">{{ responseMsg }}</p>
  </div>
</template>
