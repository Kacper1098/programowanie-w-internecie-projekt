<template>
  <v-container fluid>
    <v-row>
      <b>{{ facilityName }}</b>
      <v-col cols="12">
        <v-row>
          <v-col>
            <v-sheet height="300">
              <v-calendar
                  :now="today"
                  :value="today"
                  color="primary"
                  locale="pl"
              >
              </v-calendar>
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="12">
        <v-row>
          <v-col cols="6">
            <v-subheader><b>Wizyty na dziś</b></v-subheader>
            <v-simple-table>

              <template v-slot:default>

                <thead>
                <tr>
                  <th class="text-left">Godzina od</th>
                  <th class="text-left">Godzina do</th>
                  <th class="text-left">Pacjent</th>
                  <th class="text-left">Akcje</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="visit in visits" :key="visit.id">
                  <td width="10%">{{ visit.start_time }}</td>
                  <td width="10%">{{ visit.end_time }}</td>
                  <td width="30%">
                    {{ visit.patient.name }} {{ visit.patient.surname }} ({{ visit.patient.pesel }})
                  </td>
                  <td width="5%">
                    <v-tooltip top>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="primary" fab small elevation="0" v-bind="attrs" v-on="on" :to="`/visit/perform/${visit.id}`">
                          <v-icon>mdi-application-import</v-icon>
                        </v-btn>
                      </template>
                      <span>Przeprowadź wizytę</span>
                    </v-tooltip>
                  </td>
                </tr>
                <tr v-if="!visits.length">
                  <td colspan="6">Brak wizyt.</td>
                </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-col>
          <v-col cols="6">
            <v-subheader><b>Menu szybkich akcji</b></v-subheader>
            <v-row class="quick-actions-row">
              <v-col cols="4">
                <v-btn x-large color="teal" dark to="/visit/list">Lista wizyt</v-btn>
              </v-col>
              <v-col cols="4">
                <v-btn x-large color="teal" dark to="/visit/new">Nowa wizyta</v-btn>
              </v-col>
            </v-row>
            <v-row class="quick-actions-row">
              <v-col cols="4">
                <v-btn x-large color="purple" dark to="/patient/list">Lista pacjentów</v-btn>
              </v-col>
              <v-col cols="4">
                <v-btn x-large color="purple" dark to="/patient/new">Dodaj pacjenta</v-btn>
              </v-col>
            </v-row>
          </v-col>

        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'Home',
  data: () => ({
    visits: [],
    today: new Date().toISOString().slice(0, 10),
    facilityName: ''
  }),
  mounted() {
    this.facilityName = this.$store.state.facilityName
    console.log(this.facilityName)
    this.$http.get('/visits/my_visits/')
        .then((result) => {
          this.visits = result.data
        })
        .catch(error => {
          console.log(error);
        })
  }

};
</script>
<style scoped>
.quick-actions-row {
  margin-left: 4px;
}

.quick-actions-row .v-btn {
  width: 100%;
}
</style>