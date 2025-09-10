<template>
  <nav class="bg-white shadow sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center space-x-2">
        <span class="text-2xl">🏥</span>
        <router-link to="/" class="text-xl font-bold text-gray-800">Hospital Queue</router-link>
      </div>
      <ul class="hidden md:flex space-x-6 text-gray-600 font-medium">
        <li><router-link to="/" class="hover:text-blue-600">Home</router-link></li>
        <li><router-link to="/hospitals" class="hover:text-blue-600">Hospitals</router-link></li>
        <li><router-link to="/dashboard" class="hover:text-blue-600">Dashboard</router-link></li>
        <li><router-link to="/login" class="hover:text-blue-600">Login</router-link></li>
        <li><router-link to="/register" class="hover:text-blue-600">Register</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script setup></script>

<style scoped></style>
