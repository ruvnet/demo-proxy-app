<script setup lang="ts">
import { reactive } from 'vue';
//@ts-ignore
import { CreateStory, EditorStory, CapitolAiWrapper } from '@capitol.ai/vue';

const state = reactive({
  storyId: "",
})

const handleStorySubmit = (newUuid: string) => {
  console.log(`[App] Story submitted successfully. UUID: ${newUuid}`);
  state.storyId = newUuid;
}

const sidebarSettings = {
  enabledTextBlock: false,
  enabledDataSourcesBlock: false,
  enabledImageBlock: false,
  enabledChartBlock: false,
  enabledQuoteBlock: false,
  enabledMetricBlock: false,
  enabledTableBlock: false,
};
</script>

<template>
  <CapitolAiWrapper>
    <h1 class="title">Vue -Interactive Story Creation and Editing</h1>
    <CreateStory
      v-if="!state.storyId"
      :callbackOnSubmit="handleStorySubmit"
      :sidebarSettings="sidebarSettings"
      :enablePrompts="true"
      :enableSources="false"
      :enableYCVotes="false"
    />
    <EditorStory
      v-if="state.storyId"
      :storyId="state.storyId"
      :sidebarSettings="sidebarSettings"
      :enableDocRemix="false"
      :enableHistory="false"
      :enableExportToGoogle="false"
      :enableDownload="false"
      :enabledShare="false"
      :enableHeaderMenu="false"
    />
  </CapitolAiWrapper>
</template>
