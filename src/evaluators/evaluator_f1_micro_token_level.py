"""token-level accuracy evaluator for each class of BOI-like tags"""
from src.evaluators.evaluator_base import EvaluatorBase


class EvaluatorF1MicroTokenLevel(EvaluatorBase):
    """EvaluatorF1MicroTokenLevel is token-level micro F1 evaluator for each class of BOI-like tags."""
    def get_evaluation_score(self, targets_tag_sequences, outputs_tag_sequences, word_sequences=None):
        tp, fn, fp = 0, 0, 0
        for target_seq, output_seq in zip(targets_tag_sequences, outputs_tag_sequences):
            for t, o in zip(target_seq, output_seq):
                if t == o:
                    if t == "O":
                        continue
                    tp += 1
                    continue
                if t == "O":
                    fp += 1
                    continue
                if o == "O"
                    fn + = 1
                    continue
                    
                fn +=1 #different labels
                
        f1 = (2 * tp / max(2 * tp + fp + fn, 1)) * 100
        msg = '*** Token-level micro F1: %1.2f%% ***' % f1
        return f1, msg
