<template>
    <v-app id="inspire">
        <v-navigation-drawer v-model="drawer" app clipped>
            <v-list dense>
                <v-list-item link to="/">
                    <v-list-item-action>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Strona główna</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-group no-action >
                    <template v-slot:activator>
                        <v-list-item-action>
                        <v-icon>mdi-calendar-account</v-icon>
                    </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Wizyta</v-list-item-title>
                        </v-list-item-content>
                    </template>
                    <v-list-item link to="/visit/new">
                        <v-list-item-content>
                            <v-list-item-title>Nowa wizyta</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item link to="/visit/list">
                        <v-list-item-content>
                            <v-list-item-title>Lista wizyt</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
                <v-list-group no-action >
                    <template v-slot:activator>
                        <v-list-item-action>
                        <v-icon>mdi-account</v-icon>
                    </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Pacjent</v-list-item-title>
                        </v-list-item-content>
                    </template>
                    <v-list-item link to="/patient/new">
                        <v-list-item-content>
                            <v-list-item-title>Dodaj pacjenta</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item link to="/patient/list">
                        <v-list-item-content>
                            <v-list-item-title>Lista pacjentow</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
                <v-list-group no-action >
                      <template v-slot:activator>
                          <v-list-item-action>
                          <v-icon>mdi-doctor</v-icon>
                      </v-list-item-action>
                          <v-list-item-content>
                              <v-list-item-title>Dentysta</v-list-item-title>
                          </v-list-item-content>
                      </template>
                      <v-list-item link to="/doctor/new">
                          <v-list-item-content>
                              <v-list-item-title>Dodaj pracownika</v-list-item-title>
                          </v-list-item-content>
                      </v-list-item>
                      <v-list-item link to="/doctor/list">
                          <v-list-item-content>
                              <v-list-item-title>Lista pracowników</v-list-item-title>
                          </v-list-item-content>
                      </v-list-item>
                  </v-list-group>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app color="blue" dark clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title><v-icon size="35">mdi-tooth-outline</v-icon> myDentist</v-toolbar-title>
            <v-spacer></v-spacer>
          <v-menu
            transition="slide-x-transition"
            bottom
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn

                color="blue"
                dark
                v-bind="attrs"
                v-on="on"
              >
                {{ fullName }}
              </v-btn>
            </template>

              <v-list>
                <v-list-item link to="/doctor/profile">
                  <v-list-item-title>Profil</v-list-item-title>
                </v-list-item>
                <v-list-item link to="/doctor/schedule">
                  <v-list-item-title>Grafik pracy</v-list-item-title>
                </v-list-item>
                <v-list-item @click="onLogout">
                  <v-list-item-title>Wyloguj</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
        </v-app-bar>
        <v-content>
            <v-container class="main-container" fluid>
                <router-view/>
            </v-container>
            </v-content>
        <v-footer color="blue" app>
            <span class="white--text">&copy; 2020</span>
        </v-footer>
    </v-app>
</template>

<script>

    export default {
        props: {
            source: String,
        },
        data: () => ({
            drawer: null,
        }),
        methods: {
            onLogout() {
                this.$store.commit({type: 'setAuthenticated', authenticated: false})
                sessionStorage.clear();
                this.$router.push('/login')
            }
        },
        computed: {
          fullName() {
            return this.$store.state.firstName + ' ' + this.$store.state.lastName;
          }
        }
    }
</script>
<style scoped>
    .main-container {
        display: flex;
        align-items: center;
    }
</style>