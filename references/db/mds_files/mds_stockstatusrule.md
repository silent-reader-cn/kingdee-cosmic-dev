# 备货状态规则-mds_stockstatusrule

## 备货状态规则-使用范围表 t_mds_stockstatusrule_u

- **表名称：** 备货状态规则-使用范围表
- **表名：** t_mds_stockstatusrule_u

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
| 1 | pk_t_mds_stockstatusrule_u |  | fdataid,fuseorgid |
| 2 | idx_t_mds_stockstatusrule_u_uo |  | fuseorgid |

---

## 备货状态规则-多语言表 t_mds_stockstatusrule_l

- **表名称：** 备货状态规则-多语言表
- **表名：** t_mds_stockstatusrule_l

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
| 1 | pk_mds_stockstatusrule_l |  | fpkid |
| 2 | idx_mds_stockstatusrule_l_id |  | fid,flocaleid |

---

## 备货状态规则-使用范围位图表 t_mds_stockstatusrule_m

- **表名称：** 备货状态规则-使用范围位图表
- **表名：** t_mds_stockstatusrule_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_stockstatusrule_m |  | forgid |

---

## 调整范围-多选基础资料表 t_mds_ruleset_range

- **表名称：** 调整范围-多选基础资料表
- **表名：** t_mds_ruleset_range

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_ruleset_range_eid |  | fentryid |
| 2 | pk_mds_ruleset_range |  | fpkid |

---

## 备货状态规则-主表 t_mds_stockstatusrule

- **表名称：** 备货状态规则-主表
- **表名：** t_mds_stockstatusrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftargetentity | 目标实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftargetstatus | 目标状态 | varchar | 5 |  | √ | ' ' | 目标状态,枚举: 0 :按BOM备货状态 1 :按历史用量备货状态 2 :按客户需求备货状态 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_stockstatusrule_master |  | fmasterid |
| 2 | idx_t_mds_stockstatusrule_createorg |  | fcreateorgid |
| 3 | pk_mds_stockstatusrule |  | fid |
| 4 | idx_mds_stockstatusrule_no |  | fnumber |

---

## 单据体-子表 t_mds_rulesetentity

- **表名称：** 单据体-子表
- **表名：** t_mds_rulesetentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatus | 备货状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 3 | fmatchelement | 匹配要素 | varchar | 255 |  | √ | ' ' | 匹配要素,枚举: 0 :客户编码 1 :检修设备类型 2 :检修级别 3 :客舱构型 4 :资源计划状态 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fallowadjust | 允许手工调整 | bpchar | 1 |  | √ | '0' | 允许手工调整 |
| 6 | ffilterconditionval | 过滤条件值(后台) | text | 0 |  |  | null | 过滤条件值(后台) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_rulesetentity |  | fentryid |
| 2 | idx_mds_rulesetentity_id |  | fid |
