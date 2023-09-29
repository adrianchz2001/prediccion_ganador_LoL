def preprocessing_dataframe(df):
    
    df['gameDuration'] = round(df['gameDuration']/60, 2)
    
    df.drop(columns = ['gameId', 'creationTime', 'seasonId', 'gameDuration'], inplace = True)
    
    return df

def feature_selection(df):
    
    X = df.drop('winner', axis=1)
    Y = df['winner']

    feature_names = X.columns

    model = ExtraTreesClassifier(n_estimators = 200)
    model = model.fit(X, Y)

    importance_scores = model.feature_importances_

    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance_scores})

    importance_df = importance_df.sort_values(by = 'Importance', ascending = False)

    X = df[importance_df.iloc[:12, 0]]
    
    return X