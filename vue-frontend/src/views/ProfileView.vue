<script setup>
import { getCSRFToken } from '@/sessions/csrf';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const profile = ref(null)

onMounted(async () => {
  const res = await fetch('/api/profile/', { credentials: 'include' })
  if (res.ok) profile.value = await res.json()
})

async function logout() {
  const res = await fetch('/api/profile/logout/', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    }
  })
  if (res.ok) {
    router.push('/')
  }
}

</script>
<template>
<div v-if="profile" class="dev">
  <div>{{ profile.first_name }}</div>
  <div>{{ profile.last_name }}</div>
  <div>{{ profile.bio }}</div>
  <button @click="logout">Logout</button>
</div>

</template>
<style scoped>
.dev {
  color: aliceblue;
}
</style>
