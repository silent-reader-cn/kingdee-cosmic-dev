# 寻源流程-pbd_sourceflow

## 寻源流程-主表 t_pds_flowconfig

- **表名称：** 寻源流程-主表
- **表名：** t_pds_flowconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissupplier | fissupplier | bpchar | 1 |  | √ | '0' |  |
| 3 | fismanualscore | fismanualscore | bpchar | 1 |  | √ | '0' |  |
| 4 | fminisuppliers | fminisuppliers | int4 | 32 |  | √ | 0 |  |
| 5 | fpriority | fpriority | int4 | 32 |  | √ | 0 |  |
| 6 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 7 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 8 | fisnegotiable | fisnegotiable | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmatchfield | fmatchfield | int4 | 32 |  | √ | 0 |  |
| 12 | fisneedbiddoc | fisneedbiddoc | bpchar | 1 |  | √ | '0' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | finvitenodeid | finvitenodeid | int8 | 64 |  | √ | 0 |  |
| 16 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 17 | fisneednotice | fisneednotice | bpchar | 1 |  | √ | '0' |  |
| 18 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 20 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 21 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | '1' |  |
| 22 | fisdecisionresult | fisdecisionresult | bpchar | 1 |  | √ | '0' |  |
| 23 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fchassistypeid | fchassistypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fisauditscore | fisauditscore | bpchar | 1 |  | √ | '0' |  |
| 29 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 30 | ftendency | ftendency | varchar | 50 |  | √ | ' ' |  |
| 31 | fdescription | fdescription | varchar | 510 |  | √ | ' ' |  |
| 32 | fbiddoc | fbiddoc | varchar | 30 |  | √ | ' ' |  |
| 33 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 34 | fischgmaterial | fischgmaterial | bpchar | 1 |  | √ | '0' |  |
| 35 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 寻源方式 pbd_sourcetype |
| 36 | fissourcesupplier | fissourcesupplier | bpchar | 1 |  | √ | '0' |  |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | '0' |  |
| 40 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |
| 41 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
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
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

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
