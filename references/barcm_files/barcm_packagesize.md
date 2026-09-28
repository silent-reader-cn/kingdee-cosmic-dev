# 包装规格-barcm_packagesize

## 包装规格-主表 t_barcm_packsize

- **表名称：** 包装规格-主表
- **表名：** t_barcm_packsize

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpackagelevel | 包装层级 | bpchar | 1 |  | √ | ' ' | 包装层级,枚举: A :2 B :3 C :4 D :5 |
| 4 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmixedload | 是否混装 | bpchar | 1 |  | √ | ' ' | 是否混装 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 18 | fsourcedataid | 原资料ID | int8 | 64 |  | √ | 0 | 原资料ID |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packsize |  | fid |
| 2 | idx_barcm_packsize_number |  | fnumber |
| 3 | idx_t_barcm_packsize_master |  | fmasterid |
| 4 | idx_t_barcm_packsize_createorg |  | fcreateorgid |

---

## 包装规格明细-多语言表 t_barcm_psdetail_l

- **表名称：** 包装规格明细-多语言表
- **表名：** t_barcm_psdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flevelremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_psdetail_l |  | fpkid |
| 2 | idx_barcm_psdetail_l_feidfld |  | fentryid,flocaleid |

---

## 包装规格明细-子表 t_barcm_psdetail

- **表名称：** 包装规格明细-子表
- **表名：** t_barcm_psdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 层级 | int4 | 32 |  | √ | 1 | 层级 |
| 3 | fcontainerprinttplid | 容器打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 4 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :物料 B :容器 |
| 5 | flevelremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fpackcontainertypeid | 包装容器类型 | int8 | 64 |  | √ | 0 | 包装容器类型 barcm_containertype_m |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcontainerbcruleid | 容器条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fnextlevelqty | 下级数量 | int4 | 32 |  | √ | 1 | 下级数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_psdetail |  | fentryid |
| 2 | idx_barcm_psdetail_fid |  | fid |

---

## 包装规格-使用范围表 t_barcm_packsize_u

- **表名称：** 包装规格-使用范围表
- **表名：** t_barcm_packsize_u

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
| 1 | idx_t_barcm_packsize_u_uo |  | fuseorgid |
| 2 | pk_t_barcm_packsize_u |  | fdataid,fuseorgid |

---

## 包装规格-多语言表 t_barcm_packsize_l

- **表名称：** 包装规格-多语言表
- **表名：** t_barcm_packsize_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packsize_l |  | fpkid |
| 2 | idx_barcm_packsize_l_fidfld |  | fid,flocaleid |
