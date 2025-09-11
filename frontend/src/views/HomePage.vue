<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50">
    <!-- Navigation -->
    <Navbar />

    <!-- Hero Section -->
    <section class="relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div class="text-center">
          <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
            <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Hospital Queue
            </span>
            <br>
            <span class="text-2xl md:text-4xl text-gray-600">Management System</span>
          </h1>
          <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Streamline your healthcare experience with our intelligent queue management system.
            Book appointments, track your position, and get real-time updates.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link
              to="/hospitals"
              class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-4 rounded-xl font-semibold text-lg hover:shadow-lg transform hover:scale-105 transition-all duration-200"
            >
              Book Appointment
            </router-link>
            <router-link
              to="/dashboard"
              class="border-2 border-blue-600 text-blue-600 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-blue-50 transition-all duration-200"
            >
              My Dashboard
            </router-link>
          </div>
        </div>
      </div>

      <!-- Background decoration -->
      <div class="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div class="absolute -top-40 -right-40 w-80 h-80 bg-blue-100 rounded-full opacity-20"></div>
        <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-indigo-100 rounded-full opacity-20"></div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Why Choose Our System?</h2>
          <p class="text-xl text-gray-600">Experience healthcare queuing like never before</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center p-8 rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 hover:shadow-xl transition-all duration-300">
            <div class="w-16 h-16 bg-blue-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl text-white">📅</span>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Easy Booking</h3>
            <p class="text-gray-600">Book appointments with just a few clicks. Choose your preferred doctor and time slot instantly.</p>
          </div>

          <div class="text-center p-8 rounded-2xl bg-gradient-to-br from-green-50 to-emerald-50 hover:shadow-xl transition-all duration-300">
            <div class="w-16 h-16 bg-green-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl text-white">📊</span>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Real-time Updates</h3>
            <p class="text-gray-600">Get live queue status and estimated wait times. Never miss your turn again.</p>
          </div>

          <div class="text-center p-8 rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 hover:shadow-xl transition-all duration-300">
            <div class="w-16 h-16 bg-purple-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl text-white">🏥</span>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Multiple Hospitals</h3>
            <p class="text-gray-600">Access healthcare services from various hospitals and specialists in one platform.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Actions Section -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Quick Actions</h2>
          <p class="text-xl text-gray-600">Everything you need at your fingertips</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <router-link
            to="/hospitals"
            class="group bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
          >
            <div class="text-center">
              <div class="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-700 transition-colors">
                <span class="text-xl text-white">🏥</span>
              </div>
              <h3 class="font-semibold text-gray-900 mb-2">Browse Hospitals</h3>
              <p class="text-sm text-gray-600">Find and book at your preferred hospital</p>
            </div>
          </router-link>

          <router-link
            to="/dashboard"
            class="group bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
          >
            <div class="text-center">
              <div class="w-12 h-12 bg-green-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:bg-green-700 transition-colors">
                <span class="text-xl text-white">📋</span>
              </div>
              <h3 class="font-semibold text-gray-900 mb-2">My Tickets</h3>
              <p class="text-sm text-gray-600">View and manage your appointments</p>
            </div>
          </router-link>

          <router-link
            to="/queue-status"
            class="group bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
          >
            <div class="text-center">
              <div class="w-12 h-12 bg-purple-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:bg-purple-700 transition-colors">
                <span class="text-xl text-white">📊</span>
              </div>
              <h3 class="font-semibold text-gray-900 mb-2">Queue Status</h3>
              <p class="text-sm text-gray-600">Check live queue information</p>
            </div>
          </router-link>

          <div class="group bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300">
            <div class="text-center">
              <div class="w-12 h-12 bg-orange-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:bg-orange-700 transition-colors">
                <span class="text-xl text-white">📞</span>
              </div>
              <h3 class="font-semibold text-gray-900 mb-2">Support</h3>
              <p class="text-sm text-gray-600">Get help and support</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
</script>
