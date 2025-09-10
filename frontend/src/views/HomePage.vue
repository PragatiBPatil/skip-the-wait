<template>
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
import Navbar from "@/components/Navbar.vue";
import Hero from "@/components/Hero.vue";
import HowItWorks from "@/components/HowItWorks.vue";
import Doctors from "@/components/Doctors.vue";
import LiveQueue from "@/components/LiveQueue.vue";
import LoginSection from "@/components/LoginSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "HomePage",
  components: { Navbar, Hero, HowItWorks, Doctors, LiveQueue, LoginSection, Footer },
};
</script>
