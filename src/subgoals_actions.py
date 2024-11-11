from constant import BASE_IMAGE_PATH
TYPE="SINGLE"

#replace_text_here
TAG="PATTAYA"
gm_moments = {
    "scenario": "Abi decided to attend ICSE 2019 and is making travel arrangements (not doing the third-party registration sequence) - she is the second author on a paper that got accepted, so she doesn't have to go, but she has decided to go.",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Abby wants to know where people are staying",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Home.png",
            "Actions": [
                {
                    "action": "Click on attending",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019CLICKATT.png",
    
                    }
                },
                {
                    "action": "Click on accommodation",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019CLICKATT.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                    }
                },
                {
                    "action": "Scroll",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                    }
                }
            ]
        },
        {
            "subgoal": "How many days to stay at the conference",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Acco.png",
            "Actions": [
                {
                    "action": "Click on program",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Acco.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019AccoEx.png",
            
                    }
                },
                {
                    "action": "Click Week overview",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019AccoEx.png",
                        
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Week.png",
                       
                    }
                },
                {
                    "action": "Go up the page and click on tracks",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Week.png",
                    
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019WeekAfter.png",
                    
                    }
                }
            ]
        }
    ]
}

def generate_strings(gm_moments):
    result = []
    scenario = gm_moments["scenario"]
    for subgoal_info in gm_moments["Subgoals"]:
        subgoal_string = f"Scenario: {scenario}\n"
        subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
        subgoal_string += f"Question: Will ABI have thought of this as a step toward achieving the overall use case?\n"
        subgoal_string += f"Subgoal Page Image: {subgoal_info['subgoal_page_image']}\n"
        result.append(subgoal_string)
        

        subgoal_string += "Actions:\n"
        for action_info in subgoal_info["Actions"]:
            subgoal_string = f"Scenario: {scenario}\n"
            subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
            subgoal_string += f"Current Action: {action_info['action']}\n"
            
            subgoal_string += "Before Action "
            subgoal_string += f"Question: {action_info['before_action']['question']}"
            subgoal_string += f"Page Image on which the action would take: {action_info['before_action']['page_image_on_which_abi_take_the_action']}\n"
            result.append(subgoal_string)

            subgoal_string = f"Scenario: {scenario}\n"
            subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
            subgoal_string += f"Current Action: {action_info['action']}\n"
            subgoal_string += "After Action "
            subgoal_string += f"Question: {action_info['after_action']['question']}"
            subgoal_string += f" and get all information she need"
            subgoal_string += f"Page Image on which ABI will land after taking the action: {action_info['after_action']['page_image_on_which_abi_is_after_the_action']}\n"
            result.append(subgoal_string)
       
    return result

# Generate strings
strings_to_iterate_over = generate_strings(gm_moments)


