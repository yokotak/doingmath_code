# simple_list = [1, 2, 3]
# simple_list2 = [4, 5, 6]
# for x, y in zip(simple_list, simple_list2):
#     print(x, y)
import matplotlib.pyplot as plt

def find_corr_x_y(x, y):
    n = len(x)

    #積の和を求める
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)
        sum_prod_x_y = sum(prod)
        sum_x = sum(x)
        sum_y = sum(y)
        squred_sum_x = sum_x**2
        squred_sum_y = sum_y**2
        x_squre = []
        for xi in x:
            x_squre.append(xi**2)

        # find the sum
        x_squre_sum =sum(x_squre)

        y_squre = []
        for yi in y:
            y_squre.append(yi**2)

        # find the sum
        y_squre_sum =sum(y_squre)

        #use formla to calculate correlation
        numerator = n * sum_prod_x_y - sum_x * sum_y
        denominator_term1 = n * x_squre_sum - squred_sum_x
        denominator_term2 = n * y_squre_sum - squred_sum_y
        denominator = (denominator_term1 * denominator_term2) ** 0.5
        correlation = numerator / denominator

        return correlation
    
if __name__ == "__main__":
    highschool_score = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
    college_exam = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
    highschool_score_2 = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
    college_exam_2 = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]    
    correlation = find_corr_x_y(highschool_score, college_exam)
    print(correlation)
    plt.scatter(highschool_score, college_exam)
    plt.scatter(highschool_score_2, college_exam_2)
    plt.show()
