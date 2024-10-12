<template>
  <div class="card">
    <h3>{{ actor }}</h3>
    <p>{{ prompt }}</p>
  </div>
</template>

<script setup>
defineProps({
  actor: String,
  prompt: String
})
</script>

<style scoped>
.card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
h3 {
  margin-top: 0;
}
</style>