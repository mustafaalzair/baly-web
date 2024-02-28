var swiper = new Swiper('.blog-slider', {
  spaceBetween: 30,
  effect: 'fade',
  loop: true,
  mouseWheel: {
    invert: false,
  },
  // autoHeight: true
  pagination: {
    el: '.blog-slider__pagination',
    clickable: true,
  },
  autoplay: {
    delay: 5000, // الفترة الزمنية بالمللي ثانية بين الانتقالات
    disableOnInteraction: false, // تعطيل تلقائيًا عند التفاعل مع المستخدم
  },
});