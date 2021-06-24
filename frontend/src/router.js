// router.js
import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/auth/Login.vue';
import NewVisit from "./components/visit/NewVisit";
import Home from "./components/home/Home";
import VisitList from "./components/visit/VisitList";
import Layout from "./components/Layout";
import NewPatient from "./components/patient/NewPatient";
import PatientList from "./components/patient/PatientList";
import Register from "./components/auth/Register";
import Profile from "./components/doctor/Profile";
import Schedule from "./components/doctor/Schedule";
import PatientCard from "./components/patient/PatientCard";
import DoctorList from "./components/doctor/DoctorList";
import NewDoctor from "./components/doctor/NewDoctor";
import EmailConfirm from "./components/auth/EmailConfirm";
import PerformVisit from "./components/visit/PerformVisit";

Vue.use(Router);

export default new Router({
  mode: 'hash',
  base: '/',
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
      name: 'layout',
      component: Layout,
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: '/dashboard',
          name: 'home',
          component: Home,
          meta: {
            requiresAuth: true
          },
        },
        {
          path: '/visit/new',
          name: 'new_visit',
          component: NewVisit
        },
        {
          path: '/visit/list',
          name: 'visit_list',
          component: VisitList
        },
        {
          path: '/visit/perform/:id',
          name: 'visit_perform',
          component: PerformVisit
        },
        {
          path: '/patient/new',
          name: 'new_patient',
          component: NewPatient
        },
        {
          path: '/patient/list',
          name: 'patient_list',
          component: PatientList
        },
        {
          path: '/patient/card/:id',
          name: 'patient_card',
          component: PatientCard
        },
        {
          path: '/doctor/profile',
          name: 'doctor_profile',
          component: Profile
        },
        {
          path: '/doctor/schedule',
          name: 'doctor_schedule',
          component: Schedule
        },
        {
          path: '/doctor/new',
          name: 'new_doctor',
          component: NewDoctor
        },
        {
          path: '/doctor/list',
          name: 'doctor_list',
          component: DoctorList
        },
      ]
    },
    {
      path: '/email-confirm',
      name: 'email_confirm',
      component: EmailConfirm,
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        hideForAuth: true
      }
    },

  ]
});
