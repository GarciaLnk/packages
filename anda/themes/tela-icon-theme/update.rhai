let release = gh("vinceliuice/Tela-icon-theme");
rpm.global("tag", release);
rpm.version(sub("-", "", release));
