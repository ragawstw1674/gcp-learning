resource "google_service_account" "cloud_run_sa" {
  account_id   = "cloud-run-sa"
  display_name = "Cloud Run Service Account"
}

resource "google_project_iam_member" "view_data_role_binding" {
  project = data.google_client_config.current.project
  role    = "roles/bigquery.dataViewer" 
  member  = google_service_account.cloud_run_sa.member
}

resource "google_project_iam_member" "query_execution_role_binding" {
  project =  data.google_client_config.current.project
  role    = "roles/bigquery.jobUser" 
  member  = google_service_account.cloud_run_sa.member
}