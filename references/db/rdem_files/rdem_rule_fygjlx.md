# 研发费用归集规则-rdem_rule_fygjlx

## 研发费用归集规则-多语言表 t_rdem_rule_fygjlx_l

- **表名称：** 研发费用归集规则-多语言表
- **表名：** t_rdem_rule_fygjlx_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_fygjlx_l |  | fpkid |
| 2 | idx_rdem_rule_fygjlx_l_0 |  | fid,flocaleid |

---

## 研发费用归集规则-主表 t_rdem_rule_fygjlx

- **表名称：** 研发费用归集规则-主表
- **表名：** t_rdem_rule_fygjlx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型 |
| 9 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcollecttype | 映射项目对象 | varchar | 50 |  | √ | ' ' | 映射项目对象,枚举: costcenter :成本中心 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_fygjlx |  | fid |
| 2 | idx_rdem_rule_fygjlx_m0 |  | fmasterid |

---

## 取数规则-子表 t_rdem_rule_fygjlx_entry

- **表名称：** 取数规则-子表
- **表名：** t_rdem_rule_fygjlx_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 rdem_datasource_entry](../rdem_files/rdem_datasource_entry.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 研发费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |
| 6 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 none :按项目 |
| 7 | fjsbl | 系数 | numeric | 23 | 10 | √ | 0 | 系数 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 9 | fbaseondepr | 以会计折旧为计税基础 | bpchar | 1 |  | √ | '0' | 以会计折旧为计税基础 |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '1' | 绝对值 |
| 11 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rule_fygjlx_entry_fk |  | fid |
| 2 | pk_rdem_rule_fygjlx_entry |  | fentryid |
