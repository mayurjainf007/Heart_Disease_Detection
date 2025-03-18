provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_compute_instance" "heart_disease_server" {
  name         = "heart-disease-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata_startup_script = <<EOT
    sudo apt update && sudo apt install -y docker.io git
    git clone https://github.com/your-username/heart-disease-prediction.git
    cd heart-disease-prediction && docker-compose up -d
  EOT
}
