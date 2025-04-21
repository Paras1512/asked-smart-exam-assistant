// === Smooth Background Parallax Movement ===
document.addEventListener('mousemove', (e) => {
    const moveFactor = 0.03;
    const x = (window.innerWidth - e.pageX * moveFactor);
    const y = (window.innerHeight - e.pageY * moveFactor);
    document.body.style.backgroundPosition = `${x}px ${y}px`;
});
