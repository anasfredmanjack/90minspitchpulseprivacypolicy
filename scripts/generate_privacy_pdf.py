from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / "public" / "assets" / "90mins-pitch-pulse-logo.png"
BANNER = ROOT / "public" / "assets" / "90mins-pitch-pulse-banner.png"
OUTPUT = ROOT / "output" / "pdf" / "90mins-pitch-pulse-privacy-policy.pdf"
PUBLIC = ROOT / "public" / "90mins-pitch-pulse-privacy-policy.pdf"

LAST_UPDATED = "June 28, 2026"

SECTIONS = [
    {
        "title": "Who we are",
        "paragraphs": [
            "90mins Pitch Pulse is a football news, transfer, rumour, and match-analysis channel. This Privacy Policy explains how we handle information when you visit this website, interact with our content, contact us, or engage with our official channel and social profiles.",
            "This policy applies to 90mins Pitch Pulse pages, content, contact forms, community spaces, and related digital experiences that link to this policy. Third-party platforms such as YouTube, TikTok, Instagram, Facebook, X, or other social services also apply their own privacy policies when you use them.",
        ],
    },
    {
        "title": "Information we may collect",
        "paragraphs": [
            "We do not require visitors to create an account to read this Privacy Policy or view standard site content. When you choose to interact with us, we may receive limited information depending on the feature or platform you use.",
        ],
        "bullets": [
            "Contact information, such as your name, email address, social handle, or message content when you send an inquiry.",
            "Community interaction data, such as comments, replies, likes, shares, or public profile details made available by the platform you use.",
            "Technical information, such as browser type, device information, approximate location, referring pages, and usage activity collected by hosting, analytics, security, or embedded-media tools.",
            "Preferences, such as newsletter choices, notification interests, or content topics you choose to follow if these features are offered.",
        ],
    },
    {
        "title": "How we use information",
        "bullets": [
            "To publish, maintain, and improve football news, match analysis, transfer updates, and community content.",
            "To respond to questions, feedback, partnership requests, rights requests, or moderation concerns.",
            "To understand what content audiences find useful so we can improve coverage and presentation.",
            "To protect our pages, channel, brand, audience, and systems from abuse, spam, fraud, or security incidents.",
            "To comply with legal obligations, platform rules, and enforceable requests from public authorities where required.",
        ],
    },
    {
        "title": "Cookies, analytics, and embedded media",
        "paragraphs": [
            "This website does not need account cookies for visitors to read the policy. If we add analytics, embedded videos, social widgets, advertising tools, or similar services, those providers may use cookies, pixels, local storage, or comparable technologies to measure performance and deliver their services.",
            "You can control cookies through your browser settings. Blocking some cookies may affect embedded players, social media previews, or analytics preferences.",
        ],
    },
    {
        "title": "When information may be shared",
        "paragraphs": [
            "We do not sell personal information. We may share limited information with trusted service providers, hosting vendors, analytics providers, platform operators, professional advisers, or legal authorities when necessary for the purposes described in this policy.",
            "If 90mins Pitch Pulse is reorganized, transferred, or combined with another media property, relevant information may be transferred as part of that process while remaining subject to appropriate privacy protections.",
        ],
    },
    {
        "title": "How long information is kept",
        "paragraphs": [
            "We keep information only for as long as needed for the reason it was collected, including responding to messages, keeping business records, resolving disputes, improving content, maintaining security, or meeting legal requirements.",
            "Public comments or interactions on third-party platforms may remain visible according to the settings and retention rules of those platforms.",
        ],
    },
    {
        "title": "Your privacy choices",
        "bullets": [
            "You may request access, correction, deletion, or restriction of personal information we control, subject to applicable law.",
            "You may unsubscribe from optional emails or notifications using the unsubscribe or platform controls provided.",
            "You may adjust cookies, tracking controls, ad personalization, and social platform privacy settings directly in your browser or platform account.",
            "You may report public comments, impersonation, misuse, or privacy concerns through the relevant platform tools and by contacting us.",
        ],
    },
    {
        "title": "Children's privacy",
        "paragraphs": [
            "90mins Pitch Pulse is a general football-news channel and is not designed to knowingly collect personal information from children. If you believe a child has provided personal information directly to us without appropriate consent, contact us so we can review and take suitable action.",
        ],
    },
    {
        "title": "Security",
        "paragraphs": [
            "We use reasonable technical and organizational safeguards appropriate to the information we handle. No online service can guarantee absolute security, but we work to reduce risk and respond responsibly if an issue is identified.",
        ],
    },
    {
        "title": "Changes to this policy",
        "paragraphs": [
            "We may update this Privacy Policy when our services, tools, legal obligations, or channel operations change. The latest version will be posted on this page with a revised last-updated date.",
        ],
    },
    {
        "title": "Contact 90mins Pitch Pulse",
        "paragraphs": [
            "For privacy questions, rights requests, corrections, or concerns about content connected to 90mins Pitch Pulse, contact us through the official email address, channel page, or social profile listed on our current public profiles.",
            "Please include enough detail for us to understand your request, but avoid sending passwords, payment information, or unnecessary sensitive data.",
        ],
    },
]


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=31,
            textColor=colors.HexColor("#050505"),
            alignment=TA_LEFT,
            spaceAfter=10,
        ),
        "lead": ParagraphStyle(
            "Lead",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=11.5,
            leading=16,
            textColor=colors.HexColor("#2d2d2d"),
            spaceAfter=12,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15.5,
            leading=18,
            textColor=colors.HexColor("#ed0000"),
            spaceBefore=11,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.7,
            leading=13.5,
            textColor=colors.HexColor("#222222"),
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.4,
            leading=11,
            textColor=colors.HexColor("#5b5b5b"),
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.7,
            leading=13.5,
            leftIndent=14,
            firstLineIndent=-9,
            textColor=colors.HexColor("#222222"),
            spaceAfter=5,
        ),
    }


def draw_header_footer(canvas, doc):
    width, height = letter
    canvas.saveState()

    canvas.setFillColor(colors.HexColor("#050505"))
    canvas.rect(0, height - 58, width, 58, fill=1, stroke=0)
    canvas.drawImage(str(LOGO), 42, height - 48, 38, 38, mask="auto")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(88, height - 33, "90mins Pitch Pulse")
    canvas.setFillColor(colors.HexColor("#ed0000"))
    canvas.rect(0, height - 61, width, 3, fill=1, stroke=0)

    canvas.setFillColor(colors.HexColor("#050505"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(54, 32, "Privacy Policy")
    canvas.drawRightString(width - 54, 32, f"Page {doc.page}")
    canvas.setFillColor(colors.HexColor("#ed0000"))
    canvas.rect(54, 47, width - 108, 1.5, fill=1, stroke=0)

    canvas.restoreState()


def make_meta_table(styles):
    table = Table(
        [
            [
                Paragraph("LAST UPDATED<br/><font color='#050505'>%s</font>" % LAST_UPDATED, styles["small"]),
                Paragraph("CHANNEL FOCUS<br/><font color='#050505'>Football news and analysis</font>", styles["small"]),
            ]
        ],
        colWidths=[2.25 * inch, 2.75 * inch],
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f4f4")),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d7d7d7")),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#d7d7d7")),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    return table


def build_pdf(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=82,
        bottomMargin=68,
        title="90mins Pitch Pulse Privacy Policy",
        author="90mins Pitch Pulse",
        subject="Privacy Policy",
    )

    story = []
    banner = Image(str(BANNER), width=7 * inch, height=3.94 * inch)
    story.extend(
        [
            banner,
            Spacer(1, 16),
            Paragraph("90mins Pitch Pulse Privacy Policy", styles["title"]),
            Paragraph(
                "Clear privacy terms for the football channel where latest news, match analysis, transfers, and rumours stay in play.",
                styles["lead"],
            ),
            make_meta_table(styles),
            Spacer(1, 12),
        ]
    )

    for section in SECTIONS:
        story.append(Paragraph(section["title"], styles["section"]))
        for paragraph in section.get("paragraphs", []):
            story.append(Paragraph(paragraph, styles["body"]))
        if section.get("bullets"):
            for item in section["bullets"]:
                story.append(Paragraph(f"- {item}", styles["bullet"]))
        story.append(Spacer(1, 2))

    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)


def main():
    build_pdf(OUTPUT)
    shutil.copyfile(OUTPUT, PUBLIC)
    print(f"Wrote {OUTPUT}")
    print(f"Wrote {PUBLIC}")


if __name__ == "__main__":
    main()
