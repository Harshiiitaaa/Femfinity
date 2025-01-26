<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container">
        <!-- Login Section -->
        <section class="login-section text-center">
          <h1 class="display-4 text-dark-pink mb-4 fadeInUp">Login to Femfinity</h1>
          <p class="lead text-secondary mb-5 fadeInUp" style="animation-delay: 0.3s;">
            Please enter your credentials to continue.
          </p>

          <!-- Login Form -->
          <div class="login-form bg-white p-4 rounded shadow-lg fadeInUp">
            <form @submit.prevent="handleLogin">
              <div class="mb-3">
                <input
                  type="text"
                  v-model="username"
                  class="form-control"
                  placeholder="Username"
                  required
                />
              </div>
              <div class="mb-3">
                <input
                  type="password"
                  v-model="password"
                  class="form-control"
                  placeholder="Password"
                  required
                />
              </div>
              <div class="mb-3">
                <button type="submit" class="btn btn-gradient w-100">Login</button>
              </div>
              <div class="text-center">
                <p class="text-secondary">
                  Don't have an account? <a href="#" class="text-dark-pink">Sign up</a>
                </p>
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
  name: "LoginPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    handleLogin() {
      // Handle login logic here
      if (this.username && this.password) {
        console.log("Login successful");
      } else {
        console.log("Please fill in both fields");
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

/* Login Section */
.login-section {
  margin-top: 3rem; /* Adjusted margin to move the form up */
}

.login-section h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.login-section p {
  font-size: 1.25rem;
}

.login-form {
  max-width: 400px;
  margin: 0 auto;
}

.login-form input {
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 10px;
  border: 1px solid #ccc;
}

.login-form button {
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 50px;
  background-color: #f06292;
  color: white;
  border: none;
  cursor: pointer;
}

.login-form button:hover {
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
  .login-form button {
    padding: 0.75rem 1.5rem;
  }
}
</style>
