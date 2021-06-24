<template>
  <v-app>
      <router-view></router-view>
    <Alert/>
  </v-app>
</template>

<script>
import Alert from "./components/Alert";
export default {
  name: 'App',
  components: {
    Alert
  }
};
</script>
