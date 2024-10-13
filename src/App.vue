<template>
  <div class="container">
    <div class="header">
      <img :src="logoPath" alt="AllPrompts Logo" class="logo">
      <h1>AllPrompts</h1>
    </div>
    <input 
      v-model="searchText" 
      @input="handleSearch"
      placeholder="Search prompts..."
      class="search-input"
    />
    <div class="cards-container">
      <PromptCard
        v-for="prompt in displayPrompts"
        :key="prompt.id"
        :title="prompt.title"
        :content="prompt.content"
      />
    </div>
    <div v-if="loading" class="loading">Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import PromptCard from './components/PromptCard.vue';

const prompts = ref([]);
const displayPrompts = ref([]);
const loading = ref(false);
const searchText = ref('');
const currentChunk = ref(0);
const totalChunks = ref(0);

const basePath = import.meta.env.MODE === 'production' ? '/allprompts/' : '/';
const logoPath = computed(() => `${basePath}assets/logo.svg`);

async function init() {
  try {
    const response = await fetch(`${basePath}data/index.json`);
    const data = await response.json();
    totalChunks.value = data.totalChunks;
    loadNextChunk();
  } catch (error) {
    console.error('Failed to load index:', error);
  }
}

async function loadNextChunk() {
  if (loading.value || currentChunk.value >= totalChunks.value) return;
  
  loading.value = true;
  try {
    const response = await fetch(`${basePath}data/chunk_${currentChunk.value}.json`);
    const data = await response.json();
    prompts.value = [...prompts.value, ...data];
    if (!searchText.value) {
      displayPrompts.value = prompts.value;
    }
    currentChunk.value++;
  } catch (error) {
    console.error('Failed to load chunk:', error);
  }
  loading.value = false;
}

function handleSearch() {
  const search = searchText.value.toLowerCase();
  displayPrompts.value = prompts.value
    .filter(p => 
      p.title.toLowerCase().includes(search) || 
      p.content.some(paragraph => paragraph.toLowerCase().includes(search))
    )
    .slice(0, 7);  // 只显示最相关的7条结果
}

function handleScroll() {
  if (
    window.innerHeight + window.scrollY >= 
    document.body.offsetHeight - 500
  ) {
    loadNextChunk();
  }
}

onMounted(() => {
  init();
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
.header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.logo {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
h1 {
  color: #2c3e50;
}
.search-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.cards-container {
  display: flex;
  flex-direction: column;
}
.loading {
  text-align: center;
  margin-top: 20px;
  color: #7f8c8d;
}
</style>