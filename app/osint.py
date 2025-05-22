import socket
import whois
import ssl

def get_dns(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except Exception as e:
        return {"error": str(e)}

def get_whois(domain):
    try:
        data = whois.whois(domain)
        return {k: str(v) for k, v in data.items()}
    except Exception as e:
        return {"error": str(e)}

def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
            cert = s.getpeercert()
            return {
                "subject": cert.get("subject"),
                "issuer": cert.get("issuer"),
                "notBefore": cert.get("notBefore"),
                "notAfter": cert.get("notAfter")
            }
    except Exception as e:
        return {"error": str(e)}