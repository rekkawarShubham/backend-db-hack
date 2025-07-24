from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class AdvisorRequest(BaseModel):
    user_id: int
    question: str

class Location(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class PersonalInfo(BaseModel):
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    dependents: Optional[int] = None
    occupation: Optional[str] = None
    education_level: Optional[str] = None
    location: Optional[Location] = None

class Income(BaseModel):
    monthly_salary: Optional[float] = None
    additional_income: Optional[float] = None
    annual_bonus: Optional[float] = None

class MonthlyFixed(BaseModel):
    rent: Optional[float] = None
    utilities: Optional[float] = None
    insurance: Optional[float] = None
    loan_payments: Optional[float] = None

class MonthlyVariable(BaseModel):
    groceries: Optional[float] = None
    dining_out: Optional[float] = None
    transportation: Optional[float] = None
    entertainment: Optional[float] = None

class Expenses(BaseModel):
    monthly_fixed: Optional[MonthlyFixed] = None
    monthly_variable: Optional[MonthlyVariable] = None

class Savings(BaseModel):
    emergency_fund: Optional[float] = None
    retirement_savings: Optional[float] = None

class Stocks(BaseModel):
    amount: Optional[float] = None
    risk_level: Optional[str] = None

class MutualFunds(BaseModel):
    amount: Optional[float] = None
    fund_types: Optional[List[str]] = []

class FixedDeposits(BaseModel):
    amount: Optional[float] = None
    maturity_period: Optional[str] = None

class Crypto(BaseModel):
    amount: Optional[float] = None
    portfolio: Optional[List[str]] = []

class RealEstate(BaseModel):
    property_type: Optional[str] = None
    market_value: Optional[float] = None

class Investments(BaseModel):
    stocks: Optional[Stocks] = None
    mutual_funds: Optional[MutualFunds] = None
    fixed_deposits: Optional[FixedDeposits] = None
    crypto: Optional[Crypto] = None
    real_estate: Optional[RealEstate] = None

class LiabilityHomeLoan(BaseModel):
    type: Optional[str] = None
    principal: Optional[float] = None
    interest_rate: Optional[float] = None
    tenure_remaining: Optional[str] = None

class LiabilityCreditCard(BaseModel):
    type: Optional[str] = None
    total_limit: Optional[float] = None
    current_utilization: Optional[float] = None

class Asset(BaseModel):
    type: Optional[str] = None
    category: Optional[str] = None
    value: Optional[float] = None
    loan_remaining: Optional[float] = None

class InsuranceCoverage(BaseModel):
    life: Optional[float] = None
    health: Optional[float] = None
    vehicle: Optional[float] = None
    business: Optional[float] = None

class FinancialGoal(BaseModel):
    type: Optional[str] = None
    target_amount: Optional[float] = None
    target_date: Optional[date] = None

class CreditProfile(BaseModel):
    credit_score: Optional[int] = None
    credit_history_years: Optional[int] = None
    recent_credit_inquiries: Optional[int] = None

class RiskProfile(BaseModel):
    risk_appetite: Optional[str] = None
    investment_horizon: Optional[str] = None
    loss_tolerance: Optional[str] = None

class TaxInformation(BaseModel):
    tax_regime: Optional[str] = None
    tax_saving_investments: Optional[float] = None
    tax_bracket: Optional[str] = None

class User(BaseModel):
    user_id: Optional[int] = None
    personal_info: Optional[PersonalInfo] = None
    income: Optional[Income] = None
    expenses: Optional[Expenses] = None
    savings: Optional[Savings] = None
    investments: Optional[Investments] = None
    liabilities: Optional[List[dict]] = []  # can be refined later
    assets: Optional[List[Asset]] = []
    insurance_coverage: Optional[InsuranceCoverage] = None
    financial_goals: Optional[List[FinancialGoal]] = []
    credit_profile: Optional[CreditProfile] = None
    risk_profile: Optional[RiskProfile] = None
    tax_information: Optional[TaxInformation] = None