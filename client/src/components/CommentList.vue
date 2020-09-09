<template>
	<div>
		Users Comments:<br>
		<p v-show="comments.length === 0">There is no comment at this moment.</p>
		<ul class="list-group">
			<Comment v-for="(comment, index) in comments" :key="index" :index="index" :comment="comment"></Comment>
		</ul>
	</div>
</template>

<script>
	import Comment from "@/components/Comment";
	import axios from 'axios';
	export default {
		data() {
			// comments list is loaded from database
			return {
				comments: [],
			}
		},
		components: {
			Comment,
		},
		created() {

		},
		methods: {
			getAllComment() {
				//TODO: use https in production
				const path = '/api/comments';
				// axios.get(path).then((res) => {
				// 	this.comments = res.data.comments;
				// }).catch((error) => {
				// 	console.error(error);
				// })
			},
			updateComments(comment) {
				this.comments.push(comment);
			},
			removeComment(index) {
				this.comments.splice(index, 1);
			},
		}
	}

</script>

<style scoped>
	.comment-delete_btn {
		font-size: xx-small;
	}
</style>
