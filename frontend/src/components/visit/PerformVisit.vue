<template>
    <v-container fluid>
      <v-row>
      <v-col cols="4">
        <visit-patient-data/>
      </v-col>
      <v-col cols="8">
      <v-tabs v-model="tab" background-color="white" light>
        <v-tab v-for="item in items" :key="item.tab">
          {{ item.tab }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item v-for="item in items" :key="item.tab">
          <v-card flat>
            <v-card-text>
              <component :is="item.content"></component>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
      </v-col>
        </v-row>
    </v-container>
</template>

<script>
import VisitPatientData from "./VisitPatientData";
import VisitTools from "./VisitTools";
import VisitDocs from "./VisitDocs";
    export default {
        name: 'PerformVisit',
      components: {
          VisitPatientData,
        VisitTools,
        VisitDocs
      },
      mounted() {
        const id = this.$route.params.id;
          this.$http.get(`/visits/${id}`)
        .then(response => {
          this.patient = response.data.patient
        })
      },
      data: () => ({
          tab: null,
          items: [
              { tab: 'Narzędzia', content: 'VisitTools'},
              { tab: 'Dokumenty', content: 'VisitDocs'},
            ],
        patient: {}
        }),
    };
</script>
