const LAST_UPDATED = "June 28, 2026";

const navItems = [
  { href: "#overview", label: "Overview" },
  { href: "#data", label: "Data" },
  { href: "#choices", label: "Choices" },
  { href: "#contact", label: "Contact" },
];

const policySections = [
  {
    id: "overview",
    eyebrow: "Policy scope",
    title: "Who we are",
    paragraphs: [
      "90mins Pitch Pulse is a football news, transfer, rumour, and match-analysis channel. This Privacy Policy explains how we handle information when you visit this website, interact with our content, contact us, or engage with our official channel and social profiles.",
      "This policy applies to 90mins Pitch Pulse pages, content, contact forms, community spaces, and related digital experiences that link to this policy. Third-party platforms such as YouTube, TikTok, Instagram, Facebook, X, or other social services also apply their own privacy policies when you use them.",
    ],
  },
  {
    id: "data",
    eyebrow: "Information",
    title: "Information we may collect",
    paragraphs: [
      "We do not require visitors to create an account to read this Privacy Policy or view standard site content. When you choose to interact with us, we may receive limited information depending on the feature or platform you use.",
    ],
    bullets: [
      "Contact information, such as your name, email address, social handle, or message content when you send an inquiry.",
      "Community interaction data, such as comments, replies, likes, shares, or public profile details made available by the platform you use.",
      "Technical information, such as browser type, device information, approximate location, referring pages, and usage activity collected by hosting, analytics, security, or embedded-media tools.",
      "Preferences, such as newsletter choices, notification interests, or content topics you choose to follow if these features are offered.",
    ],
  },
  {
    id: "use",
    eyebrow: "Purpose",
    title: "How we use information",
    bullets: [
      "To publish, maintain, and improve football news, match analysis, transfer updates, and community content.",
      "To respond to questions, feedback, partnership requests, rights requests, or moderation concerns.",
      "To understand what content audiences find useful so we can improve coverage and presentation.",
      "To protect our pages, channel, brand, audience, and systems from abuse, spam, fraud, or security incidents.",
      "To comply with legal obligations, platform rules, and enforceable requests from public authorities where required.",
    ],
  },
  {
    id: "cookies",
    eyebrow: "Cookies",
    title: "Cookies, analytics, and embedded media",
    paragraphs: [
      "This website does not need account cookies for visitors to read the policy. If we add analytics, embedded videos, social widgets, advertising tools, or similar services, those providers may use cookies, pixels, local storage, or comparable technologies to measure performance and deliver their services.",
      "You can control cookies through your browser settings. Blocking some cookies may affect embedded players, social media previews, or analytics preferences.",
    ],
  },
  {
    id: "sharing",
    eyebrow: "Disclosure",
    title: "When information may be shared",
    paragraphs: [
      "We do not sell personal information. We may share limited information with trusted service providers, hosting vendors, analytics providers, platform operators, professional advisers, or legal authorities when necessary for the purposes described in this policy.",
      "If 90mins Pitch Pulse is reorganized, transferred, or combined with another media property, relevant information may be transferred as part of that process while remaining subject to appropriate privacy protections.",
    ],
  },
  {
    id: "retention",
    eyebrow: "Retention",
    title: "How long information is kept",
    paragraphs: [
      "We keep information only for as long as needed for the reason it was collected, including responding to messages, keeping business records, resolving disputes, improving content, maintaining security, or meeting legal requirements.",
      "Public comments or interactions on third-party platforms may remain visible according to the settings and retention rules of those platforms.",
    ],
  },
  {
    id: "choices",
    eyebrow: "Your control",
    title: "Your privacy choices",
    bullets: [
      "You may request access, correction, deletion, or restriction of personal information we control, subject to applicable law.",
      "You may unsubscribe from optional emails or notifications using the unsubscribe or platform controls provided.",
      "You may adjust cookies, tracking controls, ad personalization, and social platform privacy settings directly in your browser or platform account.",
      "You may report public comments, impersonation, misuse, or privacy concerns through the relevant platform tools and by contacting us.",
    ],
  },
  {
    id: "children",
    eyebrow: "Younger audiences",
    title: "Children's privacy",
    paragraphs: [
      "90mins Pitch Pulse is a general football-news channel and is not designed to knowingly collect personal information from children. If you believe a child has provided personal information directly to us without appropriate consent, contact us so we can review and take suitable action.",
    ],
  },
  {
    id: "security",
    eyebrow: "Protection",
    title: "Security",
    paragraphs: [
      "We use reasonable technical and organizational safeguards appropriate to the information we handle. No online service can guarantee absolute security, but we work to reduce risk and respond responsibly if an issue is identified.",
    ],
  },
  {
    id: "changes",
    eyebrow: "Updates",
    title: "Changes to this policy",
    paragraphs: [
      "We may update this Privacy Policy when our services, tools, legal obligations, or channel operations change. The latest version will be posted on this page with a revised last-updated date.",
    ],
  },
];

function App() {
  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>

      <header className="site-header">
        <a className="brand-link" href="#top" aria-label="90mins Pitch Pulse home">
          <img src="/assets/90mins-pitch-pulse-logo.png" alt="" />
          <span>90mins Pitch Pulse</span>
        </a>
        <nav className="site-nav" aria-label="Privacy policy sections">
          {navItems.map((item) => (
            <a key={item.href} href={item.href}>
              {item.label}
            </a>
          ))}
        </nav>
      </header>

      <main id="main">
        <section className="hero" id="top" aria-labelledby="page-title">
          <div className="hero__content">
            <img
              className="hero__logo"
              src="/assets/90mins-pitch-pulse-logo.png"
              alt="90mins Pitch Pulse"
            />
            <p className="eyebrow">Privacy Policy</p>
            <h1 id="page-title">90mins Pitch Pulse Privacy Policy</h1>
            <p className="hero__lead">
              Clear privacy terms for the football channel where latest news,
              match analysis, transfers, and rumours stay in play.
            </p>
            <dl className="hero__meta" aria-label="Policy metadata">
              <div>
                <dt>Last updated</dt>
                <dd>{LAST_UPDATED}</dd>
              </div>
              <div>
                <dt>Channel focus</dt>
                <dd>Football news and analysis</dd>
              </div>
            </dl>
          </div>
        </section>

        <section className="policy-shell" aria-label="Privacy policy content">
          <aside className="policy-aside">
            <p className="aside-label">At a glance</p>
            <h2>No account is required to read this page.</h2>
            <p>
              We collect only the information needed to run the site, respond to
              messages, moderate community spaces, and improve football coverage.
            </p>
            <nav className="toc" aria-label="Policy table of contents">
              {policySections.slice(0, 7).map((section) => (
                <a key={section.id} href={`#${section.id}`}>
                  {section.title}
                </a>
              ))}
            </nav>
          </aside>

          <article className="policy-article">
            {policySections.map((section) => (
              <section
                className="policy-section"
                id={section.id}
                key={section.id}
                aria-labelledby={`${section.id}-title`}
              >
                <p className="section-eyebrow">{section.eyebrow}</p>
                <h2 id={`${section.id}-title`}>{section.title}</h2>
                {section.paragraphs?.map((paragraph) => (
                  <p key={paragraph}>{paragraph}</p>
                ))}
                {section.bullets ? (
                  <ul>
                    {section.bullets.map((item) => (
                      <li key={item}>{item}</li>
                    ))}
                  </ul>
                ) : null}
              </section>
            ))}

            <section
              className="policy-section contact-section"
              id="contact"
              aria-labelledby="contact-title"
            >
              <p className="section-eyebrow">Questions</p>
              <h2 id="contact-title">Contact 90mins Pitch Pulse</h2>
              <p>
                For privacy questions, rights requests, corrections, or concerns
                about content connected to 90mins Pitch Pulse, contact us through
                the official email address, channel page, or social profile listed
                on our current public profiles.
              </p>
              <p>
                Please include enough detail for us to understand your request,
                but avoid sending passwords, payment information, or unnecessary
                sensitive data.
              </p>
            </section>
          </article>
        </section>
      </main>

      <footer className="site-footer">
        <img src="/assets/90mins-pitch-pulse-logo.png" alt="" />
        <p>
          90mins Pitch Pulse. Where football news never sleeps.
          <a href="#top">Back to top</a>
        </p>
      </footer>
    </>
  );
}

export default App;
