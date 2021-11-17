$(document).ready(function () {
    initCarrousel();

    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))

    let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    initAcordion();

    $('.desativar').on('click', function (e) {
        e.preventDefault();
    });


    if($('.categoria-link').children('a').length > 0){
    // colocar virgual menos o ultimo
    $('.categoria-link').children('a').each(function (index, el) {
        $(this).html($(this).html() + ',');
    });
    // tirar virgula do ultimo
        let ultimoValor=$('.categoria-link').children('a').last().html().replace(',', '');
        $('.categoria-link').children('a').last().html(ultimoValor);
   
    }

    if($('.home').length>0){
        $('.lista-menu:eq(0)').addClass('ativo')
    }
    

    
});