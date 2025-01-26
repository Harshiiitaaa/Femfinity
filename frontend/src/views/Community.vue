<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <!-- Main Content -->
    <main class="min-vh-100 bg-light-pink text-dark-gray py-5">
      <div class="container">
        <!-- Community Header -->
        <div class="community-header text-center fadeInUp">
          <h1 class="display-4 text-dark-pink mb-4">Healthy Minds Community</h1>
          <p class="lead text-secondary mb-5" style="animation-delay: 0.3s;">
            Join the conversation, share your thoughts, and learn from others. Together, we grow!
          </p>
        </div>

        <!-- Interaction Section (Chat-like) -->
        <section class="interaction-section">
          <div class="message-box">
            <!-- Displaying Messages -->
            <div class="message fadeInUp" v-for="(message, index) in messages" :key="index">
              <div class="message-user">
                <strong class="user-name">{{ message.username }}</strong>
                <span class="message-time">{{ message.time }}</span>
              </div>
              <p class="message-text">{{ message.text }}</p>
            </div>

            <!-- Input Box for New Messages -->
            <div class="input-box fadeInUp">
              <input
                type="text"
                v-model="newMessage"
                class="form-control"
                placeholder="Type your message..."
                @keyup.enter="sendMessage"
              />
              <button class="btn btn-gradient" @click="sendMessage">Send</button>
            </div>
          </div>
        </section>

        <!-- Visualization Section -->
        <section class="visualization-section mt-5">
          <h2 class="text-dark-pink mb-3 fadeInUp">Community Health Data</h2>
          <div class="chart-container">
            <canvas id="myChart" class="fadeInUp"></canvas>
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
import { Chart } from "chart.js"; // Importing Chart.js

export default {
  name: "InteractionPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      newMessage: "", // For storing new messages
      messages: [
        { username: "Alice", text: "Hey everyone! How’s your day going?", time: "2 mins ago" },
        { username: "Bob", text: "It's great, just learning about AI applications in health.", time: "5 mins ago" },
        { username: "Charlie", text: "Looking forward to learning more about AI here!", time: "10 mins ago" },
      ], // Simulating a few initial messages
    };
  },
  mounted() {
    this.createChart(); // Create the chart when the component is mounted
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        // Simulate sending the message by adding it to the messages array
        this.messages.push({
          username: "You",
          text: this.newMessage,
          time: "Just now",
        });
        this.newMessage = ""; // Clear the input after sending
      }
    },
    createChart() {
      const ctx = document.getElementById("myChart").getContext("2d");
      new Chart(ctx, {
        type: "line", // Line chart to display health data
        data: {
          labels: ["January", "February", "March", "April", "May", "June"],
          datasets: [
            {
              label: "Health Score",
              data: [65, 59, 80, 81, 56, 55],
              borderColor: "rgba(236, 64, 122, 1)", // Pink border for the line
              fill: false,
              tension: 0.1,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
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

/* Community Header */
.community-header {
  margin-bottom: 2rem;
  animation-duration: 1s;
}

.community-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
}

.community-header p {
  font-size: 1.25rem;
}

/* Styling for the message section */
.interaction-section {
  max-width: 900px;
  margin: 0 auto;
}

.message-box {
  background-color: #fff;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  animation-duration: 1s;
}

.message {
  margin-bottom: 1.5rem;
  background-color: #f3f4f7;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.message-user {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
  color: #ec407a;
}

.message-time {
  font-size: 0.85rem;
  color: #6c6c6c;
}

.message-text {
  margin-top: 0.5rem;
  font-size: 1rem;
  color: #333;
}

.input-box {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

.input-box input {
  width: 80%;
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 10px;
  border: 1px solid #ccc;
}

.input-box button {
  padding: 0.75rem 2rem;
  font-size: 1rem;
  border-radius: 50px;
  background-color: #f06292;
  color: white;
  border: none;
  cursor: pointer;
}

.input-box button:hover {
  background-color: #d63384;
}

/* Styling for the chart container */
.visualization-section {
  max-width: 900px;
  margin: 0 auto;
}

.chart-container {
  position: relative;
  height: 400px;
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
  .input-box button {
    padding: 0.75rem 1.5rem;
  }
}
</style>