<template>
    <v-container fluid>
        <h2 class="text-center mb-5">Lista wizyt</h2>
        <v-simple-table>
            <template v-slot:default>
                <thead>
                <tr>
                    <th class="text-left">Data</th>
                    <th class="text-left">Godzina od</th>
                    <th class="text-left">Godzina do</th>
                    <th class="text-left">Pacjent</th>
                    <th class="text-left">Lekarz</th>
                    <th class="text-left">Akcje</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="visit in visits" :key="visit.id">
                    <td width="15%">{{ visit.date }}</td>
                    <td width="10%">{{ visit.start_time }}</td>
                    <td width="10%">{{ visit.end_time }}</td>
                    <td width="30%">{{ visit.patient.name }} {{ visit.patient.surname }} ({{ visit.patient.pesel }})</td>
                    <td width="30%">{{ visit.doctor.name }} {{ visit.doctor.surname }} ({{ visit.doctor.pwz }})</td>
                    <td width="5%">
                        <v-tooltip left>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn color="primary" fab small elevation="0" v-bind="attrs" v-on="on" :to="`perform/${visit.id}`">
                                    <v-icon>mdi-application-import</v-icon>
                                </v-btn>
                            </template>
                            <span>Przeprowadź wizytę</span>
                        </v-tooltip>
                    </td>
                </tr>
                <tr v-if="!visits.length">
                    <td colspan="6">Brak wizyt.</td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-container>
</template>
<script>
    export default {
        name: 'VisitList',
        data: () => ({
            visits: [],
        }),
        mounted() {
            this.$http.get(`/visits/`,)
            .then((result) => {
                this.visits = result.data;
            })
            .catch(error => {
                console.log(error);
            })
        }

    }
</script>
