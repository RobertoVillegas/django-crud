let ShowForm = function () {
  let btn = $(this);
  $.ajax({
    url: btn.attr('data-url'),
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $('#modal-presentacion').modal('show');
    },
    success: function (data) {
      $('#modal-presentacion .modal-content').html(data.html_form);
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
        $('#presentacion-table tbody').html(data.catalogo);
        $('#modal-presentacion').modal('hide');
      } else {
        $('#modal-presentacion .modal-content').html(data.html_form);
      }
    },
  });
  return false;
};

// Create
$('.show-presentacion-form').click(ShowForm);
$('#modal-presentacion').on('submit', '.presentacion-create-form', SaveForm);

//Update
$('#presentacion-table').on(
  'click',
  '.show-presentacion-form-update',
  ShowForm
);
$('#modal-presentacion').on('submit', '.presentacion-update-form', SaveForm);

// Delete
$('#presentacion-table').on(
  'click',
  '.show-presentacion-form-delete',
  ShowForm
);
$('#modal-presentacion').on('submit', '.presentacion-delete-form', SaveForm);
