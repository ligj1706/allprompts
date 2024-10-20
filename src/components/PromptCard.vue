<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h3 class="text-xl font-bold mb-2 text-gray-800">{{ actor }}</h3>
    <p class="text-gray-600" :class="{ 'line-clamp-3': !expanded && isLongContent }">
      {{ formattedPrompt }}
    </p>
    <div class="mt-4 flex justify-between items-center">
      <button 
        v-if="isLongContent"
        @click="toggleExpand" 
        class="text-purple-500 hover:text-purple-700 transition duration-300"
      >
        {{ expanded ? 'Collapse' : 'Expand' }}
      </button>
      <div v-else></div> <!-- 占位，保持布局一致 -->
      <button 
        @click="copyPrompt" 
        class="w-10 h-10 rounded-full flex items-center justify-center transition duration-300"
        :class="[
          copied ? 'bg-green-500' : 'bg-purple-500 hover:bg-purple-600'
        ]"
      >
        <svg v-if="copied" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  actor: String,
  prompt: String
});

const expanded = ref(false);
const copied = ref(false);
const maxLength = 200; // 设置一个阈值，超过这个长度的内容才会被折叠

const formattedPrompt = computed(() => {
  return props.prompt.replace(/\\n/g, '\n');
});

const isLongContent = computed(() => {
  return formattedPrompt.value.length > maxLength;
});

function toggleExpand() {
  expanded.value = !expanded.value;
}

function copyPrompt() {
  navigator.clipboard.writeText(props.prompt).then(() => {
    copied.value = true;
    setTimeout(() => {
      copied.value = false;
    }, 1000); // 1秒后恢复按钮状态
  });
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>