# -*- coding: utf-8 -*-
"""Generate the AZEMAP achievements and success stories page."""

from build_common import page

BODY = r"""
<div class="page-hero achievements-hero">
  <div class="container">
    <p class="eyebrow"><span class="lang-pt">Impacto documentado</span><span class="lang-en">Documented impact</span></p>
    <h1><span class="lang-pt">Grandes realizações e histórias de sucesso</span><span class="lang-en">Key achievements and success stories</span></h1>
    <p><span class="lang-pt">Marcos do trabalho da AZEMAP na saúde, educação, protecção e promoção dos direitos das Pessoas com Albinismo na Província de Tete.</span><span class="lang-en">Milestones from AZEMAP's work in health, education, protection and the promotion of the rights of people with albinism in Tete Province.</span></p>
  </div>
</div>

<section class="section achievements-intro">
  <div class="container">
    <div class="achievement-stats">
      <article><strong>402</strong><span class="lang-pt">pessoas registadas no levantamento institucional</span><span class="lang-en">people recorded in the institutional survey</span></article>
      <article><strong>208</strong><span class="lang-pt">crianças, adolescentes e jovens dos 0 aos 18 anos</span><span class="lang-en">children and young people aged 0–18</span></article>
      <article><strong>6</strong><span class="lang-pt">comités distritais documentados em 2025</span><span class="lang-en">district committees documented in 2025</span></article>
      <article><strong>6</strong><span class="lang-pt">distritos alcançados por murais de sensibilização</span><span class="lang-en">districts reached through awareness murals</span></article>
    </div>
    <p class="achievement-source-note"><span class="lang-pt">Dados provenientes da apresentação institucional AZEMAP 2025. O cadastro é contínuo e os totais podem evoluir com novas identificações.</span><span class="lang-en">Figures are drawn from AZEMAP's 2025 institutional presentation. Registration is ongoing and totals may evolve as new people are identified.</span></p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-heading-row">
      <div>
        <p class="eyebrow"><span class="lang-pt">Marcos de impacto</span><span class="lang-en">Impact milestones</span></p>
        <h2><span class="lang-pt">Resultados construídos com as comunidades</span><span class="lang-en">Results built with communities</span></h2>
      </div>
      <p><span class="lang-pt">Trabalho realizado com famílias, unidades sanitárias, escolas, lideranças comunitárias, governo e parceiros.</span><span class="lang-en">Work delivered with families, health facilities, schools, community leaders, government and partners.</span></p>
    </div>

    <div class="achievement-feature-grid">
      <article class="achievement-feature">
        <div class="achievement-image"><img src="assets/images/realizacao-consulta-dermatologia-2023.jpg" alt="Consulta dermatológica a uma pessoa com albinismo durante uma missão médica em 2023"></div>
        <div class="achievement-copy"><span class="achievement-year">2023</span><h3><span class="lang-pt">Assistência dermatológica mais próxima</span><span class="lang-en">Dermatology care brought closer</span></h3><p><span class="lang-pt">A AZEMAP documentou consultas e tratamento dermatológico nos distritos de Angónia e Moatize, em cooperação com equipas do Hospital Provincial de Tete, Hospital Rural de Angónia, Serviço Provincial de Saúde e África Directo.</span><span class="lang-en">AZEMAP documented dermatology consultations and treatment in Angónia and Moatize, in cooperation with teams from Tete Provincial Hospital, Angónia Rural Hospital, the Provincial Health Service and África Directo.</span></p></div>
      </article>

      <article class="achievement-feature achievement-feature-reverse">
        <div class="achievement-image"><img src="assets/images/realizacao-mural-inclusao-2022.jpg" alt="Mural comunitário com mensagem de igualdade para Pessoas com Albinismo"></div>
        <div class="achievement-copy"><span class="achievement-year">2022</span><h3><span class="lang-pt">Mensagens de inclusão no espaço público</span><span class="lang-en">Inclusion messages in public spaces</span></h3><p><span class="lang-pt">Foram pintados murais de sensibilização na Cidade de Tete e nos distritos de Angónia, Magoé, Moatize, Changara e Chiúta, levando uma mensagem simples e directa contra a discriminação.</span><span class="lang-en">Awareness murals were painted in Tete City and the districts of Angónia, Magoé, Moatize, Changara and Chiúta, carrying a simple and direct message against discrimination.</span></p></div>
      </article>

      <article class="achievement-feature">
        <div class="achievement-image"><img src="assets/images/realizacao-comites-2025.jpg" alt="Formação de comités distritais para protecção e promoção dos direitos das Pessoas com Albinismo"></div>
        <div class="achievement-copy"><span class="achievement-year">2025</span><h3><span class="lang-pt">Protecção organizada a nível distrital</span><span class="lang-en">Protection organised at district level</span></h3><p><span class="lang-pt">A apresentação institucional regista secretariados de comités distritais em Tsangano, Angónia, Macanga, Moatize, Mutarara e Cidade de Tete. Estes mecanismos aproximam a prevenção, encaminhamento e promoção dos direitos das comunidades.</span><span class="lang-en">The institutional presentation records district committee secretariats in Tsangano, Angónia, Macanga, Moatize, Mutarara and Tete City. These mechanisms bring prevention, referral and rights promotion closer to communities.</span></p></div>
      </article>
    </div>
  </div>
</section>

<section class="section medical-campaign-section">
  <div class="container">
    <div class="section-heading-row">
      <div>
        <p class="eyebrow"><span class="lang-pt">Intervenção em destaque</span><span class="lang-en">Featured intervention</span></p>
        <h2><span class="lang-pt">4.ª campanha de observação e tratamento médico</span><span class="lang-en">4th medical screening and treatment campaign</span></h2>
      </div>
      <p><span class="lang-pt">Uma resposta coordenada para aproximar cuidados especializados das Pessoas com Albinismo em toda a Província de Tete.</span><span class="lang-en">A coordinated response bringing specialist care closer to people with albinism across Tete Province.</span></p>
    </div>

    <div class="campaign-lead">
      <div class="campaign-lead-image"><img src="assets/images/campanha-medica-2026-atendimento.jpg" alt="Médicas especialistas durante o atendimento a Pessoas com Albinismo no Hospital Rural de Angónia"></div>
      <div class="campaign-lead-copy">
        <span class="achievement-year">Outubro de 2026</span>
        <h3><span class="lang-pt">Cuidados especializados mais perto das comunidades</span><span class="lang-en">Specialist care closer to communities</span></h3>
        <p><span class="lang-pt">A AZEMAP promove a quarta edição da campanha de observação e tratamento médico das Pessoas com Albinismo nos distritos da Província de Tete, em parceria com a África Directo, os governos provincial e distritais e a Direcção Provincial de Saúde de Tete.</span><span class="lang-en">AZEMAP is promoting the fourth medical screening and treatment campaign for people with albinism across the districts of Tete Province, in partnership with África Directo, provincial and district governments, and the Tete Provincial Health Directorate.</span></p>
        <p><span class="lang-pt">A campanha mobiliza especialistas em oftalmologia, dermatologia e cirurgia maxilofacial, reforçando o encaminhamento e o acesso a cuidados adequados.</span><span class="lang-en">The campaign brings together specialists in ophthalmology, dermatology and maxillofacial surgery, strengthening referrals and access to appropriate care.</span></p>
      </div>
    </div>

    <div class="campaign-photo-grid">
      <figure><img src="assets/images/campanha-medica-2026-abertura.jpg" alt="Abertura e acompanhamento institucional da campanha no Hospital Rural de Angónia"><figcaption><span class="lang-pt">Abertura e acompanhamento institucional da campanha no Hospital Rural de Angónia.</span><span class="lang-en">Institutional opening and follow-up of the campaign at Angónia Rural Hospital.</span></figcaption></figure>
      <figure><img src="assets/images/campanha-medica-2026-espera.jpg" alt="Pessoas com Albinismo aguardam atendimento médico no Hospital Rural de Angónia"><figcaption><span class="lang-pt">Beneficiários aguardam atendimento médico no âmbito da campanha.</span><span class="lang-en">Beneficiaries await medical care as part of the campaign.</span></figcaption></figure>
      <figure><img src="assets/images/campanha-medica-2026-comunidade.jpg" alt="Pessoas com Albinismo reunidas durante a campanha médica em Angónia"><figcaption><span class="lang-pt">A mobilização aproxima os serviços de saúde das Pessoas com Albinismo e das suas famílias.</span><span class="lang-en">Community mobilisation brings health services closer to people with albinism and their families.</span></figcaption></figure>
    </div>

    <div class="campaign-poster-row">
      <img src="assets/images/campanha-medica-2026-cartaz.jpg" alt="Cartaz da quarta campanha gratuita de observação médica para Pessoas com Albinismo em Tete">
      <div>
        <p class="eyebrow"><span class="lang-pt">Presença provincial</span><span class="lang-en">Province-wide presence</span></p>
        <h3><span class="lang-pt">Atendimento gratuito em vários distritos</span><span class="lang-en">Free care across several districts</span></h3>
        <p><span class="lang-pt">O calendário da campanha inclui unidades sanitárias nos distritos de Angónia, Macanga, Marávia, Zumbo, Chifunde, Chiúta, Marara, Changara, Cahora Bassa, Moatize e Cidade de Tete.</span><span class="lang-en">The campaign schedule includes health facilities in the districts of Angónia, Macanga, Marávia, Zumbo, Chifunde, Chiúta, Marara, Changara, Cahora Bassa, Moatize and Tete City.</span></p>
        <a class="text-link" href="galeria.html"><span class="lang-pt">Ver mais fotografias da intervenção</span><span class="lang-en">See more photographs from the intervention</span> →</a>
      </div>
    </div>
  </div>
</section>

<section class="section success-story-section">
  <div class="container">
    <div class="success-story-card">
      <div class="success-story-photo"><img src="assets/images/historia-sucesso-medicina.jpg" alt="Técnica de medicina geral formada no Instituto de Ciências de Saúde de Tete"></div>
      <div class="success-story-content">
        <p class="eyebrow"><span class="lang-pt">História de sucesso</span><span class="lang-en">Success story</span></p>
        <h2><span class="lang-pt">Uma profissional de saúde a abrir caminhos</span><span class="lang-en">A health professional opening new paths</span></h2>
        <p><span class="lang-pt">Entre os resultados apresentados pela AZEMAP está a formação de uma técnica em Medicina Geral no Instituto de Ciências de Saúde de Tete. A conquista representa o potencial das Pessoas com Albinismo quando encontram oportunidades de educação, acompanhamento e inclusão.</span><span class="lang-en">Among the outcomes presented by AZEMAP is the graduation of a General Medicine technician from the Tete Institute of Health Sciences. Her achievement reflects the potential of people with albinism when education, support and inclusion are available.</span></p>
        <blockquote><span class="lang-pt">O sucesso não é apenas individual: torna-se uma referência para crianças e jovens que procuram o seu próprio caminho.</span><span class="lang-en">Success is not only individual: it becomes a reference for children and young people finding their own path.</span></blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section section-teal achievements-timeline-section">
  <div class="container">
    <div class="text-center center-col">
      <p class="eyebrow"><span class="lang-pt">Crescimento contínuo</span><span class="lang-en">Continuous growth</span></p>
      <h2><span class="lang-pt">Uma trajectória de presença e compromisso</span><span class="lang-en">A journey of presence and commitment</span></h2>
    </div>
    <div class="achievement-timeline">
      <article><strong>2018–2019</strong><p><span class="lang-pt">Confraternização comunitária e formação de activistas sobre direitos humanos.</span><span class="lang-en">Community gatherings and human-rights training for activists.</span></p></article>
      <article><strong>2019–2022</strong><p><span class="lang-pt">Visitas domiciliárias, distribuição de protectores solares, cremes e sabões, e campanhas comunitárias.</span><span class="lang-en">Home visits, distribution of sunscreen, creams and soap, and community campaigns.</span></p></article>
      <article><strong>2023</strong><p><span class="lang-pt">Consultas dermatológicas e tratamento em cooperação com equipas de saúde nacionais e internacionais.</span><span class="lang-en">Dermatology consultations and treatment with national and international health teams.</span></p></article>
      <article><strong>2025</strong><p><span class="lang-pt">Consolidação de comités distritais e visitas de acompanhamento a crianças órfãs e vulneráveis.</span><span class="lang-en">Consolidation of district committees and follow-up visits to orphaned and vulnerable children.</span></p></article>
    </div>
  </div>
</section>

<section class="section achievements-cta">
  <div class="container text-center center-col">
    <p class="eyebrow"><span class="lang-pt">O próximo capítulo</span><span class="lang-en">The next chapter</span></p>
    <h2><span class="lang-pt">Ajude-nos a transformar mais histórias</span><span class="lang-en">Help us transform more stories</span></h2>
    <p><span class="lang-pt">Apoie o acompanhamento de saúde, a educação inclusiva, a protecção comunitária e a defesa de direitos.</span><span class="lang-en">Support health follow-up, inclusive education, community protection and rights advocacy.</span></p>
    <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="apoie-nos.html"><span class="lang-pt">Apoiar a missão</span><span class="lang-en">Support the mission</span></a><a class="btn btn-outline" href="contacto.html"><span class="lang-pt">Falar com a AZEMAP</span><span class="lang-en">Contact AZEMAP</span></a></div>
  </div>
</section>
"""

html = page(
    title_pt="Grandes Realizações",
    title_en="Key Achievements",
    desc_pt="Grandes realizações e histórias de sucesso da AZEMAP na saúde, educação, protecção e direitos das Pessoas com Albinismo em Tete.",
    desc_en="AZEMAP's key achievements and success stories in health, education, protection and the rights of people with albinism in Tete.",
    canonical="realizacoes.html",
    active_key="realizacoes",
    body_html=BODY,
)

with open("realizacoes.html", "w", encoding="utf-8") as f:
    f.write(html)

print("realizacoes.html written:", len(html), "bytes")
