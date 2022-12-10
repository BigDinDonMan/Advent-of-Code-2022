# frozen_string_literal: true

CYCLES_MAP = {
    'addx' => 2,
    'noop' => 1
}.freeze

CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220].freeze

def get_op_data(line)
    data = line.strip.split(' ')
    [data[0], data.length > 1 ? data[1].to_i : 0]
end

def part1(lines)
    register, current_cycle = 1, 1
    res_arr = []
    lines.each do |line|
        op, value = get_op_data(line)
        cycles = CYCLES_MAP[op]
        (0...cycles).each do |c|
            res_arr << register * current_cycle if CYCLES_TO_CHECK.include?(current_cycle)
            current_cycle += 1
        end
        register += value
    end

    p "Result: #{res_arr.sum}"
end

def part2(lines)
    crt_width, crt_height = 40, 6
    sprite_pos, sprite_width = 0, 3
    rows, current_cycle = [], 0
    result = +''
    lines.each do |line|
        op, value = get_op_data(line)
        cycles = CYCLES_MAP[op]
        (0...cycles).each do |c|
            result << (((sprite_pos...(sprite_pos+sprite_width)).member?(current_cycle)) ? '#' : '.')
            current_cycle += 1
        end
        sprite_pos += value
        current_cycle = current_cycle % 40
        sprite_pos = sprite_pos % 40
    end
    cycles = [0, 40, 80, 120, 160, 200, 240]
    rows = []
    cycles[0...(cycles.length - 1)].each.with_index do |num, index|
        rows << result[(cycles[index]...cycles[index+1])]
    end
    rows.each { |r| p r }
end

lines = File.readlines('input.txt')

part1(lines)
part2(lines)