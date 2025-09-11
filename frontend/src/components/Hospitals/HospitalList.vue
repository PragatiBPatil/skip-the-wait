<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h1 class="text-3xl font-bold text-gray-900">Find Your Hospital</h1>
            <p class="text-gray-600 mt-2">Browse and book appointments at top hospitals</p>
          </div>
          <router-link
            to="/dashboard"
            class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:shadow-lg transform hover:scale-105 transition-all duration-200"
          >
            <span class="mr-2">📋</span>
            My Dashboard
          </router-link>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white rounded-2xl shadow-lg p-6 mb-8">
        <div class="flex flex-col md:flex-row gap-4">
          <div class="flex-1">
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="11" cy="11" r="8"></circle>
                  <path d="m21 21-4.35-4.35"></path>
                </svg>
              </div>
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Search hospitals by name or specialization..."
                class="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          </div>
          <div class="flex gap-2">
            <select
              v-model="selectedSpecialization"
              class="px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              <option value="">All Specializations</option>
              <option v-for="spec in specializations" :key="spec" :value="spec">{{ spec }}</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        <span class="ml-3 text-gray-600">Loading hospitals...</span>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="text-center py-20">
        <div class="text-red-500 text-6xl mb-4">⚠️</div>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">Failed to load hospitals</h3>
        <p class="text-gray-600 mb-4">{{ error }}</p>
        <button
          @click="fetchHospitals"
          class="px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors"
        >
          Try Again
        </button>
      </div>

      <!-- Hospitals Grid -->
      <div v-else-if="filteredHospitals.length > 0" class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="hospital in filteredHospitals"
          :key="hospital.id"
          class="bg-white rounded-2xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 overflow-hidden"
        >
          <div class="p-6">
            <div class="flex items-start justify-between mb-4">
              <div class="flex-1">
                <h3 class="text-xl font-bold text-gray-900 mb-2">{{ hospital.name }}</h3>
                <div class="flex items-center text-sm text-gray-600 mb-2">
                  <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                    {{ hospital.specialization }}
                  </span>
                </div>
                <p class="text-gray-600 text-sm">{{ hospital.address || 'Address not available' }}</p>
              </div>
              <div class="ml-4">
                <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                  <span class="text-white text-xl">🏥</span>
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between">
              <div class="text-sm text-gray-500">
                <span class="font-medium">{{ hospital.doctorCount || 0 }}</span> doctors available
              </div>
              <button
                @click="viewDoctors(hospital.id)"
                class="inline-flex items-center px-4 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:shadow-lg transform hover:scale-105 transition-all duration-200"
              >
                <span class="mr-2">👨‍⚕️</span>
                View Doctors
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-20">
        <div class="text-gray-400 text-6xl mb-4">🏥</div>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">No hospitals found</h3>
        <p class="text-gray-600 mb-4">Try adjusting your search criteria</p>
        <button
          @click="clearFilters"
          class="px-6 py-3 bg-gray-600 text-white rounded-xl hover:bg-gray-700 transition-colors"
        >
          Clear Filters
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import API from '../../services/api'
import { useRouter } from 'vue-router'

const hospitals = ref([])
const loading = ref(false)
const error = ref('')
const searchQuery = ref('')
const selectedSpecialization = ref('')
const router = useRouter()

async function fetchHospitals(){
  loading.value = true
  error.value = ''
  try{
    const response = await API.get('/hospitals')
    hospitals.value = response.data
  }catch(err){
    error.value = err.response?.data?.error || 'Failed to load hospitals'
    console.error('Error fetching hospitals:', err)
  }finally{
    loading.value = false
  }
}

onMounted(fetchHospitals)

const specializations = computed(() => {
  const specs = new Set(hospitals.value.map(h => h.specialization).filter(Boolean))
  return Array.from(specs).sort()
})

const filteredHospitals = computed(() => {
  let filtered = hospitals.value

  // Filter by search query
  if(searchQuery.value){
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(hospital =>
      hospital.name.toLowerCase().includes(query) ||
      (hospital.specialization || '').toLowerCase().includes(query) ||
      (hospital.address || '').toLowerCase().includes(query)
    )
  }

  // Filter by specialization
  if(selectedSpecialization.value){
    filtered = filtered.filter(hospital => hospital.specialization === selectedSpecialization.value)
  }

  return filtered
})

function viewDoctors(id){
  router.push(`/hospitals/${id}/doctors`)
}

function clearFilters(){
  searchQuery.value = ''
  selectedSpecialization.value = ''
}
</script>
