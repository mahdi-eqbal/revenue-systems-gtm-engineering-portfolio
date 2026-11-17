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
    },
    {
      id: 'cle', number: '04', category: 'n8n / GTM Operations', title: 'Campaign learning with evidence and review gates',
      description: 'A review-first n8n prototype for validating campaign outcomes, comparing variants cautiously and holding synthetic account examples for human verification.',
      problem: 'Campaign activity needs clean event data and evidence checks before teams draw conclusions or take action.',
      built: ['Validated campaign outcome intake', 'Unique-prospect variant reporting with small-sample guardrails', 'Synthetic account-fit walkthrough with transparent rules', 'Human-review and missing-evidence holds; sending disabled'],
      tools: ['n8n','JavaScript','Data Tables','Synthetic data','Human review'],
      repo: 'https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/projects/campaign-learning-engine/',
      evidence: 'https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/projects/campaign-learning-engine/evidence/n8n-execution.md',
      video: null, accent: 'blue'
    },
    {
      id: 'rlm', kind: 'product', number: '05', category: 'Python / Django / Revenue Assurance',
      preview: 'https://handofftrace.htlabs.workers.dev/',
      title: 'HandoffTrace — Lead Handoff Assurance',
      description: 'Independent assurance product in development. Explore a published interactive replay of fictional, engine-generated audit findings; customer-connected monitoring is not released.',
      problem: 'An automation can succeed without proving the individual lead reached the right CRM record, owner and timely Task.',
      built: ['Live public static showcase of five fictional engine-generated findings',
              'Private deterministic event/identity reconciliation and owner/Task/SLA checks',
              'Versioned local assurance rules, audit history and explainable review findings',
              'Selected read-only HubSpot Sandbox diagnostics; production CRM integration not released'],
      tools: ['Python','Django','JavaScript','CRM Evidence','GitHub Actions'],
      repo: 'https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/tree/main/projects/revenue-leak-monitor',
      evidence: 'https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/blob/main/projects/revenue-leak-monitor/EVIDENCE.md',
      video: null, accent: 'blue'
    },
    {
      id: 'crm-quality', number: '06', category: 'CRM Data Quality / Controlled Repair',
      title: 'CRM Data Quality & Controlled Repair',
      description: 'A reproducible offline demo and developer-test audit for reviewing duplicate candidates, validating proposed repairs and holding uncertain deliveries.',
      problem: 'Similar CRM records and stale source data can lead to unsafe cleanup. Each proposed change needs review and a traceable outcome.',
      built: ['Deterministic and fuzzy candidate matching', 'Review gates and in-memory repair verification', 'PostgreSQL delivery journal and Make/Airtable reconciliation', 'Evidence-backed recovery decision for an HTTP 401'],
      tools: ['Python','HubSpot','PostgreSQL','Make','Airtable'],
      repo: 'https://github.com/mahdi-eqbal/crm-data-quality-controlled-repair',
      evidence: 'https://github.com/mahdi-eqbal/crm-data-quality-controlled-repair/blob/main/docs/31-a11-public-verification.md',
      video: './projects/crm-data-quality/', accent: 'blue'
    },
    {
      id: 'zoho-lead-intake', number: '07', category: 'Zoho CRM / Lead Intake',
      title: 'Zoho CRM Lead Intake',
      description: 'Verified HighLevel and Google Sheets intake in Zoho CRM EU Sandbox, with a direct webhook test for a synthetic Google Ads lead.',
      problem: 'Estimate inquiries from multiple sources can arrive twice or with required fields missing.',
      built: ['HighLevel and Google Sheets intake through Make', 'Zoho email uniqueness and duplicate-specific Skip route', 'Visible required-field validation', 'Google Ads-format webhook payload verified through CRM writeback'],
      tools: ['Zoho CRM','Make','HighLevel','Google Sheets','Python'],
      repo: './projects/zoho-crm-integration/',
      evidence: 'https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/tree/main/projects/zoho-crm-integration',
      video: './projects/zoho-crm-integration/#demos', accent: 'blue'
    },
    {
      id: 'p02-ai-appointment', number: '08', category: 'HighLevel / AI Lead Qualification',
      title: 'AI website chat to a booked CRM opportunity',
      description: 'A restricted synthetic HighLevel AI chat qualifies Dublin residential interior-painting leads and moves the same CRM opportunity through the appointment handoff.',
      problem: 'A chat reply or booking link alone does not establish that a qualified enquiry reached the CRM or that a confirmed appointment advances the same opportunity.',
      built: ['AI-triggered qualification workflow and contact tagging', 'Opportunity creation in Estimates / Qualified', 'Observed repeat-enquiry guard and commercial/out-of-area exclusion', 'Confirmed API appointment moving the original opportunity to Booked'],
      tools: ['HighLevel','Conversation AI','Live Chat','Workflows','CRM','Calendar API'],
      repo: 'https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/blob/main/projects/p02-ai-lead-appointment/README.md',
      evidence: 'https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/blob/main/projects/p02-ai-lead-appointment/README.md',
      video: null, accent: 'violet'
    }
  ],
  videos: [
    { id: "zoho-intake", type: "Client demo", duration: "0:42", title: "From Inquiry to CRM", description: "Follow a valid inquiry through Make to its lead record in Zoho CRM Sandbox.", video: 'https://youtu.be/XjhBRj_1-nw', thumb: 'https://i.ytimg.com/vi/XjhBRj_1-nw/hqdefault.jpg', related: 'Zoho CRM Lead Intake' },
    { id: "zoho-quality", type: "Client demo", duration: "0:36", title: "Duplicate & Incomplete Leads", description: "See how the workflow skips a duplicate email and stops a lead with a missing last name.", video: 'https://youtu.be/yVkdavs_Cpc', thumb: 'https://i.ytimg.com/vi/yVkdavs_Cpc/hqdefault.jpg', related: 'Zoho CRM Lead Intake' },
    { id: "zoho-technical", type: "Technical walkthrough", duration: "1:55", title: "Make → Zoho CRM", description: "Review the Make execution paths, including the synthetic Google Ads-format webhook test.", video: 'https://youtu.be/CHyGE6ld82c', thumb: 'https://i.ytimg.com/vi/CHyGE6ld82c/hqdefault.jpg', related: 'Zoho CRM Lead Intake' },
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
