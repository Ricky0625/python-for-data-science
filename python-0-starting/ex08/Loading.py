def ft_tqdm(lst: range) -> None:
    for i in lst:
        yield i
        progress = (i) / max(lst) * 100
        print(f"Progress: {progress:.2f}%")
    return None