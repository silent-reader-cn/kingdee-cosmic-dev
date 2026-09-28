# 格式-barcm_barcodeformat

## 格式-主表 t_barcm_barcodeformat

- **表名称：** 格式-主表
- **表名：** t_barcm_barcodeformat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fformattype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :数字 B :文本 C :日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 17 | fexample | 示例 | varchar | 255 |  | √ | ' ' | 示例 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 20 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_barcm_barcodeformat_master |  | fmasterid |
| 2 | idx_barcm_bcformat_number |  | fnumber |
| 3 | idx_t_barcm_barcodeformat_createorg |  | fcreateorgid |
| 4 | pk_barcm_barcodeformat |  | fid |

---

## 格式-使用范围表 t_barcm_barcodeformat_u

- **表名称：** 格式-使用范围表
- **表名：** t_barcm_barcodeformat_u

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
| 1 | pk_t_barcm_barcodeformat_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_barcodeformat_u_uo |  | fuseorgid |

---

## 格式-多语言表 t_barcm_barcodeformat_l

- **表名称：** 格式-多语言表
- **表名：** t_barcm_barcodeformat_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fexample | 示例 | varchar | 255 |  | √ | ' ' | 示例 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 512 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_barcodeformat_l |  | fpkid |
| 2 | idx_barcm_bcformt_fidflid |  | fid,flocaleid |
