<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container">
        <!-- About Us Header -->
        <section class="about-us-header text-center">
          <h1 class="display-4 text-dark-pink mb-4 fadeInUp">About Us - Femfinity</h1>
          <p class="lead text-secondary mb-5 fadeInUp" style="animation-delay: 0.3s;">
            Empowering women through technology, innovation, and creativity.
          </p>
        </section>

        <!-- Team Section -->
        <section class="team-section text-center">
          <h2 class="text-dark-pink mb-4 fadeInUp">Meet Our Team</h2>
          <div class="row">
            <!-- Team Member: Raghvi Gupta -->
            <div class="col-md-3">
              <div class="team-member bg-white p-4 rounded shadow-lg fadeInUp">
                <img
                  src="https://via.placeholder.com/150"
                  alt="Raghvi Gupta"
                  class="team-member-img mb-3 rounded-circle"
                />
                <h4 class="text-dark-pink">Raghvi Gupta</h4>
                <p class="text-secondary">Lead Developer</p>
                <p class="text-dark-gray">
                  Passionate about coding and problem-solving, Raghvi leads the tech side of Femfinity.
                </p>
              </div>
            </div>

            <!-- Team Member: Nishika Agarwal -->
            <div class="col-md-3">
              <div class="team-member bg-white p-4 rounded shadow-lg fadeInUp">
                <img
                  src="https://via.placeholder.com/150"
                  alt="Nishika Agarwal"
                  class="team-member-img mb-3 rounded-circle"
                />
                <h4 class="text-dark-pink">Nishika Agarwal</h4>
                <p class="text-secondary">UI/UX Designer</p>
                <p class="text-dark-gray">
                  Nishika brings creative designs to life, ensuring our platform is user-friendly and beautiful.
                </p>
              </div>
            </div>

            <!-- Team Member: Ishita Tayal (User) -->
            <div class="col-md-3">
              <div class="team-member bg-white p-4 rounded shadow-lg fadeInUp">
                <img
                  src="https://via.placeholder.com/150"
                  alt="Ishita Tayal"
                  class="team-member-img mb-3 rounded-circle"
                />
                <h4 class="text-dark-pink">Ishita Tayal</h4>
                <p class="text-secondary">Content Strategist</p>
                <p class="text-dark-gray">
                  As a content strategist, Ishita ensures our messages are clear, impactful, and inspiring.
                </p>
              </div>
            </div>

            <!-- Team Member: Harshita Garg -->
            <div class="col-md-3">
              <div class="team-member bg-white p-4 rounded shadow-lg fadeInUp">
                <img
                  src="https://via.placeholder.com/150"
                  alt="Harshita Garg"
                  class="team-member-img mb-3 rounded-circle"
                />
                <h4 class="text-dark-pink">Harshita Garg</h4>
                <p class="text-secondary">Project Manager</p>
                <p class="text-dark-gray">
                  Harshita keeps everything running smoothly, ensuring that projects are delivered on time and on budget.
                </p>
              </div>
            </div>
          </div>
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

/* About Us Section */
.about-us-header {
  margin-bottom: 3rem;
}

.about-us-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.about-us-header p {
  font-size: 1.25rem;
}

.team-section {
  margin-top: 3rem;
}

.team-member {
  margin-bottom: 2rem;
}

.team-member-img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
}

.team-member h4 {
  font-size: 1.5rem;
  font-weight: bold;
}

.team-member p {
  font-size: 1rem;
}

/* Animations for elements */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fadeInUp {
  animation-name: fadeInUp;
  animation-duration: 1s;
  animation-timing-function: ease-out;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .team-member {
    margin-bottom: 1.5rem;
  }
}
</style>
