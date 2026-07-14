# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_common import page

PRIV_BODY = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Política de Privacidade</span><span class="lang-en">Privacy Policy</span></p>
    <h1><span class="lang-pt">Como tratamos os seus dados</span><span class="lang-en">How we handle your data</span></h1>
    <p><span class="lang-pt">A AZEMAP respeita a privacidade de todas as pessoas que a contactam, apoiam ou acompanham o seu trabalho.</span>
    <span class="lang-en">AZEMAP respects the privacy of everyone who contacts, supports, or follows its work.</span></p>
  </div>
</section>

<section class="section">
  <div class="container center-col">
    <h2><span class="lang-pt">Que dados recolhemos</span><span class="lang-en">What data we collect</span></h2>
    <p><span class="lang-pt">Recolhemos apenas os dados que nos fornece voluntariamente através dos formulários deste site — nome, contacto, e a mensagem ou pedido que nos envia. Não recolhemos dados sensíveis de saúde através dos formulários gerais de contacto.</span>
    <span class="lang-en">We only collect the data you voluntarily provide through this site's forms — your name, contact details, and the message or request you send us. We do not collect sensitive health data through general contact forms.</span></p>

    <h2><span class="lang-pt">Como usamos os seus dados</span><span class="lang-en">How we use your data</span></h2>
    <p><span class="lang-pt">Os dados são usados exclusivamente para responder ao seu pedido — informação, donativo, voluntariado ou parceria — e não são vendidos ou partilhados com terceiros para fins comerciais.</span>
    <span class="lang-en">Your data is used solely to respond to your request — information, donation, volunteering or partnership — and is never sold or shared with third parties for commercial purposes.</span></p>

    <h2><span class="lang-pt">Armazenamento</span><span class="lang-en">Storage</span></h2>
    <p><span class="lang-pt">Enquanto o sistema de envio automático não estiver activo, as submissões dos formulários são processadas manualmente pela equipa da AZEMAP. Assim que um sistema de armazenamento seguro for configurado, esta política será actualizada com mais detalhes técnicos.</span>
    <span class="lang-en">While the automated submission system is not yet active, form submissions are processed manually by the AZEMAP team. Once a secure storage system is configured, this policy will be updated with further technical details.</span></p>

    <h2><span class="lang-pt">Os seus direitos</span><span class="lang-en">Your rights</span></h2>
    <p><span class="lang-pt">Pode solicitar, a qualquer momento, o acesso, a correcção ou a eliminação dos seus dados, contactando-nos através da página de Contacto.</span>
    <span class="lang-en">You may request access to, correction of, or deletion of your data at any time by contacting us through the Contact page.</span></p>

    <h2><span class="lang-pt">Imagens e conteúdo de beneficiários</span><span class="lang-en">Images and beneficiary content</span></h2>
    <p><span class="lang-pt">O uso de fotografias e histórias de beneficiários segue regras próprias, descritas na nossa <a href="protecao-imagem.html">Política de Protecção e Uso de Imagem</a>.</span>
    <span class="lang-en">The use of beneficiary photographs and stories follows its own rules, described in our <a href="protecao-imagem.html">Safeguarding and Image-Use Policy</a>.</span></p>

    <p class="hint"><span class="lang-pt">Última actualização: Julho de 2026.</span><span class="lang-en">Last updated: July 2026.</span></p>
  </div>
</section>
"""

html = page(
    title_pt="Política de Privacidade", title_en="Privacy Policy",
    desc_pt="Como a AZEMAP recolhe, usa e protege os dados pessoais partilhados através deste site.",
    desc_en="How AZEMAP collects, uses and protects personal data shared through this site.",
    canonical="privacidade.html", active_key="", body_html=PRIV_BODY,
)
with open("/home/claude/azemap-site/privacidade.html", "w", encoding="utf-8") as f:
    f.write(html)
print("privacidade.html written:", len(html))

SAFE_BODY = """
<section class="page-hero">
  <div class="container">
    <p class="eyebrow" style="color:#F4C542;"><span class="lang-pt">Protecção e Uso de Imagem</span><span class="lang-en">Safeguarding &amp; Image-Use Policy</span></p>
    <h1><span class="lang-pt">O respeito começa antes da fotografia</span><span class="lang-en">Respect begins before the photograph</span></h1>
    <p><span class="lang-pt">Muitas das pessoas acompanhadas pela AZEMAP são crianças ou pessoas em situação de vulnerabilidade. Este compromisso orienta todo o uso de imagem e conteúdo pela associação.</span>
    <span class="lang-en">Many of the people AZEMAP works with are children or people in vulnerable situations. This commitment guides all of the association's use of imagery and content.</span></p>
  </div>
</section>

<section class="section">
  <div class="container center-col">
    <div class="grid grid-2">
      <div class="card">
        <h3><span class="lang-pt">Respeito</span><span class="lang-en">Respect</span></h3>
        <p><span class="lang-pt">Nunca usamos linguagem ou imagens que humilhem, infantilizem ou representem as Pessoas com Albinismo como vítimas indefesas.</span>
        <span class="lang-en">We never use language or images that humiliate, infantilise, or portray people with albinism as helpless victims.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Consentimento informado</span><span class="lang-en">Informed consent</span></h3>
        <p><span class="lang-pt">Procuramos o consentimento da pessoa fotografada e, no caso de crianças, do respectivo encarregado de educação, antes de qualquer publicação.</span>
        <span class="lang-en">We seek consent from the person photographed and, for children, from their guardian, before any publication.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Protecção de crianças</span><span class="lang-en">Child protection</span></h3>
        <p><span class="lang-pt">Não publicamos nomes completos de crianças, diagnósticos médicos ou moradas exactas.</span>
        <span class="lang-en">We do not publish children's full names, medical diagnoses, or exact addresses.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Minimização de dados</span><span class="lang-en">Data minimisation</span></h3>
        <p><span class="lang-pt">Recolhemos e publicamos apenas a informação estritamente necessária para contar uma história com dignidade.</span>
        <span class="lang-en">We collect and publish only the information strictly necessary to tell a story with dignity.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Privacidade</span><span class="lang-en">Privacy</span></h3>
        <p><span class="lang-pt">Removemos metadados de localização das fotografias sempre que possível, antes da publicação.</span>
        <span class="lang-en">We remove location metadata from photographs whenever possible before publication.</span></p>
      </div>
      <div class="card">
        <h3><span class="lang-pt">Pedidos de remoção</span><span class="lang-en">Removal requests</span></h3>
        <p><span class="lang-pt">Qualquer pessoa ou família pode solicitar a remoção de uma fotografia ou história a qualquer momento, sem necessidade de justificação.</span>
        <span class="lang-en">Anyone or any family may request the removal of a photograph or story at any time, with no justification required.</span></p>
      </div>
    </div>

    <hr class="divider">

    <h2 class="text-center"><span class="lang-pt">Como solicitar a remoção de conteúdo</span><span class="lang-en">How to request content removal</span></h2>
    <p class="text-center max-prose" style="margin:0 auto;"><span class="lang-pt">Contacte-nos através da página de <a href="contacto.html">Contacto</a>, indicando a página ou imagem em questão. Responderemos o mais rapidamente possível e removeremos o conteúdo assim que o pedido for confirmado.</span>
    <span class="lang-en">Contact us through the <a href="contacto.html">Contact</a> page, indicating the page or image in question. We will respond as quickly as possible and remove the content once the request is confirmed.</span></p>
  </div>
</section>
"""

html = page(
    title_pt="Protecção e Uso de Imagem", title_en="Safeguarding and Image-Use Policy",
    desc_pt="Os princípios de consentimento, protecção de crianças e dignidade que orientam o uso de imagem pela AZEMAP.",
    desc_en="The consent, child-protection and dignity principles that guide AZEMAP's use of imagery.",
    canonical="protecao-imagem.html", active_key="", body_html=SAFE_BODY,
)
with open("/home/claude/azemap-site/protecao-imagem.html", "w", encoding="utf-8") as f:
    f.write(html)
print("protecao-imagem.html written:", len(html))

NOTFOUND_BODY = """
<section class="section" style="min-height:60vh; display:flex; align-items:center;">
  <div class="container text-center center-col">
    <p class="eyebrow" style="justify-content:center;">404</p>
    <h1><span class="lang-pt">Esta página não foi encontrada</span><span class="lang-en">This page could not be found</span></h1>
    <p class="max-prose" style="margin:0 auto 30px;">
      <span class="lang-pt">O endereço que procura pode ter sido movido ou já não existe. Volte à página inicial ou explore o nosso trabalho.</span>
      <span class="lang-en">The address you're looking for may have moved or no longer exists. Return to the homepage or explore our work.</span>
    </p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn-primary" href="index.html"><span class="lang-pt">Voltar ao Início</span><span class="lang-en">Back to Home</span></a>
      <a class="btn btn-outline" href="contacto.html"><span class="lang-pt">Contactar a AZEMAP</span><span class="lang-en">Contact AZEMAP</span></a>
    </div>
  </div>
</section>
"""

html = page(
    title_pt="Página não encontrada", title_en="Page not found",
    desc_pt="A página que procura não foi encontrada no site da AZEMAP.",
    desc_en="The page you're looking for could not be found on the AZEMAP site.",
    canonical="404.html", active_key="", body_html=NOTFOUND_BODY,
)
with open("/home/claude/azemap-site/404.html", "w", encoding="utf-8") as f:
    f.write(html)
print("404.html written:", len(html))
