cd source
bash total_sim.sh \
    ../outputs/qwen25-05-base \
    Qwen/Qwen2.5-Coder-0.5B \
    qwen25-05-base \
    0 \
    0.9
bash total_pass.sh \
    ../outputs/qwen25-05-base \
    Qwen/Qwen2.5-Coder-0.5B \
    qwen25-05-base \
    0 \
    0.9
cd ..