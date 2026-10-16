// Cookie consent (styles in assets/consent.css). Adds the banner and the settings panel to the page.
// Paths start from the site root (/assets/…), so they also work on the 404 page at any address.
//
// The banner shows until a choice is made: Accept all, Reject all, or Settings (which opens the panel).
// Escape closes it without accepting anything, until the next visit. Any element with
// data-cookie-settings (the footer link, the Privacy Policy link) opens the panel too.
//
// The choice is kept in this browser (localStorage "onwun-consent"). Analytics stay off until someone
// accepts them: window.onwunConsent.analytics says whether they have, and an "onwun:consent" event fires
// on document whenever the choice changes. assets/analytics.js (Google Analytics) waits for it.
(() => {
  const KEY = 'onwun-consent';
  const DISMISSED = 'onwun-consent-dismissed';

  // Storage can be unavailable (private windows, blocked storage); then the banner just shows each visit
  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; }
  }
  function write(choice) {
    try { localStorage.setItem(KEY, JSON.stringify(choice)); } catch (e) { /* not essential */ }
  }

  const saved = read();
  window.onwunConsent = { analytics: !!(saved && saved.analytics) };

  function choose(analytics) {
    write({ analytics, date: new Date().toISOString() });
    window.onwunConsent = { analytics };
    document.dispatchEvent(new CustomEvent('onwun:consent', { detail: { analytics } }));
    hideBanner();
    if (panel.open) panel.close();
  }

  const CLOSE_ICON = '<img src="/assets/icons/close.svg" alt="" width="16" height="16">';

  const banner = document.createElement('section');
  banner.className = 'consent';
  banner.setAttribute('aria-label', 'Cookies');
  banner.hidden = true;
  banner.innerHTML = `
    <p class="consent__text">We use cookies to run the site and, with your OK, to see how it’s used. <a href="/privacy#cookies">Privacy Policy</a></p>
    <div class="consent__actions">
      <div class="consent__choices">
        <button class="consent-button" type="button" data-choice="accept">Accept all</button>
        <button class="consent-button" type="button" data-choice="reject">Reject all</button>
      </div>
      <button class="consent__settings" type="button" data-cookie-settings>Settings</button>
    </div>`;

  const panel = document.createElement('dialog');
  panel.className = 'consent-panel';
  panel.setAttribute('aria-labelledby', 'consent-panel-title');
  panel.innerHTML = `
    <div class="consent-panel__top">
      <p class="consent-panel__label">Cookie settings:</p>
      <button class="consent-panel__close" type="button" aria-label="Close">${CLOSE_ICON}</button>
    </div>
    <h2 class="consent-panel__title" id="consent-panel-title">Choose what you’re happy with.</h2>
    <div class="consent-panel__row">
      <div>
        <p class="consent-panel__name" id="consent-essential">Essential</p>
        <p class="consent-panel__desc">Keep the site working, like remembering your cookie choice. These can’t be switched off.</p>
      </div>
      <div class="consent-panel__control">
        <span class="consent-panel__always">Always on</span>
        <input class="switch" type="checkbox" role="switch" checked disabled aria-labelledby="consent-essential">
      </div>
    </div>
    <div class="consent-panel__row">
      <div>
        <label class="consent-panel__name" id="consent-analytics" for="consent-analytics-switch">Analytics</label>
        <p class="consent-panel__desc">Help us see which pages and projects people find useful, so we can improve the site. Anonymous and off unless you turn them on.</p>
      </div>
      <div class="consent-panel__control">
        <input class="switch" id="consent-analytics-switch" type="checkbox" role="switch">
      </div>
    </div>
    <div class="consent-panel__actions">
      <button class="consent-button" type="button" data-choice="reject">Reject all</button>
      <button class="consent-button" type="button" data-choice="accept">Accept all</button>
      <button class="consent-button consent-button--save" type="button" data-choice="save">Save choices</button>
    </div>`;

  const analyticsSwitch = panel.querySelector('#consent-analytics-switch');

  function showBanner() {
    banner.hidden = false;
    requestAnimationFrame(() => requestAnimationFrame(() => banner.classList.add('is-in')));
  }

  function hideBanner() {
    banner.classList.remove('is-in');
    banner.hidden = true;
  }

  function openPanel() {
    // nothing non-essential is switched on in advance: the switch shows the saved choice, or off
    analyticsSwitch.checked = window.onwunConsent.analytics;
    panel.showModal();
  }

  function onChoice(e) {
    const button = e.target.closest('[data-choice]');
    if (!button) return;
    const choice = button.dataset.choice;
    choose(choice === 'accept' || (choice === 'save' && analyticsSwitch.checked));
  }

  banner.addEventListener('click', onChoice);
  panel.addEventListener('click', (e) => {
    if (e.target === panel) panel.close(); // a click on the dimmed backdrop
    onChoice(e);
  });
  panel.querySelector('.consent-panel__close').addEventListener('click', () => panel.close());

  // Settings, from the banner, the footer or the Privacy Policy
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-cookie-settings]');
    if (!trigger) return;
    e.preventDefault();
    openPanel();
  });

  // Escape closes the banner without accepting anything (the panel closes itself on Escape)
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || banner.hidden || panel.open) return;
    hideBanner();
    try { sessionStorage.setItem(DISMISSED, '1'); } catch (err) { /* not essential */ }
  });

  function init() {
    document.body.append(banner, panel);
    let dismissed = false;
    try { dismissed = sessionStorage.getItem(DISMISSED) === '1'; } catch (e) { /* not essential */ }
    if (saved || dismissed) return;
    // slides up once the page has loaded, so it doesn't compete with the page's own entrance
    const show = () => setTimeout(showBanner, 600);
    if (document.readyState === 'complete') show();
    else window.addEventListener('load', show, { once: true });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
