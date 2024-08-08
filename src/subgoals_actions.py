from constant import BASE_IMAGE_PATH



TAG="Lincoln"
gm_moments = {
    "scenario": "File an issue",
    "Subgoals": [
        {
            "subgoal": "Find information about filing an issue",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image": BASE_IMAGE_PATH + "MOCKHomepage.png",
            "Actions": [
                {
                    "action": "Click on issue button on the side",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "MOCKHomepage.png",
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "MOCKIssueList.png"
                    }
                },
                {
                    "action": "Click on the green new issue button",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "MOCKIssueList.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "MOCKISSUECREATE.png"
                    }
                }
            ]
        }
    ]
}


asserttions = """
Do and Don't before answering a question: 

Here are a few facts you must consider before answering a question.

1. Read all the text on the page to check if something is mentioned explicitly, which might help ABI do the action.
2. Don't think ahead of time. Just look at the page. See if the page instructs her to take action or Is the page good enough for Abi to take action? 
3. Remember to Assume something from the action description. If an action says anything that exists on the page, that might not be present on the page. For example, if an action says to click on the "x" button under "y," it is possible that there is no button under x under y. You have to check that, too. 
4. Don't make any assumptions from the image. Process the information from the picture that you see. Refrain from interpreting anything from the image title or other staff. Be precise and consider what you see

"""


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
            subgoal_string += f"Current Action: {action_info['action']}\n"
            
            subgoal_string += "Before Action "
            subgoal_string += f"Question: {action_info['before_action']['question']}"
            subgoal_string += "or Is there any clear instruction/ indication in the page to do this action\n"
            subgoal_string += f"Page Image on which the action would take: {action_info['before_action']['page_image_on_which_abi_take_the_action']}\n"
            result.append(subgoal_string)

            subgoal_string = f"Scenario: {scenario}\n"
            subgoal_string += f"Subgoal: {subgoal_info['subgoal']}\n"
            subgoal_string += f"Current Action: {action_info['action']}\n"
            subgoal_string += "After Action "
            subgoal_string += f"Question: {action_info['after_action']['question']}\n"
            subgoal_string += f"Page Image on which ABI will land after taking the action: {action_info['after_action']['page_image_on_which_abi_is_after_the_action']}\n"
            result.append(subgoal_string)
       
    return result

# Generate strings
strings_to_iterate_over = generate_strings(gm_moments)


