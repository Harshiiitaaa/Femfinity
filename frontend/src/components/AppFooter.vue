<template>
  <footer class="bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 text-white py-8 mt-5">
    <div class="container text-center">
      <!-- Logo and Brand Name -->
      <div class="mb-5">
        <a href="/" class="text-4xl font-bold text-white hover:text-pink-300 transition duration-300 ease-in-out">
          Women HealthCare
        </a>
        <p class="text-lg mt-2 text-white opacity-90">Your trusted companion for better health.</p>
      </div>

      <!-- Links -->
      <div class="mb-8">
        <a href="/about" class="text-white mx-4 hover:text-pink-300 transition duration-300 ease-in-out text-lg font-medium no-underline">
          About
        </a>
        <a href="/contact" class="text-white mx-4 hover:text-pink-300 transition duration-300 ease-in-out text-lg font-medium no-underline">
          Contact
        </a>
        <a href="/privacy" class="text-white mx-4 hover:text-pink-300 transition duration-300 ease-in-out text-lg font-medium no-underline">
          Privacy Policy
        </a>
        <a href="/terms" class="text-white mx-4 hover:text-pink-300 transition duration-300 ease-in-out text-lg font-medium no-underline">
          Terms of Use
        </a>
      </div>

      <!-- Social Media Icons -->
      <div class="mb-6">
        <a href="https://facebook.com" target="_blank" class="text-white mx-3 text-2xl hover:text-pink-300 transition duration-300 ease-in-out">
          <i class="bi bi-facebook"></i>
        </a>
        <a href="https://twitter.com" target="_blank" class="text-white mx-3 text-2xl hover:text-pink-300 transition duration-300 ease-in-out">
          <i class="bi bi-twitter"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="text-white mx-3 text-2xl hover:text-pink-300 transition duration-300 ease-in-out">
          <i class="bi bi-instagram"></i>
        </a>
      </div>

      <!-- Copyright -->
      <div class="mt-4">
        <p class="text-sm text-white opacity-80">
          &copy; {{ new Date().getFullYear() }} Women HealthCare. All rights reserved.
        </p>
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
/* Enhanced Footer Styling with Gradient */
footer {
  background: linear-gradient(135deg, #f06292, #9b4d96, #5a3d9d); /* Gradient from pink to purple */
}

/* Remove Underline */
footer a {
  text-decoration: none; /* Removes underline */
}

/* Hover Effects */
footer a:hover {
  color: #e91e63; /* A soft pink color */
}

footer .bi {
  color: white;
  font-size: 2rem;
}

footer .bi:hover {
  color: #e91e63;
}

/* Text Styling */
footer p {
  font-size: 1.125rem;
  font-weight: 300; /* Lighter font for a softer feel */
}

/* Transition Effects for Links */
footer a {
  transition: color 0.3s ease-in-out;
}

footer .bi {
  transition: color 0.3s ease-in-out;
}
</style>
