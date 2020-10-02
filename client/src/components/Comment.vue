<template>
  <li class="list-group-item">
    <p class="text-left"><span>{{comment.user}}</span>:
      <span class="float-right"><button @click="deleteComment" class="comment-delete_btn btn btn-outline-danger py-0"
                                        type="button">
						Delete
					</button></span>
    </p>
    <p class="text-left pl-4 m-0">{{comment.comment}}</p>
  </li>
</template>

<script>
  export default {
    name: "Comment",
    props: {
      comment: Object,
      index: Number,
    },
    methods: {
      deleteComment() {
        // TODO: ajax to update with database
        return 0;
      },
    },
  }
</script>

<style scoped>

</style>
