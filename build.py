"""Builds the OPSA website: wraps each page body in the shared header and footer.
Edit CONTACT below to change the phone number or address on every page at once."""
import os

CONTACT = {
    "email": "support@opsa.in",
    "phone": "+91 XXXXX XXXXX",          # change later
    "address": "Mumbai, Maharashtra, India",
    "owner": "Shankar Relekar",
    "updated": "22 November 2026",
}
HERE = os.path.dirname(os.path.abspath(__file__))

NAV = [("index.html", "Home"), ("about.html", "About"), ("contact.html", "Contact"),
       ("privacy.html", "Privacy"), ("terms.html", "Terms"), ("refund.html", "Refunds")]


def page(fname, title, desc, body):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    c = CONTACT
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html" aria-label="OPSA home"><img src="assets/logo-white.png" alt="OPSA"></a>
  <button class="menu-btn" onclick="document.querySelector('nav.main').classList.toggle('open')">Menu</button>
  <nav class="main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div><img src="assets/logo-white.png" alt="OPSA"><div>Online Platform Services Available.<br>Book &bull; Hire &bull; Get it done.</div></div>
    <div><h4>Company</h4><a href="about.html">About us</a><a href="contact.html">Contact us</a></div>
    <div><h4>Policies</h4><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms &amp; Conditions</a><a href="refund.html">Refund &amp; Cancellation</a></div>
    <div><h4>Reach us</h4><a href="mailto:{c['email']}">{c['email']}</a><a href="tel:{c['phone'].replace(' ', '')}">{c['phone']}</a><span>{c['address']}</span></div>
  </div>
  <div class="legal">&copy; 2026 OPSA. Operated by {c['owner']}, {c['address']}. All rights reserved.</div>
</div></footer>
</body>
</html>
"""
    for k, v in c.items():
        html = html.replace("{{" + k + "}}", v)
    with open(os.path.join(HERE, fname), "w", encoding="utf-8") as f:
        f.write(html)


def legal(fname, title, intro, sections):
    body = (f'<div class="page-head"><div class="wrap"><h1>{title}</h1>'
            f'<p>Last updated: {{{{updated}}}}</p></div></div>\n<div class="prose">{intro}{sections}</div>')
    page(fname, f"{title} | OPSA", f"{title} for OPSA (opsa.in).", body)


# ---------- Home ----------
page("index.html", "OPSA | Book, hire and get it done",
     "OPSA lets you book verified hospitality staff and fixed-price home services in a few taps.",
     """
<section class="hero2"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow">BOOK &bull; HIRE &bull; GET IT DONE</div>
    <h1>Home services. Event staff.<br><span>One app.</span></h1>
    <p class="lead">Verified waiters, butlers, chefs and housekeeping staff, plus fixed-price home services. Booked in a few taps, paid safely online.</p>
    <div class="ctas"><a class="btn" href="contact.html">Get in touch</a><a class="btn ghost" href="#services">Explore services</a></div>
    <div class="pill"><span class="dot"></span>Launching soon in Mumbai</div>
  </div>
  <div class="phone" aria-hidden="true"><div class="screen">
    <div class="ph-top"><img src="assets/logo-white.png" alt=""><span>Good evening</span></div>
    <div class="ph-card"><small>Your booking</small><b>2 Waiters &middot; Wedding</b><span>Sat, 7:00 pm &middot; Andheri West</span><div class="ph-status"><i></i>Staff confirmed</div></div>
    <div class="ph-row"><div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6a2.5 2.5 0 1 0 0 .01M6 18a2.5 2.5 0 1 0 0 .01M8 7.5L20 18M8 16.5L20 6"/></svg><em>Salon</em></div><div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v8H3zM7 17l-1 3M12 17v3M17 17l1 3M7 9h10"/></svg><em>AC</em></div><div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v8M8 11h8l1 10H7zM10 15v3M14 15v3"/></svg><em>Cleaning</em></div><div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></svg><em>Repairs</em></div></div>
    <div class="ph-list"><small>Top rated near you</small><div><span class="av">RK</span><p><b>Ravi K.</b><br>Senior waiter &middot; 4.9 &#9733;</p></div><div><span class="av">AS</span><p><b>Anita S.</b><br>Housekeeping &middot; 4.8 &#9733;</p></div></div>
    <div class="ph-pay"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 11h12v10H6zM8 11V7a4 4 0 0 1 8 0v4"/></svg>Payment held safely until the job is done</div>
  </div></div>
</div></section>

<div class="trust"><div class="wrap trust-row">
  <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4"/></svg><span>ID-verified professionals</span></div>
  <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 11h12v10H6zM8 11V7a4 4 0 0 1 8 0v4"/></svg><span>Secure payments by Razorpay</span></div>
  <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12V3h9l9 9-9 9zM7.5 7.5h.01"/></svg><span>Clear, fixed prices</span></div>
</div></div>

<section id="services"><div class="wrap">
  <div class="kicker">Staff on demand</div>
  <h2>Hire staff for your event or hotel</h2>
  <p class="sub">Trained, ID-verified hospitality staff for weddings, parties, caterers and hotels, booked by the shift.</p>
  <div class="grid4">
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18h16M6 18a6 6 0 0 1 12 0M12 9V7M10 7h4"/></svg></div><h3>Waiters</h3><p>Food and beverage service for parties, banquets and catering events.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a4 4 0 1 1 0 8a4 4 0 0 1 0-8zM5 21a7 7 0 0 1 14 0M10 14l2 2 2-2"/></svg></div><h3>Butlers</h3><p>Personal, premium service for private events and VIP guests.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 14h10v6H7zM7 14a4 4 0 1 1 2-7.5A4 4 0 0 1 15 6a4 4 0 1 1 2 8"/></svg></div><h3>Chefs &amp; cooks</h3><p>Kitchen help and cooks for events, homes and small kitchens.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/></svg></div><h3>Housekeeping</h3><p>Cleaning and upkeep staff for homes, hotels and venues.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="kicker">At your doorstep</div>
  <h2>Home services at a fixed price</h2>
  <p class="sub">See the price before you book. No bargaining, no surprises.</p>
  <div class="grid4">
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6a2.5 2.5 0 1 0 0 .01M6 18a2.5 2.5 0 1 0 0 .01M8 7.5L20 18M8 16.5L20 6"/></svg></div><h3>Salon &amp; spa</h3><p>Grooming and beauty services at home.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v8H3zM7 17l-1 3M12 17v3M17 17l1 3M7 9h10"/></svg></div><h3>AC repair &amp; service</h3><p>Servicing, gas refill and repairs by trained technicians.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v8M8 11h8l1 10H7zM10 15v3M14 15v3"/></svg></div><h3>Cleaning</h3><p>Home, kitchen and bathroom deep cleaning.</p></div>
    <div class="svc"><div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></svg></div><h3>Technicians</h3><p>Electricians, plumbers and carpenters for everyday fixes.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="kicker">Simple by design</div>
  <h2>How OPSA works</h2>
  <div class="flow">
    <div><b>01</b><h3>Choose</h3><p>Pick a service or the staff you need, with date, time and place.</p></div>
    <div><b>02</b><h3>Pay securely</h3><p>Pay online. Your money is held safely until the job is done.</p></div>
    <div><b>03</b><h3>Get it done</h3><p>A verified professional arrives. Rate the work when it is finished.</p></div>
  </div>
</div></section>

<section class="cta-band"><div class="wrap cta-inner">
  <div><h2>Be among the first to use OPSA</h2><p>Customers, caterers, hotels and professionals: write to us and we will reach out when we launch.</p></div>
  <a class="btn" href="mailto:{{email}}">{{email}}</a>
</div></section>
""")

# ---------- About ----------
page("about.html", "About OPSA", "About OPSA, Online Platform Services Available.", """
<div class="page-head"><div class="wrap"><h1>About OPSA</h1><p>Online Platform Services Available</p></div></div>
<div class="prose">
<p>OPSA is an online platform that connects customers with independent service professionals. It starts with two things
people in Mumbai need often and find hard to arrange: reliable <strong>hospitality staff</strong> for events and hotels, and
<strong>fixed-price home services</strong>.</p>
<p>OPSA grew out of years of hands-on experience supplying waiters, bartenders and butlers to caterers and events. We saw
how hard it is for customers to find dependable staff at short notice, and how hard it is for good workers to find steady,
fairly paid work. OPSA is built to fix both sides.</p>
<h2>What we stand for</h2>
<ul>
<li><strong>Verified professionals.</strong> Service providers complete identity verification before they can take bookings.</li>
<li><strong>Clear prices.</strong> You see the price before you book.</li>
<li><strong>Safe payments.</strong> Payments are processed by Razorpay and released to the professional after the job is completed.</li>
<li><strong>Fair work.</strong> Professionals are paid on time for every completed booking.</li>
</ul>
<h2>Who runs OPSA</h2>
<p>OPSA is operated by {{owner}}, based in {{address}}. For any question, write to
<a href="mailto:{{email}}">{{email}}</a>.</p>
</div>""")

# ---------- Contact ----------
page("contact.html", "Contact OPSA", "Contact OPSA customer support.", """
<div class="page-head"><div class="wrap"><h1>Contact us</h1><p>We usually reply within 24 hours.</p></div></div>
<div class="prose">
<table class="info">
<tr><td>Email</td><td><a href="mailto:{{email}}">{{email}}</a></td></tr>
<tr><td>Phone / WhatsApp</td><td><a href="tel:{{phone}}">{{phone}}</a></td></tr>
<tr><td>Address</td><td>{{address}}</td></tr>
<tr><td>Operated by</td><td>{{owner}}</td></tr>
<tr><td>Support hours</td><td>Monday to Saturday, 10:00 am to 7:00 pm IST</td></tr>
</table>
<h2>For bookings and payments</h2>
<p>Please include your booking ID (if you have one), your registered phone number and a short description of the issue.
For refund requests, see our <a href="refund.html">Refund &amp; Cancellation Policy</a>.</p>
<h2>For service professionals</h2>
<p>Want to work with OPSA as a waiter, butler, chef, housekeeper or technician? Write to us at
<a href="mailto:{{email}}">{{email}}</a> with your name, city and the work you do.</p>
<h2>Grievance officer</h2>
<p>Name: {{owner}}<br>Email: <a href="mailto:{{email}}">{{email}}</a><br>We acknowledge complaints within 48 hours and aim to resolve them within 30 days.</p>
</div>""")

# ---------- Privacy ----------
legal("privacy.html", "Privacy Policy",
      "<p>This Privacy Policy explains how OPSA (&ldquo;OPSA&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;), operated by {{owner}}, collects, uses and protects "
      "personal data when you use the OPSA website at opsa.in and the OPSA mobile apps (together, the &ldquo;Platform&rdquo;). "
      "We process personal data in line with India&rsquo;s Digital Personal Data Protection Act, 2023 and other applicable law.</p>",
      """
<h2>1. Data we collect</h2>
<h3>Customers</h3>
<ul><li>Name, phone number, email address</li><li>Service address and location you share for a booking</li>
<li>Booking history, ratings and messages with support</li></ul>
<h3>Service professionals</h3>
<ul><li>Name, phone, email, photo, address</li>
<li>Identity and KYC details needed for verification (such as Aadhaar or PAN), checked through a licensed verification provider</li>
<li>Bank or UPI details for payouts</li><li>Location during an active job, work history and ratings</li></ul>
<h3>Payment data</h3>
<p>Payments are processed by Razorpay. We do <strong>not</strong> store your full card number, CVV or UPI PIN. We receive only
a payment reference, status and amount.</p>
<h3>Device data</h3>
<p>Device type, app version, IP address and crash logs, used to keep the Platform secure and working.</p>

<h2>2. How we use your data</h2>
<ul><li>To create your account and confirm bookings</li><li>To match customers with nearby professionals</li>
<li>To verify the identity of professionals and keep the Platform safe</li><li>To process payments, refunds and payouts</li>
<li>To send booking updates, OTPs and support replies</li><li>To prevent fraud and meet legal and tax requirements</li></ul>
<p>We do not sell your personal data.</p>

<h2>3. Who we share data with</h2>
<ul><li><strong>The other party to a booking:</strong> a professional sees the customer&rsquo;s name, service address and booking details; the customer sees the professional&rsquo;s name, photo and rating.</li>
<li><strong>Service providers</strong> that help us run the Platform, such as Razorpay (payments and payouts), identity verification providers, cloud hosting, SMS and email providers. They may use the data only to provide their service to us.</li>
<li><strong>Authorities</strong> when required by law or to protect someone&rsquo;s safety.</li></ul>

<h2>4. How long we keep data</h2>
<p>We keep account data while your account is active. Booking and payment records are kept for as long as tax and accounting
law requires (generally up to 8 years). KYC records are kept as required by law. Other data is deleted or anonymised when no longer needed.</p>

<h2>5. Your rights</h2>
<p>You can ask to access, correct or delete your personal data, or withdraw consent, by writing to
<a href="mailto:{{email}}">{{email}}</a>. Some data may need to be kept where the law requires it.</p>

<h2>6. Security</h2>
<p>We use encryption in transit, access controls and regular reviews to protect your data. No system is completely secure, so
please keep your OTPs and passwords private.</p>

<h2>7. Children</h2>
<p>The Platform is meant for people aged 18 and above. We do not knowingly collect data from children.</p>

<h2>8. Changes</h2>
<p>We may update this policy. We will post the new version here with a new &ldquo;Last updated&rdquo; date.</p>

<h2>9. Contact and grievances</h2>
<p>Grievance officer: {{owner}}, <a href="mailto:{{email}}">{{email}}</a>, {{address}}.</p>
""")

# ---------- Terms ----------
legal("terms.html", "Terms & Conditions",
      "<p>These Terms govern your use of the OPSA website (opsa.in) and mobile apps (the &ldquo;Platform&rdquo;), operated by "
      "{{owner}}, {{address}} (&ldquo;OPSA&rdquo;, &ldquo;we&rdquo;). By creating an account or making a booking, you agree to these Terms.</p>",
      """
<h2>1. What OPSA does</h2>
<p>OPSA is an online marketplace. It lets customers book services from independent service professionals
(&ldquo;Professionals&rdquo;) such as waiters, butlers, chefs, housekeeping staff and home-service technicians. Unless stated
otherwise, Professionals are independent and are not employees of OPSA.</p>

<h2>2. Accounts</h2>
<ul><li>You must be 18 or older and give correct information.</li>
<li>You are responsible for activity on your account. Keep your OTP and password private.</li>
<li>We may suspend accounts that break these Terms or are used for fraud.</li></ul>

<h2>3. Bookings and prices</h2>
<ul><li>The price, duration and scope of a service are shown before you confirm a booking.</li>
<li>Prices include applicable taxes unless shown separately. Extra work or extra hours requested on site may cost more and will be confirmed with you first.</li>
<li>A booking is confirmed only after payment succeeds and a Professional accepts it.</li></ul>

<h2>4. Payments</h2>
<ul><li>Payments are processed securely by Razorpay. OPSA does not store card numbers or UPI PINs.</li>
<li>Your payment is held until the service is completed, and then released to the Professional after deducting OPSA&rsquo;s platform fee.</li>
<li>Refunds follow our <a href="refund.html">Refund &amp; Cancellation Policy</a>.</li></ul>

<h2>5. Customer responsibilities</h2>
<ul><li>Give accurate address, timing and job details.</li>
<li>Provide a safe working environment and treat Professionals with respect.</li>
<li>Do not ask Professionals to do unsafe or illegal work, or to take payment outside the Platform.</li></ul>

<h2>6. Professional responsibilities</h2>
<ul><li>Complete identity verification and keep your details up to date.</li>
<li>Arrive on time, behave professionally and do the work as booked.</li>
<li>Do not take bookings or payments for OPSA customers outside the Platform.</li></ul>

<h2>7. Ratings and conduct</h2>
<p>Both sides can rate each other. Reviews must be honest. We may remove abusive content and suspend users for harassment, fraud or repeated no-shows.</p>

<h2>8. Limitation of liability</h2>
<p>OPSA takes reasonable care in verifying Professionals and running the Platform. To the extent the law allows, OPSA&rsquo;s total
liability for any booking is limited to the amount paid for that booking. OPSA is not liable for indirect or consequential loss.
Nothing in these Terms limits rights you have under the Consumer Protection Act, 2019.</p>

<h2>9. Changes and termination</h2>
<p>We may update these Terms or the Platform. Continued use after an update means you accept the new Terms. You can close your account at any time by writing to us.</p>

<h2>10. Governing law</h2>
<p>These Terms are governed by the laws of India. Courts in Mumbai, Maharashtra have jurisdiction.</p>

<h2>11. Contact</h2>
<p><a href="mailto:{{email}}">{{email}}</a> &middot; {{phone}} &middot; {{address}}</p>
""")

# ---------- Refund ----------
legal("refund.html", "Refund & Cancellation Policy",
      "<p>This policy explains how cancellations and refunds work for bookings made on OPSA (opsa.in and the OPSA apps).</p>",
      """
<h2>1. Cancellation by the customer</h2>
<table class="info">
<tr><td>Home services, cancelled 2 hours or more before the start time</td><td>Full refund</td></tr>
<tr><td>Home services, cancelled less than 2 hours before the start time</td><td>Refund minus a cancellation fee of up to &#8377;100</td></tr>
<tr><td>Staff hire, cancelled 24 hours or more before the shift</td><td>Full refund</td></tr>
<tr><td>Staff hire, cancelled less than 24 hours before the shift</td><td>Refund minus up to 25% of the booking value</td></tr>
<tr><td>Cancelled after the Professional has arrived or the shift has started</td><td>No refund for the time already booked</td></tr>
</table>

<h2>2. Cancellation by OPSA or the Professional</h2>
<p>If a Professional cancels, does not arrive, or we cannot find a Professional for your booking, you get a <strong>full refund</strong>,
or we will offer a replacement if you prefer.</p>

<h2>3. Problems with the service</h2>
<p>If the work was not done as booked, write to <a href="mailto:{{email}}">{{email}}</a> within 48 hours of the service with your booking ID
and photos if possible. After review we will arrange a free redo or a partial or full refund, depending on what happened.</p>

<h2>4. How refunds are paid</h2>
<ul><li>Approved refunds go back to the original payment method (UPI, card, net banking or wallet) through Razorpay.</li>
<li>We start the refund within 2 working days of approval. It usually reaches your account within <strong>5 to 7 working days</strong>, depending on your bank.</li>
<li>We do not refund in cash.</li></ul>

<h2>5. Service delivery</h2>
<p>OPSA sells services, not physical goods, so there is no shipping. Services are delivered at the address and time you choose
when booking, within the service areas shown in the app.</p>

<h2>6. Contact</h2>
<p>For any cancellation or refund question: <a href="mailto:{{email}}">{{email}}</a> &middot; {{phone}}</p>
""")

print("built", sorted(f for f in os.listdir(HERE) if f.endswith(".html")))
