<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container text-center">
        <h1 class="display-3 text-pink-700 fw-bold mb-4">Get In Touch</h1>
        <p class="lead text-secondary mb-5">
          Have questions, feedback, or just want to say hi? We’re here for you.
        </p>

        <!-- Contact Form Section -->
        <section class="d-flex justify-content-center">
          <div class="form-container">
            <h2 class="h4 text-pink-700 fw-bold mb-4">Send Us a Message</h2>
            <form @submit.prevent="handleSubmit" class="contact-form">
              <div class="row mb-4">
                <div class="col-md-6">
                  <input
                    type="text"
                    v-model="name"
                    class="form-control shadow-sm border-0"
                    placeholder="Your Name"
                    required
                  />
                </div>
                <div class="col-md-6">
                  <input
                    type="email"
                    v-model="email"
                    class="form-control shadow-sm border-0"
                    placeholder="Your Email"
                    required
                  />
                </div>
              </div>
              <div class="form-group mb-4">
                <textarea
                  v-model="message"
                  class="form-control shadow-sm border-0"
                  placeholder="Your Message"
                  rows="6"
                  required
                ></textarea>
              </div>
              <div>
                <button
                  type="submit"
                  class="btn btn-gradient btn-lg px-5 py-3 rounded-pill shadow-lg fw-bold"
                >
                  Send Message
                </button>
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
      const formData = {
        name: this.name,
        email: this.email,
        message: this.message,
      };
      console.log("Form submitted", formData);

      // Reset form fields
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
  background-color: #fff5f8;
}

.text-dark-gray {
  color: #4a4a4a;
}

.text-pink-700 {
  color: #c2185b;
}

.btn-gradient {
  background: linear-gradient(135deg, #f06292, #d63384);
  color: #fff;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.btn-gradient:hover {
  background: linear-gradient(135deg, #ec407a, #c2185b);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
  transform: scale(1.05);
}

.form-container {
  max-width: 700px;
  background-color: #ffffff;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.6s ease-out;
}

.contact-form input,
.contact-form textarea {
  border: none;
  border-radius: 8px;
  padding: 1rem;
  font-size: 1rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.contact-form input:focus,
.contact-form textarea:focus {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  outline: none;
}

textarea {
  resize: none;
}

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

@media (max-width: 768px) {
  .form-container {
    padding: 1.5rem;
  }

  .btn-gradient {
    width: 100%;
  }
}
</style>