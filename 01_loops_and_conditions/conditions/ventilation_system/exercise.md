# Exercise: Ventilation System Decision

## Instructions

1. Create a file named `ventilation_system.py`.
2. Design a program that determines the correct ventilation system for a building.
3. **Important:** The program must ask **exactly two questions**. The second question changes depending on the answer to the first.

## Logic Flow
1. **Question 1:** "What is the heating type?"
   * **(A)ir:** (Forced Air)
     * **Question 2:** "Is the soil saturated with gas?" ((Y)es / (N)o)
       * **Yes:** Install supply and extraction fans.
       * **No:** Install extraction fans.
   * **(C)ombustion:**
     * **Question 2:** "What is the indoor humidity rate?" (0-100%)
       * **> 70%:** Install supply and extraction fans.
       * **≤ 70%:** Install supply fans.



## Constraints
* **Validation:**
    * Heating must be 'A' or 'C'.
    * Gas answer must be 'Y' or 'N'.
    * Humidity must be an integer between 0 and 100.
* **Error Handling:** If *any* answer is invalid, print `Invalid answers!`.