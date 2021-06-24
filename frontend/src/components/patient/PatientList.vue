<template>
    <v-container fluid>
        <h2 class="text-center mb-5">Lista pacjentów</h2>
        <v-simple-table>
            <template v-slot:default>
                <thead>
                <tr>
                    <th class="text-left">Imię</th>
                    <th class="text-left">Nazwisko</th>
                    <th class="text-left">PESEL</th>
                    <th class="text-left">Adres</th>
                    <th class="text-left">Akcje</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="patient in patients" :key="patient.id">
                    <td width="15%">{{ patient.name }} {{ patient.second_name }}</td>
                    <td width="15%">{{ patient.surname}}</td>
                    <td width="15%">{{ patient.pesel }}</td>
                    <td width="40%">{{ patient.street }}, {{ patient.postal_code }} {{ patient.city }} {{ patient.country }}</td>
                    <td width="5%">
                        <v-tooltip left>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn color="primary" fab small elevation="0" v-bind="attrs" v-on="on" :to="`card/${patient.id}`">
                                    <v-icon>mdi-card-account-details</v-icon>
                                </v-btn>
                            </template>
                            <span>Karta pacjenta</span>
                        </v-tooltip>
                    </td>
                </tr>
                <tr v-if="!patients.length">
                    <td colspan="6">Brak pacjentów.</td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-container>
</template>
<script>
    export default {
        name: 'PatientList',
        data: () => ({
            patients: [],
        }),
        mounted() {
            this.$http.get('/patients/')
            .then((result) => {
                this.patients = result.data;
            })
            .catch(error => {
                console.log(error);
            })
        }

    }
</script>