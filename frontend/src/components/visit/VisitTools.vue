<template>
  <v-container fluid>
    <div v-if="loaded">
    <img v-for="tooth in teethSorted['top_left']" :key="tooth.id" src="/img/icons/tooth.svg"
         width="50" class="up-tooth" @click="setSelectedTooth(tooth)" :class="{ 'broken-tooth': tooth.note }">
      <a style="margin-left: 20px"></a>
    <img v-for="tooth in teethSorted['top_right']" :key="tooth.id" src="/img/icons/tooth.svg"
         width="50" class="up-tooth" @click="setSelectedTooth(tooth)" :class="{ 'broken-tooth': tooth.note }">
    <br><br>
    <img v-for="tooth in teethSorted['bottom_left']" :key="tooth.id" src="/img/icons/tooth.svg"
         width="50" @click="setSelectedTooth(tooth)" :class="{ 'broken-tooth': tooth.note }">
      <a style="margin-left: 20px"></a>
    <img v-for="tooth in teethSorted['bottom_right']" :key="tooth.id" src="/img/icons/tooth.svg"
         width="50" @click="setSelectedTooth(tooth)" :class="{ 'broken-tooth': tooth.note }">
      <div v-if="selectedTooth" style="margin-top: 50px">
        <h3>Ząb</h3>
        <table style="min-width: 200px; width: 600px; margin-top: 20px">
          <tr>
            <td><b>Położenie: </b></td><td>{{ toothPosition(selectedTooth) }}</td>
          </tr>
          <tr>
            <td><b>Numer: </b></td><td>{{ selectedTooth.number }}</td>
          </tr>
          <tr>
            <td><b>Notatka: </b></td>
            <td style="padding-top: 20px">
              <v-textarea solo v-model="selectedTooth.note"></v-textarea>
              <v-btn color="blue" @click="onSave" dark style="float: right">Zapisz</v-btn>
            </td>
          </tr>
        </table>

      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'VisitTools',
  props: ['patientId'],
  data: () => ({
    teeth: [],
    teethSorted: {},
    patient: {},
    loaded: false,
    selectedTooth: false
  }),
  created() {
    this.getPatient();
  },
  methods: {
    getPatient() {
      const id = this.$route.params.id;
      this.$http.get(`/visits/${id}`)
          .then(response => {
            this.patient = response.data.patient
            this.getTeeth();
          })
    },
    getTeeth() {
      this.$http.get(`/teeth/?patient=${this.patient.id}`)
      .then(response => {
        this.teeth = response.data
        this.sortTeeth();
      })
    },
    sortTeeth() {
      this.teethSorted['top_left'] = this.teeth
          .filter(tooth => tooth.horizontally === 'top' && tooth.vertically === 'left')
          .sort((a, b)=>b.number-a.number)
      this.teethSorted['top_right'] = this.teeth
          .filter(tooth => tooth.horizontally === 'top' && tooth.vertically === 'right')
          .sort((a, b)=>a.number-b.number)
      this.teethSorted['bottom_left'] = this.teeth
          .filter(tooth => tooth.horizontally === 'bottom' && tooth.vertically === 'left')
          .sort((a, b)=>b.number-a.number)
      this.teethSorted['bottom_right'] = this.teeth
          .filter(tooth => tooth.horizontally === 'bottom' && tooth.vertically === 'right')
          .sort((a, b)=>a.number-b.number)
      this.loaded = true
    },
    toothPosition(tooth) {
      const positionMap = {"left": "Lewy", "right": "Prawy", "top": "Górny", "bottom": "Dolny"}
      return positionMap[tooth.vertically] + ' ' + positionMap[tooth.horizontally]
    },
    setSelectedTooth(tooth) {
      this.selectedTooth = tooth;
    },
    onSave() {
      this.$http.put(`/teeth/${this.selectedTooth.id}/`,{
        ...this.selectedTooth
      })
      .then(() => {
        this.$store.dispatch('showAlert', {text: "Pomyślnie zapisano!", color: 'green'})
      })

    }
  }
};
</script>
<style scoped>
.broken-tooth {
  filter: invert(86%) sepia(65%) saturate(531%) hue-rotate(348deg) brightness(99%) contrast(98%);
}

.up-tooth {
  transform: scaleY(-1);
}

img {
  cursor: pointer;
}

img:hover {
  opacity: 50%;
}
</style>
