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
      create: createUserModel,
      recent: {}
    }
  },

  methods: {
    getUsers () {
      this.$api.get('/user/all')
        .then((response) => {
          this.users = response.data
        })
    },

    deleteUser (user) {
      this.$api.delete(`/user/${user._id}`)
        .then((response) => {
          if (response.status === 200) {
            this.getUsers()
            this.recent = user
            delete this.recent._id
          }
        })
    },

    createUser (event) {
      event.preventDefault()
      this.$api.post('/user/register', this.create)
        .then((response) => {
          if (response.status === 200) {
            this.getUsers()
            this.create = createUserModel
          }
        })
    },

    createRecent (event) {
      event.preventDefault()
      this.$api.post('/user/recreate', this.recent)
        .then((response) => {
          if (response.status === 200) {
            this.getUsers()
            this.recent = {}
          }
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
          <button class="button-delete" @click="deleteUser(user)">DELETE</button>
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
            <input v-model="create[field]" @keyup.enter="createUser"/>
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
</style>
