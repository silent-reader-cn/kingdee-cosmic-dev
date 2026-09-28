# 脱敏规则-privacy_desen_rules

## 脱敏规则-主表 t_privacy_desen_rules

- **表名称：** 脱敏规则-主表
- **表名：** t_privacy_desen_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmatchrules | 匹配规则 | varchar | 200 |  | √ | ' ' | 匹配规则 |
| 3 | fname | 脱敏规则名称 | varchar | 50 |  | √ | ' ' | 脱敏规则名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fruletype | 规则类型 | bpchar | 1 |  | √ | ' ' | 规则类型,枚举: 0 :正则表达式 1 :插件 |
| 7 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 8 | fdescription | 脱敏规则描述 | varchar | 500 |  | √ | ' ' | 脱敏规则描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 13 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | frange | 适用范围 | varchar | 200 |  | √ | ' ' | 适用范围,枚举: all :通用 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 16 | fnumber | 脱敏规则编码 | varchar | 50 |  | √ | ' ' | 脱敏规则编码 |
| 17 | freplacement | 替换规则 | varchar | 100 |  | √ | ' ' | 替换规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_privacy_desen_rule_fname |  | fname |
| 2 | pk_t_privacy_desen_rules |  | fid |
| 3 | idx_privacy_desen_rule_fnumber |  | fnumber |

---

## 脱敏规则-多语言表 t_privacy_desen_rules_l

- **表名称：** 脱敏规则-多语言表
- **表名：** t_privacy_desen_rules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 脱敏规则名称 | varchar | 255 |  | √ | ' ' | 脱敏规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 脱敏规则描述 | varchar | 1000 |  |  | null | 脱敏规则描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_privacy_desen_rules_l |  | fpkid |
| 2 | idx_privacy_desen_rules_l_fid |  | fid,flocaleid |
