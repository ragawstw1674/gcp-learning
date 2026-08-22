resource "google_bigquery_dataset" "test_dataset" {
  dataset_id                  = "test_dataset"
  description                 = "Dataset for learning"
  location                    = "asia-south2"
}

resource "google_bigquery_table" "test_table" {
  dataset_id = google_bigquery_dataset.test_dataset.dataset_id
  table_id   = "test"
  schema = <<EOF
[
  {
    "name": "name",
    "type": "STRING"
  }
]
EOF
}