<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <div v-if="!expanded" class="content-preview">
      <p>{{ contentPreview }}</p>
    </div>
    <div v-else class="full-content">
      <p v-for="(paragraph, index) in content" :key="index">{{ paragraph }}</p>
    </div>
    <div class="card-footer">
      <button @click="toggleExpand" class="expand-btn">
        {{ expanded ? 'Collapse' : 'Expand' }}
      </button>
      <button @click="copyContent" class="copy-btn">Copy</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  title: String,
  content: Array
});

const expanded = ref(false);
const contentPreview = computed(() => {
  return props.content[0].slice(0, 100) + (props.content[0].length > 100 ? '...' : '');
});

function toggleExpand() {
  expanded.value = !expanded.value;
}

function copyContent() {
  const fullContent = props.content.join('\n\n');
  navigator.clipboard.writeText(fullContent).then(() => {
    alert('Content copied to clipboard!');
  });
}
</script>

<style scoped>
.card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  margin-bottom: 20px;
}
h3 {
  margin-top: 0;
  color: #2c3e50;
}
.content-preview, .full-content {
  color: #34495e;
}
.card-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}
button {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.expand-btn {
  background-color: #3498db;
  color: white;
}
.copy-btn {
  background-color: #2ecc71;
  color: white;
}
</style>