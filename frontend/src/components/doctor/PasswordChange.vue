<template>
 <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="blue" outlined dark style="margin-right: 20px" v-bind="attrs" v-on="on"
        >
          Zmień hasło
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Zmiana hasła</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid">
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  label="Stare hasło"
                  type="password"
                  v-model="oldPass"
                  required
                  :rules="requiredRule"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  label="Nowe hasło"
                  type="password"
                  v-model="newPass"
                  required
                  :rules="requiredRule"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  label="Powtórz nowe hasło"
                  type="password"
                  v-model="newPass2"
                  required
                  :rules="requiredRule"
                ></v-text-field>
              </v-col>
            </v-row>
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
  name: 'PasswordChange',
  data: () => ({
    dialog: false,
    valid: false,
    oldPass: '',
    newPass: '',
    newPass2: '',
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
  }),
  methods: {
    onSave() {
      if (!this.validateFields())
        return
      this.$http.put('/change_password/',{
        old_password: this.oldPass,
        new_password1: this.newPass,
        new_password2: this.newPass2
      })
      .then(response => {
        this.dialog = false;
        this.$store.dispatch('showAlert', {text: 'Pomyślnie zmieniono hasło', color: 'green'})
      })
      .catch(error => {
        const errors = error.response.data
        const message = errors[Object.keys(errors)[0]][0]
        this.$store.dispatch('showAlert', {text: message, color: 'red'})
      })
    },
    validateFields() {
       return this.$refs.form.validate()
    }
  }
};
</script>
