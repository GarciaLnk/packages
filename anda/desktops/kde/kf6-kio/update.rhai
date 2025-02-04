let v = gitlab_tag("invent.kde.org", "2729");
v.crop(1);
let nums = v.split(".");
let majmin = nums[0] + "." + nums[1];
rpm.global("majmin_ver_kf6", majmin);
