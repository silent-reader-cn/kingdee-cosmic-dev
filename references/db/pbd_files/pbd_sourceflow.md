# 寻源流程-pbd_sourceflow

## 寻源流程-主表 t_pds_flowconfig

- **表名称：** 寻源流程-主表
- **表名：** t_pds_flowconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fishidden | fishidden | bpchar | 1 |  | √ | '0' |  |
| 3 | fissupplier | fissupplier | bpchar | 1 |  | √ | '0' |  |
| 4 | fismanualscore | fismanualscore | bpchar | 1 |  | √ | '0' |  |
| 5 | fminisuppliers | fminisuppliers | int4 | 32 |  | √ | 0 |  |
| 6 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 7 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 8 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 9 | fisnegotiable | fisnegotiable | bpchar | 1 |  | √ | '0' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmatchfield | fmatchfield | int4 | 32 |  | √ | 0 |  |
| 13 | fisneedbiddoc | fisneedbiddoc | bpchar | 1 |  | √ | '0' |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | finvitenodeid | finvitenodeid | int8 | 64 |  | √ | 0 |  |
| 17 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fisneednotice | fisneednotice | bpchar | 1 |  | √ | '0' |  |
| 19 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 20 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 21 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 22 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | '1' |  |
| 23 | fisdecisionresult | fisdecisionresult | bpchar | 1 |  | √ | '0' |  |
| 24 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fchassistypeid | fchassistypeid | int8 | 64 |  | √ | 0 |  |
| 29 | fisauditscore | fisauditscore | bpchar | 1 |  | √ | '0' |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | ftendency | ftendency | varchar | 50 |  | √ | ' ' |  |
| 32 | fdescription | fdescription | varchar | 510 |  | √ | ' ' |  |
| 33 | fbiddoc | fbiddoc | varchar | 30 |  | √ | ' ' |  |
| 34 | fsupcompareid | fsupcompareid | int8 | 64 |  | √ | 0 |  |
| 35 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 36 | fischgmaterial | fischgmaterial | bpchar | 1 |  | √ | '0' |  |
| 37 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [寻源方式 pbd_sourcetype](../pbd_files/pbd_sourcetype.md) |
| 38 | fissourcesupplier | fissourcesupplier | bpchar | 1 |  | √ | '0' |  |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 41 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | '0' |  |
| 42 | fquocompareid | fquocompareid | int8 | 64 |  | √ | 0 |  |
| 43 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |
| 44 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_flow_fnumber |  | fnumber |
| 2 | pk_pds_flowconfig |  | fid |
| 3 | idx_pds_flow_masterid |  | fmasterid |
| 4 | idx_pds_flow_fsource |  | fsourceclassid |
| 5 | idx_pds_flow_fcreatetime |  | fcreatetime |
| 6 | idx_pds_flow_fsourcetype |  | fsourcetypeid |
| 7 | idx_pds_flow_fpurdeptid |  | fpurdeptid |

---

## 业务类型-多选基础资料表 t_pds_flow_biztype

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_pds_flow_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pds_flow_biztype_fid |  | fid |
| 2 | pk_pds_flow_biztype |  | fpkid |
| 3 | idx_t_pds_flow_biztype_bid |  | fbasedataid |

---

## 寻源流程-多语言表 t_pds_flowconfig_l

- **表名称：** 寻源流程-多语言表
- **表名：** t_pds_flowconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 1020 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_srctype_l_fid |  | fid,flocaleid |
| 2 | pk_pds_flowconfig_l |  | fpkid |
| 3 | idx_pds_srctype_l_fname |  | fname |
