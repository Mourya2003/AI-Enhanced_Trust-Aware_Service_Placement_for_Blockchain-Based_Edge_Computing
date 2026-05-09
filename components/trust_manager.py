import time


class TrustManager:
    """
    Adaptive Trust Management System
    Formula:
    Ti = alpha*S + beta*A - gamma*F + delta*R
    """

    def __init__(self):

        # --------------------------------
        # ADAPTIVE TRUST PARAMETERS
        # --------------------------------

        self.alpha = 2.0     # Success reward

        self.beta = 1.0      # Recency weight

        self.gamma = 3.0     # Failure penalty

        self.delta = 1.5     # Reliability reward

    def calculate_recency(self, last_active_time):

        current_time = time.time()

        time_diff = current_time - last_active_time

        return max(
            0.5,
            1.0 - (time_diff / 3600)
        )

    def update_trust(self, node, is_success):

        # --------------------------------
        # UPDATE TASK COUNTS
        # --------------------------------

        node.total_tasks += 1

        if is_success:
            node.success_count += 1
        else:
            node.failure_count += 1

        # --------------------------------
        # CALCULATE METRICS
        # --------------------------------

        recency_factor = self.calculate_recency(
            node.last_activity_time
        )

        reliability = (
            node.success_count / node.total_tasks
        )

        # --------------------------------
        # SUCCESS CASE
        # --------------------------------

        if is_success:

            trust_gain = (
                (self.alpha * recency_factor)
                + (self.delta * reliability)
            )

            node.trust_score += trust_gain

        # --------------------------------
        # FAILURE CASE
        # --------------------------------

        else:

            trust_penalty = (
                self.gamma * (1.2 - reliability)
            )

            node.trust_score -= trust_penalty

        # --------------------------------
        # CLAMP TRUST RANGE
        # --------------------------------

        node.trust_score = max(
            30.0,
            min(100.0, node.trust_score)
        )

        # --------------------------------
        # UPDATE ACTIVITY TIME
        # --------------------------------

        node.last_activity_time = time.time()

        return node.trust_score