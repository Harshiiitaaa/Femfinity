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
                <option value="under 18">Under 18</option>
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
                <option value="below 5'0&quot; (152 cm)">Below 5'0&quot; (152 cm)</option>
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
                <option value="below 40 kg">Below 40 kg</option>
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
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="sometimes">Sometimes</option>
                <option value="often">Often</option>
                <option value="always">Always</option>
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
                <option value="less than 1 hour">Less than 1 hour</option>
                <option value="1 - 2 hours">1 - 2 hours</option>
                <option value="3 - 4 hours">3 - 4 hours</option>
                <option value="5 - 6">5 - 6 hours</option>
                <option value="more than 6 hours">More than 6 hours</option>

              </select>
            </div>

            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">How often do you compare your appearance to others on social media or in real life?</label>
              <select
                class="form-select"
                v-model="form.socialMediaCompare"
                required>
                <option value="" disabled selected>Select an option</option>
                <option value="never">Never</option>
                <option value="rarely">Rarely</option>
                <option value="sometimes">Sometimes</option>
                <option value="often">Often</option>
                <option value="always">Always</option>

              </select>
            </div>

            <!-- Question 7 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">How often do you work out?</label>
              <select
                class="form-select"
                v-model="form.workoutFrequency"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="never">Never</option>
                <option value="less than once a week">Less than once a week</option>
                <option value="1 - 2 times a week">1 - 2 times a week</option>
                <option value="3 - 4 times a week">3 - 4 times a week</option>
                <option value="5 times or more times a week">5 times or more times a week</option>
                
              </select>
            </div>

            <!-- Question 8 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">Do you follow a specific diet?</label>
              <select
                class="form-select"
                v-model="form.diet"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="no, I don't follow any specific diet">No, I don't follow any specific diet</option>
                <option value="yes, a balanced diet">Yes, a balanced diet</option>
                <option value="yes, a vegetarian or vegan diet">Yes, a vegetarian or vegan diet</option>
                <option value="yes, a weight loss or restrictive diet">Yes, a weight loss or restrictive diet</option>
              </select>
            </div>

            <!-- Question 9 -->
            <div class="form-group mb-4">
              <label class="form-label text-dark-gray">Do you feel the need for validation from others?</label>
              <select
                class="form-select"
                v-model="form.validationNeed"
                required
              >
                <option value="" disabled selected>Select an option</option>
                <option value="yes, I feel the need for validation frequently">Yes, I feel the need for validation frequently</option>
                <option value="sometimes, I seek validation from others">Sometimes, I seek validation from others</option>
                <option value="no, I do not feel the need for validation">No, I do not feel the need for validation</option>
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
import instance from '@/axios.js';
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
    async submitForm() {
      try {
        // Prepare the data to send to the backend
        const formData = {
          "what's your age?": [this.form.age],
          "what's your height?": [this.form.height],
          "what's your weight range?": [this.form.weight],
          "how often do you worry about your body image?": [this.form.bodyImageWorry],
          "how many hours do you spend on social media each day?": [this.form.socialMediaHours],
          "how often do you compare your appearance to others on social media or in real life?": [this.form.workoutFrequency],
          "do you work out regularly?": [this.form.diet],
          "do you follow a specific diet?": [this.form.validationNeed],
          "do you feel that you need validation in your life?": [this.form.validationNeed],
        };

        // Show analyzing message
        this.score = "Analyzing...";

        console.log(formData)

        // Send the data to the backend
        const response = await instance.post("predict", formData);
        console.log(response)
        // Update the score based on the response
        this.score = response.data.prediction || "Error calculating score";
      } catch (error) {
        console.error("Error:", error);
        this.score = "Error in prediction";
      }},
  },
};
</script>

<style scoped>
/* Color Palette */
.bg-light-pink {
  background: linear-gradient(to bottom right, #fff5f8, #ffe0ec);
}

.text-dark-gray {
  color: #4a4a4a;
}

.text-dark-pink {
  color: #d63384;
}

.text-secondary {
  color: #6c757d;
}

/* Form Section */
.about-us-header {
  margin-bottom: 2rem; /* Reduced spacing */
  text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.about-us-header h1 {
  font-size: 2.4rem; /* Smaller header font size */
  font-weight: 700;
}

.about-us-header p {
  font-size: 1rem; /* Smaller paragraph font size */
  line-height: 1.4; /* Adjusted line height */
}

.form-section {
  margin-top: 2rem; /* Reduced margin */
  padding: 2rem; /* Reduced padding */
  background: #ffffff;
  border-radius: 12px; /* Slightly smaller radius */
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease-in-out;
}

.form-section:hover {
  transform: translateY(-3px); /* Slight hover effect */
}

.form-group {
  margin-bottom: 1rem; /* Reduced spacing between form groups */
}

.form-control,
.form-select {
  border: 1px solid #ddd;
  border-radius: 8px; /* Smaller border radius */
  padding: 0.6rem; /* Reduced padding */
  font-size: 0.9rem; /* Smaller font size */
  transition: all 0.3s ease;
}

.form-control:focus,
.form-select:focus {
  border-color: #d63384;
  box-shadow: 0 0 4px rgba(214, 51, 132, 0.4); /* Softer shadow */
  outline: none;
}

/* Buttons */
.btn-dark-pink {
  background: linear-gradient(to right, #d63384, #f776ad);
  color: white;
  border: none;
  border-radius: 20px; /* Slightly smaller radius */
  padding: 0.6rem 1rem; /* Reduced button size */
  font-size: 0.9rem; /* Smaller font size */
  font-weight: bold;
  transition: background 0.3s ease, transform 0.2s ease;
}

.btn-dark-pink:hover {
  background: linear-gradient(to right, #c12675, #e65a97);
  transform: scale(1.03); /* Slightly reduced hover scale */
}

/* Score Display Section */
.score-display {
  margin-top: 1.5rem; /* Reduced margin */
  padding: 1.5rem; /* Reduced padding */
  background: #ffe0ec;
  border-radius: 15px; /* Smaller radius */
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.score-display:hover {
  transform: translateY(-3px);
}

.score-display h3 {
  font-size: 2.5rem; /* Reduced font size */
  font-weight: bold;
  color: #d63384;
  text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

/* Animations */
.fadeInUp {
  animation: fadeInUp 0.8s ease-out;
}

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

/* Responsive Adjustments */
@media (max-width: 768px) {
  .about-us-header h1 {
    font-size: 2rem; /* Smaller header font size for mobile */
  }

  .btn-dark-pink {
    padding: 0.5rem 0.9rem; /* Reduced button size for mobile */
    font-size: 0.85rem; /* Smaller font size */
  }
}
</style>
