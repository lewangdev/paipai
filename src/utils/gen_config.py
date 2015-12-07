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
capture_offset = (32, 267)
capture_pos_offset = dict(
        plate_limit=(6 * hw + nw + 3, hh + mb),
        participant_count=(7 * hw + nw + 3, 2 * (hh + mb)),
        system_time=(6 * hw + nw + 3, 8 * (hh + mb) + 1),
        price_accepted=(8 * hw + nw + 2, 9 * (hh + mb) + 2),
        time_price_accepted=(10 * hw + nw, 10 * (hh + mb) + 2))


if __name__ == '__main__':
    capture_pos = {}
    w,h = capture_offset
    for k,v in capture_pos_offset.items():
        ow,oh = v
        capture_pos[k] = (w + ow, h + oh)
    print capture_pos
