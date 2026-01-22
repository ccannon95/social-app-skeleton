import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { checkSession } from './sessions/sessionAuth'

async function bootstrap() {
  const user = await checkSession()
  const app = createApp(App)

  app.use(createPinia())
  app.use(router)

  if (!user) {
    router.push('/')
  } else {
    router.push('/user') //later profile or feed
  }

  app.mount('#app')
}

bootstrap()
