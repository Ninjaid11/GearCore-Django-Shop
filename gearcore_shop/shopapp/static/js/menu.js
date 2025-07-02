document.addEventListener('DOMContentLoaded', () => {
  const dropdownBtn = document.querySelector('.dropdown-btn');
  const dropdownContent = document.querySelector('.dropdown-content');
  const submenuTrigger = document.querySelector('.submenu-trigger');
  const submenu = document.querySelector('.submenu');

  dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    dropdownContent.classList.toggle('show');
  });

  submenuTrigger.addEventListener('click', (e) => {
    e.stopPropagation();
    submenu.classList.toggle('show');
  });

  document.addEventListener('click', () => {
    dropdownContent.classList.remove('show');
    submenu.classList.remove('show');
  });
});