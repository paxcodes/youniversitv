<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-white text-dark">
      <q-toolbar>
        <q-toolbar-title> <strong>youniversiTV</strong> </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- <q-footer elevated class="bg-grey-8 text-white center">
      <q-toolbar>
        <q-toolbar-title>
          <div><strong>youniversiTV</strong></div>
          <span class="text-weight-light text-subtitle2">
            Hand-built by <s>pandas</s>&nbsp;<a
              href="https://github.com/paxcodes/"
              target="_blank"
              >Pax</a
            >
          </span>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer> -->
  </q-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainLayout',

  components: {},

  setup() {
    return {};
  },
});
</script>
