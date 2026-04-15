from incentive_fraud.generators.synthetic_claims import main as generate_claims
from incentive_fraud.generators.synthetic_partner_transactions import main as generate_txns

if __name__ == "__main__":
    generate_claims()
    generate_txns()
