# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/home/claude")
from build_common import page

pdf_size_bytes = os.path.getsize("/home/claude/azemap-site/assets/documents/BR-242-III-Serie-2018-AZEMAP.pdf")
pdf_size_mb = round(pdf_size_bytes / (1024*1024), 1)

TRANS_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Transparência</span><span class="lang-en">Transparency</span></p>
    <h1><span class="lang-pt">Reconhecimento legal e prestação de contas</span><span class="lang-en">Legal recognition and accountability</span></h1>
    <p><span class="lang-pt">A confiança começa com a clareza. Aqui reunimos a informação legal, de governação e de prestação de contas da AZEMAP.</span>
    <span class="lang-en">Trust begins with clarity. Here we gather AZEMAP's legal, governance and accountability information.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card">
        <h3><span class="lang-pt">Reconhecimento Legal</span><span class="lang-en">Legal Recognition</span></h3>
        <p><span class="lang-pt">Reconhecida como pessoa jurídica pelo Governo da Província de Tete em 25 de Agosto de 2016.</span>
        <span class="lang-en">Recognised as a legal entity by the Government of Tete Province on 25 August 2016.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Publicação Oficial</span><span class="lang-en">Official Publication</span></h3>
        <p><span class="lang-pt">Estatutos publicados no Boletim da República, III Série, Número 242, de 12 de Dezembro de 2018.</span>
        <span class="lang-en">Statutes published in the Boletim da República, III Series, Number 242, on 12 December 2018.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Governação</span><span class="lang-en">Governance</span></h3>
        <p><span class="lang-pt">Assembleia Geral, Conselho de Administração e Conselho Fiscal — ver detalhes na página Sobre Nós.</span>
        <span class="lang-en">General Assembly, Board of Directors and Supervisory Board — see details on the About Us page.</span></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container center-col">
    <p class="eyebrow" style="justify-content:center;"><span class="lang-pt">Documento legal</span><span class="lang-en">Legal document</span></p>
    <h2 class="text-center"><span class="lang-pt">Boletim da República — Reconhecimento e Estatutos da AZEMAP</span><span class="lang-en">Boletim da República — AZEMAP Recognition and Statutes</span></h2>
    <div class="card" style="display:flex; align-items:center; gap:20px; flex-wrap:wrap; margin-top:24px;">
      <div style="width:56px; height:56px; border-radius:12px; background:var(--blue-50); display:flex; align-items:center; justify-content:center; color:var(--teal-700); flex-shrink:0;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" width="30" height="30"><path d="M4 19.5V6a2 2 0 0 1 2-2h8l6 6v9.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 19.5Z"/><path d="M14 4v5a1 1 0 0 0 1 1h5"/></svg>
      </div>
      <div style="flex:1; min-width:220px;">
        <h3 style="margin-bottom:4px;"><span class="lang-pt">Boletim da República — III Série, N.º 242</span><span class="lang-en">Boletim da República — III Series, No. 242</span></h3>
        <p class="hint" style="margin:0;">
          <span class="lang-pt">Documento oficial · PDF · {pdf_size_mb} MB · Publicado a 12 de Dezembro de 2018</span>
          <span class="lang-en">Official document · PDF · {pdf_size_mb} MB · Published 12 December 2018</span>
        </p>
      </div>
      <a class="btn btn-outline btn-sm" href="assets/documents/BR-242-III-Serie-2018-AZEMAP.pdf" target="_blank" rel="noopener">
        <span class="lang-pt">Ver / Descarregar</span><span class="lang-en">View / Download</span>
      </a>
    </div>
    <p class="hint" style="margin-top:16px;">
      <span class="lang-pt">O reconhecimento da AZEMAP consta na primeira página (Despacho do Governo da Província de Tete) e os estatutos completos entre as páginas 4 e 7 desta edição do Boletim da República. As restantes entidades publicadas na mesma edição não têm qualquer relação com a AZEMAP.</span>
      <span class="lang-en">AZEMAP's recognition appears on the first page (Government of Tete Province notice), and its full statutes span pages 4 to 7 of this Boletim da República edition. The other entities published in the same edition have no relation to AZEMAP.</span>
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <h3><span class="lang-pt">Relatórios de Actividades</span><span class="lang-en">Activity Reports</span></h3>
        <p><span class="lang-pt">Ainda não foram publicados relatórios de actividades. Serão disponibilizados aqui assim que aprovados pela Assembleia Geral.</span>
        <span class="lang-en">No activity reports have been published yet. They will be made available here once approved by the General Assembly.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Resumos Financeiros</span><span class="lang-en">Financial Summaries</span></h3>
        <p><span class="lang-pt">Ainda não foram publicados resumos financeiros. Nenhum valor de donativos ou orçamento é apresentado sem verificação.</span>
        <span class="lang-en">No financial summaries have been published yet. No donation or budget figures are presented without verification.</span></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt text-center">
  <div class="container center-col">
    <h2><span class="lang-pt">Verificação institucional</span><span class="lang-en">Institutional verification</span></h2>
    <p><span class="lang-pt">Instituições, doadores e parceiros podem solicitar verificação adicional directamente à AZEMAP.</span>
    <span class="lang-en">Institutions, donors and partners may request additional verification directly from AZEMAP.</span></p>
    <a class="btn btn-primary" href="contacto.html"><span class="lang-pt">Contactar para verificação</span><span class="lang-en">Contact for verification</span></a>
  </div>
</section>
"""

html = page(
    title_pt="Transparência", title_en="Transparency",
    desc_pt="Reconhecimento legal, estatutos, governação e prestação de contas da AZEMAP — Associação Zé Manuel Pinto.",
    desc_en="Legal recognition, statutes, governance and accountability for AZEMAP — Zé Manuel Pinto Association.",
    canonical="transparencia.html", active_key="transparencia", body_html=TRANS_BODY,
)
with open("/home/claude/azemap-site/transparencia.html", "w", encoding="utf-8") as f:
    f.write(html)
print("transparencia.html written:", len(html))

# ---------------- CONTACTO ----------------
SUBJECTS = [
    ("Pedido de informação", "Information request"), ("Donativo", "Donation"),
    ("Parceria", "Partnership"), ("Voluntariado", "Volunteering"),
    ("Apoio a beneficiário", "Beneficiary support"), ("Comunicação social", "Press"),
    ("Outro", "Other"),
]
subj_pt = "\n            ".join(f'<option value="{pt}">{pt}</option>' for pt, en in SUBJECTS)
subj_en = "\n            ".join(f'<option value="{pt}">{en}</option>' for pt, en in SUBJECTS)

CONTACT_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Contacto</span><span class="lang-en">Contact</span></p>
    <h1><span class="lang-pt">Fale com a AZEMAP</span><span class="lang-en">Get in touch with AZEMAP</span></h1>
    <p><span class="lang-pt">Estamos disponíveis para responder a pedidos de informação, parcerias, donativos e voluntariado.</span>
    <span class="lang-en">We're available to answer questions about information, partnerships, donations and volunteering.</span></p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <h2><span class="lang-pt">Informações de contacto</span><span class="lang-en">Contact information</span></h2>
      <p><strong><span class="lang-pt">Associação Zé Manuel Pinto — AZEMAP</span><span class="lang-en">Zé Manuel Pinto Association — AZEMAP</span></strong><br>
      <span class="lang-pt">Bairro Filipe Samuel Magaia, Cidade de Tete, Moçambique</span><span class="lang-en">Filipe Samuel Magaia neighbourhood, Tete City, Mozambique</span></p>
      <p>
        <strong><span class="lang-pt">Email:</span><span class="lang-en">Email:</span></strong><br>
        <a href="mailto:Flaviapinto.954@gmail.com">Flaviapinto.954@gmail.com</a><br>
        <a href="mailto:queduchanga@yahoo.com.br">queduchanga@yahoo.com.br</a>
      </p>
      <p>
        <strong><span class="lang-pt">Telefone:</span><span class="lang-en">Phone:</span></strong><br>
        <a href="tel:+258848234747">+258 84 823 4747</a> ·
        <a href="tel:+258828475600">+258 82 847 5600</a><br>
        <a href="tel:+258845627085">+258 84 562 7085</a> ·
        <a href="tel:+258827076993">+258 82 707 6993</a>
      </p>
      <a class="btn btn-primary" href="https://wa.me/258848234747?text=Ol%C3%A1%2C%20gostaria%20de%20saber%20mais%20sobre%20o%20trabalho%20da%20AZEMAP." target="_blank" rel="noopener">
        <span class="lang-pt">Falar no WhatsApp</span><span class="lang-en">Message on WhatsApp</span>
      </a>
      <div class="notice notice-info" style="margin-top:26px;">
        <span class="lang-pt"><strong>Em caso de emergência médica</strong>, contacte imediatamente a unidade sanitária ou os serviços de emergência disponíveis na sua área. A AZEMAP não presta serviços médicos de emergência.</span>
        <span class="lang-en"><strong>In a medical emergency</strong>, please contact your local health unit or emergency services immediately. AZEMAP does not provide emergency medical services.</span>
      </div>
    </div>
    <div class="rounded-photo">
      <iframe title="Mapa aproximado — Cidade de Tete" src="https://www.openstreetmap.org/export/embed.html?bbox=33.55%2C-16.22%2C33.62%2C-16.13&layer=mapnik&marker=-16.1636%2C33.5867" style="width:100%; height:100%; min-height:340px; border:0;" loading="lazy"></iframe>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container center-col">
    <h2 class="text-center"><span class="lang-pt">Envie-nos uma mensagem</span><span class="lang-en">Send us a message</span></h2>
    <form data-azemap-form="contact" novalidate style="margin-top:28px;">
      <input type="text" class="honeypot" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="form-grid">
        <div class="field">
          <label for="c-name"><span class="lang-pt">Nome completo</span><span class="lang-en">Full name</span> *</label>
          <input type="text" id="c-name" name="name" data-validate="required">
          <span class="field-error"><span class="lang-pt">Por favor indique o seu nome.</span><span class="lang-en">Please enter your name.</span></span>
        </div>
        <div class="field">
          <label for="c-email"><span class="lang-pt">Email</span><span class="lang-en">Email</span> *</label>
          <input type="email" id="c-email" name="email" data-validate="required email">
          <span class="field-error"><span class="lang-pt">Por favor indique um email válido.</span><span class="lang-en">Please enter a valid email.</span></span>
        </div>
        <div class="field">
          <label for="c-phone"><span class="lang-pt">Telefone</span><span class="lang-en">Phone</span></label>
          <input type="tel" id="c-phone" name="phone">
        </div>
        <div class="field">
          <label for="c-org"><span class="lang-pt">Organização</span><span class="lang-en">Organisation</span> <span class="hint">(<span class="lang-pt">opcional</span><span class="lang-en">optional</span>)</span></label>
          <input type="text" id="c-org" name="organisation">
        </div>
        <div class="field full">
          <label for="c-subject"><span class="lang-pt">Assunto</span><span class="lang-en">Subject</span> *</label>
          <select id="c-subject" name="subject" data-validate="required" class="lang-pt">
            {subj_pt}
          </select>
          <select id="c-subject-en" name="subject" data-validate="required" class="lang-en" disabled>
            {subj_en}
          </select>
        </div>
        <div class="field full">
          <label for="c-message"><span class="lang-pt">Mensagem</span><span class="lang-en">Message</span> *</label>
          <textarea id="c-message" name="message" data-validate="required"></textarea>
          <span class="field-error"><span class="lang-pt">Por favor escreva a sua mensagem.</span><span class="lang-en">Please write your message.</span></span>
        </div>
        <div class="field full">
          <label class="checkbox-row"><input type="checkbox" name="consent" data-validate="required">
            <span><span class="lang-pt">Aceito que os meus dados sejam usados para me responderem, conforme a</span><span class="lang-en">I agree that my data may be used to reply to me, in line with the</span> <a href="privacidade.html"><span class="lang-pt">Política de Privacidade</span><span class="lang-en">Privacy Policy</span></a>. *</span>
          </label>
          <span class="field-error"><span class="lang-pt">É necessário aceitar para continuar.</span><span class="lang-en">You must agree to continue.</span></span>
        </div>
      </div>
      <button type="submit" class="btn btn-primary"><span class="lang-pt">Enviar mensagem</span><span class="lang-en">Send message</span></button>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
"""

html = page(
    title_pt="Contacto", title_en="Contact",
    desc_pt="Contacte a AZEMAP por email, telefone, WhatsApp ou através do formulário de contacto.",
    desc_en="Contact AZEMAP by email, phone, WhatsApp, or via the contact form.",
    canonical="contacto.html", active_key="contacto", body_html=CONTACT_BODY,
)
with open("/home/claude/azemap-site/contacto.html", "w", encoding="utf-8") as f:
    f.write(html)
print("contacto.html written:", len(html))
