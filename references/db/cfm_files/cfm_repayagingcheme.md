# 还款计划方案-cfm_repayagingcheme

## 还款计划方案-主表 t_cfm_paymentbyinstalment

- **表名称：** 还款计划方案-主表
- **表名：** t_cfm_paymentbyinstalment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fdescrible | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdrawmonthsettle | 提款当月还款 | bpchar | 1 |  | √ | '0' | 提款当月还款 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | foffetday | 偏移天数 | int4 | 32 |  | √ | 0 | 偏移天数 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 17 | fperiod | 还款周期 | varchar | 30 |  | √ | ' ' | 还款周期,枚举: 1 :年 2 :半年 3 :季 4 :月 5 :对年 7 :对季 6 :对月 |
| 18 | fmonth | 还款月 | varchar | 30 |  | √ | ' ' | 还款月 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fday | 还款日 | varchar | 30 |  | √ | ' ' | 还款日 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_paymentbyinstalment_pkey |  | fid |
| 2 | idx_t_cfm_pbyinstalment_se |  | fstatus,fenable |

---

## 还款计划方案-多语言表 t_cfm_paymentbyinstalment_l

- **表名称：** 还款计划方案-多语言表
- **表名：** t_cfm_paymentbyinstalment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_pbyinstalment_l |  | fid,flocaleid |
| 2 | t_cfm_paymentbyinstalment_l_pkey |  | fpkid |
