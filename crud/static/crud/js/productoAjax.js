let ShowForm = () => {
  let btn = $(this);
  $.ajax({
    url: btn.attr('data-url'),
    type: 'get',
    dataType: 'json',
    beforeSend: () => {
      $('#modal-producto').modal('show');
    },
    success: (data) => {
      $('#modal-producto .modal-content').html(data.html_form);
    },
  });
};

let SaveForm = () => {
  let form = $(this);
  $.ajax({
    url: form.attr('data-url'),
    data: form.serialize(),
    type: form.attr('method'),
    dataType: 'json',
    success: (data) => {
      if (data.form_is_valid) {
        $('#producto-table tbody').html(data.producto);
        $('#modal-producto').modal('hide');
      } else {
        $('#modal-producto .modal-content').html(data.html_form);
      }
    },
  });
  return false;
};

// Create
$('.show-producto-form').click(ShowForm);
$('#modal-producto').on('submit', '.producto-create-form', SaveForm);

//Update
$('#producto-table').on('click', '.show-producto-form-update', ShowForm);
$('#modal-producto').on('submit', '.producto-update-form', SaveForm);

// Delete
$('#producto-table').on('click', '.show-producto-form-delete', ShowForm);
$('#modal-producto').on('submit', '.producto-delete-form', SaveForm);
