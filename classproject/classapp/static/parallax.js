const studentBox = document.querySelector('.student-box');

window.addEventListener('mousemove', (event) => {
  const { pageX, pageY } = event;
  const boxWidth = studentBox.offsetWidth;
  const boxHeight = studentBox.offsetHeight;

  // Calculate parallax offsets based on mouse position and box dimensions
  const xOffset = (pageX - window.innerWidth / 2) / (boxWidth / 2);
  const yOffset = (pageY - window.innerHeight / 2) / (boxHeight / 2);

  // Apply parallax effect using transform3d
  studentBox.style.transform = `translate3d(${xOffset}px, ${yOffset}px, 0)`;
});