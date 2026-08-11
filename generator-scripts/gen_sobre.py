# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Sobre Nós</span><span class="lang-en">About Us</span></p>
    <h1><span class="lang-pt">Uma associação nascida da dor, transformada em esperança</span><span class="lang-en">An association born of pain, transformed into hope</span></h1>
    <p><span class="lang-pt">A AZEMAP nasceu em 2015, após a morte de Zé Manuel Pinto, pessoa com albinismo. A experiência familiar revelou as dificuldades enfrentadas diariamente pelas Pessoas com Albinismo e despertou a necessidade de criar uma organização dedicada à dignidade, protecção, inclusão e defesa dos seus direitos.</span>
    <span class="lang-en">AZEMAP was founded in 2015, after the death of Zé Manuel Pinto, a person with albinism. That family experience revealed the difficulties faced daily by people with albinism and sparked the need to create an organisation dedicated to dignity, protection, inclusion and the defence of their rights.</span></p>
  </div>
</section>

<section class="section">
  <div class="container center-col text-center">
    <p style="font-size:1.25rem; font-family:var(--font-display); font-weight:700; color:var(--teal-800); font-style:normal;">
      <span class="lang-pt">&ldquo;Não nasceu do conforto. Nasceu da dor, da urgência e da necessidade de existir com dignidade.&rdquo;</span>
      <span class="lang-en">&ldquo;It was not born of comfort. It was born of pain, urgency, and the need to exist with dignity.&rdquo;</span>
    </p>
    <p class="hint" style="margin-top:10px;"><span class="lang-pt">Em memória de Zé Manuel Pinto</span><span class="lang-en">In memory of Zé Manuel Pinto</span></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="text-center center-col" style="margin-bottom:40px;">
      <p class="eyebrow" style="justify-content:center;"><span class="lang-pt">Percurso</span><span class="lang-en">Timeline</span></p>
      <h2><span class="lang-pt">Uma década de acção</span><span class="lang-en">A decade of action</span></h2>
    </div>
    <div class="timeline center-col">
      <div class="timeline-item">
        <div class="timeline-year">2015</div>
        <p><span class="lang-pt">Criação da AZEMAP, em memória de Zé Manuel Pinto.</span><span class="lang-en">AZEMAP is founded, in memory of Zé Manuel Pinto.</span></p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">25 <span class="lang-pt">de Agosto de</span><span class="lang-en">August</span> 2016</div>
        <p><span class="lang-pt">Reconhecimento como pessoa jurídica pelo Governo da Província de Tete.</span><span class="lang-en">Recognised as a legal entity by the Government of Tete Province.</span></p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">12 <span class="lang-pt">de Dezembro de</span><span class="lang-en">December</span> 2018</div>
        <p><span class="lang-pt">Publicação do reconhecimento e dos estatutos no Boletim da República, III Série, Número 242.</span><span class="lang-en">Recognition and statutes published in the Boletim da República, III Series, Number 242.</span></p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">2025&ndash;2026</div>
        <p><span class="lang-pt">A AZEMAP assinala aproximadamente 10 anos de trabalho e activismo.</span><span class="lang-en">AZEMAP marks approximately 10 years of work and advocacy.</span></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container center-col quote-block">
    <blockquote style="border-left:4px solid var(--orange-600); padding-left:22px; margin:0; color:var(--ink-700); font-size:clamp(1.2rem, 2vw, 1.7rem); line-height:1.5; font-weight:700; font-family:var(--font-display); text-align:left; max-width:980px;">
      <span class="lang-pt">&ldquo;Continuaremos a trabalhar para que nenhuma Pessoa com Albinismo seja privada de saúde, educação, protecção, respeito ou oportunidades por causa da sua condição.&rdquo;</span>
      <span class="lang-en">&ldquo;We will continue to work so that no person with albinism is deprived of health, education, protection, respect or opportunities because of their condition.&rdquo;</span>
    </blockquote>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center center-col" style="margin-bottom:40px;">
      <p class="eyebrow" style="justify-content:center;"><span class="lang-pt">Governação</span><span class="lang-en">Governance</span></p>
      <h2><span class="lang-pt">Como a AZEMAP é dirigida</span><span class="lang-en">How AZEMAP is governed</span></h2>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <h3><span class="lang-pt">Assembleia Geral</span><span class="lang-en">General Assembly</span></h3>
        <p><span class="lang-pt">O órgão supremo da AZEMAP, composto por todos os associados, responsável por eleger os restantes órgãos e aprovar os planos e contas anuais.</span>
        <span class="lang-en">AZEMAP's supreme body, made up of all members, responsible for electing the other bodies and approving annual plans and accounts.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Conselho de Direcção</span><span class="lang-en">Board of Directors</span></h3>
        <p><span class="lang-pt">O órgão executivo, responsável pela gestão diária e pela representação da associação.</span>
        <span class="lang-en">The executive body, responsible for day-to-day management and representing the association.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Conselho Fiscal</span><span class="lang-en">Supervisory Board</span></h3>
        <p><span class="lang-pt">O órgão consultivo de fiscalização, responsável por analisar as contas e o funcionamento financeiro.</span>
        <span class="lang-en">The advisory oversight body, responsible for reviewing accounts and financial operations.</span></p>
      </div>
    </div>
  </div>
</section>
"""

html = page(
    title_pt="Sobre Nós",
    title_en="About Us",
    desc_pt="Conheça a história da AZEMAP, nascida em 2015 em memória de Zé Manuel Pinto, a sua missão e governação.",
    desc_en="Learn about AZEMAP's history, founded in 2015 in memory of Zé Manuel Pinto, its mission and governance.",
    canonical="sobre.html",
    active_key="sobre",
    body_html=BODY,
)
with open("sobre.html", "w", encoding="utf-8") as f:
    f.write(html)
print("sobre.html written:", len(html))
