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
                                <v-toolbar-title>Rejestracja</v-toolbar-title>
                                <v-spacer></v-spacer>
                            </v-toolbar>
                            <v-card-text>
                                <v-stepper v-model="e1" class="no-border-stepper">
                                    <v-stepper-header class="no-border-stepper">
                                        <v-stepper-step :complete="e1 > 1" color="blue" step="1">Użytkownik
                                        </v-stepper-step>

                                        <v-divider></v-divider>

                                        <v-stepper-step :complete="e1 > 2" step="2" color="blue">Dane osobowe
                                        </v-stepper-step>
                                        <v-divider></v-divider>
                                        <v-stepper-step step="3" color="blue">Placówka</v-stepper-step>
                                    </v-stepper-header>

                                    <v-stepper-items>
                                        <v-stepper-content step="1">
                                            <v-card>
                                                <v-card-text>
                                                    <v-form ref="step1">
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="user.username"
                                                                        label="Login"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        type="email"
                                                                        v-model="user.email"
                                                                        label="Adres e-mail"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="user.password"
                                                                        type="password"
                                                                        :rules="requiredRule"
                                                                        label="Hasło"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        type="password"
                                                                        label="Powtórz hasło"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                    </v-form>
                                                    <v-card-actions>
                                                        <v-row justify="end">
                                                            <v-btn
                                                                    color="blue"
                                                                    dark
                                                                    @click="()=>nextStep(2)"
                                                            >
                                                                Dalej
                                                            </v-btn>
                                                        </v-row>
                                                    </v-card-actions>
                                                </v-card-text>

                                            </v-card>

                                        </v-stepper-content>

                                        <v-stepper-content step="2">
                                            <v-card>
                                                <v-card-text>
                                                    <v-form ref="step2">
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="doctor.name"
                                                                        label="Imię"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="doctor.second_name"
                                                                        label="Drugie imię"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="doctor.surname"
                                                                        label="Nazwisko"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="doctor.pwz"
                                                                        label="PWZ"
                                                                        required
                                                                        :rules="requiredRule"
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="doctor.telephone"
                                                                        label="Numer telefonu"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                    </v-form>
                                                    <v-card-actions>

                                                        <v-row justify="space-between">
                                                            <v-btn
                                                                    color="blue"
                                                                    outlined
                                                                    @click="e1 = 1"
                                                            >
                                                                Wróć
                                                            </v-btn>
                                                            <v-btn
                                                                    color="blue"
                                                                    dark
                                                                    @click="nextStep(3)"
                                                            >
                                                                Dalej
                                                            </v-btn>
                                                        </v-row>
                                                    </v-card-actions>
                                                </v-card-text>

                                            </v-card>

                                        </v-stepper-content>

                                        <v-stepper-content step="3">
                                            <v-card>
                                                <v-card-text>
                                                    <v-form ref="step3">
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.name"
                                                                        label="Nazwa"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.telephone"
                                                                        label="Numer telefonu"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.email"
                                                                        label="Adres e-mail"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.country"
                                                                        label="Kraj"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>

                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.city"
                                                                        label="Miasto"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.street"
                                                                        label="Ulica"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                            <v-col>
                                                                <v-text-field
                                                                        v-model="facility.postal_code"
                                                                        label="Kod pocztowy"
                                                                        :rules="requiredRule"
                                                                        required
                                                                ></v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                    </v-form>
                                                    <v-card-actions>
                                                        <v-row justify="space-between">
                                                            <v-btn
                                                                    color="blue"
                                                                    outlined
                                                                    @click="e1 = 2"
                                                            >
                                                                Wróć
                                                            </v-btn>
                                                            <v-btn
                                                                    color="blue"
                                                                    dark
                                                                    @click="register"
                                                            >
                                                                Zarejestruj
                                                            </v-btn>
                                                        </v-row>
                                                    </v-card-actions>
                                                </v-card-text>

                                            </v-card>
                                        </v-stepper-content>


                                    </v-stepper-items>
                                </v-stepper>

                                <v-row justify="end">
                                    <v-btn class="mr-8" text color="blue" to="/login">Zaloguj się</v-btn>
                                </v-row>

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
        data() {
            return {
                e1: 1,
                requiredRule: [
                    v => !!v || 'To pole jest wymagane',
                ],
                user: {
                    username: '',
                    email: '',
                    password: '',
                },
                doctor: {
                    name: '',
                    surname: '',
                    second_name: '',
                    pwz: '',
                    telephone: ''
                },
                facility: {
                    name: '',
                    telephone: '',
                    email: '',
                    country: '',
                    city: '',
                    street: '',
                    postal_code: '',
                }
            }
        },
        methods: {
            register() {
                const valid = this.$refs.step3.validate();
                if (valid) {

                    this.$http.post('/users/', {
                        user: this.user,
                        facility: this.facility,
                        doctor: this.doctor
                    })
                        .then((result) => {
                          this.$store.dispatch('showAlert', {text: "Pomyślnie utworzono konto! Potwierdz email", color: 'green'})
                          this.$router.push('/login');
                        })
                        .catch(error => {
                            console.log(error);
                        })
                }

            },
            nextStep(step) {
                let valid = false;
                if (step == 2)
                    valid = this.$refs.step1.validate()
                else if (step == 3)
                    valid = this.$refs.step2.validate()
                if (valid) {
                    this.e1 = step
                }
            }
        }
    }
</script>
<style scoped>
    .no-border-stepper {
        box-shadow: none;
        -webkit-box-shadow: none;
    }
</style>