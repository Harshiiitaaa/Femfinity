<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
     <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container">
        <!-- Form Header -->
        <section class="about-us-header text-center">
          <h1 class="display-4 text-dark-pink mb-4 fadeInUp">Self-Esteem Assessment</h1>
          <p class="lead text-secondary mb-5 fadeInUp" style="animation-delay: 0.3s;">
            Answer a few questions to evaluate your self-esteem. Your responses will remain confidential.
          </p>
        </section>

        <!-- Form Section -->
        <section class="form-section bg-white p-4 rounded shadow-lg">
          <form @submit.prevent="submitForm">
            <!-- Question 1 -->
            <div class="form-group mb-4">
              <label for="age" class="form-label text-dark-gray">What's your age?</label>
              <select id="age" class="form-select" v-model="form.age" required>
                <option value="" disabled selected>Select your age range</option>
                <option value="Under 18">Under 18</option>
                <option value="18 - 24">18 - 24</option>
                <option value="25 - 34">25 - 34</option>
                <option value="35 - 44">35 - 44</option>
              </select>
            </div>

            <!-- Question 2 -->
            <div class="form-group mb-4">
              <label for="height" class="form-label text-dark-gray">What's your height?</label>
              <select id="height" class="form-select" v-model="form.height" required>
                <option value="" disabled selected>Select your height range</option>
                <option value="Below 5'0&quot; (152 cm)">Below 5'0&quot; (152 cm)</option>
                <option value="5'0&quot; - 5'5&quot; (152 - 165 cm)">5'0&quot; - 5'5&quot; (152 - 165 cm)</option>
                <option value="5'6&quot; - 5'10&quot; (167 - 178 cm)">5'6&quot; - 5'10&quot; (167 - 178 cm)</option>
                <option value="5'11&quot; and above (179+ cm)">5'11&quot; and above (179+ cm)</option>
              </select>
            </div>

            <!-- Question 3 -->
            <div class="form-group mb-4">
              <label for="weight" class="form-label text-dark-gray">What's your weight range?</label>
              <select id="weight" class="form-select" v-model="form.weight" required>
                <option value="" disabled selected>Select your weight range</option>
                <option value="Below 40 kg">Below 40 kg</option>
                <option value="40 - 50 kg">40 - 50 kg</option>
                <option value="51 - 60 kg">51 - 60 kg</option>
                <option value="61 - 70 kg">61 - 70 kg</option>
                <option value="71 kg and above">71 kg and above</option>
              </select>
            </div>

            <!-- Question 4 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">How often do you worry about your body image?</label>
              <select
                class="form-select"
                v-model="form.bodyImageWorry"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="Never">Never</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Always">Always</option>
              </select>
            </div>

            <!-- Question 5 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">How many hours do you spend on social media each day?</label>
              <select
                class="form-select"
                v-model="form.socialMediaHours"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="Never">Never</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Always">Always</option>
              </select>
            </div>

            <!-- Question 6 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">How often do you work out?</label>
              <select
                class="form-select"
                v-model="form.workoutFrequency"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="Never">Never</option>
                <option value="Less than once a week">Less than once a week</option>
                <option value="1 - 2 times a week">1 - 2 times a week</option>
                <option value="3 - 4 times a week">3 - 4 times a week</option>
                <option value="5 or more times a week">5 or more times a week</option>
              </select>
            </div>

            <!-- Question 7 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">Do you follow a specific diet?</label>
              <select
                class="form-select"
                v-model="form.diet"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="No, I don't follow any specific diet">No, I don't follow any specific diet</option>
                <option value="Yes, a balanced diet">Yes, a balanced diet</option>
                <option value="Yes, a vegetarian or vegan diet">Yes, a vegetarian or vegan diet</option>
                <option value="Yes, a weight loss or restrictive diet">Yes, a weight loss or restrictive diet</option>
              </select>
            </div>

            <!-- Question 8 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">Do you feel the need for validation from others?</label>
              <select
                class="form-select"
                v-model="form.validationNeed"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="Yes, I feel the need for validation frequently">Yes, I feel the need for validation frequently</option>
                <option value="Sometimes, I seek validation from others">Sometimes, I seek validation from others</option>
                <option value="No, I do not feel the need for validation">No, I do not feel the need for validation</option>
                <option value="I am indifferent about validation">I am indifferent about validation</option>
              </select>
            </div>

            <!-- Submit Button -->
            <div class="text-center">
              <button type="submit" class="btn btn-dark-pink px-4 py-2 rounded">
                Submit
              </button>
            </div>
          </form>
        </section>

        <!-- Result Section -->
        <section class="result-section mt-5 text-center fadeInUp">
          <h2 class="text-dark-pink">Self-Esteem Score</h2>
          <p class="lead text-secondary mb-4">
            Your self-esteem score based on your responses:
          </p>
          <div class="score-display bg-white p-4 rounded shadow-lg">
            <h3 class="text-dark-pink">{{ score }}</h3>
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
  name: "SelfEsteemForm",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      form: {
        age: "",
        height: "",
        weight: "",
        bodyImageWorry: "",
        socialMediaHours: "",
        workoutFrequency: "",
        diet: "",
        validationNeed: "",
      },
      score: "Pending Analysis", // Initial score placeholder
    };
  },
  methods: {
    submitForm() {
      // Placeholder: Logic to calculate or fetch score from ML model
      this.score = "Analyzing..."; // Update with dynamic result after integrating ML
      setTimeout(() => {
        this.score = "85"; // Example score after calculation
      }, 2000); // Simulate a delay for analysis
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

/* Form Section */
.about-us-header {
  margin-bottom: 3rem;
}

.about-us-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.about-us-header p {
  font-size: 1.25rem;
}

.form-section {
  margin-top: 3rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-control {
  border-radius: 5px;
  padding: 0.75rem;
}

.btn-dark-pink {
  background-color: #d63384;
  border-color: #d63384;
}

.btn-dark-pink:hover {
  background-color: #c12675;
  border-color: #c12675;
}

/* Score Display Section */
.score-display h2 {
  font-size: 2rem;
}

.score-display p {
  font-size: 1.25rem;
}

.score-display h3 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #d63384;
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
  .form-group {
    margin-bottom: 1rem;
  }
}
</style>