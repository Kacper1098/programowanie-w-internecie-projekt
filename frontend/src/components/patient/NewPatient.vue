<template>
    <v-container>
        <h2 class="text-center">Nowy pacjent</h2>
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

                    <v-col>
                        <v-text-field
                                v-model="secondName"
                                label="Drugie imię"
                        ></v-text-field>
                    </v-col>
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
                        <v-select
                                :items="sex_choices"
                                :item-text="item=>item.sex"
                                :item-value="item=>item.val"
                                label="Płeć"
                                v-model="sex"
                                :rules="requiredRule"
                        ></v-select>
                    </v-col>
                    <v-col>
                        <v-text-field
                                v-model="pesel"
                                label="PESEL"
                                :rules="requiredRule"
                                required
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field
                                v-model="country"
                                :rules="requiredRule"
                                label="Kraj"
                                required
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                                v-model="city"
                                label="Miasto"
                                :rules="requiredRule"
                        ></v-text-field>
                    </v-col>

                    <v-col>
                        <v-text-field
                                v-model="street"
                                label="Ulica"
                                :rules="requiredRule"
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                                v-model="postal_code"
                                :rules="requiredRule"
                                label="Kod pocztowy"
                                required
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field
                                v-model="phone"
                                label="Numer telefonu"
                                required
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                                v-model="email"
                                label="Adres e-mail"
                                required
                        ></v-text-field>
                    </v-col>
                </v-row>
            </v-container>
            <v-row justify="center">
                <v-btn color="blue" @click="createPatient" dark>Dodaj pacjenta</v-btn>
            </v-row>
        </v-form>
    </v-container>
</template>

<script>

    export default {
        name: 'NewPatient',
        data: () => ({
            valid: false,
            name: '',
            secondName: '',
            surname: '',
            requiredRule: [
                v => !!v || 'To pole jest wymagane',
            ],
            email: '',
            sex: '',
            country: '',
            street: '',
            postal_code: '',
            phone: '',
            pesel: '',
            city: '',
            sex_choices: [{sex: 'Kobieta', val: 'f'}, {sex: 'Mężczyzna', val: 'm'}, {sex: 'Nieznana', val: 'u'}]
        }),
        methods: {
            createPatient() {
                this.$refs.form.validate()
                if (this.valid) {

                    this.$http.post('/patients/', {
                        name: this.name,
                        surname: this.surname,
                        second_name: this.secondName,
                        email: this.email,
                        sex: this.sex,
                        country: this.country,
                        postal_code: this.postal_code,
                        street: this.street,
                        telephone: this.phone,
                        pesel: this.pesel,
                        city: this.city
                    })
                        .then(result => {
                            this.$router.push('/patient/list');
                        })
                        .catch(error => {
                            console.log(error);
                        })
                }
            },
        }

    };
</script>
