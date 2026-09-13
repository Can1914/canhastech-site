/* CanhasTech analytics — GA4 + Microsoft Clarity, loaded only after consent (KVKK). */
(function(){
  var GA='G-2STNGSKBXE', CL='yhtj5b2zsf', KEY='ct_consent';
  var en=document.documentElement.lang==='en';
  var T=en?{t:'We use cookies for analytics',m:'Only to understand which pages are read and where visitors come from. No ads, no selling data.',a:'Accept',r:'Decline',p:'Privacy notice'}
          :{t:'Analitik için çerez kullanıyoruz',m:'Sadece hangi sayfaların okunduğunu ve ziyaretçilerin nereden geldiğini anlamak için. Reklam yok, veri satışı yok.',a:'Kabul et',r:'Reddet',p:'KVKK metni'};
  var privacy=(location.pathname.indexOf('/en/')>-1?'':'')+'kvkk.html';
  function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}window.gtag=gtag;
  function load(){
    if(window.__ctLoaded)return;window.__ctLoaded=true;
    var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);
    gtag('js',new Date());gtag('config',GA,{anonymize_ip:true});
    (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(window,document,"clarity","script",CL);
  }
  function track(name,params){
    if(!window.__ctLoaded)return;
    try{gtag('event',name,params||{})}catch(e){}
    try{window.clarity&&window.clarity('event',name)}catch(e){}
  }
  window.ctTrack=track;
  function banner(){
    var b=document.createElement('div');b.className='consent-bar';b.setAttribute('role','dialog');b.setAttribute('aria-label',T.t);
    b.innerHTML='<div class="cb-text"><b>'+T.t+'</b><span>'+T.m+' <a href="'+privacy+'">'+T.p+'</a></span></div><div class="cb-actions"><button type="button" class="btn sm" data-c="no">'+T.r+'</button><button type="button" class="btn sm primary" data-c="yes">'+T.a+'</button></div>';
    b.addEventListener('click',function(e){var x=e.target.closest('[data-c]');if(!x)return;set(x.dataset.c);b.remove();if(x.dataset.c==='yes')load()});
    document.body.appendChild(b);
  }
  var c=get();
  if(c==='yes')load();else if(c!=='no')banner();
  /* conversion events */
  document.addEventListener('click',function(e){
    var a=e.target.closest('a,button');if(!a)return;
    if(a.classList.contains('wa'))track('whatsapp_click',{page:location.pathname});
    if(a.getAttribute('href')==='#demo'||a.id==='dsend')track('demo_cta_click',{label:a.textContent.trim()});
    if(a.classList.contains('lang'))track('language_switch',{to:a.textContent.trim()});
    if(a.id==='tNext'||a.id==='tPrev')track('app_tour_scroll',{dir:a.id});
  });
  document.addEventListener('submit',function(e){
    if(e.target.id==='demoform')track('demo_request',{profile:(document.getElementById('dtype')||{}).value});
    if(e.target.id==='contact')track('contact_request',{type:(document.getElementById('ptype')||{}).value});
  });
  /* scroll depth on Has Rep page */
  if(/hasrep\.html/.test(location.pathname)){var marks=[25,50,75,100],fired={};addEventListener('scroll',function(){var p=Math.round((scrollY+innerHeight)/document.body.scrollHeight*100);marks.forEach(function(m){if(p>=m&&!fired[m]){fired[m]=1;track('scroll_depth',{percent:m})}})},{passive:true})}
})();
