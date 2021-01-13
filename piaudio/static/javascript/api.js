const services = {
  list: async function () {
    return fetch("/api/services/")
      .then(response => {
        if (!response.ok) {
          // indicate error
          return null;
        }
        return response.json();
      });
  },
  get: async function (service_id) {
    return fetch(`/api/service/${service_id}`)
      .then(response => {
        if (!response.ok) {
          // indicate error
          return null;
        }
        return response.json();
      })
  },
  set: async function (service_id, state) {
    return fetch(`/api/service/${service_id}?state=${state}`, { method: "POST" })
      .then(response => {
        return response;
      })
  },
};
