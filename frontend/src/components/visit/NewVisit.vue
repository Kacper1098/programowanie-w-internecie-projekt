<template>
    <v-container fluid>
        <v-form v-model="valid" lazy-validation>
            <h2 class="text-center">Nowa wizyta</h2>
            <v-row align="center" justify="center">
                <v-col class="d-flex" cols="12" sm="6">
                    <v-autocomplete
                            :items="doctors"
                            :item-text="doctor_select_text"
                            @change="setHours"
                            :item-value="item => item.id"
                            v-model="doctor"
                            return-object
                            label="Lekarz"
                            required
                    ></v-autocomplete>
                </v-col>
            </v-row>
            <v-row align="center" justify="center">
                <v-col class="d-flex" cols="12" sm="6">
                    <v-autocomplete
                            :items="patients"
                            :item-text="patient_select_text"
                            label="Pacjent"
                            :item-value="item => item.id"
                            v-model="patient"
                            return-object
                            required
                    ></v-autocomplete>
                </v-col>
            </v-row>
            <v-row justify="center">
                <v-col class="d-flex" cols="12" sm="6">
                    <v-menu
                            v-model="menu"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                    >
                        <template v-slot:activator="{ on }">
                            <v-text-field
                                    v-model="date"
                                    label="Data wizyty"
                                    readonly
                                    v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker @click.native="getDoctorsHours" locale="pl" v-model="date"
                                       @input="menu2 = false"></v-date-picker>
                    </v-menu>
                </v-col>
            </v-row>
            <v-row align="center" justify="center">
                <v-col class="d-flex" cols="12" sm="6">
                    <v-select
                            :items="hours"
                            label="Godzina wizyty"
                            v-model="hour"
                            no-data-text="Brak dostępnych godzin."
                            required
                    ></v-select>
                </v-col>
            </v-row>
            <v-row justify="center">
                <v-btn color="blue" @click="createVisit" dark>Umów wizytę</v-btn>
            </v-row>

        </v-form>

    </v-container>
</template>

<script>

    export default {
        name: 'NewVisit',
        data: () => ({
            valid: false,
            hours: [],
            doctors: [],
            patients: [],
            date: '',
            menu: false,
            hoursFromApi: {},
            doctor: '',
            patient: '',
            hour: '',

        }),
        methods: {
            doctor_select_text: item => item.name + ' ' + item.surname + ' (' + item.pwz + ')',
            patient_select_text: item => item.name + ' ' + item.surname + ' (' + item.pesel + ')',
            getDoctorsHours() {
                this.$http.get(`/doctors_hours?date=${this.date}`)
                .then(result => {
                    this.hoursFromApi = result.data;
                    this.setHours();
                })
                .catch(error => {
                    console.log(error)
                })
            },
            setHours() {
                this.hours = ''
                if (this.hoursFromApi)
                    this.hours = this.hoursFromApi[this.doctor.id]
            },
            createVisit() {
                this.$http.post(`/visits/`, {
                    patient_id: this.patient.id,
                    doctor_id: this.doctor.id,
                    date: this.date,
                    start_time: this.hour.split('-')[0],
                    end_time: this.hour.split('-')[1]
                })
                    .then(result => {
                        this.$router.push('/visit/list');
                    })
                    .catch(error => {
                        console.log(error);
                    })
            }
        },

        mounted() {
            this.$http.get(`/doctors/`)
                .then((result) => {
                    this.doctors = result.data;
                    this.setHours();
                })
                .catch(error => {
                    console.log(error);
                })
            this.$http.get(`/patients/`)
                .then((result) => {
                    this.patients = result.data
                })
                .catch(error => {
                    console.log(error);
                })
        }

    };
</script>
