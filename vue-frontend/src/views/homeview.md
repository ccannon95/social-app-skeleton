<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const username = ref('')
const password = ref('')
const error = ref(null)

async function signup() {
  error.value = null
  const res = await fetch('http://127.0.0.1:8000/api/signup/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username.value,
      password: password.value
    })
  })
  if (res.ok) {
    router.push('/next')
    return
  }
  error.value = await res.json()
}

</script>
<template>
  <input v-model="username" placeholder="username" />
  <input v-model="password" placeholder="password" type="password" />
  <button @click="signup">signup</button>

    <pre v-if="error">{{ error }}</pre>
</template>
