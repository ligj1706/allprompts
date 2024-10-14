<template>
  <div class="container mx-auto px-4 py-8 bg-gray-100 min-h-screen">
    <header class="text-center mb-8">
      <img src="./assets/logo.svg" alt="AllPrompt Logo" class="w-40 mx-auto mb-4">
      <h1 class="text-4xl font-bold text-gray-800 mb-2">AllPrompt</h1>
      <p class="text-xl text-gray-600">Find top prompts and boost your creativity!</p>
    </header>

    <div class="search-container mb-8">
      <input 
        type="text" 
        v-model="searchText" 
        @input="handleSearch"
        placeholder="Search prompts..."
        class="w-full p-3 rounded-l-lg border-2 border-gray-300 focus:outline-none focus:border-purple-500"
      >
      <button @click="handleSearch" class="bg-purple-500 text-white p-3 rounded-r-lg hover:bg-purple-600 transition duration-300">
        Search
      </button>
    </div>

    <!-- Skeleton loader -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="i in 9" :key="i" class="bg-white p-6 rounded-lg shadow-md animate-pulse">
        <div class="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
        <div class="h-4 bg-gray-200 rounded w-1/2"></div>
      </div>
    </div>

    <!-- Prompt cards -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <PromptCard
        v-for="prompt in displayPrompts"
        :key="prompt.id"
        :actor="prompt.actor"
        :prompt="prompt.prompt"
      />
    </div>

    <div class="pagination mt-8 flex justify-center items-center">
      <button 
        @click="prevPage" 
        :disabled="currentPage === 1"
        class="px-4 py-2 bg-purple-500 text-white rounded-l-lg disabled:opacity-50"
      >
        Previous
      </button>
      <span class="px-4 py-2 bg-white">{{ currentPage }} / {{ totalPages }}</span>
      <button 
        @click="nextPage" 
        :disabled="currentPage === totalPages"
        class="px-4 py-2 bg-purple-500 text-white rounded-r-lg disabled:opacity-50"
      >
        Next
      </button>
    </div>

    <footer class="mt-12 text-center text-gray-600">
      <p>
        Prompts sourced from public domain. For copyright inquiries or contributions, contact: mscreate358@gmail.com
      </p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import PromptCard from './components/PromptCard.vue';

const prompts = ref([]);
const loading = ref(true);
const searchText = ref('');
const currentPage = ref(1);
const itemsPerPage = 30; // Keep original value

const displayPrompts = computed(() => {
  let filtered = searchText.value
    ? prompts.value.filter(p => 
        p.actor.toLowerCase().includes(searchText.value.toLowerCase()) || 
        p.prompt.toLowerCase().includes(searchText.value.toLowerCase())
      )
    : prompts.value;
  
  if (searchText.value) {
    return filtered.slice(0, 9);
  }
  
  const start = (currentPage.value - 1) * itemsPerPage;
  return filtered.slice(start, start + itemsPerPage);
});

const totalPages = computed(() => 
  Math.ceil(prompts.value.length / itemsPerPage)
);

const updateMetaTags = () => {
  const startIndex = (currentPage.value - 1) * itemsPerPage + 1;
  const endIndex = Math.min(startIndex + itemsPerPage - 1, prompts.value.length);
  
  document.title = `AI Prompts Page ${currentPage.value} | AllPrompt`;
  
  const descriptionMeta = document.querySelector('meta[name="description"]');
  if (descriptionMeta) {
    descriptionMeta.setAttribute('content', `Explore AI prompts ${startIndex}-${endIndex} out of ${prompts.value.length}. Find the perfect prompt for your AI project on AllPrompt.`);
  }
};

watch(currentPage, updateMetaTags);
onMounted(() => {
  loadPrompts().then(updateMetaTags);
});

function prevPage() {
  if (currentPage.value > 1) currentPage.value--;
}

function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++;
}

async function loadPrompts() {
  try {
    const response = await fetch('/data/prompts.json'); // Keep original path
    const allPrompts = await response.json();
    prompts.value = allPrompts.slice(0, 300); // Load first 300 prompts initially
    loading.value = false;

    // Load the rest of the prompts after a delay
    setTimeout(() => {
      prompts.value = allPrompts;
    }, 2000);
  } catch (error) {
    console.error('Failed to load prompts:', error);
    loading.value = false;
  }
}

function handleSearch() {
  currentPage.value = 1;
}

onMounted(() => {
  loadPrompts();
});
</script>

<style scoped>
.search-container {
  display: flex;
}

.search-container input {
  flex-grow: 1;
}

.search-container button {
  white-space: nowrap;
}
</style>