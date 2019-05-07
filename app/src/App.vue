<template>
  <div class="app">
    <div class="title">
      <h1>
        JFlask Admin
        <img :src="require('./assets/badge.svg')" />
      </h1>
      <p><i class="far fa-snowflake"></i>&nbsp; Jflask Admin app for fast-management</p>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');

html, body, .app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  background-color: #100D24;
  font-family: 'Montserrat', sans-serif;
}

.title {
  padding: 2.5em;
  padding-bottom: 1em;

  .fa-snowflake {
    color: #43b2ed;
  }

  h1 {
    color: #00FF9D;
    font-weight: 700;
    margin: 0;
  }

  p {
    color: #76F2D7;
    margin: 0;
  }
}
</style>
