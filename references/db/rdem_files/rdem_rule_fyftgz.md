# 费用分摊规则-rdem_rule_fyftgz

## 费用分摊规则-使用范围表 t_rdem_rule_fyftgz_u

- **表名称：** 费用分摊规则-使用范围表
- **表名：** t_rdem_rule_fyftgz_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rdem_rule_fyftgz_u |  | fdataid,fuseorgid |
| 2 | idx_t_rdem_rule_fyftgz_u_uo |  | fuseorgid |

---

## 费用分摊规则-主表 t_rdem_rule_fyftgz

- **表名称：** 费用分摊规则-主表
- **表名：** t_rdem_rule_fyftgz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 5 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型 |
| 9 | fpurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: jjkc :加计扣除 gqrd :高新认定 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 规则编号 | varchar | 30 |  | √ | ' ' | 规则编号 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rule_fyftgz_m0 |  | fmasterid |
| 2 | pk_rdem_rule_fyftgz |  | fid |
| 3 | idx_t_rdem_rule_fyftgz_createorg |  | fcreateorgid |
| 4 | idx_t_rdem_rule_fyftgz_master |  | fmasterid |

---

## 费用分摊规则-多语言表 t_rdem_rule_fyftgz_l

- **表名称：** 费用分摊规则-多语言表
- **表名：** t_rdem_rule_fyftgz_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rule_fyftgz_l_0 |  | fid,flocaleid |
| 2 | pk_rdem_rule_fyftgz_l |  | fpkid |

---

## 费用分摊规则-子表 t_rdem_rule_fyftgz_entry

- **表名称：** 费用分摊规则-子表
- **表名：** t_rdem_rule_fyftgz_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffconditionjson | 过滤条件 | varchar | 50 |  | √ | ' ' | 过滤条件 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fshareratio | 分摊比例 | varchar | 200 |  | √ | ' ' | 分摊比例 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 rdem_datasource_entry](../rdem_files/rdem_datasource_entry.md) |
| 5 | fshareresult | 分摊结果 | varchar | 200 |  | √ | ' ' | 分摊结果 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgroupdime | 分组维度 | varchar | 50 |  | √ | ' ' | 分组维度,枚举: taxorg :税务组织 costcenter :成本中心 staffnumber :人员工号 |
| 8 | fsharetype | 分摊类型 | int8 | 64 |  | √ | 0 | [分摊类型 rdem_share_type](../rdem_files/rdem_share_type.md) |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '1' | 绝对值 |
| 11 | ffiltercondition | 参与分摊数据范围 | varchar | 2000 |  | √ | ' ' | 参与分摊数据范围 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_fyftgz_entry |  | fentryid |
| 2 | idx_rdem_rule_fyftgz_entry_fk |  | fid |
