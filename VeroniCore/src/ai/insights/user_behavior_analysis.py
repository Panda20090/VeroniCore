# user_behavior_analysis.py
# This script tracks and analyzes user interactions, preferences, and habits to provide personalized recommendations and insights.

import json
from collections import defaultdict

class UserBehaviorAnalyzer:
    def __init__(self):
        self.user_data = defaultdict(list)
        self.insights = {}

    def log_interaction(self, user_id, interaction):
        self.user_data[user_id].append(interaction)
        print(f"Logged interaction for user {user_id}: {interaction}")

    def analyze_behavior(self, user_id):
        if user_id not in self.user_data:
            print(f"No data available for user {user_id}")
            return {}

        interactions = self.user_data[user_id]
        self.insights[user_id] = self._generate_insights(interactions)
        return self.insights[user_id]

    def _generate_insights(self, interactions):
        # Placeholder for analysis logic
        # Example: Counting interactions by type
        interaction_types = defaultdict(int)
        for interaction in interactions:
            interaction_types[interaction['type']] += 1

        # Example insights
        insights = {
            'most_common_interaction': max(interaction_types, key=interaction_types.get),
            'interaction_summary': interaction_types
        }
        return insights

    def get_recommendations(self, user_id):
        if user_id not in self.insights:
            print(f"No insights available for user {user_id}")
            return []

        # Placeholder for recommendation logic
        insights = self.insights[user_id]
        recommendations = []
        if insights['most_common_interaction'] == 'click':
            recommendations.append('Consider promoting more clickable content.')
        elif insights['most_common_interaction'] == 'purchase':
            recommendations.append('Offer loyalty rewards for frequent purchases.')
        
        return recommendations

if __name__ == "__main__":
    # Example usage of UserBehaviorAnalyzer
    analyzer = UserBehaviorAnalyzer()

    # Log some interactions
    analyzer.log_interaction(user_id='user123', interaction={'type': 'click', 'details': 'Clicked on product page'})
    analyzer.log_interaction(user_id='user123', interaction={'type': 'purchase', 'details': 'Bought product XYZ'})

    # Analyze behavior and generate insights
    insights = analyzer.analyze_behavior(user_id='user123')
    print(f"Insights: {insights}")

    # Get personalized recommendations
    recommendations = analyzer.get_recommendations(user_id='user123')
    print(f"Recommendations: {recommendations}")
    