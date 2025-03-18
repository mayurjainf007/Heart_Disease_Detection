provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "heart_disease_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  tags = {
    Name = "HeartDiseasePrediction"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install docker.io -y",
      "git clone https://github.com/your-username/heart-disease-prediction.git",
      "cd heart-disease-prediction && docker-compose up -d"
    ]
  }
}
