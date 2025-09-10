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
        <li v-if="user" @click="logout" class="hover:text-blue-600 cursor-pointer">Logout</li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { useAuth } from '../stores/auth'

const { user, logout } = useAuth()
</script>

<style scoped></style>
