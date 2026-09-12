/* CanhasTech — shared behaviour: kinetic type, scroll reveal, glass glow, active nav */
(function(){
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* split [data-kinetic] text into per-character spans with a stagger */
  document.querySelectorAll('[data-kinetic]').forEach(el=>{
    const txt=el.textContent;const base=parseFloat(el.dataset.delay||0);const step=parseFloat(el.dataset.step||0.028);
    el.setAttribute('aria-label',txt);el.classList.add('k');el.textContent='';
    [...txt].forEach((c,i)=>{const s=document.createElement('span');s.className='ch'+(c===' '?' sp':'');s.textContent=c===' '?' ':c;s.style.animationDelay=(base+i*step)+'s';s.setAttribute('aria-hidden','true');el.appendChild(s)});
  });
  /* stagger multi-line headings */
  document.querySelectorAll('h1,h2').forEach(h=>h.querySelectorAll('.line>span').forEach((s,i)=>{if(!s.style.animationDelay)s.style.animationDelay=(0.08+i*0.12)+'s'}));

  /* reveal on scroll: blocks below the fold rest quiet, then rise */
  const els=document.querySelectorAll('.rv');
  if(reduce||!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('go'))}
  else{
    els.forEach(e=>{if(e.getBoundingClientRect().top>innerHeight*.92)e.classList.add('pre');else e.classList.add('go')});
    const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.remove('pre');en.target.classList.add('go');io.unobserve(en.target)}}),{threshold:.12});
    els.forEach(e=>io.observe(e));
  }

  /* cursor-following glow on glass cards */
  document.querySelectorAll('.glass').forEach(card=>card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();card.style.setProperty('--mx',(e.clientX-r.left)+'px');card.style.setProperty('--my',(e.clientY-r.top)+'px')}));

  /* active nav link */
  const here=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('nav ul a').forEach(a=>{const h=a.getAttribute('href').split('#')[0]||'index.html';if(h===here)a.classList.add('active')});
})();
