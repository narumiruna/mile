from wise import RateRequest


def main():
    print(RateRequest(source="USD", target="TWD").do().value)
