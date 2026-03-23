cd source
bash total_sim.sh \
    ../outputs/qwen25-05-base \
    Qwen/Qwen2.5-Coder-0.5B \
    qwen25-05-base \
    0 \
    0.9
bash total_sim.sh \
    ../outputs/qwen25-15-base \
    Qwen/Qwen2.5-Coder-1.5B \
    qwen25-15-base \
    0 \
    0.9
bash total_sim.sh \
    ../outputs/qwen25-30-base \
    Qwen/Qwen2.5-Coder-3B \
    qwen25-30-base \
    0 \
    0.9
cd ..