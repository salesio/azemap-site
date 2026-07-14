# Website da AZEMAP — Associação Zé Manuel Pinto

Site institucional, bilingue (Português/English), estático e pronto a publicar.

## 1. O que é isto

Um site completo em HTML/CSS/JS puro (sem necessidade de build, Node, ou servidor) para a
AZEMAP. Foi construído como um conjunto estático porque permite ter, hoje, um site completo,
rápido e fácil de editar por qualquer pessoa — mesmo sem conhecimentos de programação — mas
está organizado de forma a poder evoluir para Next.js + Supabase (ou outra stack) mais tarde,
seguindo a mesma arquitectura de conteúdo.

### Como ver o site
Não precisa de instalar nada. Basta abrir `index.html` num navegador, ou, para testar o site
como um servidor real (recomendado, evita problemas com caminhos relativos):

```bash
cd azemap-site
python3 -m http.server 8000
# depois abra http://localhost:8000 no navegador
```

Qualquer servidor de ficheiros estáticos funciona (Netlify, Vercel, GitHub Pages, cPanel, etc.).
Basta enviar a pasta `azemap-site/` completa.

## 2. Estrutura de páginas

| Ficheiro | Página |
|---|---|
| `index.html` | Página Inicial |
| `sobre.html` | Sobre Nós (história, timeline, liderança, governação) |
| `trabalho.html` | O Nosso Trabalho (as 4 áreas: Saúde, Educação, Apoio Social, Advocacia) |
| `onde-trabalhamos.html` | Onde Trabalhamos (distritos, sede) |
| `historias.html` | Histórias de Impacto |
| `noticias.html` | Notícias e Actividades (estado vazio pronto a preencher) |
| `galeria.html` | Galeria (com lightbox acessível) |
| `apoie-nos.html` | Apoie-nos / Donativos |
| `voluntariado.html` | Voluntariado |
| `parceiros.html` | Parceiros |
| `transparencia.html` | Transparência (documento legal, governação) |
| `contacto.html` | Contacto |
| `privacidade.html` | Política de Privacidade |
| `protecao-imagem.html` | Protecção e Uso de Imagem (salvaguarda) |
| `404.html` | Página de erro 404 |

`assets/css/style.css` — todo o sistema de design (cores, tipografia, componentes).
`assets/js/main.js` — idioma, menu móvel, formulários, lightbox da galeria.
`assets/images/` — fotografias de terreno fornecidas.
`assets/documents/` — o PDF do Boletim da República.

## 3. Como o site foi gerado

As páginas HTML foram geradas por pequenos scripts Python (`build_common.py` +
`gen_*.py`, incluídos na pasta `/generator-scripts` para referência futura) que garantem que
o cabeçalho, rodapé, menu e estilo são sempre consistentes. **Não precisa destes scripts para
usar o site** — os ficheiros `.html` já estão completos e funcionam sozinhos. Mas se quiser
alterar um texto que se repete em todas as páginas (por exemplo, um número de telefone no
rodapé), é mais seguro editar o script gerador correspondente e voltar a correr
`python3 gen_*.py`, para não ter de alterar 15 ficheiros à mão.

Para uma alteração pontual numa única página, pode editar o `.html` directamente — é HTML e
CSS simples, sem build necessário.

## 4. Bilingue (PT/EN)

Cada bloco de texto existe duas vezes no HTML, dentro de `<span class="lang-pt">` e
`<span class="lang-en">`. O botão PT/EN no cabeçalho apenas mostra/esconde estes blocos via
CSS e guarda a escolha no navegador (localStorage). Não há duplicação de páginas — o mesmo
ficheiro serve os dois idiomas.

**Para editar um texto**: procure o texto em português dentro de `<span class="lang-pt">`, e
a tradução correspondente logo a seguir em `<span class="lang-en">`.

## 5. Logótipo

Ainda não foi fornecido o logótipo oficial em alta resolução. O site usa:
1. Um logótipo temporário (SVG, inline no código, em `build_common.py` → `SVG_LOGO`), com um
   símbolo simples inspirado em protecção solar e solidariedade — não é o logótipo oficial.
2. Uma paleta de cores derivada da fita/emblema visível no ficheiro que enviou
   (`assets/images/logo-temporario-ref.png`), combinada com as cores que já tinha definido
   (laranja "esperança", amarelo "sol", creme e azul-claro).

**Quando tiver o logótipo oficial em alta resolução:**
1. Guarde o ficheiro (idealmente `.svg` ou `.png` com fundo transparente) em
   `assets/images/logo-oficial.svg` (ou `.png`).
2. Em `build_common.py`, dentro da função `build_header`, substitua o bloco `SVG_LOGO` por:
   `<img class="brand-mark" src="assets/images/logo-oficial.svg" alt="AZEMAP">`
3. Corra todos os `gen_*.py` outra vez (ver secção 3) para actualizar as 15 páginas.

Se preferir, posso fazer esta substituição por si assim que enviar o ficheiro do logótipo.

## 6. Formulários (Contacto, Apoie-nos, Voluntariado)

**Ainda não há um backend ligado.** Isto foi uma escolha deliberada: o site está 100%
funcional e pode ser publicado hoje, e os formulários já têm validação completa (campos
obrigatórios, formato de email, casa de consentimento) e um sistema de fallback que:
- nunca descarta silenciosamente uma submissão — guarda-a no `localStorage` do navegador da
  pessoa que preencheu o formulário, e mostra uma mensagem clara a dizer que a equipa da
  AZEMAP irá processar o pedido manualmente;
- tem protecção anti-spam (honeypot).

**Para ligar um envio real de emails ou uma base de dados**, as opções mais simples são:
- **Formspree / Getform / Web3Forms** (mais rápido): crie uma conta gratuita, e substitua o
  `data-azemap-form="..."` de cada `<form>` por um `action="https://..."` apontado para o
  serviço, e mude o `main.js` para usar `fetch()` para esse endpoint em vez do fallback local.
- **Supabase** (mais robusto, permite gerir submissões, voluntários e donativos num painel):
  criar tabelas `contact_submissions`, `volunteer_applications`, `donation_enquiries` com
  Row Level Security activada (sem leitura pública), e enviar os dados via `fetch()` para a
  Supabase REST API a partir do `main.js`.

Se quiser, posso implementar a ligação a qualquer um destes serviços assim que escolher.

## 7. Conteúdo ainda por confirmar (não inventado)

Seguindo as suas instruções, o site **não inventa** nenhuma destas informações — estão
marcadas como pendentes até serem fornecidas:

- [ ] Logótipo oficial em alta resolução
- [ ] Morada exacta do escritório (o site mostra apenas "Cidade de Tete" de forma aproximada)
- [ ] Dados bancários / M-Pesa / e-Mola / PayPal para donativos
- [ ] Confirmação da cobertura activa em todos os distritos de Tete
- [ ] Links de Facebook / Instagram / YouTube / LinkedIn (ficam ocultos até serem confirmados)
- [ ] Relatórios de actividades e resumos financeiros (secção de Transparência)
- [ ] Logótipos dos parceiros (nomes aparecem em texto até haver ficheiro aprovado)
- [ ] Fotografias e biografias da restante equipa (usa iniciais como marcador temporário)

## 8. Imagens e privacidade

As 7 fotografias de terreno fornecidas foram usadas no hero, nas histórias de impacto e na
galeria, com legendas cuidadosas que não identificam crianças pelo nome nem partilham
informação médica. **As capturas de ecrã do WhatsApp não foram publicadas** — apenas serviram
de base para escrever as três histórias de impacto, tal como pediu.

## 9. Acessibilidade

- Link "Saltar para o conteúdo" no topo de cada página
- Navegação por teclado em todo o site, incluindo menu móvel e lightbox da galeria
- Contraste de cores testado para WCAG AA
- `prefers-reduced-motion` respeitado
- Formulários com mensagens de erro associadas aos campos (não apenas cor)

## 10. Próximos passos recomendados antes do lançamento

1. Rever todos os textos com a Presidente (Flávia Pinto), especialmente a mensagem
   presidencial em `sobre.html`, que está marcada como rascunho.
2. Confirmar e substituir o logótipo temporário.
3. Decidir e configurar um serviço de envio de formulários.
4. Publicar o site num domínio (ex.: `www.azemap.org`) e actualizar os `<link rel="canonical">`
   em cada página, hoje apontados para esse domínio como referência.
5. Confirmar os dados para donativos antes de anunciar a secção "Apoie-nos" publicamente.
