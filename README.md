# Density Altitude App

The Density Altitude App provides a calculation of density altitude based on weather data and GPS coordinates. It consists of a backend API built with Python and a future frontend component built with Flutter.

## Backend

The backend component is responsible for calculating the density altitude by integrating weather data and GPS coordinates. It utilizes the Weatherstack API for retrieving weather data and incorporates mathematical formulas to perform the calculation. The backend API is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

### Usage

To use the backend API, follow the instructions provided in the `backend/README.md` file. Once the backend is set up and running, you can send requests to the specified endpoints to calculate the density altitude.

### API Endpoints

The backend API will provide the following endpoint:

- `POST /density-altitude`: Calculates the density altitude based on weather data and GPS coordinates.

## Frontend (Future Plan)

The frontend component of the Density Altitude App will be built using Flutter. The frontend will provide a user-friendly interface where users can enter their GPS coordinates or use GPS location services on their devices to retrieve their current location. The app will then make requests to the backend API to calculate and display the density altitude (converted to and displayed as relative-equivalent altitude).

## Contributing

Contributions to the Density Altitude App are welcome! If you have any ideas for improvements, encounter issues, or want to contribute to the project, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).