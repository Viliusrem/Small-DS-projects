age = 28
sex = 0
bmi = 26.2
number_of_children = 3
smoker = 0

def insurance_calc(age, sex, bmi, number_of_children, smoker):
  return 250*age - 128*sex + 370*bmi + 425*number_of_children + 24000*smoker - 12500

insurance_cost = insurance_calc(age, sex, bmi, number_of_children, smoker)

new_insurance_cost = insurance_calc(age + 4, sex, bmi, number_of_children, smoker)

change_in_insurance_cost = new_insurance_cost - insurance_cost

new_insurance_cost_bmi = insurance_calc(age, sex, bmi + 3.1, number_of_children, smoker)

new_insurance_cost_sex = insurance_calc(age, 1, bmi, number_of_children, smoker)

print('\n', "This person's insurance cost is", insurance_cost, "dollars.")

print('\n', "This person's insurance cost is", new_insurance_cost, "dollars.")

print('\n', "People who are four years older have estimated insurance costs that are", change_in_insurance_cost, "dollars different, where the sign of", change_in_insurance_cost, "tells us whether the cost is higher of lower.")

print('\n', "The change in estimated insurance cost after increasing BMI by 3.1 is", insurance_cost - new_insurance_cost_bmi ,"dollars.")

print('\n', "The change in estimated cost for being male instead of female is", insurance_cost - new_insurance_cost_sex ,"dollars.")


