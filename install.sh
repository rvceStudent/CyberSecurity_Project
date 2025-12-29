sudo cp deployment/firewall.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable firewall
sudo systemctl start firewall
