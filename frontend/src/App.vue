<template>
  <div>
    <Navbar />
    <router-view />
    <NotificationContainer />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import NotificationContainer from './components/NotificationContainer.vue'
</script>

<style></style>
