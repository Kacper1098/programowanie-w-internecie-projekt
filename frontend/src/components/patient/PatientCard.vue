<template>
  <v-container>
      <v-tabs v-model="tab" background-color="white" light>
        <v-tab v-for="item in items" :key="item.tab">
          {{ item.tab }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item v-for="item in items" :key="item.tab">
          <v-card flat>
            <v-card-text>
              <component v-bind:is="item.content"></component>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
  </v-container>
</template>

<script>
import PatientInfo from "./PatientInfo";
import PatientMedical from "./PatientMedical";
import PatientVisits from "./PatientVisits";

export default {
  name: 'PatientCard',
  components: {
    PatientInfo,
    PatientMedical,
    PatientVisits
  },
  data: () => ({
    tab: null,
    items: [
        { tab: 'Dane osobowe', content: 'PatientInfo' },
        { tab: 'Dane medyczne', content: 'PatientMedical' },
        { tab: 'Wizyty', content: 'PatientVisits' },
      ]
  }),
};
</script>
