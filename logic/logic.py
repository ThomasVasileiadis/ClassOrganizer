import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import tensorflow as tf


# Generate random data
n_samples = 10000
obligations = np.random.choice(['podosfairo', 'family', 'other'], size=n_samples)
obligation_start_time = pd.to_timedelta(np.random.randint(1, 24, size=n_samples), unit='h')
obligation_end_time = obligation_start_time + pd.to_timedelta(np.random.randint(1, 4, size=n_samples), unit='h')
obligation_duration = obligation_end_time - obligation_start_time
class_time = pd.to_datetime(np.random.randint(15, 21, size=n_samples), unit='h').strftime('%H:%M')
class_duration = 45
day = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], size=n_samples)
teacher = np.random.choice(['teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5'], size=n_samples)
student = np.random.choice(['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7'], size=n_samples)

# Save data to dataframe
data = {'student': student, 'obligations': obligations, 'obligation_start_time': obligation_start_time, 'obligation_end_time': obligation_end_time, 'obligation_duration': obligation_duration, 'class_time': class_time, 'class_duration': class_duration, 'day': day, 'teacher': teacher, }
df = pd.DataFrame(data)

# Export data to CSV
current_path = os.getcwd()
df.to_csv(current_path + '/logic/training_data.csv', index=False)


# Define the RL agent class
class SchedulingAgent:
    def __init__(self, state_dim, action_dim):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = 0.99  # Discount factor
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        
        # Create actor and critic networks
        self.actor = self.build_actor_network()
        self.critic = self.build_critic_network()
        
    def build_actor_network(self):
        # Define and compile the actor network (policy)
        actor = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(self.state_dim,)),
            tf.keras.layers.Dense(self.action_dim, activation='softmax')
        ])
        actor.compile(optimizer=self.actor_optimizer, loss='categorical_crossentropy')
        return actor

    def build_critic_network(self):
        # Define and compile the critic network (value)
        critic = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(self.state_dim,)),
            tf.keras.layers.Dense(1, activation='linear')
        ])
        critic.compile(optimizer=self.critic_optimizer, loss='mean_squared_error')
        return critic

    def choose_action(self, state):
        # Implement the agent's action selection logic
        action_probs = self.actor.predict(state)
        action = np.random.choice(self.action_dim, p=action_probs[0])
        return action

    def learn(self, state, action, reward, next_state):
        # Implement the agent's learning process using PPO

        # Calculate advantage using the critic network
        advantage = self.calculate_advantage(state, next_state, reward)

        # One-hot encode the action
        action_one_hot = tf.one_hot(action, self.action_dim)

        # Calculate the probabilities of the selected actions
        selected_action_prob = tf.reduce_sum(action_one_hot * self.actor(state), axis=1)

        # Calculate the old probabilities of the selected actions
        old_action_prob = tf.reduce_sum(action_one_hot * self.old_actor(state), axis=1)

        # Calculate the ratio of new to old probabilities
        ratio = selected_action_prob / (old_action_prob + 1e-5)

        # Calculate surrogate loss
        surrogate_loss = tf.minimum(ratio * advantage, tf.clip_by_value(ratio, 1 - clip_epsilon, 1 + clip_epsilon) * advantage)

        # Calculate the critic's value estimate
        predicted_values = self.critic(state)

        # Define the value loss
        value_loss = tf.losses.mean_squared_error(predicted_values, reward)

        # Calculate the total loss
        total_loss = -surrogate_loss + value_loss

        # Update actor and critic networks
        actor_gradients = tf.gradients(total_loss, self.actor.trainable_variables)
        critic_gradients = tf.gradients(value_loss, self.critic.trainable_variables)

        self.actor_optimizer.apply_gradients(zip(actor_gradients, self.actor.trainable_variables))
        self.critic_optimizer.apply_gradients(zip(critic_gradients, self.critic.trainable_variables))

    def calculate_advantage(self, state, next_state, reward):
        # Implement the advantage calculation using the critic network
        next_state_values = self.critic(next_state)
        advantages = reward + self.gamma * next_state_values - self.critic(state)
        return advantages

# Load and preprocess data
def load_and_preprocess_data():
    # Load student data and teacher availability data
    # Perform data preprocessing

    return student_data, teacher_availability

# Training loop
def train_scheduling_agent():
    # Load and preprocess data
    student_data, teacher_availability = load_and_preprocess_data()

    # Define state and action dimensions based on your data
    state_dim = len(student_data.columns)  # Adjust as needed
    action_dim = 7  # Adjust based on your scheduling problem

    # Initialize the agent
    agent = SchedulingAgent(state_dim, action_dim)

    num_episodes = 1000  # Set an appropriate number of episodes
    clip_epsilon = 0.2  # PPO clip parameter (tune as needed)

    for episode in range(num_episodes):
        state = initial_state  # Define the initial state for scheduling
        done = False

        while not done:
            action = agent.choose_action(state)
            
            # Implement scheduling logic and obtain reward, next_state
            
            agent.learn(state, action, reward, next_state)
            
            state = next_state

if __name__ == "__main__":
    train_scheduling_agent()


