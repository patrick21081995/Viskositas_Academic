# Viskositas_Academic

Academic version of **Viskositas** (_Viskositas_ — https://github.com/patrick21081995/VISKOSITAS) with viscosity prediction of CaO-SiO₂-MgO-Al₂O₃-MnO-FeO-CaF₂-Na₂O systems. _Viskositas Academic_ is a neural network and has better efficiency when compared to classic equations, neural networks in literature and other commercial software and uses the values of chemical composition and temperature to predict the viscosity value of the chemical system at the given temperature (The database, applications, and references are in **Viskositas**).

## Neural Network

With a preprocessing data (_preprocessing_data.d_ file) relating depolymerization (NBO/T) and liquidus temperature (Tliq) parameters Viskositas Academic was developed. (_viskositas_academic_pipeline.s_ file). A database for training, validation and testing was separated and the test dataset was **NOT** used for training the neural network (_viskositas_academic_neural_network.py_ file).

| Metrics/ Models | **_Viskositas 1.0.1_** | _Viskositas Academic_ | _FactSage® 7.2_ |
| :---: | :---: | :---: | :---: |
|  Mean Absolute Error (log η) | **_0.2309_** | 0.8112 | 0.8112 |
| Standard Deviation (log η) | **_0.5446_** | 1.3348 | 1.3348 |
| Coefficient of Determination (R²) | **_0.9864_** | 0.8212 | 0.8212 |

*η - Pa.s

## GUI

Using tkinter (https://docs.python.org/3/library/tkinter.html) package the Viskositas Academic GUI application was developed (_viskositas_academic_GUI.py_ file). The application has various functionalities (e.g. Cut, Copy, Paste, Delete, reports generation, open files), and is **FREE TO USE!**

# Contact

- E-mail: patrick.dosanjos@outlook.com
- Linkedin: https://www.linkedin.com/in/patrick-queiroz-dos-anjos/

# License

© 2022, Patrick Queiroz dos Anjos. Licensed under the MIT License.
