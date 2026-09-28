# 条码规则属性项-barcm_barcoderuleprop

## 条码规则属性项-多语言表 t_barcm_bcruleprop_l

- **表名称：** 条码规则属性项-多语言表
- **表名：** t_barcm_bcruleprop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcruleprop_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_bcruleprop_l |  | fpkid |

---

## 关联业务对象单据体-多语言表 t_barcm_bcrulepropentry_l

- **表名称：** 关联业务对象单据体-多语言表
- **表名：** t_barcm_bcrulepropentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 2 | fmulbofieldname | 业务对象字段多语言 | varchar | 255 |  | √ | ' ' | 业务对象字段多语言 |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcruleporentry_l |  | fpkid |
| 2 | idx_barcm_bcrpropel_fidflcid |  | fentryid,flocaleid |

---

## 关联业务对象单据体-子表 t_barcm_bcrulepropentry

- **表名称：** 关联业务对象单据体-子表
- **表名：** t_barcm_bcrulepropentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体标识 | varchar | 80 |  | √ | ' ' | 实体标识 |
| 3 | fmulbofieldname | 业务对象字段多语言 | varchar | 255 |  | √ | ' ' | 业务对象字段多语言 |
| 4 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fboid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fbofieldsign | 业务对象字段 | varchar | 255 |  | √ | ' ' | 业务对象字段 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fispresetentry | 系统预置(表体) | bpchar | 1 |  | √ | '0' | 系统预置(表体) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcrpropentry_fid |  | fid |
| 2 | pk_barcm_bcrulepropentry |  | fentryid |

---

## 条码规则属性项-主表 t_barcm_bcruleprop

- **表名称：** 条码规则属性项-主表
- **表名：** t_barcm_bcruleprop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsndimensionid | 序列号维度 | int8 | 64 |  | √ | 0 | 序列号维度 bd_sndimension |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsuitentitytype | 适用单据体类型 | bpchar | 1 |  | √ | ' ' | 适用单据体类型,枚举: A :不区分 B :仅单据体 C :仅子单据体 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmapparsepropid | 对应解析属性项 | int8 | 64 |  | √ | 0 | 条码规则属性项 barcm_barcoderuleprop |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 17 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ffieldname | 标识名 | varchar | 80 |  | √ | ' ' | 标识名 |
| 21 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 22 | fpurpose | 用途 | bpchar | 1 |  | √ | ' ' | 用途,枚举: A :通用 B :生成目标单 C :生码与解析 |
| 23 | fpropertytypeid | 属性类型 | int8 | 64 |  | √ | 0 | 条码属性类型 barcm_barcodeproptype |
| 24 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 25 | fmapbasedataid | 对应基础资料 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fcustompadlock | 设置PDA锁定性 | bpchar | 1 |  | √ | '0' | 设置PDA锁定性 |
| 28 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 29 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_barcm_bcruleprop_createorg |  | fcreateorgid |
| 2 | idx_t_barcm_bcruleprop_master |  | fmasterid |
| 3 | pk_barcm_bcruleprop |  | fid |
| 4 | idx_barcm_bcruleprop_number |  | fnumber |

---

## 条码规则属性项-使用范围表 t_barcm_bcruleprop_u

- **表名称：** 条码规则属性项-使用范围表
- **表名：** t_barcm_bcruleprop_u

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
| 1 | idx_t_barcm_bcruleprop_u_uo |  | fuseorgid |
| 2 | pk_t_barcm_bcruleprop_u |  | fdataid,fuseorgid |
