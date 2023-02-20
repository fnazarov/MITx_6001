def lowest_payment(balance,annualInterestRate,year):
    """
    Find the lowest minium payment to pay off the debt given the credit
    annual intr rate and year
    """
    bal_end = balance
    mon_int_rate = annualInterestRate / 12
    m_lower = balance / (12 * year)
    m_upper = (balance)
    min_mon_paymen = (m_lower + m_upper) / 2
    qutardu = True
    while qutardu:
        bal_end = balance
        for i in range ( 0,12 ):
            mon_unpaid_bal = bal_end - min_mon_paymen

            bal_end = mon_unpaid_bal + mon_unpaid_bal * mon_int_rate
        if bal_end <= 1 and bal_end >= 0:
            break
        if bal_end > 1:
            m_lower = min_mon_paymen
            min_mon_paymen = (m_lower + m_upper) / 2
        else:
            m_upper = min_mon_paymen
            min_mon_paymen = (m_lower + m_upper) / 2

    low_payment = round ( min_mon_paymen,2 )
    print ( "Lowest Payment: ",low_payment )

    def payment_end(credit,annualInterestRate,rate):
        """
        Find how many year it takes to pay off the debt
        """
        bal_end = credit
        mon_int_rate = annualInterestRate / 12
        m_lower = 1
        m_upper = credit / rate
        min_year = (m_lower + m_upper) / 2
        qutardu = True
        while qutardu:
            bal_end = balance
            for i in range ( 0,12 * min_year ):
                mon_unpaid_bal = bal_end - rate

                bal_end = mon_unpaid_bal + mon_unpaid_bal * mon_int_rate
            if bal_end <= 1 and bal_end >= 0:
                break
            if bal_end > 1:
                m_lower = min_year
                min_year = (m_lower + m_upper) / 2
            else:
                m_upper = min_year
                min_year = (m_lower + m_upper) / 2

        print ( "A takes months to pay off the debt: ",min_year / 12 )