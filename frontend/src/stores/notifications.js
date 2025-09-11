import { ref } from 'vue'

const notifications = ref([])

export function useNotifications() {
  function add(notification) {
    const id = Date.now() + Math.random()
    const newNotification = {
      id,
      type: 'info',
      duration: 5000,
      ...notification
    }

    notifications.value.push(newNotification)

    // Auto remove after duration
    if (newNotification.duration > 0) {
      setTimeout(() => {
        remove(id)
      }, newNotification.duration)
    }

    return id
  }

  function remove(id) {
    const index = notifications.value.findIndex(n => n.id === id)
    if (index > -1) {
      notifications.value.splice(index, 1)
    }
  }

  function clear() {
    notifications.value = []
  }

  function success(title, message = '', duration = 5000) {
    return add({ type: 'success', title, message, duration })
  }

  function error(title, message = '', duration = 7000) {
    return add({ type: 'error', title, message, duration })
  }

  function warning(title, message = '', duration = 6000) {
    return add({ type: 'warning', title, message, duration })
  }

  function info(title, message = '', duration = 5000) {
    return add({ type: 'info', title, message, duration })
  }

  return {
    notifications: readonly(notifications),
    add,
    remove,
    clear,
    success,
    error,
    warning,
    info
  }
}

// Helper function for readonly
function readonly(ref) {
  return {
    get value() {
      return ref.value
    }
  }
}
