# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

# ---------------- HISTORIAS ----------------
STORIES = [
    dict(img="beneficiaria-protetor.jpg", tags="saude tete",
         meta_pt="Cidade de Tete · Saúde", meta_en="Tete City · Health",
         title_pt="Identificação e acompanhamento de uma nova beneficiária",
         title_en="Identifying and following up a new beneficiary",
         text_pt="Durante uma actividade na Cidade de Tete, a equipa da AZEMAP identificou uma Pessoa com Albinismo que já havia recebido protector solar em ocasiões anteriores. O caso foi encaminhado para confirmação do registo e continuidade do acompanhamento.",
         text_en="During an activity in Tete City, the AZEMAP team identified a person with albinism who had already received sunscreen on previous occasions. The case was referred for registration confirmation and continued follow-up.",
         obj="50% 15%"),
    dict(img="visita-domiciliaria.jpg", tags="saude tete apoio-social",
         meta_pt="Tete · Saúde", meta_en="Tete · Health",
         title_pt="O acompanhamento familiar faz a diferença",
         title_en="Family follow-up makes a difference",
         text_pt="A utilização regular de protector solar, combinada com o apoio e compromisso das famílias, contribui para uma melhor protecção da pele das crianças com albinismo.",
         text_en="Regular sunscreen use, combined with families' support and commitment, contributes to better skin protection for children with albinism.",
         obj="50% 20%"),
    dict(img="calomue-distribuicao.jpg", tags="saude calomue",
         meta_pt="Calomué · Saúde", meta_en="Calomué · Health",
         title_pt="Distribuição de protector solar em Calomué",
         title_en="Sunscreen distribution in Calomué",
         text_pt="A equipa da AZEMAP deslocou-se ao Centro de Saúde de Calomué para entregar protector solar aos beneficiários e reforçar o acompanhamento local.",
         text_en="The AZEMAP team travelled to the Calomué Health Centre to deliver sunscreen to beneficiaries and strengthen local follow-up.",
         obj="50% 15%"),
    dict(img="familia-criancas-2.jpg", tags="saude apoio-social",
         meta_pt="Tete · Apoio Social", meta_en="Tete · Social Support",
         title_pt="Uma família, dois motivos para continuar",
         title_en="One family, two reasons to keep going",
         text_pt="Numa comunidade rural de Tete, a AZEMAP acompanha uma família com duas crianças com albinismo, apoiando o acesso a protector solar e reforçando a orientação familiar sobre os cuidados necessários.",
         text_en="In a rural community in Tete, AZEMAP supports a family with two children with albinism, helping with access to sunscreen and reinforcing family guidance on the care they need.",
         obj="50% 20%"),
    dict(img="jovem-oculos.jpg", tags="apoio-social educacao",
         meta_pt="Tete · Apoio Social", meta_en="Tete · Social Support",
         title_pt="Proximidade que gera confiança",
         title_en="Closeness that builds trust",
         text_pt="As visitas domiciliárias da AZEMAP permitem identificar necessidades de saúde, educação e protecção social, e construir uma relação de confiança duradoura com as famílias acompanhadas.",
         text_en="AZEMAP's home visits help identify health, education and social protection needs, and build a lasting relationship of trust with the families it supports.",
         obj="50% 15%"),
    dict(img="familia-criancas-1.jpg", tags="saude educacao",
         meta_pt="Tete · Saúde", meta_en="Tete · Health",
         title_pt="Óculos que abrem um novo horizonte",
         title_en="Glasses that open a new horizon",
         text_pt="A distribuição de óculos de sol e produtos de protecção ajuda crianças e jovens com albinismo a participar com mais conforto nas actividades do dia-a-dia, dentro e fora da escola.",
         text_en="Distributing sunglasses and protective products helps children and young people with albinism take part more comfortably in everyday activities, at school and beyond.",
         obj="50% 10%"),
]

def story_card(s):
    return f"""<article class="card story-card" data-tags="{s['tags']}">
        <img src="assets/images/{s['img']}" alt="" style="object-position:{s['obj']};">
        <div class="story-body">
          <p class="story-meta"><span class="lang-pt">{s['meta_pt']}</span><span class="lang-en">{s['meta_en']}</span></p>
          <h3><span class="lang-pt">{s['title_pt']}</span><span class="lang-en">{s['title_en']}</span></h3>
          <p><span class="lang-pt">{s['text_pt']}</span><span class="lang-en">{s['text_en']}</span></p>
        </div>
      </article>"""

stories_html = "\n      ".join(story_card(s) for s in STORIES)

HIST_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Histórias de Impacto</span><span class="lang-en">Impact Stories</span></p>
    <h1><span class="lang-pt">Histórias que respeitam quem as vive</span><span class="lang-en">Stories that respect the people who live them</span></h1>
    <p><span class="lang-pt">Cada história é partilhada com o cuidado devido à privacidade e dignidade das Pessoas com Albinismo. Não usamos nomes completos de crianças nem informação médica sensível.</span>
    <span class="lang-en">Every story is shared with the care owed to the privacy and dignity of people with albinism. We do not use children's full names or sensitive medical information.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="filter-row" data-filter-group="[data-tags]" data-empty-state="#historias-empty">
      <button class="filter-chip" data-filter="all" aria-pressed="true"><span class="lang-pt">Todas</span><span class="lang-en">All</span></button>
      <button class="filter-chip" data-filter="saude" aria-pressed="false"><span class="lang-pt">Saúde</span><span class="lang-en">Health</span></button>
      <button class="filter-chip" data-filter="educacao" aria-pressed="false"><span class="lang-pt">Educação</span><span class="lang-en">Education</span></button>
      <button class="filter-chip" data-filter="apoio-social" aria-pressed="false"><span class="lang-pt">Apoio Social</span><span class="lang-en">Social Support</span></button>
    </div>
    <div class="grid grid-3">
      {stories_html}
    </div>
    <div id="historias-empty" class="empty-state" style="display:none;">
      <p><span class="lang-pt">Sem histórias nesta categoria por agora.</span><span class="lang-en">No stories in this category yet.</span></p>
    </div>
  </div>
</section>
"""

html = page(
    title_pt="Histórias de Impacto", title_en="Impact Stories",
    desc_pt="Histórias reais e dignificantes do acompanhamento da AZEMAP às Pessoas com Albinismo em Tete, Moçambique.",
    desc_en="Real, dignified stories from AZEMAP's work with people with albinism in Tete, Mozambique.",
    canonical="historias.html", active_key="historias", body_html=HIST_BODY,
)
with open("historias.html", "w", encoding="utf-8") as f:
    f.write(html)
print("historias.html written:", len(html))

# ---------------- NOTICIAS ----------------
CATS = [
    ("saude", "Saúde", "Health"), ("educacao", "Educação", "Education"),
    ("apoio-social", "Apoio Social", "Social Support"), ("advocacia", "Advocacia", "Advocacy"),
    ("formacao", "Formação", "Training"), ("eventos", "Eventos", "Events"),
    ("parcerias", "Parcerias", "Partnerships"), ("consciencializacao", "Dia da Consciencialização", "Awareness Day"),
]
chips = "\n      ".join(
    f'<button class="filter-chip" data-filter="{k}" aria-pressed="false"><span class="lang-pt">{pt}</span><span class="lang-en">{en}</span></button>'
    for k, pt, en in CATS
)

NEWS_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Notícias e Actividades</span><span class="lang-en">News and Activities</span></p>
    <h1><span class="lang-pt">O que se passa na AZEMAP</span><span class="lang-en">What's happening at AZEMAP</span></h1>
    <p><span class="lang-pt">Acompanhe as actividades, formações e campanhas da associação.</span>
    <span class="lang-en">Follow the association's activities, training sessions and campaigns.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="filter-row" data-filter-group="[data-news-item]" data-empty-state="#news-empty">
      <button class="filter-chip" data-filter="all" aria-pressed="true"><span class="lang-pt">Todas</span><span class="lang-en">All</span></button>
      {chips}
    </div>
    <div id="news-empty" class="empty-state">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19.5V6a2 2 0 0 1 2-2h8l6 6v9.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 19.5Z"/><path d="M14 4v5a1 1 0 0 0 1 1h5"/></svg>
      <h3><span class="lang-pt">Ainda sem notícias publicadas</span><span class="lang-en">No published news yet</span></h3>
      <p class="max-prose" style="margin:0 auto;"><span class="lang-pt">Esta secção está pronta para receber as próximas notícias e actividades da AZEMAP. Assim que forem publicadas, vai encontrá-las aqui, organizadas por categoria, distrito e data.</span>
      <span class="lang-en">This section is ready to receive AZEMAP's upcoming news and activities. Once published, you'll find them here, organised by category, district and date.</span></p>
    </div>
  </div>
</section>
"""

html = page(
    title_pt="Notícias e Actividades", title_en="News and Activities",
    desc_pt="Notícias, formações, campanhas e eventos da AZEMAP em Tete, Moçambique.",
    desc_en="News, training, campaigns and events from AZEMAP in Tete, Mozambique.",
    canonical="noticias.html", active_key="noticias", body_html=NEWS_BODY,
)
with open("noticias.html", "w", encoding="utf-8") as f:
    f.write(html)
print("noticias.html written:", len(html))

# ---------------- GALERIA ----------------
GALLERY = [
    dict(img="calomue-distribuicao.jpg", tags="saude calomue 2026",
         cap_pt="Saúde inclusiva em Calomué — actividade de distribuição de protector solar realizada junto do Centro de Saúde de Calomué.",
         cap_en="Inclusive health in Calomué — sunscreen distribution activity held at the Calomué Health Centre.", obj="50% 15%"),
    dict(img="beneficiaria-protetor.jpg", tags="saude 2026",
         cap_pt="Protecção solar nas comunidades — a AZEMAP acompanha famílias e distribui produtos de protecção solar a Pessoas com Albinismo em diferentes comunidades da Província de Tete.",
         cap_en="Sun protection in the communities — AZEMAP supports families and distributes sun protection products to people with albinism across communities in Tete Province.", obj="50% 12%"),
    dict(img="visita-domiciliaria.jpg", tags="saude apoio-social 2026",
         cap_pt="Apoio próximo das famílias — as visitas domiciliárias permitem identificar necessidades de saúde, educação e protecção social.",
         cap_en="Support close to families — home visits help identify health, education and social protection needs.", obj="50% 18%"),
    dict(img="familia-criancas-2.jpg", tags="saude apoio-social 2026",
         cap_pt="Acompanhamento em comunidades rurais da Província de Tete.",
         cap_en="Follow-up in rural communities across Tete Province.", obj="50% 20%"),
    dict(img="jovem-oculos.jpg", tags="apoio-social educacao 2026",
         cap_pt="Proximidade e confiança entre a AZEMAP e as famílias acompanhadas.",
         cap_en="Closeness and trust between AZEMAP and the families it supports.", obj="50% 15%"),
    dict(img="familia-criancas-1.jpg", tags="saude educacao 2026",
         cap_pt="Distribuição de óculos e produtos de protecção solar a um jovem beneficiário.",
         cap_en="Distributing glasses and sun protection products to a young beneficiary.", obj="50% 8%"),
    dict(img="apoio-comunitario.jpg", tags="saude apoio-social 2026",
         cap_pt="Encontro entre uma colaboradora da associação e uma beneficiária, com protector solar em mãos.",
         cap_en="A meeting between an association collaborator and a beneficiary, holding sunscreen.", obj="50% 12%"),
]

def gallery_item(g):
    return f"""<figure class="card" style="padding:0; overflow:hidden; cursor:pointer;" data-lightbox-trigger data-tags="{g['tags']}" data-caption="{g['cap_pt']}" tabindex="0" role="button" aria-label="Ampliar imagem / Enlarge image">
        <img src="assets/images/{g['img']}" alt="" style="aspect-ratio:1/1; object-fit:cover; object-position:{g['obj']}; border-radius:var(--radius-md);">
      </figure>"""

gallery_html = "\n      ".join(gallery_item(g) for g in GALLERY)

GAL_BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Galeria</span><span class="lang-en">Gallery</span></p>
    <h1><span class="lang-pt">Momentos do trabalho no terreno</span><span class="lang-en">Moments from our fieldwork</span></h1>
    <p><span class="lang-pt">Todas as imagens são utilizadas com o devido cuidado de consentimento e dignidade. Clique numa imagem para a ampliar.</span>
    <span class="lang-en">All images are used with appropriate care for consent and dignity. Click an image to enlarge it.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="filter-row" data-filter-group="[data-lightbox-trigger]" data-empty-state="#gallery-empty">
      <button class="filter-chip" data-filter="all" aria-pressed="true"><span class="lang-pt">Todas</span><span class="lang-en">All</span></button>
      <button class="filter-chip" data-filter="saude" aria-pressed="false"><span class="lang-pt">Saúde</span><span class="lang-en">Health</span></button>
      <button class="filter-chip" data-filter="educacao" aria-pressed="false"><span class="lang-pt">Educação</span><span class="lang-en">Education</span></button>
      <button class="filter-chip" data-filter="apoio-social" aria-pressed="false"><span class="lang-pt">Apoio Social</span><span class="lang-en">Social Support</span></button>
    </div>
    <div class="grid grid-4">
      {gallery_html}
    </div>
    <div id="gallery-empty" class="empty-state" style="display:none;">
      <p><span class="lang-pt">Sem imagens nesta categoria por agora.</span><span class="lang-en">No images in this category yet.</span></p>
    </div>
    <p class="hint" style="margin-top:26px;">
      <span class="lang-pt">As capturas de ecrã do WhatsApp utilizadas para preparar este conteúdo são material de origem interno e não são publicadas nesta galeria.</span>
      <span class="lang-en">The WhatsApp screenshots used to prepare this content are internal source material and are not published in this gallery.</span>
    </p>
  </div>
</section>
"""

html = page(
    title_pt="Galeria", title_en="Gallery",
    desc_pt="Fotografias do trabalho de terreno da AZEMAP com Pessoas com Albinismo na Província de Tete.",
    desc_en="Field photographs of AZEMAP's work with people with albinism in Tete Province.",
    canonical="galeria.html", active_key="galeria", body_html=GAL_BODY,
)
with open("galeria.html", "w", encoding="utf-8") as f:
    f.write(html)
print("galeria.html written:", len(html))
