const services = {
  list: async function() {
    const response = await fetch("/api/services/")
    return response.json()
  },
  get: async function(service_id) {
    const response = await fetch(`/api/service/${service_id}`)
    return response.json()
  },
  set: async function(service_id, state) {
    const response = await fetch(`/api/service/${service_id}?state=${state}`, { method: "POST" })
    return response
  },
}
