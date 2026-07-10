import pandas as pd
import os


def export_report(results):

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(results)

    df.to_excel("output/report.xlsx", index=False)

    print("\nRelatório salvo em output/report.xlsx")