<template>
  <div
    v-if="show"
    class="fixed top-4 right-4 z-50 max-w-sm w-full"
  >
    <div
      :class="[
        'rounded-xl shadow-lg p-4 flex items-start space-x-3',
        type === 'success' ? 'bg-green-50 border border-green-200' :
        type === 'error' ? 'bg-red-50 border border-red-200' :
        type === 'warning' ? 'bg-yellow-50 border border-yellow-200' :
        'bg-blue-50 border border-blue-200'
      ]"
    >
      <!-- Icon -->
      <div class="flex-shrink-0">
        <svg
          :class="[
            'h-5 w-5',
            type === 'success' ? 'text-green-400' :
            type === 'error' ? 'text-red-400' :
            type === 'warning' ? 'text-yellow-400' :
            'text-blue-400'
          ]"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle v-if="type === 'success'" cx="12" cy="12" r="10"></circle>
          <path v-if="type === 'success'" d="M9 12l2 2 4-4"></path>
          <circle v-if="type === 'error'" cx="12" cy="12" r="10"></circle>
          <path v-if="type === 'error'" d="M15 9l-6 6m0-6l6 6"></path>
          <circle v-if="type === 'warning'" cx="12" cy="12" r="10"></circle>
          <path v-if="type === 'warning'" d="M12 8v4m0 4h.01"></path>
          <circle v-if="type === 'info'" cx="12" cy="12" r="10"></circle>
          <path v-if="type === 'info'" d="M12 8v4m0 4h.01"></path>
        </svg>
      </div>

      <!-- Content -->
      <div class="flex-1 min-w-0">
        <p class="text-sm font-medium text-gray-900">{{ title }}</p>
        <p v-if="message" class="text-sm text-gray-600 mt-1">{{ message }}</p>
      </div>

      <!-- Close button -->
      <div class="flex-shrink-0">
        <button
          @click="close"
          class="inline-flex text-gray-400 hover:text-gray-600 transition-colors"
        >
          <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'info',
    validator: (value) => ['success', 'error', 'warning', 'info'].includes(value)
  },
  title: {
    type: String,
    required: true
  },
  message: {
    type: String,
    default: ''
  },
  duration: {
    type: Number,
    default: 5000
  }
})

const emit = defineEmits(['close'])
const show = ref(true)

function close() {
  show.value = false
  emit('close')
}

// Auto close after duration
if (props.duration > 0) {
  onMounted(() => {
    setTimeout(() => {
      close()
    }, props.duration)
  })
}
</script>
