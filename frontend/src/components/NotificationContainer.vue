<template>
  <div class="fixed top-4 right-4 z-50 space-y-2">
    <NotificationToast
      v-for="notification in notifications"
      :key="notification.id"
      :type="notification.type"
      :title="notification.title"
      :message="notification.message"
      :duration="notification.duration"
      @close="remove(notification.id)"
    />
  </div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import NotificationToast from './NotificationToast.vue'
import { useNotifications } from '../stores/notifications'

const { notifications, remove } = useNotifications()
</script>
