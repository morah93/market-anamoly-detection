# import pandas as pd
# import numpy as np
# from datetime import datetime
# from sklearn.preprocessing import StandardScaler

# class InvestmentBot:
#     def __init__(self, model, scaler, feature_importance):
#         self.model = model
#         self.scaler = scaler
#         self.feature_importance = feature_importance
#         self.risk_levels = {
#             'Low': 0.3,
#             'Medium': 0.6,
#             'High': 0.8
#         }


#     def _determine_risk_level(self, probability):
#         if probability < self.risk_levels['Low']:
#             return 'Low'
#         elif probability < self.risk_levels['Medium']:
#             return 'Medium'
#         elif probability < self.risk_levels['High']:
#             return 'High'
#         return 'Very High'

#     def _identify_key_factors(self):
#         """Identify top contributing factors based on feature importance"""
#         top_features = self.feature_importance.nlargest(3, 'importance')
#         return top_features['feature'].tolist()

#     def analyze_market_conditions(self, market_data):
#         """Analyze current market conditions and return risk assessment"""
#         scaled_data = self.scaler.transform(market_data)
#         crash_prob = self.model.predict_proba(scaled_data)[0][1]

#         key_factors = self._identify_key_factors()
#         risk_level = self._determine_risk_level(crash_prob)

#         return self._generate_report(crash_prob, risk_level, key_factors, market_data)

#     def _generate_report(self, probability, risk_level, key_factors, market_data):
#         report = {
#             'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'market_risk': {
#                 'probability': f"{probability:.1%}",
#                 'risk_level': risk_level
#             },
#             'key_factors': key_factors,
#             'current_readings': {factor: f"{market_data[factor].iloc[0]:.2f}" for factor in key_factors},
#             'recommendations': self._get_recommendations(risk_level),
#             'explanation': self._get_explanation(probability, risk_level, key_factors, market_data)
#         }
#         return report

#     def _get_recommendations(self, risk_level):
#         recommendations = {
#             'Low': [
#                 "Consider maintaining current market exposure",
#                 "Look for opportunities to add to positions",
#                 "Focus on long-term investment goals"
#             ],
#             'Medium': [
#                 "Review portfolio diversification",
#                 "Consider adding some defensive positions",
#                 "Maintain balanced asset allocation"
#             ],
#             'High': [
#                 "Consider reducing high-risk positions",
#                 "Increase cash holdings",
#                 "Add defensive assets like bonds or gold"
#             ],
#             'Very High': [
#                 "Consider moving to defensive positions",
#                 "Significantly increase cash holdings",
#                 "Implement hedging strategies"
#             ]
#         }
#         return recommendations[risk_level]

#     def _get_explanation(self, probability, risk_level, key_factors, market_data):
#         explanation = f"Based on current market conditions, our AI model indicates a {probability:.1%} probability of market stress. "
#         explanation += f"This represents a {risk_level} risk level. "
#         explanation += "\n\nKey factors influencing this assessment:\n"

#         for factor in key_factors:
#             value = float(market_data[factor].iloc[0])
#             explanation += f"- {factor}: Current reading of {value:.2f}\n"

#         return explanation

# # Example usage:
# if __name__ == "__main__":
#     # Assuming we have the best performing model from market_anomaly.py
#     best_model = models['Random Forest']  # or whichever model performed best

#     # Example definition of scaler
#     scaler = StandardScaler()

#     # Assuming you have some training data to fit the scaler
#     # scaler.fit(training_data)

#     # Create the investment bot
#     bot = InvestmentBot(
#         model=best_model,
#         scaler=scaler,
#         feature_importance=feature_importance
#     )

#     # Get latest market data (example)
#     latest_data = pd.DataFrame({
#         'VIX': [25.5],
#         'XAU BGNL': [1900.0],
#         'DXY': [90.5],
#         'MXUS': [3000.0],
#         'MXJP': [1200.0],
#         'GTITL30YR': [2.5]
#     })

#     # Get analysis and recommendations
#     analysis = bot.analyze_market_conditions(latest_data)

#     # Print the report in a user-friendly format
#     print("=== Market Analysis Report ===")
#     print(f"Time: {analysis['timestamp']}")
#     print(f"\nRisk Assessment:")
#     print(f"Market Stress Probability: {analysis['market_risk']['probability']}")
#     print(f"Risk Level: {analysis['market_risk']['risk_level']}")

#     print("\nKey Market Factors:")
#     for factor in analysis['key_factors']:
#         print(f"- {factor}: {analysis['current_readings'][factor]}")

#     print("\nRecommended Actions:")
#     for rec in analysis['recommendations']:
#         print(f"- {rec}")

#     print("\nDetailed Explanation:")
#     print(analysis['explanation'])





import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import joblib

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

    # def _determine_risk_level(self, probability):
    #     if probability < self.risk_levels['Low']:
    #         return 'Low'
    #     elif probability < self.risk_levels['Medium']:
    #         return 'Medium'
    #     elif probability < self.risk_levels['High']:
    #         return 'High'
    #     return 'Very High'

    def _determine_risk_level(self, crash_prob):
        # Logic to determine risk level
        if crash_prob > 0.8:
            return 'High'
        elif crash_prob > 0.5:
            return 'Medium'
        else:
            return 'Low'

    def _identify_key_factors(self):
        """Identify top contributing factors based on feature importance"""
        top_features = self.feature_importance.nlargest(3, 'importance')
        return top_features['feature'].tolist()

    def analyze_market_conditions(self, market_data):
        """Analyze current market conditions and return risk assessment"""
        print(f"Available methods in bot: {dir(self)}")
        scaled_data = self.scaler.transform(market_data)
        crash_prob = self.model.predict_proba(scaled_data)[0][1]

        key_factors = self._identify_key_factors()
        risk_level = self._determine_risk_level(crash_prob)

        return self._generate_report(crash_prob, risk_level, key_factors, market_data)

    def _generate_report(self, probability, risk_level, key_factors, market_data):
        report = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'market_risk': {
                'probability': f"{probability:.1%}",
                'risk_level': risk_level
            },
            'key_factors': key_factors,
            'current_readings': {factor: f"{market_data[factor].iloc[0]:.2f}" for factor in key_factors},
            'recommendations': self._get_recommendations(risk_level),
            'explanation': self._get_explanation(probability, risk_level, key_factors, market_data)
        }
        return report

    def _get_recommendations(self, risk_level):
        recommendations = {
            'Low': [
                "Consider maintaining current market exposure",
                "Look for opportunities to add to positions",
                "Focus on long-term investment goals"
            ],
            'Medium': [
                "Review portfolio diversification",
                "Consider adding some defensive positions",
                "Maintain balanced asset allocation"
            ],
            'High': [
                "Consider reducing high-risk positions",
                "Increase cash holdings",
                "Add defensive assets like bonds or gold"
            ],
            'Very High': [
                "Consider moving to defensive positions",
                "Significantly increase cash holdings",
                "Implement hedging strategies"
            ]
        }
        return recommendations[risk_level]

    def _get_explanation(self, probability, risk_level, key_factors, market_data):
        explanation = f"Based on current market conditions, our AI model indicates a {probability:.1%} probability of market stress. "
        explanation += f"This represents a {risk_level} risk level. "
        explanation += "\n\nKey factors influencing this assessment:\n"

        for factor in key_factors:
            value = float(market_data[factor].iloc[0])
            explanation += f"- {factor}: Current reading of {value:.2f}\n"

        return explanation


# Example usage:
if __name__ == "__main__":
    # Load the best performing model, scaler, and feature importance from files
    best_model = joblib.load('api/models/random_forest_model.joblib')  # Load the trained model
    scaler = joblib.load('api/models/scaler.joblib')  # Load the scaler used for feature scaling
    feature_importance = joblib.load('api/models/feature_importance.joblib')  # Load the feature importance

    # Example: Get the latest market data (make sure to match feature columns as required)
    latest_data = pd.DataFrame({
        'VIX': [25.5],
        'XAU BGNL': [1900.0],
        'DXY': [90.5],
        'MXUS': [3000.0],
        'MXJP': [1200.0],
        'GTITL30YR': [2.5]
    })

    # Initialize the InvestmentBot with the loaded components
    bot = InvestmentBot(
        model=best_model,
        scaler=scaler,
        feature_importance=feature_importance
    )

    # Get analysis and recommendations
    analysis = bot.analyze_market_conditions(latest_data)

    # Print the report in a user-friendly format
    print("=== Market Analysis Report ===")
    print(f"Time: {analysis['timestamp']}")
    print(f"\nRisk Assessment:")
    print(f"Market Stress Probability: {analysis['market_risk']['probability']}")
    print(f"Risk Level: {analysis['market_risk']['risk_level']}")

    print("\nKey Market Factors:")
    for factor in analysis['key_factors']:
        print(f"- {factor}: {analysis['current_readings'][factor]}")

    print("\nRecommended Actions:")
    for rec in analysis['recommendations']:
        print(f"- {rec}")

    print("\nDetailed Explanation:")
    print(analysis['explanation'])
