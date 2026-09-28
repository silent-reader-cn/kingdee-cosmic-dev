# 高新费用归集规则-rdem_high_tech_collrule

## 高新费用归集规则-多语言表 t_rdem_rule_gqgjlx_l

- **表名称：** 高新费用归集规则-多语言表
- **表名：** t_rdem_rule_gqgjlx_l

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
| 1 | pk_rdem_rule_gqgjlx_l |  | fpkid |
| 2 | idx_rdem_rule_gqgjlx_l_0 |  | fid,flocaleid |

---

## 高新费用归集规则-主表 t_rdem_rule_gqgjlx

- **表名称：** 高新费用归集规则-主表
- **表名：** t_rdem_rule_gqgjlx

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
| 9 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcollecttype | 映射项目对象 | varchar | 50 |  | √ | ' ' | 映射项目对象,枚举: costcenter :成本中心 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 17 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 规则编号 | varchar | 30 |  | √ | ' ' | 规则编号 |
| 20 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rdem_rule_gqgjlx_master |  | fmasterid |
| 2 | pk_rdem_rule_gqgjlx |  | fid |
| 3 | idx_t_rdem_rule_gqgjlx_createorg |  | fcreateorgid |
| 4 | idx_rdem_rule_gqgjlx_m0 |  | fmasterid |

---

## 取数规则-子表 t_rdem_rule_gxgjlx_entry

- **表名称：** 取数规则-子表
- **表名：** t_rdem_rule_gxgjlx_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 rdem_datasource_entry](../rdem_files/rdem_datasource_entry.md) |
| 4 | fjsbl | 系数 | numeric | 23 | 10 | √ | 0 | 系数 |
| 5 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 6 | fbaseondepr | 以会计折旧为计税基础 | bpchar | 1 |  | √ | '0' | 以会计折旧为计税基础 |
| 7 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '1' | 绝对值 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |
| 12 | fcosttype | 高新费用类别 | int8 | 64 |  | √ | 0 | [高新费用类别 rdem_high_tech_costtype](../rdem_files/rdem_high_tech_costtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_gxgjlx_entry |  | fentryid |
| 2 | idx_rdem_rule_gxgjlx_entry_fk |  | fid |
