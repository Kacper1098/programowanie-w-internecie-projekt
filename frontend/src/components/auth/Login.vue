<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="blue"
                dark
                flat
              >
                <v-toolbar-title>Logowanie</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    name="login"
                    prepend-icon="mdi-account"
                    type="text"
                    v-model="input.username"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="Hasło"
                    name="password"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="input.password"
                  ></v-text-field>
                </v-form>
                  <v-card-actions class="mt-5">
                <v-btn color="blue" outlined to="/register">Rejestracja</v-btn>
                <v-spacer></v-spacer>
                <v-btn color="blue" dark v-on:click="login()">Zaloguj</v-btn>
              </v-card-actions>
              </v-card-text>

            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login() {
              this.$http.post('/token-auth/', {
                  username: this.input.username,
                  password: this.input.password,
              })
              .then((result) => {
                this.$store.commit({type: 'setAuthenticated', authenticated: true, token: result.data.token});
                this.$store.commit({
                  type: 'setFullName', firstName: result.data.user.name, lastName: result.data.user.surname
                });
                this.$store.commit({
                  type: 'setDoctorId', doctorId: result.data.user.doctor_id
                });
                this.$store.commit({
                  type: 'setFacilityName', facilityName: result.data.user.facility_name
                });
                this.$http.defaults.headers.common['Authorization'] = `JWT ${result.data.token}`;
                this.$router.push('/');
              })
              .catch(error=>{
                if (error.response.status == 400) {
                  this.$store.dispatch('showAlert', {'text': 'Niepoprawne dane logowania', 'color': 'red'})
                }
              })
            }
        }
    }
</script>

<style scoped>
    .v-card__actions {
        padding: 0
    }
</style>