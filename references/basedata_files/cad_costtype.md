# 标准成本方案-cad_costtype

## 标准成本方案-主表 t_cad_costtype

- **表名称：** 标准成本方案-主表
- **表名：** t_cad_costtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | felementtypeid | 成本要素分类 | int8 | 64 |  | √ | 0 | 成本要素分类 cad_elementtype |
| 6 | fradiogroupfield | fradiogroupfield | varchar | 30 |  | √ | ' ' |  |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fisupdate | 允许更新 | bpchar | 1 |  | √ | '0' | 允许更新 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fuorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fisuseversion | 卷算不按物料版本计算 | bpchar | 1 |  | √ | '0' | 卷算不按物料版本计算 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :自由分配 5 :全局共享 7 :私有 1 :逐级分配 6 :管控范围内共享 |
| 21 | fexpirationdatetime | fexpirationdatetime | timestamp | 0 |  |  | null |  |
| 22 | ftype | 标准成本属性 | varchar | 30 |  | √ | ' ' | 标准成本属性,枚举: 0 :核算成本 1 :模拟成本 |
| 23 | fradiogroupfield2 | fradiogroupfield2 | varchar | 30 |  | √ | ' ' |  |
| 24 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fsupattr | fsupattr | bpchar | 1 |  | √ | '0' |  |
| 26 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 27 | fradiogroupfield1 | fradiogroupfield1 | varchar | 30 |  | √ | ' ' |  |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_costtype_pkey |  | fid |
| 2 | idx_t_cad_costtype_createorg |  | fcreateorgid |
| 3 | idx_t_cad_costtype_master |  | fmasterid |

---

## 标准成本方案-使用范围表 t_cad_costtype_u

- **表名称：** 标准成本方案-使用范围表
- **表名：** t_cad_costtype_u

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
| 1 | t_cad_costtype_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_cad_costtype_u_uo |  | fuseorgid |

---

## 标准成本方案-多语言表 t_cad_costtype_l

- **表名称：** 标准成本方案-多语言表
- **表名：** t_cad_costtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_costtype_l_pkey |  | fpkid |

---

## 标准成本方案-使用范围位图表 t_cad_costtype_m

- **表名称：** 标准成本方案-使用范围位图表
- **表名：** t_cad_costtype_m

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
| 1 | pk_t_cad_costtype_m |  | forgid |
