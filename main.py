from collections import defaultdict


FILE_PATH = "sample.log"


def parse_time(time_str: str) -> int:
    fields = time_str.split(":")
    hour = int(fields[1])
    return hour


def increse_count(key: any, counter: dict):
    if key not in counter:
        counter[key] = [key, 0]
    counter[key][1] += 1


def get_top_frequent(counter: dict, k=10) -> list[list[str, int]]:
    sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    top_k_list = sorted_list[:k]
    return top_k_list


def show_frequency(field: str, sorted_list: list[list[any, int]]):
    print(f"most frequent in {field.upper()} field")
    print("-" * 100)
    for key, count in sorted_list:
        print(f"{key:<20}: {count}")
    print()


def main():
    ip_counter = defaultdict(int)
    request_counter = defaultdict(int)
    error_404_counter = 0
    log_time_counter = defaultdict(int)

    with open(FILE_PATH, mode="r") as file_log:
        for line in file_log:
            clean_line = line.strip()

            fields = clean_line.split(" ")
            ip = fields[0]
            time = parse_time(fields[1])
            request = fields[3]
            status_code = fields[5]

            ip_counter[ip] += 1
            request_counter[request] += 1
            log_time_counter[time] += 1
            error_404_counter = (
                error_404_counter + 1 if status_code == "404" else error_404_counter
            )

    sorted_ips_frequent = get_top_frequent(ip_counter)
    sorted_request_frequent = get_top_frequent(request_counter)
    sorted_log_time_frequent = get_top_frequent(log_time_counter, 1)

    show_frequency("ip", sorted_ips_frequent)
    show_frequency("request", sorted_request_frequent)
    show_frequency("log_time", sorted_log_time_frequent)

    print(f"Number of Error 404 occursion")
    print("-" * 100)
    print(f"error 404: {error_404_counter}")


if __name__ == "__main__":
    main()
