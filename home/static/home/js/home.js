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
