const ui = {
  // Initialise the ui for the application.
  initialise: function () {
    // Register the click functions for the service check boxes.
    const serviceCheckBox = ui.selectServiceCheckBox();

    serviceCheckBox.click(function () {
      const serviceId = $(this).attr("id");

      services.set(serviceId, "active")
        .then((response) => {
          if (!response.ok) {
            // todo : display error
          }
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
          $(this).prop("checked", service.state === "active");
        })
        .catch(error => {
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
