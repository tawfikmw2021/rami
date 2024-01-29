const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    allowedHosts: 'all',
    port:8085,
    host:'0.0.0.0'
  }
})
