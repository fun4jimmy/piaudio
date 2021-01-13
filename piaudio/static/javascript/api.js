const services = {
  list: function () {
    return fetch("/api/services/")
      .then(response => {
        switch (response.status) {
          case 200:
            return response.json();
          default:
            throw new Error(`services.list() failed: ${response.statusText}.`);
        }
      });
  },
  get: function (service_id) {
    return fetch(`/api/service/${service_id}`)
      .then(response => {
        switch (response.status) {
          case 200:
            return response.json();
          case 404:
            return null;
          default:
            throw new Error(`services.get(${service_id}) failed: ${response.statusText}.`);
        }
      });
  },
  set: function (service_id, state) {
    return fetch(`/api/service/${service_id}?state=${state}`, { method: "POST" })
      .then(response => {
        if (response.ok) {
          return;
        }

        switch (response.status) {
          case 404:
          case 500:
          default:
            throw new Error(`services.set(${service_id}, ${state}) failed: ${response.statusText}.`);
        }
      });
  },
};
