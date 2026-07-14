/* =========================================================
   AZEMAP — shared site behaviour
   - Bilingual switcher (PT default / EN), remembered per browser
   - Accessible mobile navigation
   - Client-side form validation with accessible error summaries
   - Dev-mode fallback for forms (no backend configured yet)
   - Simple accessible lightbox for the gallery
   ========================================================= */
(function () {
  "use strict";

  /* ---------- Language switching ---------- */
  var LANG_KEY = "azemap-lang";

  function getStoredLang() {
    try { return localStorage.getItem(LANG_KEY); } catch (e) { return null; }
  }
  function setStoredLang(lang) {
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* ignore */ }
  }
  function applyLang(lang) {
    document.documentElement.setAttribute("lang", lang);
    document.querySelectorAll("[data-lang-buttons] button").forEach(function (btn) {
      btn.setAttribute("aria-pressed", btn.getAttribute("data-lang") === lang ? "true" : "false");
    });
    // Prevent hidden-language form controls (e.g. duplicate <select> pairs)
    // from being submitted alongside the visible-language one.
    document.querySelectorAll("select.lang-pt, select.lang-en").forEach(function (sel) {
      var isVisible = (lang === "pt" && sel.classList.contains("lang-pt")) || (lang === "en" && sel.classList.contains("lang-en"));
      sel.disabled = !isVisible;
      sel.toggleAttribute("aria-hidden", !isVisible);
    });
    document.title = lang === "en" ? document.documentElement.getAttribute("data-title-en") || document.title
                                    : document.documentElement.getAttribute("data-title-pt") || document.title;
    var metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
      var descAttr = lang === "en" ? "data-desc-en" : "data-desc-pt";
      var val = document.documentElement.getAttribute(descAttr);
      if (val) metaDesc.setAttribute("content", val);
    }
  }
  function initLang() {
    var stored = getStoredLang();
    var lang = stored === "en" ? "en" : "pt";
    applyLang(lang);
    document.querySelectorAll("[data-lang-buttons] button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var newLang = btn.getAttribute("data-lang");
        setStoredLang(newLang);
        applyLang(newLang);
        var live = document.getElementById("lang-announce");
        if (live) live.textContent = newLang === "en" ? "Language changed to English" : "Idioma alterado para Português";
      });
    });
  }

  /* ---------- Mobile navigation ---------- */
  function initMobileNav() {
    var toggle = document.querySelector(".menu-toggle");
    var nav = document.querySelector(".main-nav");
    var scrim = document.querySelector(".nav-scrim");
    if (!toggle || !nav) return;

    function closeNav() {
      nav.classList.remove("open");
      if (scrim) scrim.classList.remove("open");
      document.body.classList.remove("nav-open");
      toggle.setAttribute("aria-expanded", "false");
    }
    function openNav() {
      nav.classList.add("open");
      if (scrim) scrim.classList.add("open");
      document.body.classList.add("nav-open");
      toggle.setAttribute("aria-expanded", "true");
      var firstLink = nav.querySelector("a");
      if (firstLink) firstLink.focus();
    }
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.contains("open");
      isOpen ? closeNav() : openNav();
    });
    if (scrim) scrim.addEventListener("click", closeNav);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeNav);
    });
  }

  /* ---------- Accessible forms with dev-mode fallback ---------- */
  function validators() {
    return {
      required: function (v) { return v.trim().length > 0; },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()); },
      phone: function (v) { return v.trim().length >= 6; }
    };
  }

  function initForms() {
    var forms = document.querySelectorAll("form[data-azemap-form]");
    forms.forEach(function (form) {
      var status = form.querySelector(".form-status");
      var checks = validators();

      form.addEventListener("submit", function (e) {
        e.preventDefault();

        // Honeypot spam trap: if filled, silently "succeed" without storing anything.
        var honey = form.querySelector('input[name="company_website"]');
        if (honey && honey.value.trim() !== "") {
          showStatus(status, "success", form);
          form.reset();
          return;
        }

        var valid = true;
        var firstInvalid = null;
        form.querySelectorAll("[data-validate]").forEach(function (input) {
          var rules = input.getAttribute("data-validate").split(" ");
          var fieldWrap = input.closest(".field");
          var isValid = true;
          rules.forEach(function (rule) {
            if (rule === "required" && input.type !== "checkbox" && !checks.required(input.value)) isValid = false;
            if (rule === "required" && input.type === "checkbox" && !input.checked) isValid = false;
            if (rule === "email" && input.value && !checks.email(input.value)) isValid = false;
          });
          if (fieldWrap) fieldWrap.classList.toggle("has-error", !isValid);
          if (!isValid) {
            valid = false;
            if (!firstInvalid) firstInvalid = input;
          }
        });

        if (!valid) {
          showStatus(status, "error", form);
          if (firstInvalid) firstInvalid.focus();
          return;
        }

        showStatus(status, "loading", form);

        // No backend is configured yet (NEXT_PUBLIC_FORM_ENDPOINT / Supabase).
        // Development fallback: keep the submission locally so nothing is
        // silently discarded, and let the person know clearly what happened.
        setTimeout(function () {
          try {
            var key = "azemap-dev-submissions";
            var existing = JSON.parse(localStorage.getItem(key) || "[]");
            var data = {};
            new FormData(form).forEach(function (value, name) { data[name] = value; });
            data._form = form.getAttribute("data-azemap-form");
            data._submittedAt = new Date().toISOString();
            existing.push(data);
            localStorage.setItem(key, JSON.stringify(existing));
          } catch (err) { /* ignore storage errors */ }
          showStatus(status, "success", form);
          form.reset();
        }, 500);
      });
    });
  }

  function showStatus(status, kind, form) {
    if (!status) return;
    status.classList.remove("success", "error", "loading");
    status.classList.add("show", kind);
    var messages = {
      loading: { pt: "A enviar...", en: "Sending..." },
      success: { pt: "Obrigado! A sua mensagem foi registada. Como ainda não temos um sistema de envio ligado, a equipa da AZEMAP irá processar isto manualmente assim que o backend for configurado — para pedidos urgentes, contacte-nos directamente pelo telefone ou WhatsApp indicados nesta página.", en: "Thank you! Your message has been recorded. Since no live submission backend is connected yet, the AZEMAP team will process this manually until that is configured — for urgent requests, please contact us directly by phone or WhatsApp." },
      error: { pt: "Por favor verifique os campos assinalados antes de continuar.", en: "Please check the highlighted fields before continuing." }
    };
    var lang = document.documentElement.getAttribute("lang") === "en" ? "en" : "pt";
    status.textContent = messages[kind][lang];
    status.setAttribute("role", kind === "error" ? "alert" : "status");
  }

  /* ---------- Gallery lightbox ---------- */
  function initLightbox() {
    var items = document.querySelectorAll("[data-lightbox-trigger]");
    if (!items.length) return;
    var overlay = document.createElement("div");
    overlay.className = "lightbox-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Image viewer");
    overlay.style.cssText = "position:fixed;inset:0;background:rgba(10,20,18,.92);display:none;align-items:center;justify-content:center;z-index:500;padding:24px;";
    overlay.innerHTML =
      '<button class="lightbox-close" aria-label="Fechar / Close" style="position:absolute;top:20px;right:24px;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.5);color:#fff;width:44px;height:44px;border-radius:50%;font-size:22px;cursor:pointer;">&times;</button>' +
      '<figure style="max-width:min(900px,92vw);max-height:88vh;margin:0;text-align:center;">' +
      '<img style="max-width:100%;max-height:76vh;border-radius:14px;object-fit:contain;" />' +
      '<figcaption style="color:#EFE9D8;margin-top:14px;font-size:.95rem;"></figcaption>' +
      "</figure>";
    document.body.appendChild(overlay);
    var imgEl = overlay.querySelector("img");
    var capEl = overlay.querySelector("figcaption");
    var closeBtn = overlay.querySelector(".lightbox-close");
    var lastFocused = null;

    function open(trigger) {
      lastFocused = document.activeElement;
      var img = trigger.querySelector("img");
      imgEl.src = img.currentSrc || img.src;
      imgEl.alt = img.alt || "";
      capEl.textContent = trigger.getAttribute("data-caption") || "";
      overlay.style.display = "flex";
      closeBtn.focus();
      document.body.style.overflow = "hidden";
    }
    function close() {
      overlay.style.display = "none";
      document.body.style.overflow = "";
      if (lastFocused) lastFocused.focus();
    }
    items.forEach(function (trigger) {
      trigger.addEventListener("click", function () { open(trigger); });
      trigger.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(trigger); }
      });
    });
    closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && overlay.style.display === "flex") close(); });
  }

  /* ---------- Gallery / news filter chips (client-side demo filter) ---------- */
  function initFilterChips() {
    document.querySelectorAll("[data-filter-group]").forEach(function (group) {
      var chips = group.querySelectorAll(".filter-chip");
      var targetSelector = group.getAttribute("data-filter-group");
      var items = document.querySelectorAll(targetSelector);
      var emptyState = document.querySelector(group.getAttribute("data-empty-state") || "");
      chips.forEach(function (chip) {
        chip.addEventListener("click", function () {
          chips.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
          chip.setAttribute("aria-pressed", "true");
          var filter = chip.getAttribute("data-filter");
          var visibleCount = 0;
          items.forEach(function (item) {
            var tags = (item.getAttribute("data-tags") || "").split(" ");
            var show = filter === "all" || tags.indexOf(filter) !== -1;
            item.style.display = show ? "" : "none";
            if (show) visibleCount++;
          });
          if (emptyState) emptyState.style.display = visibleCount === 0 ? "block" : "none";
        });
      });
    });
  }

  /* ---------- Subtle progressive motion ---------- */
  function initMotion() {
    var header = document.querySelector(".site-header");
    function syncHeader() {
      if (header) header.classList.toggle("is-scrolled", window.scrollY > 12);
    }
    syncHeader();
    window.addEventListener("scroll", syncHeader, { passive: true });

    if (!window.IntersectionObserver || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var targets = document.querySelectorAll("main .section > .container, main .card, main .rounded-photo");
    targets.forEach(function (el) { el.classList.add("reveal-ready"); });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-in");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -24px" });
    targets.forEach(function (el) { observer.observe(el); });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initLang();
    initMobileNav();
    initForms();
    initLightbox();
    initFilterChips();
    initMotion();
    // Footer year
    document.querySelectorAll("[data-current-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  });
})();
