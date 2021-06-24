<template>
  <v-container>
    <h2 class="text-center">Grafik pracy</h2>
  <v-row>
    <v-col>

       <v-sheet
      tile
      height="54"
      class="d-flex"
    >
      <v-btn
        icon
        class="ma-2"
        @click="prevWeek"
      >
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
         <v-spacer></v-spacer>
         <b>{{ month }}</b>
      <v-spacer></v-spacer>
      <v-btn
        icon
        class="ma-2"
        @click="nextWeek"
      >
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-sheet>
      <v-sheet height="700">
        <v-calendar
          ref="calendar"
          locale="pl"
          :now="today"
          :events="events"
          v-model="today"
          color="primary"
          type="week"
          :event-color="getEventColor"
          @click:date="setSchedule"
        ></v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
    <ScheduleDialog :dialog="dialog" :date="pickedDate" @closeDialog="dialog = false" @refresh="getSchedules"
                    :scheduleStart="scheduleStart" :scheduleEnd="scheduleEnd"/>
  </v-container>
</template>
<script>
  import ScheduleDialog from "./ScheduleDialog";
  export default {
    components: {ScheduleDialog},
    data: () => ({
      today: new Date().toISOString().slice(0, 10),
      dialog: false,
      pickedDate: {},
      events: [],
      month: '',
      apiSchedules: {},
      scheduleStart: '',
      scheduleEnd: '',
    }),
    mounted () {
      this.$refs.calendar.scrollToTime('8:00')
      this.getSchedules()
    },
    methods: {
      setSchedule(date) {
        this.pickedDate = date;
        this.scheduleStart = this.apiSchedules[date.date] ? this.apiSchedules[date.date].start : '08:00'
        this.scheduleEnd = this.apiSchedules[date.date] ? this.apiSchedules[date.date].end : '16:00'
        this.dialog = true;
      },
      prevWeek() {
        this.$refs.calendar.prev();
        this.getSchedules();
      },
      nextWeek() {
        this.$refs.calendar.next();
        this.getSchedules();
      },
      getSchedules() {
        let date_from = new Date(this.$refs.calendar.lastStart.date);
        let date_to = new Date(this.$refs.calendar.lastEnd.date);
        date_from.setDate(date_from.getDate() - 7)
        date_to.setDate(date_to.getDate() + 7)
        date_from = date_from.toISOString().slice(0, 10)
        date_to = date_to.toISOString().slice(0, 10)

        this.$http.get(`/doctors_schedule/?date_from=${date_from}&date_to=${date_to}`)
        .then(response => {
          this.events = [];
          this.apiSchedules = response.data
          const name = `${this.$store.state.firstName} ${this.$store.state.lastName}`
          for (const [key, value] of Object.entries(response.data)) {
            this.events.push({
              name,
              start: `${key}  ${value.start}`,
              end: `${key}  ${value.end}`,
              color: 'teal'
            })
          }
          this.setMonth();
        })
      },
      setMonth() {
        let date_from = new Date(this.$refs.calendar.lastStart.date);
        let date_to = new Date(this.$refs.calendar.lastEnd.date);
        let date = date_from
        if(date_to.getDate() >= 4)
          date = date_to
        this.month = new Date(date).toLocaleString('pl-pl', { month: 'long', year: 'numeric' })
      },
      getEventColor(event){
        return event.color
      }
    },
  }
</script>
