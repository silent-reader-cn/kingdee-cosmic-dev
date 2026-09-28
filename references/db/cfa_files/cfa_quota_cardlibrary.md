# 指标卡片库-cfa_quota_cardlibrary

## 指标卡片库-主表 t_cfa_quota_cardlibrary

- **表名称：** 指标卡片库-主表
- **表名：** t_cfa_quota_cardlibrary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyoydecreasedifference | 显示增减差值（同比） | bpchar | 1 |  | √ | '0' | 显示增减差值（同比） |
| 3 | frelativeny | 相对年初 | bpchar | 1 |  | √ | '0' | 相对年初 |
| 4 | ftargetdecreaseratio | 显示增减比例(%)（目标） | bpchar | 1 |  | √ | '0' | 显示增减比例(%)（目标） |
| 5 | fcardlistyle | 卡片样式 | varchar | 50 |  | √ | ' ' | 卡片样式,枚举: 0 :简洁样式 1 :紧凑样式 |
| 6 | fyoy | 同比 | bpchar | 1 |  | √ | '0' | 同比 |
| 7 | ftarget | 目标 | bpchar | 1 |  | √ | '0' | 目标 |
| 8 | frelativenyname | 相对年初名称 | varchar | 50 |  | √ | ' ' | 相对年初名称 |
| 9 | fcurrentperiodquota | 本期指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frelativenydecreasediffer | 显示增减差值（相对年初） | bpchar | 1 |  | √ | '0' | 显示增减差值（相对年初） |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fqoqname | 环比名词 | varchar | 50 |  | √ | ' ' | 环比名词 |
| 16 | frelativenydecreaseratio | 显示增减比例(%)（相对年初） | bpchar | 1 |  | √ | '0' | 显示增减比例(%)（相对年初） |
| 17 | fyoyname | 同比名称 | varchar | 50 |  | √ | ' ' | 同比名称 |
| 18 | fqoq | 环比 | bpchar | 1 |  | √ | '0' | 环比 |
| 19 | fyoydecreaseratio | 显示增减比例(%)（同比） | bpchar | 1 |  | √ | '0' | 显示增减比例(%)（同比） |
| 20 | fshowredfont | 负数以红色字体显示 | bpchar | 1 |  | √ | '0' | 负数以红色字体显示 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | ftargetdecreasedifference | 显示增减差值（目标） | bpchar | 1 |  | √ | '0' | 显示增减差值（目标） |
| 24 | fcurrentyearquota | 本年指标 | int8 | 64 |  | √ | 0 | [指标库 ipo_quota_info](../ipobase_files/ipo_quota_info.md) |
| 25 | ftargetname | 目标名称 | varchar | 50 |  | √ | ' ' | 目标名称 |
| 26 | fqoqdecreaseratio | 显示增减比例(%)（环比） | bpchar | 1 |  | √ | '0' | 显示增减比例(%)（环比） |
| 27 | fqoqdecreasedifference | 显示增减差值（环比） | bpchar | 1 |  | √ | '0' | 显示增减差值（环比） |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 卡片编码 | varchar | 30 |  | √ | ' ' | 卡片编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_quota_cardlibrary |  | fid |
| 2 | index_cfa_quota_cardlibraryi |  | fnumber |

---

## 指标卡片库-多语言表 t_cfa_quota_cardlibrary_l

- **表名称：** 指标卡片库-多语言表
- **表名：** t_cfa_quota_cardlibrary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 卡片名称 | varchar | 50 |  | √ | ' ' | 卡片名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfa_quota_cardlibrary_l_0 |  | fid |
| 2 | pk_cfa_quota_cardlibrary_l |  | fpkid |
