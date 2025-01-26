<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container text-center">
        <h1 class="display-4 text-pink-700 mb-4">About Us</h1>
        <p class="lead text-secondary mb-5">
          Welcome to Femfinity – a platform dedicated to empowering women to take control of their health.
        </p>
        
        <section>
          <h2 class="h3 font-weight-bold text-pink-700 mb-4">Our Journey</h2>
          <p class="text-secondary mb-4">
            Femfinity was born out of the desire to create something truly meaningful for women everywhere. We saw a gap in the health space, where women often lacked tools to effectively monitor their well-being and make informed decisions about their health. What started as an idea between passionate individuals has transformed into a mission to bring predictive technology, health insights, and a sense of community to women.
          </p>

          <h3 class="h4 font-weight-bold text-pink-700 mb-4">What We’re Solving</h3>
          <p class="text-secondary mb-4">
            Women frequently encounter challenges in identifying potential health issues at an early stage due to a lack of tools designed to address their specific health concerns. These challenges are compounded by the absence of accessible platforms that facilitate consistent symptom tracking, provide meaningful insights, and offer personalized guidance.
          </p>
          <p class="text-secondary mb-4">
            Women’s health, which often involves complex and interconnected physical, emotional, and hormonal factors, requires a holistic approach that goes beyond basic symptom management. The inability to monitor their health effectively can lead to delays in seeking medical attention, worsening conditions, and heightened stress.
          </p>
          <p class="text-secondary mb-4">
            This is where Femfinity steps in. We offer a comprehensive solution that integrates predictive technology for early illness detection with features like health journaling and tailored advice. Our platform empowers women to take charge of their well-being and provides a safe, supportive space to track, understand, and improve their overall health in a way that resonates with their unique experiences and needs.
          </p>

          <h3 class="h4 font-weight-bold text-pink-700 mb-4">Meet the Dream Team</h3>
          <div class="row">
            <div class="col-md-3 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <h5 class="text-dark-pink font-weight-bold">Raghvi Gupta</h5>
                <p class="text-secondary">The go-getter, always thinking ahead, and a constant source of energy. She brings the spark that gets things rolling!</p>
              </div>
            </div>
            <div class="col-md-3 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <h5 class="text-dark-pink font-weight-bold">Nishika Agarwal</h5>
                <p class="text-secondary">The problem-solver with a sharp mind. When things seem complicated, she’s the one figuring out how to make it all work smoothly.</p>
              </div>
            </div>
            <div class="col-md-3 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <h5 class="text-dark-pink font-weight-bold">Ishita Tayal</h5>
                <p class="text-secondary">The creative heart of Femfinity. If you can imagine it, she’s the one who brings it to life with both tech and design flair.</p>
              </div>
            </div>
            <div class="col-md-3 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <h5 class="text-dark-pink font-weight-bold">Harshita Garg</h5>
                <p class="text-secondary">The quiet force behind the scenes. She’s the calm in the storm, making sure everything runs just as it should.</p>
              </div>
            </div>
          </div>

          <h3 class="h4 font-weight-bold text-pink-700 mb-4">What Drives Us</h3>
          <p class="text-secondary mb-4">
            Each one of us at Femfinity brings our own unique spark to the table, and together, we share a simple belief: empowering women through better health is more than just a mission. It’s our passion. It’s what gets us excited to come to work every day, to push boundaries, and to make a real difference.
          </p>
          <p class="text-secondary mb-4">
            We’re not just a team; we’re a family working towards a common goal: to make every woman feel strong, informed, and in control of her health. And we believe that with the right tools, support, and knowledge, every woman can achieve just that.
          </p>
        </section>
      </div>
    </main>

    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  name: "AboutUsPage",
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style scoped>
/* Color Palette */
.bg-light-pink {
  background-color: #fff5f8; /* Light pink background */
}

.text-dark-gray {
  color: #4a4a4a;
}

.text-dark-pink {
  color: #d63384;
}

.text-pink-700 {
  color: #c2185b;
}

.text-pink-500 {
  color: #ec407a;
}

.btn-gradient {
  background: linear-gradient(135deg, #f06292, #d63384); /* Pink Gradient */
  color: #ffffff;
}

.btn-gradient:hover {
  background: linear-gradient(135deg, #ec407a, #c2185b); /* Darker Pink Gradient */
  color: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.card {
  background-color: #ffffff;
  border-radius: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .card {
    margin-bottom: 1.5rem;
  }
}
</style>
