<script>
export default {
  name: 'Index',

  created () {
    this.getUsers()
  },

  data () {
    return {
      users: [],
      create: {
        username: '',
        password: ''
      }
    }
  },

  methods: {
    getUsers () {
      this.$api.get('/user/all')
        .then((response) => {
          this.users = response.data
        })
    },

    deleteUser (userId) {
      this.$api.delete(`/user/${userId}`)
        .then((response) => {
          if (response.status === 200) {
            this.getUsers()
          }
        })
    },

    createUser (event) {
      event.preventDefault()
      this.$api.post('/user/register', this.create)
        .then((response) => {
          if (response.status === 200) {
            this.getUsers()
            this.create = {
              username: '',
              password: ''
            }
          }
        })
    }
  }
}
</script>

<template>
  <div class="content">
    <ul class="users">
      <li class="user" v-for="(user, idx) in users" :key="idx">
        <pre>{{ user }}</pre>
        <button class="button-delete" @click="deleteUser(user._id)">DELETE</button>
      </li>
    </ul>
    <div class="create">
      <div class="create__field">
        <span>username</span>
        <input v-model="create.username" @keyup.enter="createUser"/>
      </div>
      <div class="create__field">
        <span>password</span>
        <input v-model="create.password" @keyup.enter="createUser"/>
      </div>
      <button class="button-create" @click="createUser">CREATE</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.user {
  width: 50%;
  color: white;

  pre {
    background-color: #384B5C;
    padding: 5px;
  }
}

.create {
  width: 50%;
  padding: 1.5em;

  &__field {
    margin-bottom: 10px;

    span {
      font-size: 1.2em;
      color: white;
      margin: 5px;
    }

    input {
      color: lightgray;
      padding: 5px;
      font-size: 1.2em;
      width: 50%;
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
  border: 1px solid lightgray;
  border-radius: 3px;
  font-size: 1em;
}

.button-delete {
  color: white;
  background-color: rgb(214, 105, 105);
}

.button-create {
  color: white;
  background-color: rgb(113, 122, 206);
}
</style>
