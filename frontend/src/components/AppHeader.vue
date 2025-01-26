<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500">
    <div class="container-fluid">
      <!-- Logo and Brand Name -->
      <a class="navbar-brand text-white text-3xl font-bold" href="/">
        <i class="bi bi-heart-fill"></i> Women HealthCare
      </a>

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
            <a
              class="nav-link text-white hover:text-pink-300 transition duration-300 ease-in-out"
              href="/about-us"
            >
              <i class="bi bi-info-circle"></i> About Us
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link text-white hover:text-pink-300 transition duration-300 ease-in-out"
              href="/community"
            >
              <i class="bi bi-people"></i> Community
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link text-white hover:text-pink-300 transition duration-300 ease-in-out"
              href="/contact-us"
            >
              <i class="bi bi-envelope"></i> Contact Us
            </a>
          </li>

          <!-- Login/Register links -->
          <li class="nav-item ms-auto">
            <a
              class="nav-link text-white hover:text-pink-300 transition duration-300 ease-in-out"
              href="/login"
            >
              <i class="bi bi-box-arrow-in-right"></i> Login/Register
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "AppHeader",
};
</script>

<style scoped>
/* Custom navbar styling */
.navbar {
  background: linear-gradient(135deg, #f06292, #9b4d96, #5a3d9d); /* Gradient from pink to purple */
  padding: 0.8rem 1rem; /* Adjust padding for a more compact navbar */
}

/* Custom Toggler Icon Color */
.navbar-toggler-icon {
  background-color: white;
}

/* Reduced font size for navbar links */
.navbar-nav .nav-link {
  color: white;
  font-size: 1rem; /* Reduced font size */
  font-weight: 500; /* Slightly bolder links */
  display: flex;
  align-items: center;
}

.navbar-nav .nav-link i {
  margin-right: 8px; /* Space between icon and text */
}

.navbar-nav .nav-link:hover {
  color: #e91e63; /* Hover color for links */
  text-decoration: underline; /* Underline effect on hover */
  transform: scale(1.05); /* Slight zoom effect on hover */
}

/* Responsive Navbar Styles */
@media (max-width: 991px) {
  .navbar-nav .nav-link {
    font-size: 0.9rem; /* Adjust font size for smaller screens */
  }
}

/* Transition Effects */
.navbar-nav .nav-link,
.navbar-toggler-icon {
  transition: color 0.3s ease, transform 0.3s ease;
}
</style>
