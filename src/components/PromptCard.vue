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
        :class="[
          'px-4 py-2 rounded transition duration-300',
          copied ? 'bg-gray-400 text-white' : 'bg-purple-500 text-white hover:bg-purple-600'
        ]"
      >
        {{ copied ? 'Copied!' : 'Copy' }}
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
    }, 300); // 300豪秒后恢复按钮状态
  });
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 修改为 5 行 */
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>