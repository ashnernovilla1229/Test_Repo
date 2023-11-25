
print(
"Let us take an example, Trevor, who has deposited his money at ABC Bank Ltd. \
As per the bank policy, Trevor has been offered an interest rate of 6% on a sum of $1,000 \
that has been deposited for a period of 3 years. Calculate the interest \
to be earned by Trevor at the end of 3 years.")


def interest_rate_calculator():
    Outstanding_principal_sum = int(input("Input the Outstanding principal sum: "))
    Rate_of_interest = int(input("Input the rate of interest: "))
    Tenure_of_deposit = int(input("Input the Tenure of deposit: "))

    result = Outstanding_principal_sum * (Rate_of_interest / 100) * Tenure_of_deposit

    print(result)

    return result


if __name__ == "__main__":
    interest_rate_calculator()