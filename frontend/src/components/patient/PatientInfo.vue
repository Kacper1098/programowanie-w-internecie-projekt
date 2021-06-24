<template>
  <v-container>
    <v-form ref="form"
            v-model="valid"
            :lazy-validation="lazy">
      <v-container>
        <v-row>
          <v-col>
            <h3>Dane podstawowe</h3>
            <v-text-field
                v-model="patient.name"
                :rules="requiredRule"
                label="Imię"
                required
            ></v-text-field>
            <v-text-field
                v-model="patient.secondName"
                label="Drugie imię"
            ></v-text-field>
            <v-text-field
                v-model="patient.surname"
                :rules="requiredRule"
                label="Nazwisko"
                required
            ></v-text-field>
            <v-text-field
                v-model="patient.pesel"
                label="PESEL"
                :rules="requiredRule"
                required
            ></v-text-field>
            <v-select
                :items="sex_choices"
                :item-text="item=>item.sex"
                :item-value="item=>item.val"
                label="Płeć"
                v-model="patient.sex"
                :rules="requiredRule"
            ></v-select>
          </v-col>
          <v-col>
            <h3>Adres</h3>
            <v-text-field
                v-model="patient.country"
                :rules="requiredRule"
                label="Kraj"
                required
            ></v-text-field>
            <v-text-field
                v-model="patient.city"
                label="Miasto"
                :rules="requiredRule"
            ></v-text-field>
            <v-text-field
                v-model="patient.street"
                label="Ulica"
                :rules="requiredRule"
            ></v-text-field>
            <v-text-field
                v-model="patient.postal_code"
                :rules="requiredRule"
                label="Kod pocztowy"
                required
            ></v-text-field>
          </v-col>
          <v-col>
            <h3>Kontakt</h3>
            <v-text-field
                v-model="patient.telephone"
                label="Numer telefonu"
                required
            ></v-text-field>
            <v-text-field
                v-model="patient.email"
                label="Adres e-mail"
                required
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
      <v-row justify="center">
        <v-btn color="blue" @click="savePatient" dark>Zapisz</v-btn>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>

export default {
  name: 'PatientInfo',
  data: () => ({
    valid: false,
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
    patient: {
      name: '',
      secondName: '',
      surname: '',
      email: '',
      sex: '',
      country: '',
      street: '',
      postal_code: '',
      telephone: '',
      pesel: '',
      city: '',
    },
    sex_choices: [{sex: 'Kobieta', val: 'f'}, {sex: 'Mężczyzna', val: 'm'}, {sex: 'Nieznana', val: 'u'}],
    items: [
      'web', 'shopping', 'videos', 'images', 'news',
    ],
  }),
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      const id = this.$route.params.id
      this.$http.get(`/patients/${id}/`)
          .then(response => {
            console.log(response.data)
            this.patient = response.data
            this.patient.secondName = response.data.second_name
          })
    },
    savePatient() {
      this.$refs.form.validate()
      const id = this.$route.params.id
      if (this.valid) {
        this.$http.put(`/patients/${id}/`, {
          ...this.patient,
          second_name: this.patient.secondName
        })
            .then(result => {
              this.$store.dispatch('showAlert', {
                text: 'Pomyślnie zapisano!', color: 'green'
              });
            })
            .catch(error => {
              this.$store.dispatch('showAlert', {
                text: 'Błąd, niepoprawne dane', color: 'red'
              });
            })
      }
    }
  }

};
</script>
