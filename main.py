workers = {
    1: {"name": "Crissy", "position": "Data engineer", "salary": 6500},
    2: {"name": "Simon", "position": "Data analyst", "salary": 7500},
    3: {"name": "Markus", "position": "Project manager", "salary": 9000},
    4: {"name": "Peter", "position": "Director", "salary": 12000},
    5: {"name": "John", "position": "HR manager", "salary": 7500},
    6: {"name": "Ashe", "position": "Scrum master", "salary": 7000}
}


def calculate_pay_raise(workers):
    for worker_id, worker_data in workers.items():
        worker_data["salary"] *= 1.5
    return workers


if __name__ == "__main__":
    workers = calculate_pay_raise(workers)
    for worker_id, worker_data in workers.items():
        print(f"Worker {worker_id}: {worker_data}")
