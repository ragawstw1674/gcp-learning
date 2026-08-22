resource "google_cloud_run_v2_service" "bigquery" {
  depends_on = [
    google_bigquery_table.test_table
  ]
  name     = "bigquery-sample-api"
  location =  "asia-south2"
  ingress  = "INGRESS_TRAFFIC_ALL"
  template {
    service_account = google_service_account.cloud_run_sa.email
    scaling {
        max_instance_count = 1
    }
    containers {
      image = "asia-south2-docker.pkg.dev/project-9fea4311-98eb-450f-b3b/myapp/bigquery-sample-api:v1"
      env {
        name = "BILLING_PROJECT_ID"
        value = data.google_client_config.current.project
      }
      env {
        name = "DATA_PROJECT_ID"
        value = data.google_client_config.current.project
      }
      env {
        name = "DATASET_NAME"
        value = "test_dataset"
      }
      env {
        name = "TABLE_NAME"
        value = "test"
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public_access" {
  project  = google_cloud_run_v2_service.bigquery.project
  location = google_cloud_run_v2_service.bigquery.location
  name     = google_cloud_run_v2_service.bigquery.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
