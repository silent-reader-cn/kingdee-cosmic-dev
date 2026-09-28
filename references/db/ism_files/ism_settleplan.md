# 组织间结算方案配置（废弃）-ism_settleplan

## 组织间结算方案配置（废弃）-主表 t_ism_settleplan

- **表名称：** 组织间结算方案配置（废弃）-主表
- **表名：** t_ism_settleplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsettlepricingtimepoint | 结算价取价时点： | varchar | 20 |  | √ | 'billauditdate' | 结算价取价时点：,枚举: billauditdate :单据审核日期 billbusinessdate :单据业务日期 querycutoffdate :查询截止日期 cursysydate :当前系统日期 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbillgenerate | 应收应付单据生成： | bpchar | 1 |  | √ | '0' | 应收应付单据生成： |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 11 | fisdefault | 默认方案 | bpchar | 1 |  | √ | '0' | 默认方案 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_settleplan_pkey |  | fid |
| 2 | idx_ism_stp_fno |  | fnumber |

---

## 组织间结算方案配置（废弃）-多语言表 t_ism_settleplan_l

- **表名称：** 组织间结算方案配置（废弃）-多语言表
- **表名：** t_ism_settleplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_settleplan_l_pkey |  | fpkid |
| 2 | idx_ism_stp_l_fid |  | fid,flocaleid |

---

## 结算单据范围-子表 t_ism_settlebillrange

- **表名称：** 结算单据范围-子表
- **表名：** t_ism_settlebillrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fbilltype | 单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_settlebillrange_pkey |  | fentryid |
| 2 | idx_ism_str_fid |  | fid |
