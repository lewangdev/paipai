#coding=utf8


button_pos = {
        "raise":(),
        "bid":(),
        "bid_confirm":(),
        "bid_cancel":()}

input_pos = {
        "custom_delta":(),
        "custom_price":(),
        "check_code":()}



# 汉字 width
hw=14

# 汉字 height
hh=12

# margin bottom
mb=3

# 正常数字宽度
nw=7

# 粗体数字宽度
bw=8

capture_width= 19 * bw
capture_offset = (39, 206)
capture_pos_offset = dict(
        plate_limit=(6 * hw + nw, hh + mb),
        participant_count=(7 * hw + nw, 2 * (hh + mb)),
        system_time=(6 * hw + nw, 8 * (hh + mb)),
        price_accepted=(8 * hw + nw, 9 * (hh + mb)),
        time_price_accepted=(10 * hw + nw, 10 * (hh + mb)))


if __name__ == '__main__':
    capture_pos = {}
    w,h = capture_offset
    for k,v in capture_pos_offset.items():
        ow,oh = v
        capture_pos[k] = (w + ow, h + oh)
    print capture_pos
