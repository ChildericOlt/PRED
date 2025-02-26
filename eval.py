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

    n_classes = len(np.unique(y_test))
    y_pred_proba = model.predict_proba(X_test)

    if n_classes > 2:
        y_test_bin = label_binarize(y_test, classes=np.unique(y_test))
    else:
        y_test_bin = y_test  # Pas besoin de binariser pour une classification binaire

    palette = sns.color_palette("husl", max(n_classes, 3))  

    plt.figure(figsize=(8, 6))

    if n_classes > 2:
        for i in range(n_classes):
            fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, color=palette[i], label=f'Classe {i} (AUC = {roc_auc:.2f})')
    else:
        fpr, tpr, _ = roc_curve(y_test_bin, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.2f})')

    plt.plot([0, 1], [0, 1], 'k--', label="Random (AUC = 0.50)")

    plt.xlabel('Taux de faux positifs (FPR)')
    plt.ylabel('Taux de vrais positifs (TPR)')
    plt.title('Courbes ROC')
    plt.legend()
    plt.grid()
    plt.show()

    auc_roc = roc_auc_score(y_test,y_test_bin, multi_class='ovo')
    return accuracy, precision, recall, f1, conf_matrix, f"AUC-ROC: {auc_roc:.10f}"


# utilisation : 
"""import sys
sys.path.append("eval.py")  # Exemple : "/home/user/projet/"
from eval import notation

notation(X_test, y_test, y_pred, model) """