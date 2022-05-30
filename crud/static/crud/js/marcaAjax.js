let ShowMarcaForm = function () {
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

let SaveMarcaForm = function () {
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
$('.show-marca-form').click(ShowMarcaForm);
$('#modal-marca').on('submit', '.marca-create-form', SaveMarcaForm);

//Update
$('#marca-table').on('click', '.show-marca-form-update', ShowMarcaForm);
$('#modal-marca').on('submit', '.marca-update-form', SaveMarcaForm);

// Delete
$('#marca-table').on('click', '.show-marca-form-delete', ShowMarcaForm);
$('#modal-marca').on('submit', '.marca-delete-form', SaveMarcaForm);
