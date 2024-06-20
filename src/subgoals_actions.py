from constant import BASE_IMAGE_PATH

gm_moments = {
    "scenario": "Abi wants to submit Assignment 7",
    "Subgoals": [
        {
            "subgoal": "Find assignment 7",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"HomePage.png",
            "Actions": [
                {
                    "action": "Click on assignment 7 link under Coming up section (Before)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"HomePage.png",
                     
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"Assignment7.png",
                    }
                },
                {
                    "action": "Click on Github link (Before)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"Assignment7.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"AfterclickingGithub.png",
                    }
                }
            ]
        },
        {
            "subgoal": "Go to Gradescope to submit assignment",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"HomePage.png",
            "Actions": [
                {
                    "action": "Click on assignment 7 link under Coming up section (Before)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"HomePage.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"Assignment7.png",
                    }
                },
                {
                    "action": "Click on load assignment 7 for submission (Before)",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH+"Assignment7.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"Afterclickingload.png",
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
        subgoal_string += f"Question: {subgoal_info['question']}\n"
        subgoal_string += f"Subgoal Page Image: {subgoal_info['subgoal_page_image']}\n"
        result.append(subgoal_string)
        

        subgoal_string += "Actions:\n"
        for action_info in subgoal_info["Actions"]:
            subgoal_string = f"Scenario: {scenario}\n"
            subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
            subgoal_string += f"    Current Action: {action_info['action']}\n"
            
            subgoal_string += "    Before Action "
            subgoal_string += f"Question: {action_info['before_action']['question']}\n"
            subgoal_string += f"      Page Image on which the action would take: {action_info['before_action']['page_image_on_which_abi_take_the_action']}\n"
            result.append(subgoal_string)

            subgoal_string = f"Scenario: {scenario}\n"
            subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
            subgoal_string += f" Current Action: {action_info['action']}\n"
            subgoal_string += "    After Action "
            subgoal_string += f"      Question: {action_info['after_action']['question']}\n"
            subgoal_string += f"      Page Image on which ABI will land after taking the action: {action_info['after_action']['page_image_on_which_abi_is_after_the_action']}\n"
            
        result.append(subgoal_string)
    return result

# Generate strings
strings_to_iterate_over = generate_strings(gm_moments)

