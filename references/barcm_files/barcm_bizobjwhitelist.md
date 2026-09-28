# 条码业务对象白名单-barcm_bizobjwhitelist

## 条码业务对象白名单-使用范围表 t_barcm_bizobjwl_u

- **表名称：** 条码业务对象白名单-使用范围表
- **表名：** t_barcm_bizobjwl_u

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
| 1 | pk_t_barcm_bizobjwl_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_bizobjwl_u_uo |  | fuseorgid |

---

## 条码业务对象白名单-多语言表 t_barcm_bizobjwl_l

- **表名称：** 条码业务对象白名单-多语言表
- **表名：** t_barcm_bizobjwl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmainbizentityname | 主业务实体名称 | varchar | 50 |  | √ | ' ' | 主业务实体名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bizobjwl_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_bizobjwl_l |  | fpkid |

---

## 条码业务对象白名单-主表 t_barcm_bizobjwl

- **表名称：** 条码业务对象白名单-主表
- **表名：** t_barcm_bizobjwl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisallowgenbc | 允许生成条码 | bpchar | 1 |  | √ | ' ' | 允许生成条码 |
| 8 | fmainbizentitymark | 主业务实体标识 | varchar | 50 |  | √ | ' ' | 主业务实体标识 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbillname | 单据名称 | varchar | 80 |  | √ | ' ' | 单据名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 14 | fmainbizentityname | 主业务实体名称 | varchar | 50 |  | √ | ' ' | 主业务实体名称 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fbizobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 20 | fissystem | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 21 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 24 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bizobjwl |  | fid |
| 2 | idx_t_barcm_bizobjwl_master |  | fmasterid |
| 3 | idx_barcm_bizobjwl_number |  | fnumber |
| 4 | idx_t_barcm_bizobjwl_createorg |  | fcreateorgid |
