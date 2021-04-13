




from typing import List
class DescriptiveStats:

    def calc_count(self,x: List[float]) -> int:
        """Returns the number of data points in a data set"""
        return len(x)

    def calc_minimum(self,x: List[float]) -> float:
        """Returns the lowest data point in a data set"""
        return min(x)

    def calc_maximum(self,x: List[float]) -> float:
        """Returns the highest data point in a data set"""
        return max(x)

    def calc_range(self,x: List[float]) -> float:
    """Returns the difference between the lowest and highest values in a data set"""
        return self.calc_maximum(x) - self.calc_minimum(x)

    def calc_mean(self,x: List[float]) -> float:
    """Returns the average value of a data set"""
        return sum(x) / self.calc_count(x)

    def calc_median(self,x: List[float]) -> float:
       """Returns the middle value of a data set"""
        if self.calc_count(x) % 2 == 1:
            return sorted(x)[self.calc_count(x) // 2]
        if self.calc_count(x) % 2 == 0:
            return ((sorted(x)[(self.calc_count(x) // 2) - 1]) + \
                    (sorted(x)[self.calc_count(x) // 2])) / 2

    def calc_quantile(self,x: List[float], y: float) -> float:
    """Returns a particular part of a data set"""
        return sorted(x)[int(y * self.calc_count(x))]

    def calc_interquantile_range(self,x: List[float]) -> float:
    """Returns the difference in value between the upper quartile and lower quartile of a data set"""
        return self.calc_quantile(x, 0.75) - self.calc_quantile(x, 0.25)

    def calc_mode(self,x: List[float]) -> List[float]:
    """Returns the number that is repeated most  in a data set"""
        frequency_dict = {}
        for i in x:
            if i not in frequency_dict:
                frequency_dict[i] = 1
            else:
                frequency_dict[i] += 1
        modes = []
        highest_frequency = sorted(frequency_dict.values())[-1]
        for key, value in frequency_dict.items():
            if value == highest_frequency:
                modes.append(key)
        return modes

    def calc_variance(self,x: List[float]) -> float:
    """Returns the variability from the mean of a data set"""
        assert self.calc_count(x) >= 2, "Variance requires at least two elements"
        return sum([(i - (self.calc_mean(x)))**2 for i in x]) / self.calc_count(x)

    def calc_bessel_variance(self,x: List[float]) -> float:
       """Returns the variability from the mean of a data set"""
        assert self.calc_count(x) >= 2, "Variance requires at least two elements"
        return sum([(i - (self.calc_mean(x)))**2 for i in x]) / (self.calc_count(x) - 1)

    def calc_standard_deviation(self,x: List[float]) -> float:
        """Returns the dispersion of a dataset relative to its mean and is
        calculated as the square root of the
        variance"""
        assert self.calc_count(x) >= 2, "Standard Deviation requires at least two " \
        "elements"
        return (sum([(i - (self.calc_mean(x)))**2 for i in x]) / self.calc_count(x))**0.5

    def calc_bessel_standard_deviation(self,x: List[float]) -> float:
        """Bessel's correction is the use of n - 1 instead of n in the formula for the sample variance and sample standard deviation"""
        assert self.calc_count(x) >= 2, "Standard Deviation requires at least two " \
        "elements"
        return (sum([(i - (self.calc_mean(x)))**2 for i in x]) / \
                (self.calc_count(x) - 1))**0.5

    def calc_covariance(self,x: List[float], y: List[float]) -> float:
        """Returns how much two random variables vary together."""
        assert self.calc_count(x) == self.calc_count(y), "x and y must contain the same " \
        "number of elements"
        return sum([(i - (self.calc_mean(x))) * (j - (self.calc_mean(y))) for i, \
                    j in zip(x, y)]) / (self.calc_count(x) - 1)

    def calc_correlation(self,x: List[float], y: List[float]) -> float:
        """Returns the strength of the relationship between the relative movements of two variables"""
        if self.calc_bessel_standard_deviation(x) > 0 and \
        self.calc_bessel_standard_deviation(y) > 0:
            return self.calc_covariance(x, y) / self.calc_bessel_standard_deviation(x) / \
            self.calc_bessel_standard_deviation(y)
        else:
            return 0
