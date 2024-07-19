import psutil
import csv
import time

import threading

def log_network_usage(netLog="network_usage_log.csv", interval=0.25):
    with open(netLog, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header only if the file is new or empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Upload Spead (Mbps)", "Download Speed (Mbps)", "Total Upload (MB)", "Total Download (MB)"])

        timer = 0
        totalBytesSent = 0
        totalBytesRecv = 0

        while True:
            # Grab current bytes sent and received
            netIO= psutil.net_io_counters()
            bytesSent, bytesRecv = netIO.bytes_sent, netIO.bytes_recv

            # Wait time interval amount of time
            time.sleep(interval)

            # Grab new bytes sent and received
            netIO = psutil.net_io_counters()
            bytesSentNew, bytesRecvNew = netIO.bytes_sent, netIO.bytes_recv

            # Retrieve the amount of bytes that are different from the previous interval step
            totalBytesSent += bytesSentNew - bytesSent
            totalBytesRecv += bytesRecvNew - bytesRecv

            # Track the change over time, i.e., the time interval
            sentSpeed = (bytesSentNew - bytesSent) / interval
            recvSpeed = (bytesRecvNew - bytesRecv) / interval

            # Convert speed to Mbps
            sentSpeedMbps = round(((sentSpeed * 8)/1000)/1024, 2)
            recvSpeedMbps = round(((recvSpeed * 8)/1000)/1024, 2)

            # Convert the total to MB
            totalSentMB = round((totalBytesSent / (1024 * 1024)), 2)
            totalRecvMB = round((totalBytesRecv / (1024 * 1024)), 2)

            timer += interval

            writer.writerow([timer, sentSpeedMbps, recvSpeedMbps, totalSentMB, totalRecvMB ])
            # print(f"Logged at {timestamp} - Upload Speed: {sent_speed / 1024:.2f} KB/s, Download Speed: {recv_speed / 1024:.2f} KB/s")
            file.flush()

def start_network_monitoring():
    thread = threading.Thread(target=log_network_usage)
    thread.daemon = True
    thread.start()