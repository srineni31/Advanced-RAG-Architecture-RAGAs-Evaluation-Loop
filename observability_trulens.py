from trulens_eval import TruChain, Feedback
import logging

class TruLensObserver:
    def __init__(self):
        self.feedback = Feedback()
        logging.basicConfig(filename='results/latency_logs.csv', level=logging.INFO)

    def track(self, llm_chain):
        tru = TruChain(chain=llm_chain, app_id="RAG_Obs_Monitor")
        tru.run()
        logging.info("TruLens Monitoring Completed.")
