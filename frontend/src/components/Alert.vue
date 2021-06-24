<template>
    <v-snackbar
      :color="alert.color"
      v-model="alert.display"
      :timeout="2000"
    >
      {{ alert.text }}
        <v-btn
          text
          @click="alert.display = false"
        >
          Zamknij
        </v-btn>
    </v-snackbar>
</template>

<script>
import { mapState } from 'vuex';
    export default {
      name: 'Alert',
      data: () => ({
        display: false,
        color: '',
        text: ''
      }),
      computed: {
        ...mapState(['alert'])
      }

    }
</script>
