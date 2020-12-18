import sys

def parse_to_active_cubes(message):
    active_cubes: set(tuple(int,int,int,int)) = set()
    lines: List[str] = message.splitlines()
    line: str
    y_coord: int = -1
    for line in lines:
        y_coord += 1
        x_coord: int = -1
        c: str
        for c in line:
            x_coord += 1
            if c == '.':
                continue
            active_cubes.add((x_coord, y_coord, 0, 0))
    return active_cubes

#def find_bounds(active_cubes: set(tuple[int,int,int])):
def find_bounds(active_cubes: set):
    absmax: int = sys.maxsize
    absmin: int = -sys.maxsize - 1
    x_range: tuple(int,int) = (absmax, absmin)
    y_range: tuple(int,int) = (absmax, absmin)
    z_range: tuple(int,int) = (absmax, absmin)
    w_range: tuple(int,int) = (absmax, absmin)
    cube: tuple(int,int,int)
    for cube in active_cubes:
        x_range = (min(x_range[0],cube[0]), max(x_range[1],cube[0]))
        y_range = (min(y_range[0],cube[1]), max(y_range[1],cube[1]))
        z_range = (min(z_range[0],cube[2]), max(z_range[1],cube[2]))
        w_range = (min(w_range[0],cube[3]), max(w_range[1],cube[3]))
    return {
        'x': x_range,
        'y': y_range,
        'z': z_range,
        'w': z_range,
    }

def grow_bounds(bounds):
    return {
        'x': (bounds['x'][0]-1, bounds['x'][1]+1),
        'y': (bounds['y'][0]-1, bounds['y'][1]+1),
        'z': (bounds['z'][0]-1, bounds['z'][1]+1),
        'w': (bounds['w'][0]-1, bounds['w'][1]+1),
    }

def process_cycle(active_cubes):
    new_active_cubes = set()
    bounds: map = find_bounds(active_cubes)
    bounds: map = grow_bounds(bounds)
    def capture_new_cube_state(x, y, z, w):
        cube = (x,y,z,w)
        is_active = cube in active_cubes
        active_adjacent = count_adjacent_active(active_cubes, (x,y,z,w))
        if is_active and (active_adjacent == 2 or active_adjacent == 3):
            new_active_cubes.add(cube)
        elif (not is_active) and active_adjacent == 3:
            new_active_cubes.add(cube)
    for_each_cube_in_bounds(bounds, capture_new_cube_state)
    return new_active_cubes


def process_6_cycles(active_cubes):
    for i in range(0, 6):
        active_cubes = process_cycle(active_cubes)
    return active_cubes


def for_each_cube_in_bounds(bounds, do_something):
    for x in range(bounds['x'][0],bounds['x'][1]+1):
        for y in range(bounds['y'][0],bounds['y'][1]+1):
            for z in range(bounds['z'][0],bounds['z'][1]+1):
                for w in range(bounds['w'][0],bounds['w'][1]+1):
                    do_something(x,y,z,w)

def count_adjacent_active(active_cubes, target_cube):
    adjacent_bounds = {
        'x': (target_cube[0]-1, target_cube[0]+1),
        'y': (target_cube[1]-1, target_cube[1]+1),
        'z': (target_cube[2]-1, target_cube[2]+1),
        'w': (target_cube[3]-1, target_cube[3]+1),
    }
    active_count = 0
    def count_if_active(x, y, z, w):
        nonlocal target_cube
        nonlocal active_count
        cube = (x,y,z,w)
        # Skip reference to itself
        if cube == target_cube:
            return
        if cube in active_cubes:
            active_count += 1
    for_each_cube_in_bounds(adjacent_bounds, count_if_active)
    return active_count

