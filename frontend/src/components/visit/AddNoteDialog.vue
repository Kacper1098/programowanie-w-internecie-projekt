<template>
 <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="blue" dark style="margin-top: 20px; float: right" v-bind="attrs" v-on="on"
        >
          Dodaj notatkę
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Dodaj notatkę</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid">
          <v-container>
            <v-text-field outlined label="Tytuł" v-model="title" :rules="requiredRule"></v-text-field>
            <v-textarea outlined v-model="note" :rules="requiredRule" label="Treść" required></v-textarea>
          </v-container>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Wróć
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="onSave"
          >
            Zapisz
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>

export default {
  name: 'AddNoteDialog',
  props: ['patientId'],
  data: () => ({
    dialog: false,
    valid: false,
    note: '',
    title: '',
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
  }),
  methods: {
    onSave() {
      if (!this.validateFields())
        return
      this.$http.post(`/patient-notes/`,{
        note: this.note,
        patient: this.patientId,
        title: this.title
      })
      .then(() => {
        this.$emit('getNotes');
        this.dialog = false;
        this.$store.dispatch('showAlert', {text: 'Pomyślnie dodano notatkę!', color: 'green'})
      })
      .catch(() => {
        this.$store.dispatch('showAlert', {text: "Błąd dodawania notatki", color: 'red'})
      })
    },
    validateFields() {
       return this.$refs.form.validate()
    }
  }
};
</script>
