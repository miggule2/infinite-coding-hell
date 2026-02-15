import random
import os
import sys
from PNUhash import PNUhash

HM = 100000000
MASK64 = 0xFFFFFFFFFFFFFFFF
UINT64_C1 = 0xbf58476d1ce4e5b9
UINT64_C2 = 0x94d049bb133111eb

def digits(n: int, length: int):
    s = f"{n:0{length}d}"
    return [int(ch) for ch in s]

def make_gift_code(K: int, salt: int) -> str:
    d = digits(K, 12)
    H = digits(PNUhash(K, salt), 8)
    
    code_digits = [
        H[0], H[1],
        d[0], d[1], d[2], d[3],
        H[2], H[3],
        d[4], d[5], d[6], d[7],
        H[4], H[5],
        d[8], d[9], d[10], d[11],
        H[6], H[7]
    ]
    return "".join(str(x) for x in code_digits)

def extract_K_from_code(code: str) -> int:
    k_str = code[2:6] + code[8:12] + code[14:18]
    return int(k_str)

def is_valid(code: str, salt: int) -> bool:
    if len(code) != 20: return False
    try:
        K = extract_K_from_code(code)
        H_target = digits(PNUhash(K, salt), 8)
        return (int(code[0]) == H_target[0] and int(code[1]) == H_target[1] and
                int(code[6]) == H_target[2] and int(code[7]) == H_target[3] and
                int(code[12]) == H_target[4] and int(code[13]) == H_target[5] and
                int(code[18]) == H_target[6] and int(code[19]) == H_target[7])
    except:
        return False

def classify_codes(codes, salt):
    seen_valid = set()
    valid = 0; invalid = 0; used = 0
    for code in codes:
        if is_valid(code, salt):
            if code in seen_valid:
                used += 1
            else:
                valid += 1; seen_valid.add(code)
        else:
            invalid += 1
    return valid, invalid, used

def make_valid_codes(count, salt):
    codes = []
    used_K = set()
    while len(codes) < count:
        K = random.randrange(10**12)
        if K in used_K: continue
        used_K.add(K)
        codes.append(make_gift_code(K, salt))
    return codes

def make_invalid_codes(count, salt, existing_codes):
    codes = []
    while len(codes) < count:
        if random.random() < 0.3:
            digit_len = random.randint(1, 18)
            temp_num = random.randrange(10**digit_len)
        else:
            temp_num = random.randrange(10**20)
            
        code = f"{temp_num:020d}"
        
        if code in existing_codes: continue
        if not is_valid(code, salt):
            existing_codes.add(code)
            codes.append(code)
    return codes

def generate_file(folder, idx, N, salt):
    valid_ratio = random.uniform(0.55, 0.65)
    used_ratio = random.uniform(0.05, 0.15)
    
    valid_target = int(N * valid_ratio)
    used_target = int(N * used_ratio)
    
    if valid_target < 1: valid_target = 1
    
    invalid_target = N - valid_target - used_target
    
    if invalid_target < 0:
        valid_target += invalid_target 
        invalid_target = 0

    valid_codes = make_valid_codes(valid_target, salt)
    
    all_codes_set = set(valid_codes)
    invalid_codes = make_invalid_codes(invalid_target, salt, all_codes_set)
    
    used_codes = [random.choice(valid_codes) for _ in range(used_target)]
    
    final_codes = valid_codes + invalid_codes + used_codes
    random.shuffle(final_codes)
    
    v, i, u = classify_codes(final_codes, salt)
    
    filename = f"{idx:02d}"
    inp_path = os.path.join(folder, f"{filename}.inp")
    with open(inp_path, "w") as f:
        f.write(f"{N} {salt}\n")
        for code in final_codes:
            f.write(code + "\n")
            
    out_path = os.path.join(folder, f"{filename}.out")
    with open(out_path, "w") as f:
        f.write(f"{v}\n{i}\n{u}\n")

def main():
    random.seed(20251207) 
    
    if not os.path.exists("Sample"): os.makedirs("Sample")
    if not os.path.exists("Evaluation"): os.makedirs("Evaluation")

    sample_Ns = [10, 20, 50, 1000, 10000]
    sample_salts = [7, 13, 23, 41, 59]
    for idx, (N, salt) in enumerate(zip(sample_Ns, sample_salts), 1):
        generate_file("Sample", idx, N, salt)

    eval_Ns = [
        10000, 20000, 40000, 60000, 80000, 
        100000, 130000, 160000, 200000, 250000,
        300000, 330000, 360000, 390000, 420000, 450000
    ]
    eval_Ns = eval_Ns[-15:]
    eval_salts = [random.randint(10, 99) for _ in range(15)]

    for idx, (N, salt) in enumerate(zip(eval_Ns, eval_salts), 1):
        generate_file("Evaluation", idx, N, salt)

if __name__ == "__main__":
    main()