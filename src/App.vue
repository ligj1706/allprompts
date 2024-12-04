<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Main content area -->
    <div class="container mx-auto px-4 py-8">
      <header class="text-center mb-8 px-4 sm:px-6">
        <img src="./assets/logo.svg" alt="AllPrompt - Professional AI Prompts Library" class="w-24 sm:w-32 mx-auto mb-4">
        <h1 class="text-3xl sm:text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-700 via-purple-500 to-purple-400 mb-2">AllPrompt</h1>
        <p class="text-lg sm:text-xl bg-clip-text text-transparent bg-gradient-to-r from-purple-600 to-purple-300 px-2">35,000+ Prompts at Your Fingertips: Search, Find, Create!</p>
      </header>

      <!-- Search Bar with semantic markup -->
      <div role="search" aria-label="Search prompts" class="flex flex-col sm:flex-row gap-2 mb-8 px-4 sm:px-0">
        <input 
          type="text" 
          v-model="searchText" 
          @input="handleSearch"
          placeholder="Search prompts..."
          aria-label="Search input"
          class="w-full p-3 rounded-lg border-2 border-gray-300 focus:outline-none focus:border-purple-500"
        >
        <button 
          @click="handleSearch" 
          aria-label="Search button"
          class="w-full sm:w-auto px-6 py-3 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition duration-300"
        >
          Search
        </button>
      </div>

      <!-- Main content grid -->
      <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md">
        <!-- Skeleton loader -->
        <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
          <div v-for="i in 21" :key="i" class="bg-gray-50 p-4 sm:p-6 rounded-lg animate-pulse h-32">
            <div class="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
            <div class="h-4 bg-gray-200 rounded w-1/2"></div>
          </div>
        </div>

        <!-- Prompt cards grid -->
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
          <PromptCard
            v-for="prompt in displayPrompts"
            :key="prompt.id"
            :actor="prompt.actor"
            :prompt="prompt.prompt"
          />
        </div>

        <!-- Pagination -->
        <div class="mt-8 flex flex-col sm:flex-row justify-center items-center gap-2">
          <button 
            @click="prevPage" 
            :disabled="currentPage === 1"
            class="w-full sm:w-auto px-4 py-2 bg-purple-500 text-white rounded-lg disabled:opacity-50 hover:bg-purple-600 transition"
          >
            Previous
          </button>
          <span class="px-4 py-2 bg-gray-50 border border-gray-200 rounded">
            {{ currentPage }} / {{ totalPages }}
          </span>
          <button 
            @click="nextPage" 
            :disabled="currentPage === totalPages"
            class="w-full sm:w-auto px-4 py-2 bg-purple-500 text-white rounded-lg disabled:opacity-50 hover:bg-purple-600 transition"
          >
            Next
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="bg-gradient-to-br from-gray-900 to-gray-800 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12 lg:gap-8">
          <!-- Column 1: Professional AI Prompts -->
          <div>
            <h2 class="text-xl font-bold text-white mb-6">Professional AI Prompts by Industry</h2>
            <ul class="space-y-4">
              <li>
                <a href="https://oceanshell.gumroad.com/l/usbmc" 
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 Essential AI Prompts for the Product Manager
                </a>
              </li>
              <li>
                <a href="https://oceanshell.gumroad.com/l/lqwds"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 Strategic HR Prompts
                </a>
              </li>
              <li>
                <a href="https://oceanshell.gumroad.com/l/ijxwyq"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 Proven Prompts for Teaching Success
                </a>
              </li>
              <li>
                <a href="https://oceanshell.gumroad.com/l/guhqr"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 AI Prompts Digital Marketing Agency Playbook
                </a>
              </li>
              <li>
                <a href="https://oceanshell.gumroad.com/l/sqvhz"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 AI Prompts Content Creator's Success Blueprint
                </a>
              </li>
              <li>
                <a href="https://oceanshell.gumroad.com/l/ftdmbs"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   99 Proven Prompts to Scale Your E-commerce Business
                </a>
              </li>
            </ul>
          </div>

          <!-- Column 2: AI Productivity -->
          <div>
            <h2 class="text-xl font-bold text-white mb-6">AI Productivity Mastery</h2>
            <div class="space-y-4">
              <a href="https://www.amazon.com/dp/B0DHSRTHRQ"
                 class="block text-gray-300 hover:text-purple-400 transition-colors"
                 target="_blank" rel="noopener noreferrer">
                <p class="font-semibold">AI Productivity Mastery</p>
                <p class="text-sm mt-1">The Beginner's Guide to LLM Productivity - Boost Your Work and Study Efficiency Today</p>
              </a>
              
              <a href="https://trigaten.github.io/Prompt_Survey_Site/"
                 class="block text-gray-300 hover:text-purple-400 transition-colors"
                 target="_blank" rel="noopener noreferrer">
                <p class="font-semibold">The Prompt Report</p>
                <p class="text-sm mt-1">Established a structured framework for understanding prompts, including 33 key terms and 58 commonly used prompting techniques.</p>
              </a>
            </div>
          </div>

          <!-- Column 3: More Resources -->
          <div>
            <h2 class="text-xl font-bold text-white mb-6">More Resources</h2>
            <ul class="space-y-4">
              <li>
                <a href="https://platform.openai.com/docs/guides/prompt-engineering"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   OpenAI: Prompt Engineering
                </a>
              </li>
              <li>
                <a href="https://docs.anthropic.com/en/prompt-library/library"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   Anthropic: Prompt Library
                </a>
              </li>
              <li>
                <a href="https://learn.microsoft.com/en-us/ai-builder/prompts-overview"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   Microsoft: Overview of Prompts
                </a>
              </li>
              <li>
                <a href="https://developers.google.com/machine-learning/resources/prompt-eng"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   Google: Prompt Engineering for Generative AI
                </a>
              </li>
              <li>
                <a href="https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"
                   class="text-gray-300 hover:text-purple-400 transition-colors"
                   target="_blank" rel="noopener noreferrer">
                   Deeplearning: ChatGPT Prompt Engineering for Developers
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Bottom Section -->
        <div class="mt-12 pt-8 border-t border-gray-700 flex flex-col sm:flex-row justify-between items-center text-gray-400 text-sm">
          <div class="flex items-center space-x-4 mb-4 sm:mb-0">
            <a href="https://x.com/Yunmengwuji"
               class="hover:text-purple-400 transition-colors"
               target="_blank" rel="noopener noreferrer">
               <span class="sr-only">Twitter</span>
               <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                 <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/>
               </svg>
            </a>
            <span>Contact for collaborations: mscreate358@gmail.com</span>
          </div>
          <p> 2024 AllPrompt - Making AI Accessible</p>
        </div>
      </div>
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
const itemsPerPage = 21; // Default: 7 rows x 3 columns = 21 items per page

const displayPrompts = computed(() => {
  let filtered = searchText.value
    ? prompts.value.filter(p => 
        p.actor.toLowerCase().includes(searchText.value.toLowerCase()) || 
        p.prompt.toLowerCase().includes(searchText.value.toLowerCase())
      )
    : prompts.value;
  
  if (searchText.value) {
    return filtered.slice(0, 9); // Show maximum 9 most relevant results when searching
  }
  
  const start = (currentPage.value - 1) * itemsPerPage;
  return filtered.slice(start, start + itemsPerPage); // Show 21 items per page when not searching
});

const totalPages = computed(() => {
  if (searchText.value) {
    return 1; // Single page for search results
  }
  return Math.ceil(prompts.value.length / itemsPerPage); // Multiple pages for normal browsing
});

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

function prevPage() {
  if (currentPage.value > 1) currentPage.value--;
}

function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++;
}

async function loadPrompts() {
  try {
    const response = await fetch('./data/prompts.json');
    const data = await response.json();
    prompts.value = data;
    loading.value = false;
    updateMetaTags();
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
/* Base styles remain unchanged */
</style>