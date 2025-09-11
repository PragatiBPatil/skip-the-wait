<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex items-center justify-center px-4">
    <div class="max-w-md w-full">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <span class="text-2xl text-white">🔐</span>
        </div>
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Welcome Back</h1>
        <p class="text-gray-600">Sign in to your account to continue</p>
      </div>

      <!-- Login Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Email Field -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
              Email Address
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                </svg>
              </div>
              <input
                id="email"
                v-model="form.email"
                type="email"
                placeholder="Enter your email"
                class="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                :class="{ 'border-red-500 focus:ring-red-500': errors.email }"
                required
              />
            </div>
            <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
          </div>

          <!-- Password Field -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
              Password
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
                </svg>
              </div>
              <input
                id="password"
                v-model="form.password"
                type="password"
                placeholder="Enter your password"
                class="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                :class="{ 'border-red-500 focus:ring-red-500': errors.password }"
                required
              />
            </div>
            <p v-if="errors.password" class="mt-1 text-sm text-red-600">{{ errors.password }}</p>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full flex justify-center items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:shadow-lg transform hover:scale-105 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ loading ? 'Signing in...' : 'Sign In' }}
          </button>
        </form>

        <!-- Error Message -->
        <div v-if="generalError" class="mt-4 p-4 bg-red-50 border border-red-200 rounded-xl">
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-red-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 8v4m0 4h.01"></path>
              </svg>
            </div>
            <div class="ml-3">
              <p class="text-sm text-red-800">{{ generalError }}</p>
            </div>
          </div>
        </div>

        <!-- Register Link -->
        <div class="mt-6 text-center">
          <p class="text-gray-600">
            Don't have an account?
            <router-link
              to="/register"
              class="font-semibold text-blue-600 hover:text-blue-500 transition-colors duration-200"
            >
              Create one here
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../../stores/auth'

const { login } = useAuth()
const router = useRouter()

// Form state
const form = reactive({
  email: '',
  password: ''
})

// UI state
const loading = ref(false)
const generalError = ref('')
const errors = reactive({
  email: '',
  password: ''
})

// Validation functions
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!email) return 'Email is required'
  if (!emailRegex.test(email)) return 'Please enter a valid email address'
  return ''
}

function validatePassword(password) {
  if (!password) return 'Password is required'
  if (password.length < 6) return 'Password must be at least 6 characters'
  return ''
}

function validateForm() {
  errors.email = validateEmail(form.email)
  errors.password = validatePassword(form.password)
  return !errors.email && !errors.password
}

async function handleSubmit() {
  // Reset errors
  generalError.value = ''
  Object.keys(errors).forEach(key => {
    errors[key] = ''
  })

  // Validate form
  if (!validateForm()) {
    return
  }

  loading.value = true

  try {
    await login(form.email, form.password)
    router.push('/')
  } catch (error) {
    console.error('Login error:', error)

    // Handle different error types
    if (error.response?.status === 401) {
      generalError.value = 'Invalid email or password. Please try again.'
    } else if (error.response?.status === 400) {
      generalError.value = error.response.data?.error || 'Please check your input and try again.'
    } else if (error.response?.data?.error) {
      generalError.value = error.response.data.error
    } else {
      generalError.value = 'Something went wrong. Please try again later.'
    }
  } finally {
    loading.value = false
  }
}

// Clear errors when user starts typing
function clearFieldError(field) {
  if (errors[field]) {
    errors[field] = ''
  }
  if (generalError.value) {
    generalError.value = ''
  }
}

// Watch for input changes to clear errors
import { watch } from 'vue'
watch(() => form.email, () => clearFieldError('email'))
watch(() => form.password, () => clearFieldError('password'))
</script>
