import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import HospitalList from '../components/HospitalList.vue'
import DoctorList from '../components/DoctorList.vue'
import QueueView from '../components/QueueView.vue'
import PatientDashboard from '../components/PatientDashboard.vue'

const routes = [
  { path: '/', redirect: '/login' },  // default route
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/hospitals', component: HospitalList },
  { path: '/doctors/:hospitalId', component: DoctorList, props: true },
  { path: '/queue/:doctorId', component: QueueView, props: true },
  { path: '/dashboard', component: PatientDashboard },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
