<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-pink-500">
    <div class="container-fluid">
      <!-- Logo and Brand Name -->
      <a class="navbar-brand text-white" href="/">Women HealthCare</a>

      <!-- Toggler for small screens -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navbar Links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link text-white" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="/features">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="/community">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white" href="/contact">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppHeader',
};
</script>

<style scoped>
/* Custom styles for AppHeader */
.navbar {
  background-color: #f06292;
}
.navbar-toggler-icon {
  background-color: white;
}
.navbar-nav .nav-link {
  color: white;
}
.navbar-nav .nav-link:hover {
  color: #e91e63;
}
</style>
