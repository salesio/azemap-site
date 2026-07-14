# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

def programme_section(anchor, tag_pt, tag_en, title_pt, title_en, context_pt, context_en,
                       response_pt, response_en, activities, img, img_alt, reverse=False):
    acts_html = "\n        ".join(
        f'<li><span class="lang-pt">{a[0]}</span><span class="lang-en">{a[1]}</span></li>' for a in activities
    )
    media = f"""<div class="rounded-photo"><img src="assets/images/{img}" alt="{img_alt}" style="aspect-ratio:4/5; object-position:50% 18%;"></div>"""
    text = f"""<div>
      <p class="eyebrow"><span class="lang-pt">{tag_pt}</span><span class="lang-en">{tag_en}</span></p>
      <h2>{title_pt and f'<span class="lang-pt">{title_pt}</span>'}{title_en and f'<span class="lang-en">{title_en}</span>'}</h2>
      <p><span class="lang-pt">{context_pt}</span><span class="lang-en">{context_en}</span></p>
      <p><strong><span class="lang-pt">Resposta da AZEMAP:</span><span class="lang-en">AZEMAP's response:</span></strong> <span class="lang-pt">{response_pt}</span><span class="lang-en">{response_en}</span></p>
      <p style="font-weight:700; color:var(--teal-800); margin-bottom:6px;"><span class="lang-pt">Actividades</span><span class="lang-en">Activities</span></p>
      <ul style="color:var(--ink-600);">{acts_html}</ul>
    </div>"""
    cols = f'{media}\n    {text}' if not reverse else f'{text}\n    {media}'
    return f"""<section class="section{' section-alt' if reverse else ''}" id="{anchor}">
  <div class="container split">
    {cols}
  </div>
</section>"""

saude = programme_section(
    "saude", "Saúde e Protecção Solar", "Health &amp; Sun Protection",
    "Saúde e Protecção Solar", "Health and Sun Protection",
    "As Pessoas com Albinismo enfrentam elevado risco de queimaduras solares graves e cancro de pele, com acesso limitado a produtos de protecção e a cuidados dermatológicos especializados.",
    "People with albinism face a high risk of severe sunburn and skin cancer, with limited access to protective products and specialised dermatological care.",
    "a AZEMAP distribui protector solar, óculos e roupa de protecção, apoia consultas dermatológicas e encaminha casos para tratamento, mantendo o acompanhamento junto das famílias e das unidades sanitárias.",
    "AZEMAP distributes sunscreen, sunglasses and protective clothing, supports dermatological consultations and refers cases for treatment, while maintaining follow-up with families and health units.",
    [
        ("Distribuição de protector solar", "Sunscreen distribution"),
        ("Distribuição de óculos de sol", "Sunglasses distribution"),
        ("Distribuição de roupa de protecção", "Protective clothing distribution"),
        ("Apoio a crianças com queimaduras solares graves", "Support for children with severe sunburn"),
        ("Apoio a consultas dermatológicas", "Support for dermatological consultations"),
        ("Encaminhamento para tratamento de cancro de pele", "Referral for skin cancer treatment"),
        ("Visitas a beneficiários doentes e acompanhamento familiar", "Visits to sick beneficiaries and family follow-up"),
        ("Trabalho com centros de saúde e serviços provinciais", "Work with health centres and provincial services"),
    ],
    "calomue-distribuicao.jpg", "Equipa da AZEMAP junto ao Centro de Saúde de Calomué",
    reverse=False,
)

educacao = programme_section(
    "educacao", "Educação Inclusiva", "Inclusive Education",
    "Educação Inclusiva", "Inclusive Education",
    "Crianças com albinismo enfrentam frequentemente baixa visão, discriminação e exclusão na escola, o que compromete a sua permanência e sucesso educativo.",
    "Children with albinism often face low vision, discrimination and exclusion at school, which undermines their attendance and educational success.",
    "a AZEMAP apoia com material escolar e uniformes, forma professores, sensibiliza escolas e acompanha os alunos, promovendo a inclusão em sala de aula e a prevenção do bullying.",
    "AZEMAP supports children with school materials and uniforms, trains teachers, raises awareness in schools and follows up with students, promoting classroom inclusion and preventing bullying.",
    [
        ("Distribuição de material escolar", "School materials distribution"),
        ("Distribuição de uniformes", "Uniform distribution"),
        ("Apoio a crianças rejeitadas ou negligenciadas pela família", "Support for children rejected or neglected by their families"),
        ("Formação de professores", "Teacher training"),
        ("Sensibilização nas escolas", "Awareness-raising in schools"),
        ("Inclusão em sala de aula", "Classroom inclusion"),
        ("Incentivo a sentarem-se perto do quadro por baixa visão", "Encouraging children with low vision to sit near the front"),
        ("Acompanhamento escolar e prevenção da discriminação", "School follow-up and discrimination prevention"),
    ],
    "familia-criancas-1.jpg", "Jovem beneficiário da AZEMAP com material de protecção solar",
    reverse=True,
)

apoio_social = programme_section(
    "apoio-social", "Apoio Social e Protecção", "Social Support and Protection",
    "Apoio Social e Protecção", "Social Support and Protection",
    "Pessoas com albinismo em situação de vulnerabilidade social, incluindo crianças abandonadas ou em risco, precisam de identificação, acompanhamento e ligação a serviços de apoio.",
    "People with albinism in situations of social vulnerability, including abandoned or at-risk children, need identification, follow-up and referral to support services.",
    "a AZEMAP identifica beneficiários, realiza visitas familiares, promove a inclusão social e orienta as famílias, mobilizando a comunidade para a protecção contra a violência e a negligência.",
    "AZEMAP identifies beneficiaries, carries out family visits, promotes social inclusion and guides families, mobilising the community to protect against violence and neglect.",
    [
        ("Apoio a crianças abandonadas ou vulneráveis", "Support for abandoned or vulnerable children"),
        ("Visitas familiares", "Family visits"),
        ("Identificação de beneficiários", "Beneficiary identification"),
        ("Inclusão social", "Social inclusion"),
        ("Orientação familiar", "Family guidance"),
        ("Formação de jovens activistas", "Development of young activists"),
        ("Encaminhamento para serviços adequados", "Referral to appropriate services"),
        ("Mobilização comunitária e protecção contra a violência", "Community mobilisation and protection against violence"),
    ],
    "jovem-oculos.jpg", "Família acompanhada pela AZEMAP, com duas crianças com albinismo",
    reverse=False,
)

advocacia = programme_section(
    "advocacia", "Advocacia e Direitos Humanos", "Advocacy and Human Rights",
    "Advocacia e Direitos Humanos", "Advocacy and Human Rights",
    "A discriminação e a violência contra Pessoas com Albinismo persistem por falta de informação e de políticas públicas consistentes.",
    "Discrimination and violence against people with albinism persist due to a lack of information and consistent public policy.",
    "a AZEMAP realiza campanhas de sensibilização, educação em direitos humanos e advocacia junto de instituições públicas, representando os interesses das Pessoas com Albinismo em fóruns nacionais e internacionais.",
    "AZEMAP runs awareness campaigns, human rights education and advocacy with public institutions, representing the interests of people with albinism in national and international forums.",
    [
        ("Campanhas contra a discriminação", "Anti-discrimination campaigns"),
        ("Campanhas contra a violência", "Anti-violence campaigns"),
        ("Educação em direitos humanos", "Human rights education"),
        ("Sensibilização comunitária", "Community awareness"),
        ("Murais escolares", "School murals"),
        ("Sessões de formação", "Training sessions"),
        ("Participação em fóruns nacionais e internacionais", "Participation in national and international forums"),
        ("Advocacia para políticas públicas", "Public policy advocacy"),
    ],
    "apoio-comunitario.jpg", "Colaboradora da AZEMAP com um beneficiário",
    reverse=True,
)

BODY = f"""
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">O Nosso Trabalho</span><span class="lang-en">Our Work</span></p>
    <h1><span class="lang-pt">Quatro frentes, uma só missão</span><span class="lang-en">Four fronts, one mission</span></h1>
    <p><span class="lang-pt">A AZEMAP actua em saúde, educação, apoio social e advocacia, sempre com respeito pela dignidade e autonomia de cada Pessoa com Albinismo.</span>
    <span class="lang-en">AZEMAP works across health, education, social support and advocacy, always respecting the dignity and autonomy of every person with albinism.</span></p>
    <div class="hero-actions" style="margin-top:22px;">
      <a class="btn btn-ghost-light btn-sm" href="#saude"><span class="lang-pt">Saúde</span><span class="lang-en">Health</span></a>
      <a class="btn btn-ghost-light btn-sm" href="#educacao"><span class="lang-pt">Educação</span><span class="lang-en">Education</span></a>
      <a class="btn btn-ghost-light btn-sm" href="#apoio-social"><span class="lang-pt">Apoio Social</span><span class="lang-en">Social Support</span></a>
      <a class="btn btn-ghost-light btn-sm" href="#advocacia"><span class="lang-pt">Advocacia</span><span class="lang-en">Advocacy</span></a>
    </div>
  </div>
</section>

{saude}
{educacao}
{apoio_social}
{advocacia}

<section class="section text-center">
  <div class="container center-col">
    <h2><span class="lang-pt">Quer apoiar uma destas áreas?</span><span class="lang-en">Want to support one of these areas?</span></h2>
    <p><span class="lang-pt">Cada contribuição pode ser direccionada para uma necessidade concreta — protector solar, material escolar, transporte para consultas, ou apoio institucional.</span>
    <span class="lang-en">Every contribution can be directed to a concrete need — sunscreen, school materials, transport to appointments, or institutional support.</span></p>
    <a class="btn btn-primary" href="apoie-nos.html"><span class="lang-pt">Ver formas de apoiar</span><span class="lang-en">See ways to help</span></a>
  </div>
</section>
"""

html = page(
    title_pt="O Nosso Trabalho",
    title_en="Our Work",
    desc_pt="Saúde e protecção solar, educação inclusiva, apoio social e advocacia: conheça as quatro áreas de intervenção da AZEMAP.",
    desc_en="Health and sun protection, inclusive education, social support and advocacy: explore AZEMAP's four programme areas.",
    canonical="trabalho.html",
    active_key="trabalho",
    body_html=BODY,
)
with open("trabalho.html", "w", encoding="utf-8") as f:
    f.write(html)
print("trabalho.html written:", len(html))
