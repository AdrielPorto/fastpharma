jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
jQuery('.quantity').each(function () {
    var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find('.quantity-up'),
        btnDown = spinner.find('.quantity-down'),
        min = input.attr('min'),
        max = input.attr('max');

    btnUp.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue >= max) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });

    btnDown.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });








    //Selects current tab label & shows current tab pane / content, while hiding all other labels and content that is not selected
    const selectTab = element => {

        //stores the active class for tab labels
        const active = document.querySelector('.ativo');

        //stores visible class for tab pane / content
        const visible = document.querySelector('.content-visible');

        //refrences actual element with the corresponding tab pane / content
        //get the element's id from the href of the selected tab label
        //use split method on the href to get the id or '#' which gives us an array of the url and the selected id
        //from the array we grab the index of [1] to isolate the id we want
        const tabContent = document.getElementById(element.href.split('#')[1]);

        //the console log will show the id of the tab label selected
        //console.log(element.href.split('#')[1]);

        //first, if the active class exists on our tab label we remove it
        if (active) {
            active.classList.remove('ativo');
        }

        //add back the active class to the selected tab label
        element.classList.add('ativo');

        //similarly, if the visible class exists on our tab pane / content we remove it
        if (visible) {
            visible.classList.remove('content-visible');
        }

        //add back the visible class to the corresponding tab pane / content
        tabContent.classList.add('content-visible');

    }

    //event delegation
    document.addEventListener('click', event => {
        
        //if a tab label is clicked
        if (event.target.matches('.tab-item')) {
            //run the selectTab function, pass in the click event target 
            event.preventDefault();
            selectTab(event.target);


            //the console log will show which tab label / anchor link is being selected
            //console.log(event.target);
        }
    }, false);





    $('.tabs a').on('click', function () {
        console.log($(this).attr('href'));

        if ($(this).attr('href') === "#item3") {
            $('#item3').removeClass('d-none');
        } else {
            $('#item3').addClass('d-none');
        }
    })



});