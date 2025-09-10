import { createRouter, createWebHistory } from 'vue-router'
import Login from './components/Auth/Login.vue'
import Register from './components/Auth/Register.vue'
import HospitalList from './components/Hospitals/HospitalList.vue'
import DoctorList from './components/Hospitals/DoctorList.vue'
import QueueView from './components/Queue/QueueView.vue'
import PatientDashboard from './components/Dashboard/PatientDashboard.vue'

const routes = [
  { path: '/', component: HospitalList },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/hospitals/:id/doctors', component: DoctorList, props: true },
  { path: '/queue/:ticketId', component: QueueView, props: true },
  { path: '/dashboard', component: PatientDashboard },
  { path: '/add-hospital', component: () => import('./components/Hospitals/AddHospital.vue') },
  { path: '/add-doctor', component: () => import('./components/Hospitals/AddDoctor.vue') },
  { path: '/doctor-dashboard', component: () => import('./components/Dashboard/DoctorDashboard.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
