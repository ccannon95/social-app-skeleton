<script setup>
import { getCSRFToken } from '@/sessions/csrf';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const username = ref('')
const password = ref('')

const error = ref(null)

async function signup() {
  error.value = null
  const response = await fetch('/api/signup/', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
    body: JSON.stringify ({
      username: username.value,
      password: password.value
    })
  })
  if (response.ok) {
    router.push('/next')
    return
  }
  error.value = await response.json()
}
</script>
<template>
  <div class="dev">
    <h1>signup</h1>
    <input v-model="username" placeholder="Email">
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="signup">Submit</button>
    <p>{{ error }}</p>
  </div>

</template>
<style scoped>
.dev {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
</style>
