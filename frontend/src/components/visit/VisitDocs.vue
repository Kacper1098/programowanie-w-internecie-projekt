<template>
  <v-container fluid>
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
        <add-note-dialog :patientId="patient.id" @getNotes="getNotes"/>
  </v-container>
</template>

<script>
import AddNoteDialog from "./AddNoteDialog";
export default {
  name: 'VisitDocs',
  components: {
    AddNoteDialog
  },
  data: () => ({
    notes: [],
    patient: {}
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
            this.getNotes();
          })
    },
    getNotes() {
      this.$http.get(`/patient-notes/?patient=${this.patient.id}`)
          .then(response => {
            this.notes = response.data
          })
    },
    trimDate(date) {
      return date.slice(0, 10)
    }
  }
};
</script>
