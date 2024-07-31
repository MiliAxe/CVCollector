# CVCollector

This project is designed to streamline the process of managing resumes, job positions, and candidate information. It provides a user-friendly interface for HR departments to handle resumes efficiently.

## Features

- **Resume Submission**: Candidates can submit their resumes in PDF format.
- **Job Positions**: Manage and display various job positions available in the company.
- **Automated Messaging**: Send automated messages to candidates regarding their application status.
- **Database Integration**: Store and retrieve candidate information from a database.
- **Specialization Markup**: Generate specialized markup for different job positions.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/resume-management-system.git
    cd resume-management-system
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Copy `config_sample.env` to `config.env`:

    ```sh
    cp config_sample.env config.env
    ```

    - Update `config.env` with your configuration details.

## Usage

1. Run the main application:

```sh
python main.py
```

## Configuration

### Adding Specializations and Departments

You can add change the specializations and departments by updating the buttons in the `buttons.py` file. Make sure to add the corresponding prefixes in the `callback-data` to handle the button clicks.

### Database Configuration

You can use any database of your choice. For now, you can change this in the `database.py` file. Change the database connection to the method that suits your database.

## Project Structure

- **`buttons.py`**: Contains functions for generating button markups.
- **`commands.py`**: Handles various command-line operations.
- **`config.py`**: Configuration settings for the application.
- **`database.py`**: Database operations and functions.
- **`get_resumes_conv.py`**: Handles resume conversion processes.
- **`main.py`**: Entry point of the application.
- **`positions_conv.py`**: Manages job positions and related operations.
- **`utils.py`**: Utility functions used across the project.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:

    ```sh
    git checkout -b feature/your-feature-name
    ```

3. Make your changes and commit them:

    ```sh
    git commit -m "Add your message here"
    ```

4. Push to the branch:

    ```sh
    git push origin feature/your-feature-name
    ```

5. Create a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Disclaimer

The code in this project is not really thought out and is not meant to be used in production. It is only for educational purposes.
Also note that this project uses the Jalali date format for the date picker.
