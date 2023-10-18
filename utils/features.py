target_variable = 'y'
feature_categories = ['귀점', '조회', '상설', '총동의', '사랑온', '통합보장', '환산']
category_values = ['당월', '직3']

def generate_combined_feature_names(categories, features):
    combined_names = []
    for category in categories:
        for feature in features:
            combined_name = f'{feature}_{category}'
            combined_names.append(combined_name)
    return combined_names

feature_names = generate_combined_feature_names(category_values, feature_categories)
