/* Slider */

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
