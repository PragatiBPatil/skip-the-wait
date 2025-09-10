<template>
  <section class="bg-gray-50 py-16 px-6">
    <h2 class="text-3xl font-bold text-center mb-12">Available Doctors</h2>
    <div class="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">
      <div class="p-6 bg-white rounded-xl shadow hover:scale-105 transition">
        <h3 class="text-xl font-semibold">👨‍⚕️ Dr. Sharma</h3>
        <p class="text-gray-600">Cardiologist</p>
        <p class="text-sm mt-2">Now Serving: Token #12</p>
        <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Book Token</button>
      </div>
      <div class="p-6 bg-white rounded-xl shadow hover:scale-105 transition">
        <h3 class="text-xl font-semibold">👩‍⚕️ Dr. Mehta</h3>
        <p class="text-gray-600">Orthopedic</p>
        <p class="text-sm mt-2">Estimated Wait: 15 mins</p>
        <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Book Token</button>
      </div>
      <div class="p-6 bg-white rounded-xl shadow hover:scale-105 transition">
        <h3 class="text-xl font-semibold">👩‍⚕️ Dr. Rao</h3>
        <p class="text-gray-600">Pediatrician</p>
        <p class="text-sm mt-2">Next Available: Token #18</p>
        <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Book Token</button>
      </div>
    </div>
  </section>
</template>

<script setup></script>

<style scoped></style>
