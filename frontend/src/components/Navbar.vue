<template>
<nav class="bg-white shadow sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
    <div class="flex items-center space-x-2">
      <span class="text-2xl">🏥</span>
      <router-link to="/" class="text-xl font-bold text-gray-800">Hospital Queue</router-link>
    </div>
    <ul class="hidden md:flex space-x-6 text-gray-600 font-medium">
      <li><router-link to="/" class="hover:text-blue-600">Home</router-link></li>
      <li><router-link to="/dashboard" class="hover:text-blue-600">My Dashboard</router-link></li>
      <li><router-link to="/doctor-dashboard" class="hover:text-blue-600">Doctor Dashboard</router-link></li>
      <li><router-link to="/add-hospital" class="hover:text-blue-600">Add Hospital</router-link></li>
      <li><router-link to="/add-doctor" class="hover:text-blue-600">Add Doctor</router-link></li>
      <li v-if="!user"><router-link to="/login" class="hover:text-blue-600">Login</router-link></li>
      <li v-if="!user"><router-link to="/register" class="hover:text-blue-600">Register</router-link></li>
      <li v-if="user" class="relative group cursor-pointer">
        <div @click="toggleMenu" class="hover:text-blue-600 flex items-center space-x-2">
          <span>{{ user.name }}</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
        <ul v-show="menuOpen" class="absolute right-0 mt-2 w-40 bg-white border rounded shadow-lg z-50">
          <li @click="logout" class="px-4 py-2 hover:bg-gray-100 cursor-pointer">Logout</li>
        </ul>
      </li>
    </ul>
    <button @click="toggleMenu" class="md:hidden text-gray-600 focus:outline-none">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
  </div>
  <transition name="fade">
    <div v-show="menuOpen" class="md:hidden bg-white border-t border-gray-200">
      <ul class="px-4 py-2 space-y-2">
        <li><router-link to="/" class="block hover:text-blue-600">Home</router-link></li>
        <li><router-link to="/dashboard" class="block hover:text-blue-600">My Dashboard</router-link></li>
        <li><router-link to="/doctor-dashboard" class="block hover:text-blue-600">Doctor Dashboard</router-link></li>
        <li><router-link to="/add-hospital" class="block hover:text-blue-600">Add Hospital</router-link></li>
        <li><router-link to="/add-doctor" class="block hover:text-blue-600">Add Doctor</router-link></li>
        <li v-if="!user"><router-link to="/login" class="block hover:text-blue-600">Login</router-link></li>
        <li v-if="!user"><router-link to="/register" class="block hover:text-blue-600">Register</router-link></li>
        <li v-if="user" @click="logout" class="block hover:text-blue-600 cursor-pointer">Logout</li>
      </ul>
    </div>
  </transition>
</nav>
</template>

<script setup>
import { ref } from 'vue'
import { useAuth } from '../stores/auth'

const { user, logout } = useAuth()
const menuOpen = ref(false)

function toggleMenu() {
  menuOpen.value = !menuOpen.value
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>

<style scoped></style>
