# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

# ---------------- APOIE-NOS ----------------
WAYS = [
    ("Donativo geral", "General donation"),
    ("Patrocinar protector solar", "Sponsor sunscreen"),
    ("Patrocinar óculos de sol", "Sponsor sunglasses"),
    ("Apoiar material escolar", "Support school materials"),
    ("Apoiar roupa de protecção", "Support protective clothing"),
    ("Apoiar transporte para consultas", "Support transport to appointments"),
    ("Tornar-se parceiro institucional", "Become an institutional partner"),
    ("Oferecer serviços profissionais", "Offer professional services"),
    ("Voluntariado", "Volunteering"),
]
way_cards = "\n      ".join(
    f'<div class="card" style="padding:20px;"><h3 style="font-size:1rem;"><span class="lang-pt">{pt}</span><span class="lang-en">{en}</span></h3></div>'
    for pt, en in WAYS
)

SUPPORT_TYPE_OPTIONS = WAYS
support_options_html = "\n            ".join(
    f'<option value="{pt}"><span class="lang-pt">{pt}</span></option>' for pt, en in SUPPORT_TYPE_OPTIONS
)
# Select options can't hold spans; provide bilingual via data attributes handled simply: use PT value, EN label swapped via JS is extra complexity.
# Simpler: build two option sets and toggle whole <select> visibility per language.
opts_pt = "\n            ".join(f'<option value="{pt}">{pt}</option>' for pt, en in SUPPORT_TYPE_OPTIONS)
opts_en = "\n            ".join(f'<option value="{pt}">{en}</option>' for pt, en in SUPPORT_TYPE_OPTIONS)

APOIO_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Apoie-nos</span><span class="lang-en">Support Us</span></p>
    <h1><span class="lang-pt">O seu apoio protege vidas com dignidade</span><span class="lang-en">Your support protects lives with dignity</span></h1>
    <p><span class="lang-pt">Existem várias formas de apoiar o trabalho da AZEMAP — escolha a que melhor se adequa a si ou à sua organização.</span>
    <span class="lang-en">There are several ways to support AZEMAP's work — choose the one that best fits you or your organisation.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      {way_cards}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container center-col">
    <div class="notice notice-warn">
      <span class="lang-pt"><strong>Dados oficiais para donativos:</strong> ainda não foram publicados dados bancários ou de pagamento móvel. Os dados oficiais para donativos serão disponibilizados mediante contacto directo com a AZEMAP.</span>
      <span class="lang-en"><strong>Official donation details:</strong> bank or mobile-money details have not yet been published. Official donation details will be shared after direct contact with AZEMAP.</span>
    </div>
    <p class="hint"><span class="lang-pt">Assim que confirmados, os métodos de pagamento (M-Pesa, e-Mola, transferência bancária, PayPal) serão adicionados a esta página.</span>
    <span class="lang-en">Once confirmed, payment methods (M-Pesa, e-Mola, bank transfer, PayPal) will be added to this page.</span></p>
  </div>
</section>

<section class="section">
  <div class="container center-col">
    <h2 class="text-center"><span class="lang-pt">Solicitar dados para donativo</span><span class="lang-en">Request donation details</span></h2>
    <p class="text-center max-prose" style="margin:0 auto 30px;"><span class="lang-pt">Preencha este formulário e a equipa da AZEMAP entrará em contacto consigo com as informações necessárias.</span>
    <span class="lang-en">Fill in this form and the AZEMAP team will contact you with the information you need.</span></p>
    <form data-azemap-form="donation-enquiry" novalidate>
      <input type="text" class="honeypot" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="form-grid">
        <div class="field">
          <label for="d-name"><span class="lang-pt">Nome completo</span><span class="lang-en">Full name</span> *</label>
          <input type="text" id="d-name" name="name" data-validate="required">
          <span class="field-error"><span class="lang-pt">Por favor indique o seu nome.</span><span class="lang-en">Please enter your name.</span></span>
        </div>
        <div class="field">
          <label for="d-email"><span class="lang-pt">Email</span><span class="lang-en">Email</span> *</label>
          <input type="email" id="d-email" name="email" data-validate="required email">
          <span class="field-error"><span class="lang-pt">Por favor indique um email válido.</span><span class="lang-en">Please enter a valid email.</span></span>
        </div>
        <div class="field">
          <label for="d-phone"><span class="lang-pt">Telefone / WhatsApp</span><span class="lang-en">Phone / WhatsApp</span></label>
          <input type="tel" id="d-phone" name="phone">
        </div>
        <div class="field">
          <label for="d-country"><span class="lang-pt">País</span><span class="lang-en">Country</span></label>
          <input type="text" id="d-country" name="country">
        </div>
        <div class="field">
          <label for="d-type"><span class="lang-pt">Tipo de apoio</span><span class="lang-en">Type of support</span> *</label>
          <select id="d-type" name="support_type" data-validate="required" class="lang-pt">
            {opts_pt}
          </select>
          <select id="d-type-en" name="support_type" data-validate="required" class="lang-en" disabled>
            {opts_en}
          </select>
        </div>
        <div class="field">
          <label for="d-amount"><span class="lang-pt">Valor aproximado</span><span class="lang-en">Approximate amount</span> <span class="hint">(<span class="lang-pt">opcional</span><span class="lang-en">optional</span>)</span></label>
          <input type="text" id="d-amount" name="amount">
        </div>
        <div class="field full">
          <label for="d-message"><span class="lang-pt">Mensagem</span><span class="lang-en">Message</span></label>
          <textarea id="d-message" name="message"></textarea>
        </div>
        <div class="field full">
          <label class="checkbox-row"><input type="checkbox" name="consent" data-validate="required">
            <span><span class="lang-pt">Aceito que os meus dados sejam usados para me contactarem sobre este pedido, conforme a</span><span class="lang-en">I agree that my data may be used to contact me about this request, in line with the</span> <a href="privacidade.html"><span class="lang-pt">Política de Privacidade</span><span class="lang-en">Privacy Policy</span></a>. *</span>
          </label>
          <span class="field-error"><span class="lang-pt">É necessário aceitar para continuar.</span><span class="lang-en">You must agree to continue.</span></span>
        </div>
      </div>
      <button type="submit" class="btn btn-primary"><span class="lang-pt">Enviar pedido</span><span class="lang-en">Send request</span></button>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
"""

html = page(
    title_pt="Apoie-nos", title_en="Support Us",
    desc_pt="Conheça as formas de apoiar a AZEMAP: donativos, patrocínios, parcerias e voluntariado.",
    desc_en="Explore ways to support AZEMAP: donations, sponsorships, partnerships and volunteering.",
    canonical="apoie-nos.html", active_key="apoio", body_html=APOIO_BODY,
)
with open("/home/claude/azemap-site/apoie-nos.html", "w", encoding="utf-8") as f:
    f.write(html)
print("apoie-nos.html written:", len(html))

# ---------------- VOLUNTARIADO ----------------
AREAS = [
    ("Saúde comunitária", "Health outreach"), ("Educação", "Education"),
    ("Sensibilização comunitária", "Community awareness"), ("Tradução", "Translation"),
    ("Fotografia e vídeo", "Photography and video"), ("Design gráfico", "Graphic design"),
    ("Apoio jurídico", "Legal support"), ("Angariação de fundos", "Fundraising"),
    ("Administração", "Administration"), ("Recolha de dados", "Data collection"),
    ("Apoio a eventos", "Event support"), ("Comunicação digital", "Digital communication"),
]
area_opts_pt = "\n            ".join(f'<option value="{pt}">{pt}</option>' for pt, en in AREAS)
area_opts_en = "\n            ".join(f'<option value="{pt}">{en}</option>' for pt, en in AREAS)
area_tags = "\n      ".join(f'<span class="tag"><span class="lang-pt">{pt}</span><span class="lang-en">{en}</span></span>' for pt, en in AREAS)

VOL_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Voluntariado</span><span class="lang-en">Volunteer</span></p>
    <h1><span class="lang-pt">Junte o seu tempo e talento à nossa causa</span><span class="lang-en">Bring your time and talent to our cause</span></h1>
    <p><span class="lang-pt">Procuramos voluntários em diversas áreas para reforçar o trabalho da AZEMAP junto das comunidades.</span>
    <span class="lang-en">We're looking for volunteers across several areas to strengthen AZEMAP's work with communities.</span></p>
  </div>
</section>

<section class="section">
  <div class="container text-center">
    <p class="eyebrow" style="justify-content:center;"><span class="lang-pt">Áreas de voluntariado</span><span class="lang-en">Volunteer areas</span></p>
    <div style="margin-top:14px;">{area_tags}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container center-col">
    <div class="notice notice-info">
      <span class="lang-pt">Os voluntários que trabalhem com crianças ou pessoas vulneráveis poderão estar sujeitos a processos adicionais de selecção e protecção.</span>
      <span class="lang-en">Volunteers working with children or vulnerable people may be subject to additional screening and safeguarding processes.</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container center-col">
    <h2 class="text-center"><span class="lang-pt">Candidatura de voluntariado</span><span class="lang-en">Volunteer application</span></h2>
    <form data-azemap-form="volunteer" novalidate style="margin-top:26px;">
      <input type="text" class="honeypot" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="form-grid">
        <div class="field">
          <label for="v-name"><span class="lang-pt">Nome completo</span><span class="lang-en">Full name</span> *</label>
          <input type="text" id="v-name" name="name" data-validate="required">
          <span class="field-error"><span class="lang-pt">Por favor indique o seu nome.</span><span class="lang-en">Please enter your name.</span></span>
        </div>
        <div class="field">
          <label for="v-email"><span class="lang-pt">Email</span><span class="lang-en">Email</span> *</label>
          <input type="email" id="v-email" name="email" data-validate="required email">
          <span class="field-error"><span class="lang-pt">Por favor indique um email válido.</span><span class="lang-en">Please enter a valid email.</span></span>
        </div>
        <div class="field">
          <label for="v-phone"><span class="lang-pt">Telefone</span><span class="lang-en">Phone</span></label>
          <input type="tel" id="v-phone" name="phone">
        </div>
        <div class="field">
          <label for="v-location"><span class="lang-pt">Distrito ou país</span><span class="lang-en">District or country</span></label>
          <input type="text" id="v-location" name="location">
        </div>
        <div class="field">
          <label for="v-area"><span class="lang-pt">Área preferida</span><span class="lang-en">Preferred area</span> *</label>
          <select id="v-area" name="area" data-validate="required" class="lang-pt">
            {area_opts_pt}
          </select>
          <select id="v-area-en" name="area" data-validate="required" class="lang-en" disabled>
            {area_opts_en}
          </select>
        </div>
        <div class="field">
          <label for="v-availability"><span class="lang-pt">Disponibilidade</span><span class="lang-en">Availability</span></label>
          <input type="text" id="v-availability" name="availability" placeholder="ex.: fins-de-semana / weekends">
        </div>
        <div class="field full">
          <label for="v-skills"><span class="lang-pt">Competências</span><span class="lang-en">Skills</span></label>
          <input type="text" id="v-skills" name="skills">
        </div>
        <div class="field full">
          <label for="v-motivation"><span class="lang-pt">Motivação (breve)</span><span class="lang-en">Motivation (brief)</span></label>
          <textarea id="v-motivation" name="motivation"></textarea>
        </div>
        <div class="field full">
          <label class="checkbox-row"><input type="checkbox" name="consent" data-validate="required">
            <span><span class="lang-pt">Aceito o tratamento dos meus dados para fins de candidatura de voluntariado.</span><span class="lang-en">I agree to my data being processed for volunteer application purposes.</span> *</span>
          </label>
          <span class="field-error"><span class="lang-pt">É necessário aceitar para continuar.</span><span class="lang-en">You must agree to continue.</span></span>
        </div>
      </div>
      <button type="submit" class="btn btn-primary"><span class="lang-pt">Enviar candidatura</span><span class="lang-en">Submit application</span></button>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
"""

html = page(
    title_pt="Voluntariado", title_en="Volunteer",
    desc_pt="Torne-se voluntário da AZEMAP em saúde, educação, comunicação, apoio jurídico e muito mais.",
    desc_en="Become an AZEMAP volunteer in health, education, communications, legal support and more.",
    canonical="voluntariado.html", active_key="apoio", body_html=VOL_BODY,
)
with open("/home/claude/azemap-site/voluntariado.html", "w", encoding="utf-8") as f:
    f.write(html)
print("voluntariado.html written:", len(html))

# ---------------- PARCEIROS ----------------
PARTNERS = ["Africa Directo", "Serviços Provinciais de Saúde de Tete|Tete Provincial Health Services",
            "Africa Albinism Network", "Human Rights Watch", "Amor à Vida"]
def partner_card(p):
    if "|" in p:
        pt, en = p.split("|")
        return f'<div class="card partner-card"><span class="lang-pt">{pt}</span><span class="lang-en">{en}</span></div>'
    return f'<div class="card partner-card">{p}</div>'
partners_html = "\n      ".join(partner_card(p) for p in PARTNERS)

PART_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Parceiros</span><span class="lang-en">Partners</span></p>
    <h1><span class="lang-pt">Organizações que caminham com a AZEMAP</span><span class="lang-en">Organisations walking with AZEMAP</span></h1>
    <p><span class="lang-pt">A colaboração institucional fortalece o impacto do nosso trabalho junto das Pessoas com Albinismo.</span>
    <span class="lang-en">Institutional collaboration strengthens the impact of our work with people with albinism.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      {partners_html}
    </div>
    <div class="notice notice-info" style="margin-top:34px;">
      <span class="lang-pt">A apresentação de uma organização nesta secção não implica necessariamente uma parceria actualmente activa. A lista será actualizada pela AZEMAP. Os logótipos apenas serão apresentados quando existir ficheiro aprovado e autorização de utilização.</span>
      <span class="lang-en">Listing an organisation here does not necessarily imply a currently active partnership. This list will be updated by AZEMAP. Logos will only be shown once an approved file and usage permission exist.</span>
    </div>
  </div>
</section>

<section class="section section-alt text-center">
  <div class="container center-col">
    <h2><span class="lang-pt">Quer tornar-se parceiro institucional?</span><span class="lang-en">Want to become an institutional partner?</span></h2>
    <p><span class="lang-pt">Entre em contacto connosco para explorar formas de colaboração.</span>
    <span class="lang-en">Get in touch to explore ways to collaborate.</span></p>
    <a class="btn btn-primary" href="contacto.html"><span class="lang-pt">Contactar a AZEMAP</span><span class="lang-en">Contact AZEMAP</span></a>
  </div>
</section>
"""

html = page(
    title_pt="Parceiros", title_en="Partners",
    desc_pt="Organizações e instituições que colaboram com a AZEMAP no apoio às Pessoas com Albinismo.",
    desc_en="Organisations and institutions collaborating with AZEMAP in support of people with albinism.",
    canonical="parceiros.html", active_key="parceiros", body_html=PART_BODY,
)
with open("/home/claude/azemap-site/parceiros.html", "w", encoding="utf-8") as f:
    f.write(html)
print("parceiros.html written:", len(html))
