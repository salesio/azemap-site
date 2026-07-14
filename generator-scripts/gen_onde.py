# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

DISTRICTS = [
    ("Cidade de Tete", "active"),
    ("Moatize", "occasional"),
    ("Mucumbura (Cahora Bassa)", "occasional"),
    ("Chifunde", "occasional"),
    ("Cahora Bassa", "occasional"),
    ("Angónia", "occasional"),
    ("Calomué", "active"),
]
STATUS_LABEL = {
    "active": ("Activo", "Active"),
    "occasional": ("Ocasional", "Occasional"),
    "historical": ("Histórico", "Historical"),
}
rows = []
for name, status in DISTRICTS:
    pt, en = STATUS_LABEL[status]
    rows.append(f"""<li class="district-item"><span>{name}</span><span class="status-pill status-{status}"><span class="lang-pt">{pt}</span><span class="lang-en">{en}</span></span></li>""")
district_html = "\n      ".join(rows)

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Onde Trabalhamos</span><span class="lang-en">Where We Work</span></p>
    <h1><span class="lang-pt">Presença na Província de Tete</span><span class="lang-en">Presence across Tete Province</span></h1>
    <p><span class="lang-pt">A AZEMAP tem a sua sede na Cidade de Tete e desenvolve actividades em vários distritos da província, podendo alargar o seu trabalho a outras zonas de Moçambique.</span>
    <span class="lang-en">AZEMAP is headquartered in Tete City and carries out activities across several districts of the province, with the potential to extend its work to other parts of Mozambique.</span></p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <p class="eyebrow"><span class="lang-pt">Distritos</span><span class="lang-en">Districts</span></p>
      <h2><span class="lang-pt">Alcance geográfico</span><span class="lang-en">Geographic reach</span></h2>
      <p class="max-prose"><span class="lang-pt">Esta lista é actualizada conforme as actividades da AZEMAP se confirmam em cada zona. A presença permanente em todos os distritos ainda está em processo de verificação.</span>
      <span class="lang-en">This list is updated as AZEMAP's activities are confirmed in each area. Permanent presence across every district is still being verified.</span></p>
      <ul class="district-list">
        {district_html}
      </ul>
    </div>
    <div class="rounded-photo">
      <img src="assets/images/familia-criancas-2.jpg" alt="Família acompanhada pela AZEMAP numa comunidade rural da Província de Tete" style="aspect-ratio:4/5; object-position:50% 20%;">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container text-center center-col">
    <p class="eyebrow" style="justify-content:center;"><span class="lang-pt">Sede</span><span class="lang-en">Headquarters</span></p>
    <h2><span class="lang-pt">Cidade de Tete</span><span class="lang-en">Tete City</span></h2>
    <p><span class="lang-pt">Bairro Filipe Samuel Magaia, Cidade de Tete, Província de Tete, Moçambique.</span>
    <span class="lang-en">Filipe Samuel Magaia neighbourhood, Tete City, Tete Province, Mozambique.</span></p>
    <div class="notice notice-info" style="text-align:left;">
      <span class="lang-pt">Por questões de privacidade e segurança, esta página mostra apenas a localização aproximada da Cidade de Tete. A morada exacta do escritório será confirmada em breve.</span>
      <span class="lang-en">For privacy and safety reasons, this page shows only the approximate location of Tete City. The exact office address will be confirmed soon.</span>
    </div>
    <div class="rounded-photo" style="margin-top:20px;">
      <iframe title="Mapa aproximado — Cidade de Tete" src="https://www.openstreetmap.org/export/embed.html?bbox=33.55%2C-16.22%2C33.62%2C-16.13&layer=mapnik&marker=-16.1636%2C33.5867" style="width:100%; height:340px; border:0;" loading="lazy"></iframe>
    </div>
  </div>
</section>
"""

html = page(
    title_pt="Onde Trabalhamos",
    title_en="Where We Work",
    desc_pt="A AZEMAP está sediada na Cidade de Tete e desenvolve actividades em vários distritos da Província de Tete, Moçambique.",
    desc_en="AZEMAP is headquartered in Tete City and works across several districts of Tete Province, Mozambique.",
    canonical="onde-trabalhamos.html",
    active_key="onde",
    body_html=BODY,
)
with open("/home/claude/azemap-site/onde-trabalhamos.html", "w", encoding="utf-8") as f:
    f.write(html)
print("onde-trabalhamos.html written:", len(html))
