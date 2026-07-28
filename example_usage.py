from client import SyntheticDataMaskerClient

def main():
    client = SyntheticDataMaskerClient()
    res = client.mask_pii(text='Contact John at john@example.com SSN 123-45-6789')
    print(f"Result for masked_text: {res['masked_text']}")

if __name__ == "__main__":
    main()
