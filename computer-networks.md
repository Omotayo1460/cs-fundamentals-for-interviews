# 🌐 Computer Networks — Interview Q&A

[← Back to index](README.md) · Related: [OS](operating-systems.md) · [DBMS](dbms.md) · [OOP](oop.md)

---

## Core concepts (1-line each)

- A **network** connects devices to share data; the **internet** is a network of networks.
- **Protocol** = agreed rules for communication (TCP, IP, HTTP, DNS).
- **Bandwidth** = max data rate; **latency** = delay; **throughput** = actual rate achieved.

---

## Top questions

**1. OSI model — 7 layers?**
**Please Do Not Throw Sausage Pizza Away** →
Physical, Data Link, Network, Transport, Session, Presentation, Application.
Each layer serves the one above and uses the one below.

**2. OSI vs TCP/IP model?**
TCP/IP is the practical 4-layer model actually used: **Link, Internet, Transport,
Application**. OSI is the 7-layer conceptual reference. TCP/IP merges OSI's top three into
Application and bottom two into Link.

**3. TCP vs UDP?**
- **TCP** — connection-oriented, reliable, ordered, error-checked, slower (HTTP, email, file transfer).
- **UDP** — connectionless, no guarantees, fast, low overhead (video calls, gaming, DNS).

**4. How does the TCP 3-way handshake work?**
`SYN` → `SYN-ACK` → `ACK`. Client requests, server acknowledges + requests, client
acknowledges. Now the connection is established. Teardown uses a 4-way `FIN/ACK` exchange.

**5. What happens when you type a URL and press Enter?**
1. Browser checks cache, then **DNS** resolves the domain to an IP.
2. **TCP** connection (3-way handshake), then **TLS** handshake if HTTPS.
3. Browser sends an **HTTP** request.
4. Server responds with HTML; browser parses, requests CSS/JS/images, and renders.

**6. What is DNS? Recursive vs iterative resolution?**
DNS maps domain names to IP addresses. A **recursive** resolver does all the work and
returns the final answer; **iterative** means each server refers you to the next
(root → TLD → authoritative).

**7. HTTP vs HTTPS?**
HTTPS is HTTP over **TLS/SSL** — it encrypts traffic, verifies the server's identity, and
ensures integrity. HTTP is plaintext.

**8. What is an IP address? IPv4 vs IPv6?**
A unique address for a device on a network. **IPv4** = 32-bit (~4.3 billion addresses).
**IPv6** = 128-bit (vastly more), written in hex, solves IPv4 exhaustion.

**9. Public vs Private IP? What is NAT?**
Private IPs (e.g. `192.168.x.x`) are used inside local networks; public IPs are routable
on the internet. **NAT** (Network Address Translation) maps many private IPs to one public
IP at the router.

**10. What is a MAC address? IP vs MAC?**
A **MAC** is a hardware address fixed to a network interface (Data Link layer). **IP** is a
logical, changeable address (Network layer). ARP maps IP → MAC.

**11. What is a subnet mask?**
It splits an IP into **network** and **host** parts (e.g. `/24` = 255.255.255.0). Enables
subnetting to organize and secure networks.

**12. DHCP — what does it do?**
Dynamic Host Configuration Protocol automatically assigns IP addresses (and gateway/DNS)
to devices joining a network.

**13. Router vs Switch vs Hub?**
- **Hub** — broadcasts to all ports (dumb, Layer 1).
- **Switch** — forwards by MAC to the right port (Layer 2).
- **Router** — routes packets between networks by IP (Layer 3).

**14. TCP flow control vs congestion control?**
**Flow control** prevents overwhelming the *receiver* (sliding window). **Congestion
control** prevents overwhelming the *network* (slow start, AIMD).

**15. What are common HTTP status codes?**
`2xx` success, `3xx` redirect, `4xx` client error (404 not found, 401 unauthorized),
`5xx` server error (500, 503).

**16. GET vs POST?**
**GET** retrieves data, params in URL, idempotent, cacheable. **POST** submits data in the
body, not idempotent, used to create/modify.

**17. What is a port?**
A 16-bit number identifying a specific process/service on a host (HTTP 80, HTTPS 443,
SSH 22, DNS 53). IP locates the machine; port locates the app.

**18. Symmetric vs Asymmetric encryption (TLS basics)?**
**Symmetric** uses one shared key (fast). **Asymmetric** uses a public/private key pair
(secure key exchange). TLS uses asymmetric to exchange a symmetric session key, then
symmetric for speed.
