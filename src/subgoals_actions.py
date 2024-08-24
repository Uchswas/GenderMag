from constant import BASE_IMAGE_PATH
TYPE="SINGLE"



TAG =  "KOLKATA"
gm_moments =  {
    "scenario": "Add information to the README",
    "Subgoals": [
        {
            "subgoal": "Find the README",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image": BASE_IMAGE_PATH + "JabrefHomepage.png",
            "Actions": [
                {
                    "action": "Scroll down to read",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefHomepage.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefHomepage.png"
                    }
                },
                {
                    "action": "Click on README.md",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefHomepage.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefReadMe.png"
                    }
                }
            ]
        },
        {
            "subgoal": "Find out how to edit it",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image": BASE_IMAGE_PATH + "JabrefReadMe.png",
            "Actions": [
                {
                    "action": "Click the pencil button",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefReadMe.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefAfterClicklingpencil.png"
                    }
                },
                {
                    "action": "Edit the file",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefAfterClicklingpencil.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefAfterEdit.png"
                    }
                },
            
                {
                    "action": "Click 'preview change'",
                    "before_action": {
                        "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                        "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefAfterEdit.png"
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefAfterclickingpreview.png"
                    }
                },
                # {
                #     "action": "Click 'Propose File Change'",
                #     "before_action": {
                #         "question": "Will ABI know what to do at this step and is the page good enough for abi to take this action? Why?",
                #         "page_image_on_which_abi_take_the_action": BASE_IMAGE_PATH + "JabrefHomepage.png"
                #     },
                #     "after_action": {
                #         "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                #         "page_image_on_which_abi_is_after_the_action": BASE_IMAGE_PATH + "JabrefHomepage.png"
                #     }
                # },

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


