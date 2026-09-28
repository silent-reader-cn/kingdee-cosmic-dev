# 结息计划方案-cfm_inscheme

## 结息计划方案-多语言表 t_cfm_inscheme_l

- **表名称：** 结息计划方案-多语言表
- **表名：** t_cfm_inscheme_l

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
| 1 | t_cfm_inscheme_l_pkey |  | fpkid |
| 2 | idx_t_cfm_inscheme_l |  | fid,flocaleid |

---

## 结息计划方案-主表 t_cfm_inscheme

- **表名称：** 结息计划方案-主表
- **表名：** t_cfm_inscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fintereststmh | 结息月 | varchar | 30 |  | √ | ' ' | 结息月 |
| 5 | fdescrible | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdrawmonthsettle | 提款当月结息 | bpchar | 1 |  | √ | '0' | 提款当月结息 |
| 9 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fintereststpd | 结息周期 | varchar | 30 |  | √ | ' ' | 结息周期,枚举: year :年 halfyear :半年 quarter :季 month :月 toyear :对年 toquarter :对季 tomonth :对月 endinterest :到期一次性结息 custom :自定义结息日 |
| 13 | fintereststday | 结息日 | varchar | 30 |  | √ | ' ' | 结息日 |
| 14 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | foffetday | 偏移天数 | int4 | 32 |  | √ | 0 | 偏移天数 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_inscheme_se |  | fstatus,fenable |
| 2 | t_cfm_inscheme_pkey |  | fid |
