<template>
  <div class="app">
    <div class="title">
      <h1>
        JFlask Admin
        <img :src="require('./assets/badge.svg')" />
      </h1>
      <p><i class="far fa-snowflake"></i>&nbsp; JFlask Admin app for fast-management</p>
    </div>
    <router-view/>
  </div>
</template>
