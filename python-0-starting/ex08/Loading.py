def get_progress_bar(progress: int):

    """
    get_progress_bar(progress: int) -> None

    get progress bar based on current index and width of console
    """

    return f"{'=' * (progress - 1)}>{' ' * (100 - progress)}"


def ft_tqdm(lst: range) -> None:

    """
    ft_tqdm(lst: range) -> None

    A fake tqdm
    """

    console_width = 100
    max_range = max(lst) - lst.start + 1
    step = max_range // 20   # display progress every 5%

    for i in range(max_range):
        if (i % step != 0):
            yield i
            continue
        # print percentage
        percentage = round(((i + 1) / max_range) * 100)
        print(f"{percentage:>{3}}%", end="")

        # print progress bar
        progress = round(((i + 1) * console_width) / max_range)
        progress_bar = get_progress_bar(progress)
        print(f"|[{progress_bar}]|", end="")

        # print curr/max
        print(f" {(i + 1)}/{max_range}", end="\r")
        yield i
    print(f"100%|[{get_progress_bar(100)}]| {max_range}/{max_range}")
