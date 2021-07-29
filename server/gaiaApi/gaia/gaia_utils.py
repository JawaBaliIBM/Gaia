class GaiaUtils:

    @staticmethod
    def convert_positive_int(param):
        param = int(param)
        if param < 1:
            raise ValueError

        return param