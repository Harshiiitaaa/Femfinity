<template>
  <div class="d-flex justify-content-center align-items-center vh-100 bg-gradient">
    <div class="card p-4 shadow-lg" style="width: 28rem;">
      <h2 class="text-center mb-4 text-primary">Login</h2>
      <form>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            id="email"
            class="form-control"
            placeholder="Enter your email"
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            id="password"
            class="form-control"
            placeholder="Enter your password"
          />
        </div>
        <button type="submit" class="btn btn-primary w-100">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
};
</script>

<style scoped>
.bg-gradient {
  background: linear-gradient(135deg, #f06292, #9b4d96, #5a3d9d);
}
</style>