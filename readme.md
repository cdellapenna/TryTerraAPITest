This is a simple Flask application designed to listen for incoming POST requests on a specific endpoint ("/webhook-endpoint")

You must use ngrok expose our local environment to the public internet.

**Expose Your Localhost with ngrok:**
To expose your local server to the public internet, use ngrok. Follow the steps below to set it up:

1. **Download ngrok:**
   Visit https://ngrok.com/download and download the version suitable for your OS.

2. **Unzip ngrok:**
   Extract the downloaded file to get the ngrok executable.

3. **Run ngrok:**
   Open a new terminal/command prompt, navigate to the directory containing the ngrok executable, and run:

   ```
   ./ngrok http 5000
   ```

   If you're using Windows, you might omit `./`:

   ```
   ngrok http 5000
   ```

   Ensure that the getFreeStyleLibreData.py app and ngrok are running on the same port (5000 in this case).

4. **Get the ngrok URL:**
   Once ngrok is running, you will see a forwarding URL in the terminal (e.g., "https://your-ngrok-subdomain.ngrok.io"). Go to the Terra API dashboard and select "Connections." Add new source and select Freestyle Libre. For destination select webhook, and use the forwarding link displayed in the ngrok terminal with "/webhook-endpoint" inserted at the very end.

5. **Generate Data:**
   Under "Tools" on the Terra dashboard, generate Freestyle Libre Data and send to the webhook. The data should print in your python console
