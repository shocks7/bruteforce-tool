import dns.resolver

# Subdomain bruteforce tool

res = dns.resolver.Resolver()
archive = open("wordlist.txt", "r")  # r = read

subdomains = archive.read().splitlines()

target = input("Enter the target domain (ex: example.com): ")

for subdomain in subdomains:
    try:
        sub_target = subdomain + "." + target
        result = res.resolve(sub_target, "A")  # A = principal | MX = e-mail | TXT = infos

        for ip in result:
            print(sub_target, "->", ip)
    except:
        pass
