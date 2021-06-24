<template>
  <v-container>
    <h2 class="text-center">Profil</h2>
    <v-form ref="form"
            v-model="valid"
            :lazy-validation="lazy">
      <v-container>
        <v-row>
          <v-col>
            <v-text-field
                v-model="name"
                :rules="requiredRule"
                label="Imię"
                required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-text-field
                v-model="secondName"
                label="Drugie imię"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-text-field
                v-model="surname"
                :rules="requiredRule"
                label="Nazwisko"
                required
            ></v-text-field>
          </v-col>

        </v-row>
        <v-row>
          <v-col>
            <v-text-field
                v-model="pwz"
                label="PWZ"
                :rules="requiredRule"
                required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-text-field
                v-model="telephone"
                label="Telefon"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
      <v-row justify="center">
        <PasswordChange/>
        <v-btn color="blue" @click="onSave" dark>Zapisz</v-btn>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
import PasswordChange from "./PasswordChange";

export default {
  name: 'Profile',
  components: {
    PasswordChange
  },
  data: () => ({
    name: '',
    surname: '',
    secondName: '',
    pwz: '',
    telephone: '',
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
    valid: false,
    dialog: false,
  }),
  methods: {
    onSave() {
      if (!this.validateFields())
        return

      const id = this.$store.state.doctorId;
      this.$http.put(`/doctors/${id}/`, {
        name: this.name,
        surname: this.surname,
        second_name: this.secondName,
        pwz: this.pwz,
        telephone: this.telephone
      })
      .then(response => {
        this.$store.commit({
          type: 'setFullName', firstName: response.data.name, lastName: response.data.surname
        });
        this.$store.dispatch('showAlert', {
          text: 'Pomyślnie zapisano!', color: 'green'
        });
      })
    },
    validateFields() {
       return this.$refs.form.validate()
    }
  },
  mounted() {
    const id = this.$store.state.doctorId;
    this.$http.get(`/doctors/${id}/`)
        .then(response => {
          const data = response.data
          this.name = data.name
          this.surname = data.surname
          this.secondName = data.second_name
          this.telephone = data.telephone
          this.pwz = data.pwz
        })
  }

};
</script>
