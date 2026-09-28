# 条码打印模板分类-barcm_bcprinttplclass

## 条码打印模板分类-使用范围表 t_barcm_bcprinttplclass_u

- **表名称：** 条码打印模板分类-使用范围表
- **表名：** t_barcm_bcprinttplclass_u

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
| 1 | pk_t_barcm_bcprinttplclass_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_bcprinttplclass_u_uo |  | fuseorgid |

---

## 条码打印模板分类-多语言表 t_barcm_bcprinttplclass_l

- **表名称：** 条码打印模板分类-多语言表
- **表名：** t_barcm_bcprinttplclass_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 512 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_bcprinttplclass_l |  | fpkid |
| 2 | idx_barcm_bcptc_fidflid |  | fid,flocaleid |

---

## 条码打印模板分类-主表 t_barcm_bcprinttplclass

- **表名称：** 条码打印模板分类-主表
- **表名：** t_barcm_bcprinttplclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | forgid | 管理组织 | int8 | 64 |  |  | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | [条码打印模板分类 barcm_bcprinttplclass](../barcm_files/barcm_bcprinttplclass.md) |
| 18 | ffullname | ffullname | varchar | 512 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ffieldname | ffieldname | varchar | 80 |  | √ | ' ' |  |
| 21 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 22 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 23 | fpropertytypeid | fpropertytypeid | int8 | 64 |  | √ | 0 |  |
| 24 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 25 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 26 | fmapbasedataid | fmapbasedataid | varchar | 255 |  | √ | ' ' |  |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 29 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcptc_number |  | fnumber |
| 2 | idx_t_barcm_bcprinttplclass_master |  | fmasterid |
| 3 | idx_t_barcm_bcprinttplclass_createorg |  | fcreateorgid |
| 4 | pk_t_barcm_bcprinttplclass |  | fid |
