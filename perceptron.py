import sys

FEATURES = 5
THRESHOLD = 0.5

def activation(x):
    if x > THRESHOLD:
        return 1
    else:
        return 0

def load_weights(filename):
    weights = []
    bias = 0.0
    try:
        with open(filename, 'r') as file:
            for i in range(FEATURES):
                line = file.readline()
                if not line:
                    break

                weights.append(float(line.split(':')[1].strip()))
            
            line = file.readline()
            if line:
                bias = float(line.split(':')[1].strip())
            
            return True, weights, bias
    except Exception:
        print(f"Error: file {filename} non found!")
        return False, None, None

def predict(weights, bias, input_data):
    sum_bias = bias
    for i in range(FEATURES):
        sum_bias += input_data[i] * weights[i]
    return activation(sum_bias)

def main():
    success, weights, bias = load_weights("weights.txt")
    if not success:
        sys.exit(1)

    print("Insert your input:")
    input_data = [0] * FEATURES
    
    input_data[0] = int(input("Famous artist? (1=Yes, 0=No): "))
    input_data[1] = int(input("Good weather? (1=Yes, 0=No): "))
    input_data[2] = int(input("Friends? (1=Yes, 0=No): "))
    input_data[3] = int(input("Good food? (1=Yes, 0=No): "))
    input_data[4] = int(input("Alcool? (1=Yes, 0=No): "))

    decision = predict(weights, bias, input_data)

    if decision:
        print("\n?? You go to the concert!")
    else:
        print("\n?? Stay at home!")

if __name__ == "__main__":
    main()