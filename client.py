class SyntheticDataMaskerClient:
    def mask_pii(self, text: str) -> dict:
        return {
            "masked_text": 'Contact [NAME] at [EMAIL] SSN [REDACTED]'
        }
