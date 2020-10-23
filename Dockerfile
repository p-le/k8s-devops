FROM python 3.9-slim AS builder

FROM scratch
COPY --from=builder 
