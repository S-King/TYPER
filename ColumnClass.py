class Column(object):
    """Column Object to keep track of each column's analysis"""

    def __init__(self, header, col_number):
        """All we know up front is the column header"""
        self.header = header
        self.col_number = col_number
        
        # COLUMN STATS #
        self.overallavg_length = None
        
        # STRINGs
        self.string_count = 0
        self.string_avglength = None
        self.string_maxlength = None

        # INTs
        self.int_count = 0
        self.int_avglength = None
        self.int_maxlength = None

        # FLOATs
        self.float_count = 0
        self.float_avglength = None
        self.float_maxlength = None
        
        # Confidence
        self.predicted_datatype = ''
        self.pd_count = 0
        self.pd_confidence = 0.0
        
        
    def DatatypeConfidence(self, num_rows):
        counts = {"strings" : self.string_count, "ints" : self.int_count, "floats" : self.float_count }
        
        max_count = 0
        for key, value in counts.items():
            if ( value > max_count ): # Need to improve this to know when scores are close
                max_count = value
                self.pd_count = value
                self.predicted_datatype = key
                self.pd_confidence = float(value) / float(num_rows)
                # print("{} {} {}".format(key, value, num_rows))