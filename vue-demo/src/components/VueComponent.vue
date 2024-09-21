<script setup lang="ts">
import { onMounted, onBeforeUnmount } from 'vue'
import { ReactConnector } from './Connector';
import { Link } from "macp-components";

let reactConnector: ReactConnector | null = null;

onMounted(() => {
  const targetElement = document.getElementById('httpRequestComponent');
  if (targetElement) {
    reactConnector = new ReactConnector(targetElement, Link, {
      children: 'link text',
      href: 'https://www.capitol.ai/',
    });
  }
});

onBeforeUnmount(() => {
  if (reactConnector) {
    reactConnector.unmount();
  }
});
</script>


<template>
  <div id="httpRequestComponent">
      <!-- render react component in here -->
  </div>
</template>
