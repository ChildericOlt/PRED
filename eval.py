def notation(X_test, y_test, y_pred, model) : 
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
    import numpy as np
    from sklearn.preprocessing import label_binarize
    import seaborn as sns 
    import matplotlib.pyplot as plt
    from sklearn.metrics import roc_curve, auc


    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred, average='weighted')  # ou 'macro'
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')


    conf_matrix = confusion_matrix(y_test, y_pred)

    # Affichage des métriques
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1-score: {f1}')
    print(f'Confusion Matrix:\n{conf_matrix}')

    n_classes = len(np.unique(y_test))
    y_test_bin = label_binarize(y_test, classes=np.unique(y_test))
    y_pred_proba = model.predict_proba(X_test)

    palette = sns.color_palette("husl", n_classes)

    plt.figure(figsize=(8, 6))

    for i in range(n_classes):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, color=palette[i], label=f'Classe {i} (AUC = {roc_auc:.2f})')

    plt.plot([0, 1], [0, 1], 'k--', label="Random (AUC = 0.50)")

    plt.xlabel('Taux de faux positifs (FPR)')
    plt.ylabel('Taux de vrais positifs (TPR)')
    plt.title('Courbes ROC pour classification multiclasses')
    plt.legend()
    plt.grid()
    plt.show()

    auc_roc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovo')
    print(f'AUC-ROC: {auc_roc}')


# utilisation : 
"""import sys
sys.path.append("eval.py")  # Exemple : "/home/user/projet/"
from eval import notation

notation(X_test, y_test, y_pred, model) """