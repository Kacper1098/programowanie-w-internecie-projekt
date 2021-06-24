<template>
  <v-container>
    <h3>Notatki</h3>
    <v-simple-table>
        <template v-slot:default>
            <thead>
            <tr>
                <th class="text-left">Data utworzenia</th>
                <th class="text-left">Tytuł</th>
                <th class="text-left">Treść</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="note in notes" :key="note.id">
                <td width="15%">{{ trimDate(note.created) }}</td>
                <td width="15%">{{ note.title}}</td>
                <td width="55%">{{ note.note }}</td>
            </tr>
            <tr v-if="!notes.length">
                <td colspan="4">Brak notatek.</td>
            </tr>
            </tbody>
        </template>
    </v-simple-table>
    <h3 style="margin-top: 20px">Oznaczone zęby</h3>
    <v-simple-table>
        <template v-slot:default>
            <thead>
            <tr>
                <th class="text-left">Pozycja</th>
                <th class="text-left">Numer</th>
                <th class="text-left">Notatka</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="tooth in badTeeth" :key="tooth.id">
                <td width="15%">{{ toothPosition(tooth) }}</td>
                <td width="15%">{{ tooth.number}}</td>
                <td width="55%">{{ tooth.note }}</td>
            </tr>
            <tr v-if="!badTeeth.length">
                <td colspan="4">Brak oznaczonych zębów.</td>
            </tr>
            </tbody>
        </template>
    </v-simple-table>
  </v-container>
</template>

<script>

export default {
  name: 'PatientMedical',

  data: () => ({
    notes: [],
    teeth: [],
    badTeeth: []
  }),
  created() {
    this.getNotes()
    this.getTeeth()
  },
  methods: {
    getNotes() {
      const id = this.$route.params.id
      this.$http.get(`/patient-notes/?patient=${id}`)
          .then(response => {
            this.notes = response.data
          })
    },
    trimDate(date) {
      return date.slice(0, 10)
    },
    getTeeth() {
      const id = this.$route.params.id
      this.$http.get(`/teeth/?patient=${id}`)
      .then(response => {
        this.teeth = response.data
        this.filterBadTeeth();
      })
    },
    filterBadTeeth() {
      this.badTeeth = this.teeth.filter(tooth => tooth.note)
    },
    toothPosition(tooth) {
      const positionMap = {"left": "Lewy", "right": "Prawy", "top": "Górny", "bottom": "Dolny"}
      return positionMap[tooth.vertically] + ' ' + positionMap[tooth.horizontally]
    },
  }
};
</script>
