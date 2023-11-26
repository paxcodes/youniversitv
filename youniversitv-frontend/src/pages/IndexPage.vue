<template>
  <q-page class="row items-center justify-evenly">
    <iframe
      width="560"
      height="315"
      :src="mainVideo"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen
    ></iframe>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const videos = ref<string[]>(['BlSVX1WqTXk', 'vkM_2vsHWA4']);
    const mainVideo = ref<string>(
      `https://youtube.com/embed/${videos.value[0]}`
    );
    return { videos, mainVideo };
  },
  methods: {},
});
</script>
