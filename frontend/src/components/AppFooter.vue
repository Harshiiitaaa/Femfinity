<template>
  <footer class="bg-pink-500 text-white py-4 mt-5">
    <div class="container text-center">
      <!-- Logo and Brand Name -->
      <div class="mb-3">
        <a href="/" class="text-2xl font-bold text-white">Women HealthCare</a>
        <p class="text-sm mt-2">Your companion for better health.</p>
      </div>

      <!-- Links -->
      <div class="mb-4">
        <a href="/about" class="text-white mx-3 hover:underline">About</a>
        <a href="/contact" class="text-white mx-3 hover:underline">Contact</a>
        <a href="/privacy" class="text-white mx-3 hover:underline">Privacy Policy</a>
        <a href="/terms" class="text-white mx-3 hover:underline">Terms of Use</a>
      </div>

      <!-- Social Media Icons -->
      <div class="mb-3">
        <a href="https://facebook.com" target="_blank" class="text-white mx-2">
          <i class="bi bi-facebook text-xl"></i>
        </a>
        <a href="https://twitter.com" target="_blank" class="text-white mx-2">
          <i class="bi bi-twitter text-xl"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="text-white mx-2">
          <i class="bi bi-instagram text-xl"></i>
        </a>
      </div>

      <!-- Copyright -->
      <div class="mt-3">
        <p class="text-sm text-white">&copy; {{ new Date().getFullYear() }} Women HealthCare. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
};
</script>

<style scoped>
/* Custom Footer Styling */
footer {
  background-color: #f06292; /* Custom pink color */
}
footer a:hover {
  color: #e91e63;
}
footer .bi {
  color: white;
  font-size: 1.5rem;
}
footer .bi:hover {
  color: #e91e63;
}
</style>
