from main import data_a, data_b
from ouliers_detector import data_a_filtered, data_b_filtered

from scipy import stats


# A/B Test


def ab_test(sample_a, sample_b, column_name):
    # Perform Mann_Withney U test on a specified column of both samples
    _, p = stats.mannwhitneyu(
        sample_a[column_name], sample_b[column_name], alternative="less"
    )

    # check the p value less or greater than 0.05 to reject or accept null hypothesis

    if p < 0.05:
        print(f"{column_name}:Group B wins (H0 reject)")
    else:
        print(f"{column_name}: Group A wins (n0 accept)")
    # Print the p-value
    print(f"p-value = {p}")


# Call the ab_test function on the unfiltered data for the 'AOV' column
ab_test(data_a, data_b, "AOV")
ab_test(data_a, data_b, "Total_Amount_Spent")


# Run an A/B test on filtered data # that needs extra care
ab_test(data_a_filtered, data_b_filtered, "AOV")
ab_test(data_a_filtered, data_b_filtered, "Total_Amount_Spent")
