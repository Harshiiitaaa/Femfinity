<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container text-center">
        <h1 class="display-4 text-pink-700 mb-4">Contact Us</h1>
        <p class="lead text-secondary mb-5">
          We’d love to hear from you! Feel free to reach out with any questions, feedback, or messages.
        </p>

        <!-- Contact Form -->
        <section>
          <h2 class="h3 font-weight-bold text-pink-700 mb-4">Send Us a Message</h2>
          <form @submit.prevent="handleSubmit" class="form-container">
            <div class="form-row mb-3">
              <div class="col-md-6">
                <input
                  type="text"
                  v-model="name"
                  class="form-control"
                  placeholder="Your Name"
                  required
                />
              </div>
              <div class="col-md-6">
                <input
                  type="email"
                  v-model="email"
                  class="form-control"
                  placeholder="Your Email"
                  required
                />
              </div>
            </div>
            <div class="form-group mb-3">
              <textarea
                v-model="message"
                class="form-control"
                placeholder="Your Message"
                rows="5"
                required
              ></textarea>
            </div>
            <div class="form-group">
              <button type="submit" class="btn btn-gradient btn-lg px-5 py-2 rounded-pill shadow-sm">
                Send Message
              </button>
            </div>
          </form>
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
  name: "ContactUsPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      name: "",
      email: "",
      message: "",
    };
  },
  methods: {
    handleSubmit() {
      // Here you can handle the form submission (e.g., send it to an email service)
      // For now, we'll just log the data to the console
      const formData = {
        name: this.name,
        email: this.email,
        message: this.message,
      };
      console.log("Form submitted", formData);

      // Reset the form fields after submission
      this.name = "";
      this.email = "";
      this.message = "";
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

.btn-gradient {
  background: linear-gradient(135deg, #f06292, #d63384); /* Pink Gradient */
  color: #ffffff;
}

.btn-gradient:hover {
  background: linear-gradient(135deg, #ec407a, #c2185b); /* Darker Pink Gradient */
  color: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-row {
  display: flex;
  gap: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

textarea {
  border-radius: 8px;
  padding: 0.5rem;
  font-size: 1rem;
  color: #333;
}

input {
  border-radius: 8px;
  padding: 0.5rem;
  font-size: 1rem;
  color: #333;
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }
}
</style>
