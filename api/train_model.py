import joblib
import os
import sys

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market_anomaly import best_model, scaler, feature_importance

# Create models directory if it doesn't exist
os.makedirs('api/models', exist_ok=True)

# Save the model, scaler, and feature importance
joblib.dump(best_model, 'api/models/random_forest_model.joblib')
joblib.dump(scaler, 'api/models/scaler.joblib')
joblib.dump(feature_importance, 'api/models/feature_importance.joblib')

print("Model and related files have been saved successfully!")
