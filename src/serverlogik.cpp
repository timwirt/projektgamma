#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <random>
#include <cstdlib>
#include <ctime>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

class Serverlogik {
    using Dictionary = std::unordered_map<std::string, std::unordered_map<std::string, double>>;

    public:
        double random_curve(double start, double tendenz, double stdabweichung) {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::normal_distribution<double> distribution(0.0, 1.0);
            double zeitschritte=0.01;
            double St = start;
            double Yt = distribution(gen);
            St = St + (tendenz * zeitschritte * St) + (stdabweichung * std::sqrt(zeitschritte) * Yt * St);
            return St;
        }

        std::unordered_map<std::string, std::vector<double>> new_values(std::unordered_map<std::string, std::vector<double>>& gueter) {
            std::unordered_map<std::string, std::vector<double>> new_gueter;

            for (const auto& [gut, gut_array] : gueter) {
                double last = gut_array.back();
                const auto& gut_entwicklung = gueter_entwicklung.find(gut)->second;

                double start = last;
                double tendenz = gut_entwicklung.at("tendenz");
                double stdabweichung = gut_entwicklung.at("stdabweichung");

                // Generiere den neuen Wert mit random_curve
                double new_value = random_curve(start, tendenz, stdabweichung);

                // Füge den neuen Wert zum neuen Dictionary hinzu
                new_gueter[gut] = gut_array;
                new_gueter[gut].push_back(new_value);

                if (new_gueter[gut].size() > 20) {
                    new_gueter[gut].erase(new_gueter[gut].begin());
                }
            }

            return new_gueter;
        }
        
    private:
        Dictionary gueter_entwicklung = {
        {"Klausurzulassung", {{"tendenz", 0.01}, {"stdabweichung", 0.1}}},
        {"Note", {{"tendenz", 0.2}, {"stdabweichung", 0.2}}},
        {"Klopapier", {{"tendenz", 0.45}, {"stdabweichung", 0.05}}},
        {"Nudeln", {{"tendenz", 0.05}, {"stdabweichung", 0.04}}},
        {"Konserven", {{"tendenz", 0.05}, {"stdabweichung", 0.045}}},
        {"Klausurbestechungsgeld", {{"tendenz", 0.35}, {"stdabweichung", 0.15}}},
        {"Bachelor B.Sc.", {{"tendenz", 0.5}, {"stdabweichung", 0.4}}},
        {"Bachelor B.A.", {{"tendenz", -0.05}, {"stdabweichung", 0.4}}},
        {"Bachelor B.Eng.", {{"tendenz", 0.01}, {"stdabweichung", 0.4}}},
        {"Mensaessen", {{"tendenz", 0.3}, {"stdabweichung", 0.08}}},
        {"Master", {{"tendenz", -0.01}, {"stdabweichung", 0.6}}},
        {"Docktor", {{"tendenz", 0.3}, {"stdabweichung", 0.8}}}
    };

};

namespace py = pybind11;

PYBIND11_MODULE(serverlogik, m) {
    m.doc() = "Serverlogik";

    py::class_<Serverlogik>(m, "Serverlogik")
        .def(py::init<>())
        .def("random_curve", &Serverlogik::random_curve)
        .def("new_values", &Serverlogik::new_values);
}