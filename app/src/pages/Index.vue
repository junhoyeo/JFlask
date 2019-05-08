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
            <input :id="`token-${idx}`" v-model="tokens[idx]" size="50" readonly />
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
h2 {
  color: #CFCFD3;
  font-size: 1.5em;
  padding-left: 0.5rem;
}

section {
  padding-left: 1em;
  margin-bottom: 2em;
}

.none {
  color: #D67AFE;
}

.user {
  width: 80%;
  color: white;

  pre {
    color: #76F2D7;
    border: 1px solid #3D59FE;
    background-color: #1E1F44;
    padding: 5px;
  }

  input {
    color: lightgray;
    background-color: #100D24;
    border: none;
    border-bottom: 1px solid lightgray;
    font-size: 0.8em;
    margin-left: 0.5em;
  }
}

div.create {
  display: table;
  width: 70%;
  padding: 1.5em;
  padding-top: 0;

  &__field {
    margin-bottom: 10px;
    display: table-row;

    span {
      width: 120px;
      display: table-cell;
      font-size: 1.2em;
      color: white;
    }

    input {
      width: 99%;
      display: table-cell;
      color: lightgray;
      padding: 5px;
      font-size: 1.2em;
      border: 1px solid lightgray;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      border-bottom: 1px solid rgb(194, 194, 194);
    }
  }

  button {
    display: block;
  }
}

button {
  color: #00FF9D;
  border: none;
  border-radius: 3px;
  font-size: 1em;
}

.button-delete {
  background-color: #AA57E2;
}

.button-create {
  margin-top: 0.5em;
  background-color: #3D59FE;
}

.button-recreate {
  margin-top: 0.5em;
  background-color: #076FD7;
}

.button-token {
  margin-left: 0.5em;
  background-color: #3D59FE;
}
</style>
