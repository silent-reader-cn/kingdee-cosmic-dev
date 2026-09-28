# 检验仪器-qcbd_inspectioninstru

## 检验仪器-使用范围位图表 t_qcbd_inspectioninstru_m

- **表名称：** 检验仪器-使用范围位图表
- **表名：** t_qcbd_inspectioninstru_m

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
| 1 | pk_t_qcbd_inspectioninstru_m |  | forgid |

---

## 检验仪器-多语言表 t_qcbd_inspectioninstru_l

- **表名称：** 检验仪器-多语言表
- **表名：** t_qcbd_inspectioninstru_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_ispinstru_fid |  | fid,flocaleid |
| 2 | t_qcbd_inspectioninstru_l_pkey |  | fpkid |

---

## 检验仪器-使用范围表 t_qcbd_inspectioninstru_u

- **表名称：** 检验仪器-使用范围表
- **表名：** t_qcbd_inspectioninstru_u

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
| 1 | idx_t_qcbd_inspectioninstru_u_uo |  | fuseorgid |
| 2 | t_qcbd_inspectioninstru_u_pkey |  | fdataid,fuseorgid |

---

## 检验仪器-主表 t_qcbd_inspectioninstru

- **表名称：** 检验仪器-主表
- **表名：** t_qcbd_inspectioninstru

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 检验仪器分类 qcbd_inspectioninstrugrp |
| 3 | fmodel | 型号 | varchar | 50 |  | √ | ' ' | 型号 |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fspecification | 规格 | varchar | 50 |  | √ | ' ' | 规格 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fmanufacturer | 生产厂家 | varchar | 50 |  | √ | ' ' | 生产厂家 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcbd_inspectioninstru_pkey |  | fid |
| 2 | idx_t_qcbd_inspectioninstru_createorg |  | fcreateorgid |
| 3 | idx_t_qcbd_inspectioninstru_master |  | fmasterid |
| 4 | uidx_qcbd_inspectioninstru_billno |  | fnumber |
