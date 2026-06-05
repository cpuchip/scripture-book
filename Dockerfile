# Multi-stage Dockerfile to build "Beyond the Prompt" scripture book PDF with Typst

# Stage 1: Generate Typst source and QR code SVGs using Python
FROM python:3.11-slim AS builder

WORKDIR /app

# Install required python library for QR codes
RUN pip install --no-cache-dir qrcode

# Copy scripture book repository contents
COPY . .

# Build version stamp for the frontmatter (passed from build.ps1 via --build-arg,
# since git is not available inside this image).
ARG BUILD_VERSION="uncommitted build"
ENV BUILD_VERSION=$BUILD_VERSION

# Compile markdown chapters to Typst source code
RUN python scripts/build_typst.py

# Stage 2: Compile Typst source to PDF using official Typst compiler
FROM ghcr.io/typst/typst:latest AS compiler

WORKDIR /app

# Copy the template and generated assets from Builder stage
COPY --from=builder /app/dist /app/dist

# Compile the Typst source into a premium print-ready PDF
RUN typst compile dist/book.typ dist/manuscript.pdf

# Stage 3: Minimal runtime image to export output back to host filesystem
FROM alpine:latest

WORKDIR /app

# Copy compiled PDF and images from Compiler stage
COPY --from=compiler /app/dist /app/dist

# Default command to copy build outputs to the mounted volume
CMD ["sh", "-c", "mkdir -p /output && cp -rf /app/dist/* /output/ && echo 'Book PDF compilation complete! Output copied to dist/.'"]
