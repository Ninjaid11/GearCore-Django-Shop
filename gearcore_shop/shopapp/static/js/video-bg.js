document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('video-background');
  const videoElement = document.getElementById('bg-video');
  if (!container || !videoElement) return;

  const videos = JSON.parse(container.getAttribute('data-videos'));
  let videoIndex = 0;

  function fadeOutIn(nextVideoSrc) {
    videoElement.style.transition = 'opacity 1.5s';
    videoElement.style.opacity = 0;

    setTimeout(() => {
      videoElement.src = nextVideoSrc;
      videoElement.load();
      videoElement.play();
      videoElement.style.opacity = 1;
    }, 1500);
  }

  videoElement.src = videos[videoIndex];
  videoElement.load();
  videoElement.play();

  videoElement.addEventListener('ended', () => {
    videoIndex = (videoIndex + 1) % videos.length;
    fadeOutIn(videos[videoIndex]);
  });
});

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