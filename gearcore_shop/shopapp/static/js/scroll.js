document.addEventListener('DOMContentLoaded', function () {
  const scrollLink = document.querySelector('.scroll-down');
  const target = document.querySelector('#brands');

  if (scrollLink && target) {
    scrollLink.addEventListener('click', function (e) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    });
  }
});