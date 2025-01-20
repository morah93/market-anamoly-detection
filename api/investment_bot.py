import pandas as pd
import numpy as np
from datetime import datetime

class InvestmentBot:
    def __init__(self, model, scaler, feature_importance):
        self.model = model
        self.scaler = scaler
        self.feature_importance = feature_importance
        self.risk_levels = {
            'Low': 0.3,
            'Medium': 0.6,
            'High': 0.8
        }

    def analyze_market_conditions(self, market_data):
        """Analyze current market conditions and return risk assessment"""
        scaled_data = self.scaler.transform(market_data)
        crash_prob = self.model.predict_proba(scaled_data)[0][1]

        risk_level = self._determine_risk_level(crash_prob)
        key_factors = self._identify_key_factors()

        return self._generate_report(crash_prob, risk_level, key_factors, market_data)
