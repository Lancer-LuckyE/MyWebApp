<template>
  <div class="home">
    <!--    TODO: implement a header with a signup btn and a login btn-->
    <CommentList></CommentList>
  </div>
</template>

<script>
  // @ is an alias to /src
  import CommentList from '../components/CommentList'

  export default {
    name: 'Home',
    components: {
      CommentList
    }
  }
</script>
