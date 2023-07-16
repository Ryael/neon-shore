/* Swiper */

var swiper = new Swiper(".mySwiper", {
  navigation: {
    nextEl: ".arrow-right",
    prevEl: ".arrow-left"
  },
  effect: "fade",
  loop: "infinite",
  pagination: {
    el: ".swiper-pagination",
    type: "bullets",
    clickable: "boolean"
  }
});

swiper.on("slideChange", function (sld) {
  tl.seek(0);
});

/* Painting Animation */

const frames = 20;

gsap.set(".cover img", {
  maskSize: `${frames * 100}% 100%`
});

const tl = gsap.timeline({ repeat: 0, yoyo: false });

tl.to(".cover img", {
  duration: 2.5,
  maskPosition: `-${(frames - 1) * 100}% 0%`,
  ease: `steps(${frames - 1})`
});

/* Mobile Navigation */

const app = (() => {
  let body;
  let menu;
  let menuItems;

  const init = () => {
    body = document.querySelector('body');
    menu = document.querySelector('.menu-icon');
    menuItems = document.querySelectorAll('.mobile-list-item');

    applyListeners();
  }

  const applyListeners = () => {
    menu.addEventListener('click', () => toggleClass(body, 'mobile-navigation-active'));
  }

  const toggleClass = (element, stringClass) => {
    if(element.classList.contains(stringClass))
      element.classList.remove(stringClass);
    else
      element.classList.add(stringClass);
  }

  init();
})();

/* Quantity Input */

// Disable +/- buttons outside 1-99 range.
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load.
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed.
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity.
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Decrement quantity.
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Update quantity on click
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})
