const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const navLinks = document.querySelector('[data-nav-links]');
const copyButton = document.querySelector('[data-copy-email]');
const year = document.querySelector('[data-year]');

if (year) {
  year.textContent = new Date().getFullYear();
}

const updateHeader = () => {
  header?.classList.toggle('scrolled', window.scrollY > 12);
};

updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

menuButton?.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  navLinks?.classList.toggle('open', !isOpen);
});

navLinks?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    menuButton?.setAttribute('aria-expanded', 'false');
    navLinks.classList.remove('open');
  });
});

copyButton?.addEventListener('click', async () => {
  const email = copyButton.dataset.email;

  try {
    await navigator.clipboard.writeText(email);
    const originalText = copyButton.textContent;
    copyButton.textContent = 'Email copied';
    window.setTimeout(() => {
      copyButton.textContent = originalText;
    }, 1800);
  } catch {
    window.location.href = `mailto:${email}`;
  }
});
