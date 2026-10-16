// Google Analytics (GA4), only with consent. Loaded after assets/consent.js on every page.
//
// Nothing is loaded or sent until the visitor accepts analytics (Accept all, or Analytics switched on
// in Cookie settings). If they switch it off again, sending stops straight away and Google's cookies
// are removed. The property is "Onwun website" in analytics.google.com.
(() => {
  const GA_ID = 'G-ZN8PXP22KG';
  let loaded = false;

  function start() {
    window[`ga-disable-${GA_ID}`] = false;
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function gtag() { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
    document.head.append(script);
  }

  // Google's cookies are named _ga and _ga_<id>; they're set on the site's domain (and its parent, e.g.
  // onwun.com for www.onwun.com), so both are cleared
  function stop() {
    window[`ga-disable-${GA_ID}`] = true;
    const host = location.hostname;
    const domains = ['', host, `.${host}`, `.${host.split('.').slice(-2).join('.')}`];
    document.cookie.split(';').map((c) => c.split('=')[0].trim()).filter((name) => name.startsWith('_ga'))
      .forEach((name) => domains.forEach((domain) => {
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/${domain ? `; domain=${domain}` : ''}`;
      }));
  }

  if (window.onwunConsent && window.onwunConsent.analytics) start();
  document.addEventListener('onwun:consent', (e) => (e.detail.analytics ? start() : stop()));
})();
