<?php
$csv_url = 'http://localhost:80/ducks/csv'; // URL of the CSV export route

// Use cURL to get the CSV file
$ch = curl_init($csv_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$data = curl_exec($ch);

if ($data === false) {
    die('Error fetching CSV: ' . curl_error($ch));
}

curl_close($ch);

// Set headers for file download
header('Content-Type: text/csv');
header('Content-Disposition: attachment; filename="ducks.csv"');
echo $data;
?>