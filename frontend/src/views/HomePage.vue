<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container text-center">
        <h1 class="display-4 text-pink-700 mb-4 fadeIn">Welcome to Femfinity</h1>
        <p class="lead text-secondary mb-5 fadeIn">
          Empowering women to take control of their health through personalized advice and tools.
        </p>
        <div class="mt-4">
          <a
            href="/login"
            class="btn btn-gradient btn-lg px-5 py-2 rounded-pill shadow-sm bounceIn"
          >
            Get Started
          </a>
        </div>
        
        <!-- Features Section -->
        <section class="mt-5 fadeInSection">
          <h2 class="h3 font-weight-bold text-pink-700 mb-4">Our Key Features</h2>
          <div class="row">
            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-4 fadeInCard">
                <i class="bi bi-robot text-pink-500 mb-3" style="font-size: 3rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Machine Learning-Powered Predictions</h3>
                <p class="text-secondary">
                  Using advanced machine learning models trained on diverse datasets, we predict potential illnesses based on your symptoms, promoting early detection and proactive health management.
                </p>
              </div>
            </div>

            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-4 fadeInCard">
                <i class="bi bi-journal text-pink-500 mb-3" style="font-size: 3rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Health Journaling</h3>
                <p class="text-secondary">
                  Log your symptoms, habits, and daily observations in a comprehensive health journal. This data enhances prediction accuracy and provides insights into your overall health trends.
                </p>
              </div>
            </div>

            <div class="col-md-4 mb-4">
              <div class="card shadow-sm border-0 p-4 fadeInCard">
                <i class="bi bi-person-check text-pink-500 mb-3" style="font-size: 3rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Personalized Health Advice</h3>
                <p class="text-secondary">
                  Receive tailored health advice based on your symptoms and journaling data, empowering you to take informed actions for better health management.
                </p>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-4">
              <div class="card shadow-sm border-0 p-4 fadeInCard">
                <i class="bi bi-chat-left-text text-pink-500 mb-3" style="font-size: 3rem;"></i>
                <h3 class="h6 text-dark-pink font-weight-bold">Community Forum</h3>
                <p class="text-secondary">
                  Connect with others, share experiences, and seek support through our community forum. Foster a collaborative environment for health discussions.
                </p>
              </div>
            </div>

            <div class="col-md-6 mb-4">
              <div class="card shadow-sm border-0 p-4 fadeInCard">
                <i class="bi bi-chat-dots text-pink-500 mb-3" style="font-size: 3rem;"></i>
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
/* Animation Styles */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounceIn {
  0% {
    transform: scale(0.8);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

/* Applying Animations */
.fadeIn {
  animation: fadeIn 1s ease-out;
}

.fadeInSection {
  animation: fadeIn 1.5s ease-out;
}

.fadeInCard {
  animation: fadeIn 1.2s ease-out;
}

.bounceIn {
  animation: bounceIn 1s ease-out;
}

/* Color Palette */
.bg-light-pink {
  background-color: #ffebf2; /* Soft blush pink background */
}

.text-dark-gray {
  color: #6c6c6c; /* Soft dark gray for text */
}

.text-dark-pink {
  color: #ec407a; /* Warm, inviting pink for highlights */
}

.text-pink-700 {
  color: #c2185b; /* Bold pink for headers */
}

.text-pink-500 {
  color: #f06292; /* Light, playful pink for icons */
}

.btn-gradient {
  background: linear-gradient(135deg, #f8a5c2, #f06292); /* Sweet gradient from soft pink to rose */
  color: #ffffff;
  border-radius: 50px;
  text-transform: uppercase;
  font-weight: bold;
  transition: transform 0.3s ease;
}

.btn-gradient:hover {
  background: linear-gradient(135deg, #f06292, #ec407a); /* Slightly darker gradient on hover */
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.card {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 35px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
}

.card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 182, 193, 0.2); /* Soft pastel pink overlay */
  border-radius: 20px;
  z-index: -1;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.card i {
  color: #f06292; /* Light pink for icons */
}

.card h3 {
  color: #ec407a; /* Warm pink for card titles */
  font-size: 1.25rem;
  font-weight: bold;
}

.card p {
  color: #6c6c6c; /* Muted gray for description text */
  font-size: 0.95rem;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .card {
    margin-bottom: 1.5rem;
  }

  .btn-gradient {
    padding: 10px 30px;
  }
}
</style>
