# Use a lightweight Python image
FROM python:3.11-slim

##############
# Install uv #
##############

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

###################
# Install project #
###################

# Copy project files
ADD . /app

# Set the working directory inside the container
WORKDIR /app

# Install dependencies using uv
RUN uv sync --frozen

# Copy the rest of the application files
COPY . /app

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["uv", "run", "python", "main.py"]
