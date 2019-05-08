<script>
import { createUserModel } from '../models.js'
export default {
  name: 'Index',

  created () {
    this.getUsers()
  },

  data () {
    return {
      users: [],
      tokens: [],
      create: createUserModel,
      recent: {}
    }
  },

  methods: {
    getUsers () {
      this.$api.get('/user/all')
        .then((response) => {
          this.users = response.data
          this.tokens = Array(this.users.length).fill('')
        })
        .catch((error) => {
          this.$toasted.error(error.response.data.message)
        })
    },

    deleteUser (user) {
      this.$api.delete(`/user/${user._id}`)
        .then((response) => {
          if (response.status === 200) {
            this.$toasted.show(`Deleted user with _id ${user._id}`)
            this.getUsers()
            this.recent = user
            delete this.recent._id
          }
        })
        .catch((error) => {
          this.$toasted.error(error.response.data.message)
        })
    },

    createUser (event) {
      event.preventDefault()
      this.$api.post('/user/register', this.create)
        .then((response) => {
          if (response.status === 200) {
            this.$toasted.show('Created new user')
            this.getUsers()
            this.create = createUserModel
          }
        })
        .catch((error) => {
          this.$toasted.error(error.response.data.message)
        })
    },

    createRecent (event) {
      event.preventDefault()
      this.$api.post('/user/recreate', this.recent)
        .then((response) => {
          if (response.status === 200) {
            this.$toasted.show('Recreated recently deleted user')
            this.getUsers()
            this.recent = {}
          }
        })
        .catch((error) => {
          this.$toasted.error(error.response.data.message)
        })
    },

    copyUserToken (idx, user) {
      this.$api.post('/auth/plain', {
        name: user.name,
        password: user.password
      })
        .then((response) => {
          if (response.status === 200) {
            const token = response.data.token
            this.$set(this.tokens, idx, token)
            document.getElementById(`token-${idx}`).select()
            document.execCommand('copy')
            this.$toasted.show('Copied token to clipboard!')
          }
        })
        .catch((error) => {
          this.$toasted.error(error.response.data.message)
        })
    }
  }
}
</script>

<template>
  <div class="content">
    <section class="users">
      <h2>Users</h2>
      <ul class="users">
        <p class="none" v-if="!users.length">
          <i class="fas fa-exclamation-triangle"></i>&nbsp;
          No users in database
        </p>
        <li class="user" v-for="(user, idx) in users" :key="idx">
          <pre>{{ user }}</pre>
          <div class="buttons">
            <button class="button-delete" @click="deleteUser(user)">DELETE</button>
            <button class="button-token" @click="copyUserToken(idx, user)">TOKEN</button>
            <input :id="`token-${idx}`" v-model="tokens[idx]" placeholder="User Access Token" size="50" readonly />
          </div>
        </li>
        <div class="recreate" v-if="Object.keys(recent).length !== 0">
          <button class="button-recreate" @click="createRecent">RECREATE</button>
        </div>
      </ul>
    </section>
    <section class="create">
      <h2>Create User</h2>
      <div class="create">
        <template v-for="(field, idx) in Object.keys(create)">
          <div class="create__field" :key="idx">
            <span>{{ field }}</span>
            <input v-model="create[field]" @keyup.enter="createUser" />
          </div>
        </template>
        <button class="button-create" @click="createUser">CREATE</button>
      </div>
    </section>
  </div>
</template>

<style lang="scss" scoped>
@import '../scss/index.scss';
</style>
