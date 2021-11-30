$(document).ready(function () {
  $('#marcaBtn').click(function () {
    var pk = $(this).data('pid');
    $('#myModal').modal('show');
  });
  $('#myModal').on('show.bs.modal', function (event) {
    var modal = $(this);
    var pk = $(this).data('pid');
    $.ajax({
      data: { pk: pk },
      url: "{% url 'search:load_paper' %}",
      context: document.body,
      error: function (response, error) {
        alert(error);
      },
    }).done(function (response) {
      modal.html(response);
    });
  });
});
