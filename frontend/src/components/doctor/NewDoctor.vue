<template>
  <v-container>
    <h2 class="text-center">Nowy pracownik</h2>
    <v-form ref="form"
            v-model="valid"
            :lazy-validation="lazy">
      <v-container>
        <v-row>
          <v-col>

            <v-text-field
                v-model="doctor.name"
                :rules="requiredRule"
                label="Imię"
                required
            ></v-text-field>
            <v-text-field
                v-model="doctor.second_name"
                label="Drugie imię"
            ></v-text-field>
            <v-text-field
                v-model="doctor.surname"
                :rules="requiredRule"
                label="Nazwisko"
                required
            ></v-text-field>
            <v-text-field
                v-model="doctor.pwz"
                :rules="requiredRule"
                label="PWZ"
                required
            ></v-text-field>
            <v-text-field
                v-model="doctor.telephone"
                label="Telefon"
            ></v-text-field>
          </v-col>
          <v-col>
            <v-text-field
                v-model="user.login"
                :rules="requiredRule"
                label="Login"
                required
            ></v-text-field>
            <v-text-field
                v-model="user.email"
                :rules="requiredRule"
                label="Email"
                required
            ></v-text-field>
            <v-text-field
                v-model="user.password"
                :rules="requiredRule"
                type="password"
                required
                label="Hasło"
            ></v-text-field>
          </v-col>

        </v-row>
      </v-container>
      <v-row justify="center">
        <v-btn color="blue" @click="createDoctor" dark>Dodaj pracownika</v-btn>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>

export default {
  name: 'NewDoctor',
  data: () => ({
    valid: false,
    doctor: {
      name: '',
      secondName: '',
      surname: '',
      pwz: '',
      telephone: ''
    },
    user: {
      login: '',
      email: '',
      password: ''
    },
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
  }),
  methods: {
    createDoctor() {
      this.$refs.form.validate()
      if (this.valid) {

        this.$http.post('/doctors/', {
          ...this.doctor,
          user: this.user
        })
            .then(result => {
              this.$router.push('/doctor/list');
              this.$store.dispatch('showAlert', {text: "Pomyślnie utworzono!", color: 'green'})
            })
            .catch(error => {
              this.$store.dispatch('showAlert', {text: error.response.data[0], color: 'red'})
            })
      }
    },
  }

};
</script>
