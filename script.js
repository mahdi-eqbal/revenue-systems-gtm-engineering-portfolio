(function () {
  'use strict';
  const data = window.PORTFOLIO;
  if (!data) {
    document.querySelectorAll('#project-grid,#video-grid,#slice-grid,#post-grid').forEach(el => el.textContent = 'Content is temporarily unavailable.');
    return;
  }
  const $ = selector => document.querySelector(selector);
  const E = (tag, className, text) => {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined && text !== null) el.textContent = text;
    return el;
  };
  const link = (url, label, className) => {
    const el = E('a', className, label);
    el.href = url;
    el.target = '_blank';
    el.rel = 'noopener noreferrer';
    return el;
  };
  const append = (parent, ...nodes) => { nodes.forEach(node => parent.append(node)); return parent; };

  data.projects.forEach(p => {
    const card = E('article','project ' + p.accent);
    const header = E('div','project-header');
    append(header,E('span','project-num',p.number),E('span','',p.category));
    const heading = E('h3','',p.title);
    const description = E('p','',p.description);
    const list = E('ul');
    p.built.forEach(point => list.append(E('li','',point)));
    const tags = E('div','chips');
    p.tools.forEach(name => tags.append(E('span','chip',name)));
    const actions = E('div','project-actions');
    append(actions,link(p.repo,'View case study ↗'),link(p.evidence,'Review evidence ↗'));
    if (p.video) actions.append(link(p.video,'Watch demo ↗'));
    append(card,header,heading,description,list,tags,actions);
    $('#project-grid').append(card);
  });

  data.videos.forEach(v => {
    const card = E('article','video-card');
    const mediaLink = link(v.video,'','video-media');
    mediaLink.setAttribute('aria-label','Watch ' + v.title + ' on YouTube');
    const img = E('img');
    img.src = v.thumb;
    img.alt = 'Video preview for ' + v.title;
    img.loading = 'lazy';
    img.referrerPolicy = 'no-referrer';
    img.onerror = () => { img.remove(); };
    append(mediaLink,img,E('span','play','▶'));
    const body = E('div','video-body');
    const top = E('div','video-top');
    append(top,E('span','',v.type),E('span','',v.related));
    append(body,top,E('h3','',v.title),E('p','',v.description),link(v.video,'Watch on YouTube ↗','watch'));
    append(card,mediaLink,body);
    $('#video-grid').append(card);
  });
  data.slices.forEach(s => {
    const card = E('article','slice');
    const foot = E('footer');
    append(foot,E('span','',s.tool),link(s.url,'Inspect source ↗'));
    append(card,E('span','type',s.category),E('h3','',s.title),E('p','',s.description),foot);
    $('#slice-grid').append(card);
  });
  data.posts.forEach(p => {
    const card = E('article','post-card');
    const foot = E('footer');
    append(foot,E('span','',p.related),link(p.url,'Read on LinkedIn ↗'));
    append(card,E('span','type',p.type),E('h3','',p.title),E('p','',p.description),foot);
    $('#post-grid').append(card);
  });
  const toggle = $('[data-menu]');
  const nav = $('[data-nav]');
  const close = () => { toggle?.setAttribute('aria-expanded','false');nav?.classList.remove('open'); };
  toggle?.addEventListener('click',()=>{
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded',String(open));
    nav?.classList.toggle('open',open);
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click',close));
  document.addEventListener('keydown',event => { if (event.key === 'Escape') close(); });
  $('#year').textContent = new Date().getFullYear();
})();
