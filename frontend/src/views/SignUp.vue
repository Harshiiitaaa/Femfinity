<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container">
        <!-- Sign Up Header -->
        <section class="sign-up-header text-center">
          <h1 class="display-4 text-dark-pink mb-4 fadeInUp">Sign Up</h1>
          <p class="lead text-secondary mb-5 fadeInUp" style="animation-delay: 0.3s;">
            Create an account and join the Femfinity community!
          </p>
        </section>

        <!-- Sign Up Form -->
        <section class="sign-up-form-section">
          <div class="form-container bg-white p-5 rounded shadow-lg fadeInUp">
            <form @submit.prevent="handleSubmit">
              <!-- Name Field -->
              <div class="form-group mb-3">
                <label for="name" class="text-dark-pink">Full Name</label>
                <input
                  type="text"
                  id="name"
                  v-model="name"
                  class="form-control"
                  placeholder="Enter your full name"
                  required
                />
              </div>

              <!-- Email Field -->
              <div class="form-group mb-3">
                <label for="email" class="text-dark-pink">Email Address</label>
                <input
                  type="email"
                  id="email"
                  v-model="email"
                  class="form-control"
                  placeholder="Enter your email"
                  required
                />
              </div>

              <!-- Password Field -->
              <div class="form-group mb-3">
                <label for="password" class="text-dark-pink">Password</label>
                <input
                  type="password"
                  id="password"
                  v-model="password"
                  class="form-control"
                  placeholder="Enter your password"
                  required
                />
              </div>

              <!-- Confirm Password Field -->
              <div class="form-group mb-4">
                <label for="confirmPassword" class="text-dark-pink">Confirm Password</label>
                <input
                  type="password"
                  id="confirmPassword"
                  v-model="confirmPassword"
                  class="form-control"
                  placeholder="Confirm your password"
                  required
                />
              </div>

              <!-- Submit Button -->
              <div class="form-group">
                <button type="submit" class="btn btn-gradient w-100">Sign Up</button>
              </div>
            </form>
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
  name: "SignUpPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    handleSubmit() {
      if (this.password === this.confirmPassword) {
        // Handle the sign-up logic (e.g., send data to the backend)
        alert("Account successfully created!");
      } else {
        alert("Passwords do not match. Please try again.");
      }
    },
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

/* Sign Up Section */
.sign-up-header {
  margin-bottom: 3rem;
}

.sign-up-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.sign-up-header p {
  font-size: 1.25rem;
}

.sign-up-form-section {
  margin-top: 3rem;
}

.form-container {
  max-width: 500px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  font-size: 1rem;
  font-weight: 600;
  color: #d63384;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 10px;
  border: 1px solid #ccc;
}

.btn-gradient {
  background-color: #f06292;
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 50px;
  font-size: 1.1rem;
  cursor: pointer;
}

.btn-gradient:hover {
  background-color: #d63384;
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
  .form-container {
    padding: 3rem 2rem;
  }
}
</style>
