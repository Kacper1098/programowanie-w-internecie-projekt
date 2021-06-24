<template>
 <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
     <v-card>
        <v-card-title>
          <span class="headline">Godziny pracy dla dnia {{date.date}}</span>
        </v-card-title>
        <v-card-text>
          <v-select
            :items="hours_from"
            label="Od"
            v-model="hour_from"
            no-data-text="Brak dostępnych godzin."
            required
          ></v-select>
          <v-select
            :items="hours_to"
            label="Od"
            v-model="hour_to"
            no-data-text="Brak dostępnych godzin."
            required
          ></v-select>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="closeDialog"
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

  name: 'ScheduleDialog',
  props: ['dialog', 'date', 'scheduleStart', 'scheduleEnd'],
  data: () => ({
    requiredRule: [
      v => !!v || 'To pole jest wymagane',
    ],
    hours_from: [],
    hour_from: '08:00',
    hours_to: [],
    hour_to: '16:00'
  }),
  mounted() {
    this.generateHours();
  },
  methods: {
    closeDialog() {
      this.$emit('closeDialog')
    },
    generateHours() {
      let hours = []
      for(let hour = 0; hour < 24; hour++) {
        if (hour < 10) {
          hours.push(`0${hour}:00`)
          hours.push(`0${hour}:30`)
        } else {
          hours.push(`${hour}:00`)
          hours.push(`${hour}:30`)
        }
      }
      this.hours_from = hours;
      this.hours_to = hours;

    },
    onSave() {
      this.$http.post(
          `/doctors_hours/?date=${this.date.date}&hour_from=${this.hour_from}&hour_to=${this.hour_to}`
      ).then(() => {
        this.closeDialog();
        this.$emit('refresh');
      })

    }
  },
  watch: {
    scheduleStart: function(newVal, oldVal) {
      this.hour_from = newVal.slice(0, 5)
    },
    scheduleEnd: function(newVal, oldVal) {
      this.hour_to = newVal.slice(0, 5)
    }
  }
};
</script>
