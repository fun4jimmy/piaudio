const ui = {
  // Initialise the ui for the application.
  initialise: function () {
    // Register the click functions for the service check boxes.
    const serviceCheckBox = ui.selectServiceCheckBox();

    serviceCheckBox.click(function () {
      const serviceId = $(this).attr("id");
      const requestedState = $(this).prop("checked") ? "active" : "inactive";

      // We don't add a .then() handler as we don't need to do anything on success that isn't covered by .finally().
      services.set(serviceId, requestedState)
        .catch(error => {
          // handle error
        })
        .finally(() => {
          setTimeout(ui.update, 500);
        });
    });
    ui.update();
  },
  // Update the ui for the application.
  update: function () {
    // Update all the service check boxes to make sure they match the service state.
    const serviceCheckBox = ui.selectServiceCheckBox();

    serviceCheckBox.each(function (index) {
      const serviceId = $(this).attr("id");

      services.get(serviceId)
        .then((service) => {
          if (service !== null) {
            $(this).prop("checked", service.state === "active");
          } else {
            // handle service not found
          }
        })
        .catch(error => {
          // Uncheck any services whose get call failed so they are not displayed as active.
          $(this).prop("checked", false);
        });
    });
  },
  // Selects the service check box elements.
  selectServiceCheckBox: function () {
    return $(".service input[type='checkbox']");
  },
}
// Invoke initialise as soon as the application document is ready.
$(document).ready(ui.initialise);
