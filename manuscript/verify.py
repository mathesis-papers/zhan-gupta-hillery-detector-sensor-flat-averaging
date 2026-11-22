import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Quadratic:
    constant: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other):
        if not isinstance(other, Quadratic):
            other = Quadratic(Fraction(other))
        return Quadratic(self.constant + other.constant, self.radical + other.radical)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.constant, -self.radical)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Quadratic):
            other = Quadratic(Fraction(other))
        return Quadratic(
            self.constant * other.constant + 10 * self.radical * other.radical,
            self.constant * other.radical + self.radical * other.constant,
        )

    __rmul__ = __mul__

    def nonnegative(self):
        if self.constant >= 0 and self.radical >= 0:
            return True
        if self.constant < 0 and self.radical <= 0:
            return False
        if self.constant >= 0:
            return self.constant**2 >= 10 * self.radical**2
        return 10 * self.radical**2 >= self.constant**2


def determinant(matrix):
    if not matrix:
        return Quadratic(Fraction(1))
    result = Quadratic()
    for column in range(len(matrix)):
        minor = [row[:column] + row[column + 1:] for row in matrix[1:]]
        result += (-1)**column * matrix[0][column] * determinant(minor)
    return result


def check_psd(matrix):
    count = 0
    for size in range(1, len(matrix) + 1):
        for indices in itertools.combinations(range(len(matrix)), size):
            minor = [[matrix[row][column] for column in indices] for row in indices]
            assert determinant(minor).nonnegative()
            count += 1
    return count


def layer_distribution(sensor_count, weight):
    words = list(itertools.product([0, 1], repeat=sensor_count))
    return {word: Fraction(1, math.comb(sensor_count, weight))
            if sum(word) == weight else Fraction(0) for word in words}


def quarter_angle_gram(distribution, sensor_count):
    phase_table = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for first in range(sensor_count):
        row = []
        for second in range(sensor_count):
            real_part, imaginary_part = Fraction(0), Fraction(0)
            for word, probability in distribution.items():
                phase_real, phase_imaginary = phase_table[(word[second] - word[first]) % 4]
                real_part += probability * phase_real
                imaginary_part += probability * phase_imaginary
            row.append((real_part, imaginary_part))
        result.append(row)
    return result


def additional_checks():
    words = list(itertools.product([0, 1], repeat=3))
    nonsymmetric_cases = 0
    for numerator in range(13):
        parameter = Fraction(numerator, 12)
        distribution = {word: (1 + parameter * (2 * word[0] - 1)) / 8 for word in words}
        assert sum(distribution.values()) == 1
        assert min(distribution.values()) >= 0
        for first, second in itertools.product(range(3), repeat=2):
            moment = sum(probability * (2 * word[first] - 1) * (2 * word[second] - 1)
                         for word, probability in distribution.items())
            assert moment == (first == second)
        if parameter:
            assert distribution[(1, 0, 0)] != distribution[(0, 1, 0)]
        nonsymmetric_cases += 1

    unambiguous_cases = 0
    residual_minors = 0
    for sensor_count in range(3, 6):
        overlaps = [Fraction(-1, sensor_count - 1), Fraction(-1, 2 * (sensor_count - 1)),
                    Fraction(0), Fraction(1, 3), Fraction(1)]
        for overlap in overlaps:
            success = min(1 - overlap, 1 + (sensor_count - 1) * overlap)
            assert 1 - success == max(overlap, -(sensor_count - 1) * overlap)
            residual = [[Quadratic((1 if row == column else overlap)
                                   - (success if row == column else 0))
                         for column in range(sensor_count)] for row in range(sensor_count)]
            residual_minors += check_psd(residual)
            null_vector = ([1, -1] + [0] * (sensor_count - 2)
                           if overlap >= 0 else [1] * sensor_count)
            for row in residual:
                assert sum(value * coefficient for value, coefficient in zip(row, null_vector)) == Quadratic()
            unambiguous_cases += 1

    auxiliary = {word: (Fraction(0), Fraction(0)) for word in words}
    for word, vector in zip(words, [(Fraction(1, 2), Fraction(0)),
                                   (Fraction(0), Fraction(1, 2)),
                                   (Fraction(3, 10), Fraction(2, 5)),
                                   (Fraction(2, 5), Fraction(3, 10))]):
        auxiliary[word] = vector
    distribution = {word: sum(value * value for value in vector)
                    for word, vector in auxiliary.items()}
    assert sum(distribution.values()) == 1
    phases = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    patterns = [(1, 0, 0), (0, 1, 0), (1, 1, 0)]
    auxiliary_entries = 0
    for first, second in itertools.product(patterns, repeat=2):
        direct_real, direct_imaginary = Fraction(0), Fraction(0)
        reduced_real, reduced_imaginary = Fraction(0), Fraction(0)
        for word in words:
            exponent = sum((right - left) * bit for left, right, bit in zip(first, second, word)) % 4
            real, imaginary = phases[exponent]
            first_real, first_imaginary = phases[sum(bit * selected for bit, selected in zip(word, first)) % 4]
            second_real, second_imaginary = phases[sum(bit * selected for bit, selected in zip(word, second)) % 4]
            for amplitude in auxiliary[word]:
                left_real, left_imaginary = amplitude * first_real, amplitude * first_imaginary
                right_real, right_imaginary = amplitude * second_real, amplitude * second_imaginary
                direct_real += left_real * right_real + left_imaginary * right_imaginary
                direct_imaginary += left_real * right_imaginary - left_imaginary * right_real
            reduced_real += distribution[word] * real
            reduced_imaginary += distribution[word] * imaginary
        assert (direct_real, direct_imaginary) == (reduced_real, reduced_imaginary)
        auxiliary_entries += 1
    return {'nonsymmetric_parameters': nonsymmetric_cases,
            'unambiguous_symmetric_cases': unambiguous_cases,
            'unambiguous_residual_principal_minors': residual_minors,
            'diagonal_pattern_auxiliary_gram_entries': auxiliary_entries}


def main():
    count_checks = 0
    for sensor_count in range(3, 9):
        for weight in range(sensor_count + 1):
            words = [word for word in itertools.product([0, 1], repeat=sensor_count)
                     if sum(word) == weight]
            for first, second in itertools.combinations(range(sensor_count), 2):
                forward = sum(word[first] == 1 and word[second] == 0 for word in words)
                backward = sum(word[first] == 0 and word[second] == 1 for word in words)
                expected = math.comb(sensor_count - 2, weight - 1) if 1 <= weight < sensor_count else 0
                assert forward == backward == expected
                assert Fraction(forward, len(words)) == Fraction(
                    weight * (sensor_count - weight), sensor_count * (sensor_count - 1))
                count_checks += 1

    first_layer = layer_distribution(3, 1)
    second_layer = layer_distribution(3, 2)
    assert sum(first_layer.values()) == sum(second_layer.values()) == 1
    assert first_layer != second_layer
    expected_gram = [[(Fraction(1) if row == column else Fraction(1, 3), Fraction(0))
                      for column in range(3)] for row in range(3)]
    mixture_count = 0
    for numerator in range(13):
        mixture_weight = Fraction(numerator, 12)
        distribution = {word: mixture_weight * first_layer[word]
                        + (1 - mixture_weight) * second_layer[word] for word in first_layer}
        assert sum(distribution.values()) == 1
        assert quarter_angle_gram(distribution, 3) == expected_gram
        mixture_count += 1

    adjustment = Quadratic(Fraction(-1, 3), Fraction(1, 6))
    reduced_root = [[adjustment + (row == column) for column in range(3)] for row in range(3)]
    root_square = [[sum(reduced_root[row][index] * reduced_root[index][column]
                        for index in range(3)) * Fraction(2, 3)
                    for column in range(3)] for row in range(3)]
    for row, column in itertools.product(range(3), repeat=2):
        assert root_square[row][column] == Quadratic(expected_gram[row][column][0])
    principal_minors = check_psd(reduced_root)
    diagonal = reduced_root[0][0]
    dual = [[Fraction(2, 9) * diagonal * value for value in row] for row in reduced_root]
    principal_minors += check_psd(dual)
    for label in range(3):
        slack = [[dual[row][column] - Fraction(2, 9)
                  * reduced_root[row][label] * reduced_root[label][column]
                  for column in range(3)] for row in range(3)]
        principal_minors += check_psd(slack)
    success = Fraction(2, 3) * diagonal * diagonal
    assert success == Quadratic(Fraction(13, 27), Fraction(4, 27))
    assert sum(dual[index][index] for index in range(3)) == success
    error = Quadratic(Fraction(1)) - success
    assert error == Quadratic(Fraction(14, 27), Fraction(-4, 27))
    assert error.nonnegative() and error != Quadratic()

    print(json.dumps({
        'status': 'pass',
        'arithmetic': 'exact rational and Q(sqrt(10))',
        'layer_count_cases': count_checks,
        'layer_count_sensor_range': [3, 8],
        'three_sensor_segment_points': mixture_count,
        'gram': [['1', '1/3', '1/3'], ['1/3', '1', '1/3'], ['1/3', '1/3', '1']],
        'nonnegative_principal_minors': principal_minors,
        'optimal_success': '(13 + 4*sqrt(10))/27',
        'minimum_error': '(14 - 4*sqrt(10))/27',
        'additional_checks': additional_checks(),
        'coverage': 'Finite layer counts, equal-Gram witnesses, and matching measurement and upper-bound matrices; universal statements have written proofs in note.tex.'
    }, indent=2))


if __name__ == '__main__':
    main()
