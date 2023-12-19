# Capstone Project Model ML Deployment
[CH2-PS230] Bangkit Academy 2023 Batch 2 Product Capstone.

## Getting Started

-   ### Setup Google Cloud

    Create a new Google Cloud project or use an existing project.

    Enable Cloud Run API and Cloud Build API.

-   ### Clone the repository

    Activate Cloud Shell and clone the repository.

    ```
    git clone https://github.com/Capstone-Bansos-Bangkit/model-deployment.git
    ```

-   ### Navigate to the project directory

    ```
    cd model-deployment
    ```

-   ### Build image and push it to the Container Registry.
    ```
    gcloud builds submit --tag gcr.io/[project_id]/[image_name]
    ```

## Deployment

-   ### Deploy to Cloud Run

    ```
    gcloud run deploy --image gcr.io/[project_id]/[image_name] --platform managed
    ```

    Wait a few moments until the deployment is complete. If the deployment is successful, the Cloud Shell line will display the service URL.

## API Documentation
-   Endpoint: GET `/`

    This endpoint will return success to make sure that the service is running properly.

-   Endpoint: POST `/`

    Parameters:
    - AR16 : user answer.
    - KR03 : user answer.
    - KR11 : user answer.
    - KR13 : user answer.
    - KR20 : user answer.
    - KR24 : user answer.
    - KR26 : user answer.
    - KRK06 : user answer.
    - KRK08 : user answer.
    - KRK09 : user answer.
    - KRK10 : user answer.

    This endpoint accepts requests in JSON format and returns a result of `1` or `0`. The representative is 1: approved and 0: rejected.
    
    Example:
    ```
    {
        "AR16": 1,
        "KR03": 0, 
        "KR11": 1,
        "KR13": 1, 
        "KR20": 3,
        "KR24": 3,
        "KR26": 3,
        "KRK06": 1,
        "KRK08": 0,
        "KRK09": 2,
        "KRK10": 1
    }
    ```

    Result:
    ```
    {
        "result": 1
    }
    ```
        
    


