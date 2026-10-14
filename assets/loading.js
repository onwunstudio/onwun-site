// Loading states shared by every page (styles in assets/loading.css).
//
//   04 Skeleton:         image frames shimmer until their image has loaded.
//   05 Page transition:  a 1px line under the nav when following a link to another page.
(() => {
  // sessionStorage can be unavailable (private windows, blocked storage), so every use is guarded
  const session = {
    get(key) { try { return sessionStorage.getItem(key); } catch (e) { return null; } },
    set(key, value) { try { sessionStorage.setItem(key, value); } catch (e) { /* not essential */ } },
    remove(key) { try { sessionStorage.removeItem(key); } catch (e) { /* not essential */ } },
  };

  document.addEventListener('DOMContentLoaded', () => {
    // ───────── 04 Skeleton ─────────
    document.querySelectorAll('.project__mockup, .poster__frame, .media, .more__image').forEach((frame) => {
      const img = frame.querySelector('img');
      if (!img || (img.complete && img.naturalWidth)) return;
      frame.classList.add('is-loading');
      const done = () => {
        frame.classList.remove('is-loading');
        frame.classList.add('is-loaded');
      };
      img.addEventListener('load', done, { once: true });
      img.addEventListener('error', () => frame.classList.remove('is-loading'), { once: true });
    });

    // ───────── 05 Page transition ─────────
    const bar = document.createElement('div');
    bar.className = 'route-progress';
    bar.setAttribute('aria-hidden', 'true');
    bar.innerHTML = '<div class="route-progress__fill"></div>';
    document.body.append(bar);

    function setProgress(value, seconds) {
      bar.style.setProperty('--progress-t', seconds + 's');
      bar.style.setProperty('--progress', value);
    }

    function complete() {
      setProgress(1, 0.3);
      setTimeout(() => bar.classList.remove('is-active'), 300);
    }

    // Arriving from another page of the site: pick up at about 60% and finish once this page has loaded
    if (session.get('onwun-route')) {
      session.remove('onwun-route');
      bar.classList.add('is-active');
      setProgress(0.6, 0);
      if (document.readyState === 'complete') requestAnimationFrame(() => requestAnimationFrame(complete));
      else window.addEventListener('load', complete, { once: true });
    }

    // Following a link to another page: run quickly to about 60% while the browser fetches it
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (!link || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      if (link.target && link.target !== '_self') return;
      if (link.hasAttribute('download')) return;
      const url = new URL(link.href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.search === location.search) return; // same page, e.g. #work
      session.set('onwun-route', '1');
      bar.classList.add('is-active');
      setProgress(0, 0);
      requestAnimationFrame(() => requestAnimationFrame(() => setProgress(0.6, 0.5)));
    });

    // Coming back with the browser's back button can restore this page as it was left, line and all
    window.addEventListener('pageshow', (e) => {
      if (!e.persisted) return;
      session.remove('onwun-route');
      bar.classList.remove('is-active');
      setProgress(0, 0);
    });
  });
})();
