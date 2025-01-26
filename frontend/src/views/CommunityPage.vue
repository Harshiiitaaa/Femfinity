<template>
  <div>
    <!-- Header -->
    <AppHeader />

    <div class="community-forum">
      <!-- Header Section -->
      <div class="header">
        <h1 class="page-heading">Femfinity Community Forum</h1>
        <div class="stats">
          <div class="stat-card">
            <h2>{{ healthData.totalUsers }}</h2>
            <p>Active Users</p>
          </div>
          <div class="stat-card">
            <h2>{{ healthData.totalPosts }}</h2>
            <p>Total Posts</p>
          </div>
          <div class="stat-card">
            <h2>{{ healthData.totalCommunities }}</h2>
            <p>Communities</p>
          </div>
        </div>
      </div>

      <!-- Charts Section -->
      <div class="charts">
        <div class="chart">
          <h2>Activity Over Time</h2>
          <canvas id="activityChart"></canvas>
        </div>
        <div class="chart">
          <h2>Community Engagement</h2>
          <canvas id="engagementChart"></canvas>
        </div>
      </div>

      <!-- Activities Section -->
      <div class="activities">
        <h2>Latest Activities</h2>
        <ul>
          <li v-for="(activity, index) in healthData.latestActivities" :key="index">
            {{ activity }}
          </li>
        </ul>
      </div>
    </div>

    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";

// Register all required components
Chart.register(...registerables);

export default {
  name: "CommunityForum",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      healthData: {
        totalUsers: 1200,
        totalPosts: 450,
        totalCommunities: 20,
        latestActivities: [
          "User A posted in Nutrition Tips",
          "User B started a discussion on Mental Health",
          "User C shared a success story in Fitness Goals",
          "User D joined the Self-Care Community",
        ],
        activityData: [50, 100, 150],
        engagementData: [20, 30, 40],
      },
    };
  },
  methods: {
    createCharts() {
      // Activity Chart
      const activityCtx = document.getElementById("activityChart").getContext("2d");
      new Chart(activityCtx, {
        type: "line",
        data: {
          labels: ["Jan", "Feb", "Mar"], // Reduced to 3 data points
          datasets: [
            {
              label: "Active Users",
              data: this.healthData.activityData,
              backgroundColor: "rgba(240, 82, 146, 0.2)",
              borderColor: "#ec407a",
              borderWidth: 2,
              tension: 0.3, // Smooth the lines
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: true, // Ensures the chart scales with the container
          plugins: {
            legend: {
              position: "top", // Position the legend at the top
            },
          },
          layout: {
            padding: 10, // Add padding for better spacing
          },
          scales: {
            x: {
              title: {
                display: true,
                text: "Months",
                font: { size: 12 },
              },
            },
            y: {
              title: {
                display: true,
                text: "Number of Active Users",
                font: { size: 12 },
              },
              beginAtZero: true,
            },
          },
        },
      });

      // Engagement Chart
      const engagementCtx = document.getElementById("engagementChart").getContext("2d");
      new Chart(engagementCtx, {
        type: "bar",
        data: {
          labels: ["Jan", "Feb", "Mar"], // Reduced to 3 data points
          datasets: [
            {
              label: "Engagement",
              data: this.healthData.engagementData,
              backgroundColor: "rgba(240, 82, 146, 0.5)", // Updated to theme color
              borderColor: "#ec407a", // Updated to theme color
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: "top", // Position the legend at the top
            },
          },
          layout: {
            padding: 10, // Add padding for better spacing
          },
          scales: {
            x: {
              title: {
                display: true,
                text: "Months",
                font: { size: 12 },
              },
            },
            y: {
              title: {
                display: true,
                text: "Engagement Level",
                font: { size: 12 },
              },
              beginAtZero: true,
            },
          },
        },
      });
    },
  },
  mounted() {
    this.createCharts(); // Call createCharts method when the component is mounted
  },
};
</script>

<style scoped>
/* Base styles for the community forum */
.community-forum {
  animation: fadeIn 0.8s ease-in-out;
  background-color: #fff5f8; /* Updated to match the theme */
  min-height: 100vh;
  padding: 2rem;
  display: grid;
  gap: 2rem;
}

/* Header styles */
.header {
  animation: slideIn 0.6s ease-in-out;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.page-heading {
  color: #c2185b; /* Theme color for the heading */
  font-size: 2.5rem;
  font-weight: bold;
}

.stats {
  display: flex;
  gap: 1.5rem;
}

.stat-card {
  padding: 1rem 2rem;
  background-color: white;
  text-align: center;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.stat-card:hover {
  transform: scale(1.05);
}

.stat-card h2 {
  color: #c2185b; /* Theme color for stats */
  font-size: 1.5rem;
  font-weight: bold;
}

/* Chart container styles */
.charts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.chart {
  background-color: #ffffff;
  padding: 1rem;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  animation: fadeIn 1s ease-in-out;
}

.chart h2 {
  color: #374151;
  margin-bottom: 1rem;
  font-size: 1.25rem;
  font-weight: bold;
}

/* Activities Section */
.activities {
  background-color: #ffffff;
  padding: 1rem;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  animation: fadeIn 1.2s ease-in-out;
}

.activities h2 {
  color: #374151;
  margin-bottom: 1rem;
  font-size: 1.5rem;
  font-weight: bold;
}

.activities ul {
  list-style: none;
  padding: 0;
}

.activities li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #e5e7eb;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.activities li:hover {
  background-color: #f0f4f8;
  transform: translateY(-4px);
}

/* Animation keyframes */
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

@keyframes slideIn {
  from {
    transform: translateX(-20px);
  }
  to {
    transform: translateX(0);
  }
}

.chart canvas {
  max-height: 200px; /* Set a maximum height */
}

/* Responsive layout */
@media (max-width: 768px) {
  .stats {
    flex-direction: column;
  }

  .charts {
    grid-template-columns: 1fr;
  }
}
</style>