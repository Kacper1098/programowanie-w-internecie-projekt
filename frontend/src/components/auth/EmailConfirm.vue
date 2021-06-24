<script>
export default {
  name: 'EmailConfirm',
  created() {
    this.$store.dispatch('showAlert', {text: "Email został potwierdzony!", color: 'green'});
    this.$router.push('/');
  }
}
</script>
