from rxcropmaturityshared import RXCROPMATURITYSHARED

class RXCROPMATURITYSKIPRUN(RXCROPMATURITYSHARED):
    def run_phase(self):
        self._run_phase(skip_run=True)