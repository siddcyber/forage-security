# Test exercises here
import pandas as pd
import matplotlib.pyplot as plt


# Read the dataset (`transactions.csv`) as a Pandas dataframe. Note that the first row of the CSV contains the column
# names.
def exercise_0(file):
    df = pd.read_csv(file)
    return df


# Return the column names as a list from the dataframe.
def exercise_1(df):
    return list(df.columns)


# Return the first k rows from the dataframe.
def exercise_2(df, k):
    return df.head(k)


# Return a random sample of k rows from the dataframe.
def exercise_3(df, k):
    return (df.sample(k))


# Return a list of the unique transaction types.
def exercise_4(df):
    return list(df['type'].unique())


# Return a Pandas series of the top 10 transaction destinations with frequencies.
def exercise_5(df):
    return df['nameDest'].value_counts().head(10)


# Return all the rows from the dataframe for which fraud was detected.
def exercise_6(df):
    return df.loc[df['isFlaggedFraud'] == 1]


# Bonus. Return a dataframe that contains the number of distinct destinations that each source has interacted with
# to, sorted in descending order.
def exercise_7(df):
    data = df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False)
    gk = pd.DataFrame(data).reset_index()
    return gk


def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)

    fig, axs = plt.subplots(2, figsize=(6, 10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction types')
    axs[0].set_xlabel('transaction type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types Split by Fraud')
    axs[1].set_xlabel('transaction type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Visual 1')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return plt.show()


def visual_2(df):
    pass


def exercise_custom(df):
    pass


def visual_custom(df):
    pass


# Read the dataset (`transactions.csv`) as a Pandas dataframe. Note that the first row of the CSV contains the column
# names.
# df = exercise_0('transactions.csv')
print(exercise_1(exercise_0('transactions.csv')))

visual_1(exercise_0('transactions.csv'))
