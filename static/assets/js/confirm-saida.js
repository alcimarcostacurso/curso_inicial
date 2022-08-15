$(".btn-sair").click(function(){
     $form = $(this).closest('form');

     Swal.fire({
      title: '<strong class="text-info">Você tem certeza?</strong>',
      text: 'Isso irá registrar a saída!',
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Cadastrar saída!'
}).then((result) => {
   if (result.isConfirmed) {
       $form.submit()
          }
        })
   return false
});
