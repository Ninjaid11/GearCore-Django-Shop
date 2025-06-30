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