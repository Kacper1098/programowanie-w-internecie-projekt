<template>
    <v-container fluid>
        <h2 class="text-center mb-5">Lista pracowników</h2>
        <v-simple-table>
            <template v-slot:default>
                <thead>
                <tr>
                    <th class="text-left">Imię</th>
                    <th class="text-left">Nazwisko</th>
                    <th class="text-left">PWZ</th>
                    <th class="text-left">Telefon</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="doctor in doctors" :key="doctor.id">
                    <td width="15%">{{ doctor.name }} {{ doctor.second_name }}</td>
                    <td width="15%">{{ doctor.surname}}</td>
                    <td width="15%">{{ doctor.pwz }}</td>
                    <td width="15%">{{ doctor.telephone }}</td>
                </tr>
                <tr v-if="!doctors.length">
                    <td colspan="4">Brak pracowników.</td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-container>
</template>
<script>
    export default {
        name: 'DoctorList',
        data: () => ({
            doctors: [],
        }),
        mounted() {
            this.$http.get('/doctors/')
            .then((result) => {
                this.doctors = result.data;
            })
            .catch(error => {
                console.log(error);
            })
        }

    }
</script>