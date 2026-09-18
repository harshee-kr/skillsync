import pandas as pd


def load_employees():
    return pd.read_csv("employees.csv")


def load_projects():
    return pd.read_csv("projects.csv")