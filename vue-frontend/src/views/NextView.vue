<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getCSRFToken } from '@/sessions/csrf'

const router = useRouter()

const first_name = ref('')
const last_name = ref('')
const bio = ref('')
const status = ref(null)

onMounted(async () => {
  const response = await fetch('/api/profile/', {
    credentials: 'include'
  })
  if (response.ok) {
    const data = await response.json()
    first_name.value = data.first_name
    last_name.value = data.last_name
    bio.value = data.bio
  }
})

async function save() {
  const response = await fetch('/api/profile/update/', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
    body: JSON.stringify({
      first_name: first_name.value,
      last_name: last_name.value,
      bio: bio.value,
    })
  })
  if (response.ok) {
    router.push('/user')
    return
  }
  status.value = await response.json()
}
</script>

<template>
  <div class="dev">
    <h1>Update Profile</h1>

    <input v-model="first_name" placeholder="First name" />
    <input v-model="last_name" placeholder="Last name" />

    <textarea v-model="bio" placeholder="Bio (max 256 chars)" />

    <button @click="save">Save</button>

  </div>
</template>

<style scoped>
.dev {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
</style>
