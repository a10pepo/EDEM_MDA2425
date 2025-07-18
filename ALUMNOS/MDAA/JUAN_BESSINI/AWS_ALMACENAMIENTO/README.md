# End-to-End Data Engineering Project on AWS

## Description
This project demonstrates a simple data pipeline on AWS. It allows you to register airplanes, flights, and passengers, and then store this data in AWS RDS, Redshift, or an S3-based data lake using Apache Iceberg.

## How to Run the Application

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up AWS Credentials**:
    Make sure you have your AWS credentials configured. You can do this by setting the following environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
    export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
    export AWS_SESSION_TOKEN=YOUR_SESSION_TOKEN # (If you are using temporary credentials)
    export AWS_REGION=YOUR_AWS_REGION
    ```

3.  **Set up Database Credentials**:
    This application uses a `.env` file to store database credentials. Create a file named `.env` in the root of the project and add the following variables:
    ```
    RDS_HOST=your_rds_host
    RDS_PORT=your_rds_port
    RDS_USER=your_rds_user
    RDS_PASSWORD=your_rds_password
    RDS_DB=your_rds_db

    REDSHIFT_HOST=your_redshift_host
    REDSHIFT_PORT=your_redshift_port
    REDSHIFT_USER=your_redshift_user
    REDSHIFT_PASSWORD=your_redshift_password
    REDSHIFT_DB=your_redshift_db
    ```

4.  **Run the Application**:
    You can run the application from the command line. You need to specify the `--type` argument, which can be `rds` or `iceberg`.

    *   **To use RDS and Redshift**:
        ```bash
        python main.py --type rds
        ```
    *   **To use Iceberg**:
        ```bash
        python main.py --type iceberg
        ```
