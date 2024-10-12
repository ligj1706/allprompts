<template>
  <div class="container">
    <h1>All Prompts</h1>
    <input 
      v-model="searchText" 
      @input="handleSearch"
      placeholder="搜索提示词..."
      class="search-input"
    />
    <div class="cards-container">
      <PromptCard
        v-for="prompt in displayPrompts"
        :key="prompt.id"
        :actor="prompt.actor"
        :prompt="prompt.prompt"
      />
    </div>
    <div v-if="loading" class="loading">加载中...</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import PromptCard from './components/PromptCard.vue';

const prompts = ref([]);
const displayPrompts = ref([]);
const loading = ref(false);
const searchText = ref('');
const currentChunk = ref(0);
const totalChunks = ref(0);

async function init() {
  try {
    const response = await fetch('data/index.json');
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
    const response = await fetch(`data/chunk_${currentChunk.value}.json`);
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
      p.actor.toLowerCase().includes(search) || 
      p.prompt.toLowerCase().includes(search)
    )
    .slice(0, 42);
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
.search-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
}
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
.loading {
  text-align: center;
  margin-top: 20px;
}
</style>