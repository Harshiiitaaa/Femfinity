<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container text-center">
        <h1 class="display-4 text-pink-700 mb-4">Welcome to Women HealthCare</h1>
        <p class="lead text-secondary mb-5">
          Empowering women to take control of their health through personalized advice and tools.
        </p>
        <div class="mt-4">
          <a
            href="/get-started"
            class="btn btn-gradient btn-lg px-5 py-2 rounded-pill shadow-sm"
          >
            Get Started
          </a>
        </div>
        
        <!-- Features Section -->
        <section class="mt-5">
          <h2 class="h3 font-weight-bold text-pink-700 mb-4">Our Key Features</h2>
          <div class="row">
            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <i class="bi bi-robot text-pink-500 mb-3" style="font-size: 2.5rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Machine Learning-Powered Predictions</h3>
                <p class="text-secondary">
                  Using advanced machine learning models trained on diverse datasets, we predict potential illnesses based on your symptoms, promoting early detection and proactive health management.
                </p>
              </div>
            </div>

            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <i class="bi bi-journal text-pink-500 mb-3" style="font-size: 2.5rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Health Journaling</h3>
                <p class="text-secondary">
                  Log your symptoms, habits, and daily observations in a comprehensive health journal. This data enhances prediction accuracy and provides insights into your overall health trends.
                </p>
              </div>
            </div>

            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <i class="bi bi-person-check text-pink-500 mb-3" style="font-size: 2.5rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Personalized Health Advice</h3>
                <p class="text-secondary">
                  Receive tailored health advice based on your symptoms and journaling data, empowering you to take informed actions for better health management.
                </p>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <i class="bi bi-chat-left-text text-pink-500 mb-3" style="font-size: 2.5rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Community Forum</h3>
                <p class="text-secondary">
                  Connect with others, share experiences, and seek support through our community forum. Foster a collaborative environment for health discussions.
                </p>
              </div>
            </div>

            <div class="col-md-6 mb-4">
              <div class="card shadow-sm border-0 p-3">
                <i class="bi bi-chat-dots text-pink-500 mb-3" style="font-size: 2.5rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">AI-Powered Chatbot</h3>
                <p class="text-secondary">
                  Get instant support with our AI-powered chatbot. It will answer your health-related queries, guide you through the app’s features, and provide conversational assistance.
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
  name: "HomePage",
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
