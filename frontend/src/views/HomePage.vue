<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-pink-50 text-gray-800 py-8">
      <div class="container text-center">
        <h1 class="display-4 text-pink-700 mb-4">Welcome to Women HealthCare</h1>
        <p class="lead text-gray-600">
          Empowering women to take control of their health through personalized advice and tools.
        </p>
        <div class="mt-4">
          <a
            href="/get-started"
            class="btn btn-pink btn-lg px-6 py-3 rounded-lg shadow-md"
          >
            Get Started
          </a>
        </div>
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
/* Additional global styles if required */
body {
  font-family: "Poppins", sans-serif;
}

.btn-pink {
  background-color: #f06292;
  border-color: #f06292;
}

.btn-pink:hover {
  background-color: #e91e63;
  border-color: #e91e63;
}
</style>
