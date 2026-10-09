/* Portfolio content registry. Add projects, walkthroughs, implementation slices and posts here.
   Evidence links are public; do not publish secrets or private client artifacts. */
window.PORTFOLIO = {
  projects: [
    {
      id: 'p1', number: '01', category: 'HubSpot / n8n', title: 'From product intent to a reliable sales handoff',
      description: 'A controlled path from product events to qualification, identity resolution and a usable HubSpot follow-up.',
      problem: 'Product activity should not create duplicate records or sales work simply because an event arrived again.',
      built: ['Event validation and persistent processing state', 'Contact and company identity resolution', 'Qualification, routing and active-deal guards', 'Explicit failure handling and test evidence'],
      tools: ['HubSpot','n8n','PostgreSQL','REST APIs','JavaScript'],
      repo: 'https://github.com/mahdi-eqbal/p1-product-led-revenue-system',
      evidence: 'https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/main/evidence',
      video: 'https://youtu.be/Q-sc8ETdLwk', accent: 'blue'
    },
    {
      id: 'p2', number: '02', category: 'Salesforce / RevOps', title: 'A lead-to-opportunity system with state and SLAs',
      description: 'A Salesforce-centered implementation that checks lead readiness and ownership before a CRM-native sales task is created.',
      problem: 'Inbound leads need consistent qualification, routing, follow-up timing and a recoverable processing trail.',
      built: ['Inbound validation and intake idempotency', 'Lead matching before record creation', 'Deterministic routing and SLA calculation', 'Salesforce Flow task creation and API failure paths'],
      tools: ['Salesforce','Salesforce Flow','n8n','PostgreSQL','REST APIs'],
      repo: 'https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system',
      evidence: 'https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/blob/main/TEST-MATRIX.md',
      video: null, accent: 'amber'
    },
    {
      id: 'p3', number: '03', category: 'Clay / AI GTM', title: 'Account intelligence with evidence, not guesswork',
      description: 'Clay enrichment and structured Claygent research feeding explainable account prioritization and manual review.',
      problem: 'Target account decisions require traceable signals and confidence controls, not opaque AI-generated rankings.',
      built: ['Enrichment and GTM job-signal resolution', 'Evidence-aware structured Claygent outputs', 'Deterministic scoring and priority tiers', 'Uncertainty gates and actionable/review queues'],
      tools: ['Clay','Claygent','GTM Signals','AI','Scoring'],
      repo: 'https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system',
      evidence: 'https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/main/evidence/EVIDENCE-MANIFEST.md',
      video: null, accent: 'violet'
    }
  ],
  videos: [
    { id: 'walkthrough', type: 'Technical walkthrough', duration: 'Detailed demo', title: 'A revenue handoff, with the failure paths included', description: 'A tour of the HubSpot-centered system, from product signal through matching, qualification and sales follow-up.', video: 'https://youtu.be/Q-sc8ETdLwk', thumb: 'https://i.ytimg.com/vi/Q-sc8ETdLwk/hqdefault.jpg', related: 'P1' },
    { id: 'overview', type: 'Short overview', duration: 'Quick watch', title: 'The handoff in two minutes', description: 'A shorter look at the business problem and the workflow outcome.', video: 'https://youtu.be/WypfoN5QbWY', thumb: 'https://i.ytimg.com/vi/WypfoN5QbWY/hqdefault.jpg', related: 'P1' }
  ],
  slices: [
    {category:'Workflow controls', title:'Preventing duplicate sales handoffs', description:'A focused walkthrough of identity matching, duplicate-event checks and active-deal protection in P1.', source:'P1 implementation', url:'https://github.com/mahdi-eqbal/p1-product-led-revenue-system', tool:'HubSpot + n8n'},
    {category:'CRM operations', title:'Making an SLA part of the workflow', description:'Routing decisions and SLA timing feed a Salesforce-native follow-up task, with the processing state persisted.', source:'P2 implementation', url:'https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system', tool:'Salesforce + n8n'},
    {category:'AI quality controls', title:'Keeping uncertain AI research out of the action queue', description:'Structured Claygent findings are scored by rules and gated for human review where evidence is weak.', source:'P3 implementation', url:'https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system', tool:'Clay + AI'}
  ],
  posts: [
    {type:'Project breakdown', title:'A product signal is not a sales handoff', description:'Why matching, state and explicit decision paths matter in a product-led revenue workflow.', url:'https://www.linkedin.com/posts/mahdi-eqbal_product-led-revenue-qualification-sales-activity-7498856963368357888-JfZW', related:'P1'},
    {type:'Project breakdown', title:'Turning GTM research into reviewable decisions', description:'A behind-the-build explanation of AI-assisted account research and prioritization.', url:'https://www.linkedin.com/posts/mahdi-eqbal-b50329296_gtmengineering-revenuesystems-revops-activity-7500100147964538880-lta-', related:'P3'},
    {type:'Engineering note', title:'What a timed-out CRM request does not tell you', description:'Why a failed response can be different from a failed write, and what that means for retries.', url:'https://www.linkedin.com/posts/mahdi-eqbal_revops-n8n-activity-7511677770482106369-gB80', related:'Reliability'}
  ]
};
