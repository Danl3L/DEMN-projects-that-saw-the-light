import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
data = pd.read_csv('/Users/danielnavia/Desktop/EmployeeClean.csv')
def handle_greeting(message):
    greetings = ['hi', 'hello', 'hey']
    if any(greeting in message.lower() for greeting in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I assist you?"])
    return None

def generate_graph_response(message):
    if "graph of work groups" in message.lower():
        # Generate graph for work groups
        return "", generate_work_groups_graph()
    
    elif "explore distribution of roles" in message.lower():
        # Generate graph for distribution of roles
        return "", generate_roles_distribution_graph()

    elif "examine work life balance" in message.lower():
        # Generate graph for work-life balance
        return "", generate_work_life_balance_graph()

    elif "bad productivity trends" in message.lower():
        # Generate graph for productivity trends
        return generate_productivity_phrases_graph(), None
    
    elif "best work space" in message.lower():
        # Generate graph for preferred work spaces
        return generate_preferred_spaces_graph(), None
    
    return None, None

def generate_response(message):
    # Handle greetings
    greeting_response = handle_greeting(message)
    if greeting_response:
        return greeting_response, None
    
    # Generate graph response
    graph_response, graph = generate_graph_response(message)
    if graph_response is not None or graph is not None:
        return graph_response, graph
    
    if "exit" in message.lower():
        return "__exit__", None
    
    return "I'm sorry, I didn't understand that. Please try again.", None

# Define functions to generate graphs
def generate_work_groups_graph():
    # Group by 'Q1' and 'Q2'
    grouped_counts = data.groupby(['Q1', 'Q2']).size()
    grouped_counts_unstacked = grouped_counts.unstack()
    ax = grouped_counts_unstacked.plot(kind='bar', stacked=False, figsize=(10, 6))
    ax.set_ylabel('Count')
    ax.set_xlabel('Group')
    plt.legend(title='Q2', bbox_to_anchor=(1.05, 1), loc='upper left')
    return plt.gcf()

def generate_roles_distribution_graph():
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Q2', data=data)
    plt.title('Distribution of Roles')
    plt.xlabel('Count')
    plt.ylabel('Role')
    return plt.gcf()

def generate_work_life_balance_graph():
    # Examine work-life balance ratings
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Q5', data=data)
    plt.title('Work-Life Balance Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    return plt.gcf()

def generate_productivity_phrases_graph():
    print("Entering 'things that affect productivity' block")  # Debug: Confirm block entry

    # Split the phrases in column Q8 and count their occurrences
    phrases = data['Q8'].str.split(';').explode()
    phrase_counts = phrases.value_counts()

    # Find the three most common phrases
    top_three_phrases = phrase_counts.nlargest(3)

    # Prepare output message with top phrases
    output_message = "The three most common phrases are:\n"
    for phrase, count in top_three_phrases.items():
        output_message += f"{phrase}: {count} occurrences\n"

    return output_message, None

def generate_preferred_spaces_graph():
    # Count the occurrences of each response in column 'Q4'
    response_counts = data['Q4'].value_counts()

    # Find the three most common responses
    top_three_responses = response_counts.nlargest(3)

    # Prepare output message with top responses
    output_message = "The three preferred spaces are:\n"
    for phrase, count in top_three_responses.items():
        output_message += f"{phrase}: {count} occurrences\n"

    return output_message, None
