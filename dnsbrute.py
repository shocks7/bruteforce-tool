import dns.resolver


def resolve_subdomains(target_domain, wordlist):
    resolver = dns.resolver.Resolver()
    subdomains = wordlist.read().splitlines()

    for subdomain in subdomains:
        try:
            sub_target = f"{subdomain}.{target_domain}"
            result = resolver.resolve(sub_target, "A", lifetime=1.0)

            for ip in result:
                print(f"{sub_target} -> {ip}")
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.Timeout:
            print(f"Timeout resolving {sub_target}")
        except Exception as e:
            print(f"Error resolving {sub_target}: {e}")


def main():
    target_domain = input("Enter the target domain (e.g., example.com): ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    try:
        with open(wordlist_file, "r") as wordlist:
            resolve_subdomains(target_domain, wordlist)
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
