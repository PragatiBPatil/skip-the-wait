<template>
<div>
    <h1 class="text-2xl font-bold text-center my-6">🏥 Hospital Queue Management</h1>
    
    <!-- Book token form -->
    <BookToken />

    <!-- My Tickets section -->
    <MyTickets />

    <!-- Queue status widget -->
    <QueueStatus />
  </div>
  <div class="min-h-screen bg-gradient-to-b from-blue-50 to-white">
    <Navbar />
    <Hero />
    <HowItWorks />
    <Doctors />
    <LiveQueue />
    <LoginSection />
    <Footer />
  </div>
</template>

<script>
import BookToken from "../components/BookToken.vue";
import MyTickets from "../components/MyTickets.vue";
import QueueStatus from "../components/QueueStatus.vue";
import Navbar from "@/components/Navbar.vue";
import Hero from "@/components/Hero.vue";
import HowItWorks from "@/components/HowItWorks.vue";
import Doctors from "@/components/Doctors.vue";
import LiveQueue from "@/components/LiveQueue.vue";
import LoginSection from "@/components/LoginSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "HomePage",
  components: { Navbar, Hero, HowItWorks, Doctors, LiveQueue, LoginSection, Footer, BookToken, MyTickets, QueueStatus },
};
</script>
