<template>
  <div class="app">
    <h1>JFlask Admin</h1>
    <router-view/>
  </div>
</template>

<style lang="scss">
html, body, .app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  background-color: #1D2733;
}

.app {
  h1 {
    color: white;
    padding-left: 20px;
  }
}
</style>
