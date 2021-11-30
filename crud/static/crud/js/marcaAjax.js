$(document).ready(function () {
  let ShowForm = function () {
    let btn = $(this);
    $.ajax({
      url: btn.attr('data-url'),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $('#modal-marca').modal('show');
      },
      success: function (data) {
        $('#modal-marca .modal-content').html(data.html_form);
      },
    });
  };

  let SaveForm = function () {
    let form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      type: form.attr('method'),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $('#marca-table tbody').html(data.catalogo);
          $('#modal-marca').modal('hide');
        } else {
          $('#modal-marca .modal-content').html(data.html_form);
        }
      },
    });
    return false;
  };

  // Create
  $('.show-marca-form').click(ShowForm);
  $('#modal-marca').on('submit', '.marca-create-form', SaveForm);

  //Update
  $('#marca-table').on('click', '.show-marca-form-update', ShowForm);
  $('#modal-marca').on('submit', '.marca-update-form', SaveForm);

  // Delete
  $('#marca-table').on('click', '.show-marca-form-delete', ShowForm);
  $('#modal-marca').on('submit', '.marca-delete-form', SaveForm);
});
