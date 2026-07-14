# -*- coding: utf-8 -*-
"""Shared scaffolding (head, header, footer) reused by every AZEMAP page."""

OFFICIAL_LOGO = '<img class="brand-mark" src="assets/images/azemap-logo.png" alt="AZEMAP">'

def nav_link(href, label_pt, label_en, active_key, key):
    current = ' aria-current="page"' if active_key == key else ''
    return f'<li><a href="{href}"{current}><span class="lang-pt">{label_pt}</span><span class="lang-en">{label_en}</span></a></li>'

NAV_ITEMS = [
    ("index.html", "Início", "Home", "home"),
    ("sobre.html", "Sobre Nós", "About Us", "sobre"),
    ("trabalho.html", "O Nosso Trabalho", "Our Work", "trabalho"),
    ("onde-trabalhamos.html", "Onde Trabalhamos", "Where We Work", "onde"),
    ("historias.html", "Histórias", "Stories", "historias"),
    ("noticias.html", "Notícias", "News", "noticias"),
    ("galeria.html", "Galeria", "Gallery", "galeria"),
    ("parceiros.html", "Parceiros", "Partners", "parceiros"),
    ("transparencia.html", "Transparência", "Transparency", "transparencia"),
    ("contacto.html", "Contacto", "Contact", "contacto"),
]

def build_nav(active_key):
    items = "\n      ".join(nav_link(h, pt, en, active_key, k) for h, pt, en, k in NAV_ITEMS)
    return items

def build_head(title_pt, title_en, desc_pt, desc_en, canonical):
    return f"""<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_pt} | AZEMAP</title>
<meta name="description" content="{desc_pt}">
<link rel="canonical" href="https://www.azemap.org/{canonical}">
<meta property="og:title" content="{title_pt} | AZEMAP">
<meta property="og:description" content="{desc_pt}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_MZ">
<meta name="theme-color" content="#084D75">
<link rel="icon" type="image/png" href="assets/images/azemap-logo.png">
<meta property="og:image" content="https://www.azemap.org/assets/images/azemap-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<html data-title-pt="{title_pt} | AZEMAP" data-title-en="{title_en} | AZEMAP" data-desc-pt="{desc_pt}" data-desc-en="{desc_en}">"""
# NOTE: the <html ...> attributes above are illustrative only; real attributes are set on the actual <html> tag in PAGE_TEMPLATE.

def build_header(active_key):
    nav = build_nav(active_key)
    return f"""<a class="skip-link" href="#main"><span class="lang-pt">Saltar para o conteúdo</span><span class="lang-en">Skip to content</span></a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      <span class="brand-crop">{OFFICIAL_LOGO}</span>
      <span class="brand-wordmark"><strong>AZEMAP</strong><small><span class="lang-pt">Dignidade &amp; inclusão</span><span class="lang-en">Dignity &amp; inclusion</span></small></span>
    </a>
    <nav class="main-nav" aria-label="Navegação principal / Main navigation">
      <ul>
      {nav}
      </ul>
    </nav>
    <div class="header-actions">
      <div class="lang-switch" data-lang-buttons>
        <button type="button" data-lang="pt" aria-pressed="true" aria-label="Português">PT</button>
        <button type="button" data-lang="en" aria-pressed="false" aria-label="English">EN</button>
      </div>
      <a class="btn btn-primary btn-primary-desktop header-cta" href="apoie-nos.html"><span class="lang-pt">Apoiar</span><span class="lang-en">Support</span><span aria-hidden="true">→</span></a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Abrir menu / Open menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
  <div class="nav-scrim"></div>
</header>
<div id="lang-announce" class="sr-only" aria-live="polite" style="position:absolute;left:-9999px;"></div>"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="footer-brand-link" href="index.html"><span class="footer-logo-crop"><img class="footer-logo" src="assets/images/azemap-logo.png" alt="AZEMAP"></span><strong>AZEMAP</strong></a>
        <p>
          <span class="lang-pt">Associação Zé Manuel Pinto — a defender a saúde, educação, protecção e os direitos das Pessoas com Albinismo em Tete e em Moçambique.</span>
          <span class="lang-en">Zé Manuel Pinto Association — advancing health, education, protection and rights for people with albinism in Tete and across Mozambique.</span>
        </p>
        <a class="footer-contact" href="contacto.html"><span class="lang-pt">Fale com a nossa equipa</span><span class="lang-en">Talk to our team</span> <span aria-hidden="true">→</span></a>
        <div class="social-row" aria-label="Redes sociais / Social media">
          <!-- Social links are hidden until AZEMAP verifies and confirms each official URL (socialLinksVerified: false). -->
        </div>
      </div>
      <div>
        <h4><span class="lang-pt">Navegação</span><span class="lang-en">Navigate</span></h4>
        <ul>
          <li><a href="sobre.html"><span class="lang-pt">Sobre Nós</span><span class="lang-en">About Us</span></a></li>
          <li><a href="trabalho.html"><span class="lang-pt">O Nosso Trabalho</span><span class="lang-en">Our Work</span></a></li>
          <li><a href="historias.html"><span class="lang-pt">Histórias de Impacto</span><span class="lang-en">Impact Stories</span></a></li>
          <li><a href="transparencia.html"><span class="lang-pt">Transparência</span><span class="lang-en">Transparency</span></a></li>
          <li><a href="contacto.html"><span class="lang-pt">Contacto</span><span class="lang-en">Contact</span></a></li>
        </ul>
      </div>
      <div>
        <h4><span class="lang-pt">Envolva-se</span><span class="lang-en">Get Involved</span></h4>
        <ul>
          <li><a href="apoie-nos.html"><span class="lang-pt">Fazer um Donativo</span><span class="lang-en">Make a Donation</span></a></li>
          <li><a href="voluntariado.html"><span class="lang-pt">Ser Voluntário</span><span class="lang-en">Volunteer</span></a></li>
          <li><a href="parceiros.html"><span class="lang-pt">Ser Parceiro</span><span class="lang-en">Become a Partner</span></a></li>
          <li><a href="galeria.html"><span class="lang-pt">Galeria</span><span class="lang-en">Gallery</span></a></li>
        </ul>
      </div>
      <div>
        <h4><span class="lang-pt">Legal</span><span class="lang-en">Legal</span></h4>
        <ul>
          <li><a href="privacidade.html"><span class="lang-pt">Política de Privacidade</span><span class="lang-en">Privacy Policy</span></a></li>
          <li><a href="protecao-imagem.html"><span class="lang-pt">Protecção e Uso de Imagem</span><span class="lang-en">Safeguarding &amp; Image Policy</span></a></li>
          <li><a href="transparencia.html"><span class="lang-pt">Estatutos e Reconhecimento Legal</span><span class="lang-en">Statutes &amp; Legal Recognition</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span><span class="lang-pt">Associação legalmente reconhecida pelo Governo da Província de Tete em 25 de Agosto de 2016.</span><span class="lang-en">Legally recognised by the Government of Tete Province on 25 August 2016.</span></span>
      <span>&copy; <span data-current-year></span> AZEMAP — <span class="lang-pt">Associação Zé Manuel Pinto</span><span class="lang-en">Zé Manuel Pinto Association</span></span>
    </div>
  </div>
</footer>
<a class="whatsapp-fab" href="https://wa.me/258848234747?text=Ol%C3%A1%2C%20gostaria%20de%20saber%20mais%20sobre%20o%20trabalho%20da%20AZEMAP." target="_blank" rel="noopener" aria-label="Falar com a AZEMAP no WhatsApp / Message AZEMAP on WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm5.7 14.3c-.2.7-1.4 1.3-2 1.4-.5.1-1.1.1-1.8-.1-.4-.1-.9-.3-1.6-.6-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.4.7-.4h.5c.2 0 .4 0 .6.5.2.5.7 1.8.8 1.9.1.2.1.3 0 .5-.1.2-.2.3-.3.5-.2.2-.3.3-.1.6.2.3.9 1.5 1.9 2.4 1.3 1.1 2.3 1.5 2.7 1.6.2.1.4 0 .5-.1l.7-.8c.2-.3.4-.2.7-.1.3.1 1.6.8 1.9 1 .3.1.5.2.5.3.1.2.1.6-.1 1.2Z"/></svg>
  <span><span class="lang-pt">WhatsApp</span><span class="lang-en">WhatsApp</span></span>
</a>
<script src="assets/js/main.js"></script>"""

def page(title_pt, title_en, desc_pt, desc_en, canonical, active_key, body_html, lang_default="pt"):
    nav = build_nav(active_key)
    header = build_header(active_key)
    return f"""<!DOCTYPE html>
<html lang="{lang_default}" data-title-pt="{title_pt} | AZEMAP" data-title-en="{title_en} | AZEMAP" data-desc-pt="{desc_pt}" data-desc-en="{desc_en}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_pt} | AZEMAP</title>
<meta name="description" content="{desc_pt}">
<link rel="canonical" href="https://www.azemap.org/{canonical}">
<meta property="og:title" content="{title_pt} | AZEMAP">
<meta property="og:description" content="{desc_pt}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_MZ">
<meta name="theme-color" content="#084D75">
<link rel="icon" type="image/png" href="assets/images/azemap-logo.png">
<meta property="og:image" content="https://www.azemap.org/assets/images/azemap-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header}
<main id="main">
{body_html}
</main>
{FOOTER}
</body>
</html>"""
