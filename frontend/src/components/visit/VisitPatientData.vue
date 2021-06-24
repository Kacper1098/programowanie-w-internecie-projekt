<template>
    <v-container fluid>
      <h3>Dane pacjenta</h3>
      <table style="min-width: 350px">
        <tr>
          <td><b>Imię:</b></td><td>{{ patient.name }} {{patient.second_name}}</td>
        </tr>
        <tr>
          <td><b>Nazwisko:</b></td><td>{{ patient.surname }}</td>
        </tr>
        <tr>
          <td><b>Płeć:</b></td><td>{{ patient.sex }}</td>
        </tr>
        <tr>
          <td><b>PESEL:</b></td><td>{{ patient.pesel }}</td>
        </tr>
        <tr>
          <td><b>Wiek:</b></td><td>{{ patient.age }} lat</td>
        </tr>
        <tr>
          <td><b>Ulica:</b></td><td>{{ patient.street }}</td>
        </tr>
        <tr>
          <td><b>Kod pocztowy:</b></td><td>{{ patient.postal_code }}</td>
        </tr>
        <tr>
          <td><b>Miasto:</b></td><td>{{ patient.city }}</td>
        </tr>
        <tr>
          <td><b>Kraj:</b></td><td>{{ patient.country }}</td>
        </tr>
      </table>

    </v-container>
</template>

<script>

    export default {
        name: 'VisitPatientData',
        data: () => ({
          patient: {}
        }),
      mounted() {
          const id = this.$route.params.id;
          const sexMap = {"m": "Mężczyzna", "f": "Kobieta", "u": "Nieznana"}
          this.$http.get(`/visits/${id}`)
        .then(response => {
          this.patient = response.data.patient
          this.patient.sex = sexMap[this.patient.sex]
          this.patient.age = this.getAgeFromPesel(this.patient.pesel)
        })
      },
      methods: {
          getAgeFromPesel(pesel) {
            const nowYear = new Date().getFullYear()
            const twoFirst = pesel.slice(0, 2)
            const nowYearShort = nowYear - 2000
            const prefix = nowYearShort > parseInt(twoFirst) ? "20" : "19"
            const birthday = prefix + twoFirst
            return nowYear - parseInt(birthday)
          }
      }
    };
</script>
