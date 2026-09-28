# 检验项目-qcbd_inspectionitems

## 检验项目-主表 t_qcbd_inspectionitems

- **表名称：** 检验项目-主表
- **表名：** t_qcbd_inspectionitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckbasis | fcheckbasis | int8 | 64 |  | √ | 0 |  |
| 3 | fdetectiontype | 检测值类型 | varchar | 5 |  | √ | ' ' | 检测值类型,枚举: 1 :数值型 2 :文本型 3 :枚举型 |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 检验项目分类 qcbd_inspectionitemsgrp |
| 5 | fnormtype | 指标类型 | varchar | 5 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 6 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsourceentryid | 来源项目分录ID | int8 | 64 |  | √ | 0 | 来源项目分录ID |
| 9 | fhcheckcontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fradiogroupfield | 单选按钮组 | varchar | 30 |  | √ | ' ' | 单选按钮组,枚举: |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcheckinstruct | fcheckinstruct | int8 | 64 |  | √ | 0 |  |
| 17 | fhcheckbasis | 检验依据 | int8 | 64 |  | √ | 0 | 检验依据 qcbd_inspectioncrit |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 21 | fhcheckmethod | 检验方法 | int8 | 64 |  | √ | 0 | 检验方法 qcbd_inspectionmethod |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcheckmethod | fcheckmethod | int8 | 64 |  | √ | 0 |  |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 26 | fsplit | 是否已拆分 | bpchar | 1 |  | √ | '0' | 是否已拆分 |
| 27 | fhkeyquality | 关键项目 | bpchar | 1 |  | √ | '0' | 关键项目 |
| 28 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 32 | fspc | SPC | bpchar | 1 |  | √ | '0' | SPC |
| 33 | fsourceitemid | 来源项目ID | int8 | 64 |  | √ | 0 | 来源项目ID |
| 34 | fdetectionenum | 检测值枚举 | varchar | 255 |  | √ | ' ' | 检测值枚举 |
| 35 | fhcheckinstruct | 检验仪器 | int8 | 64 |  | √ | 0 | 检验仪器 qcbd_inspectioninstru |
| 36 | fhunit | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fitementryqty | 项目分录数 | int4 | 32 |  | √ | 0 | 项目分录数 |
| 39 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 40 | fradiogroupfield1 | 单选按钮组1 | varchar | 30 |  | √ | ' ' | 单选按钮组1,枚举: |
| 41 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcbd_inspectionitems_pkey |  | fid |
| 2 | idx_t_qcbd_inspectionitems_master |  | fmasterid |
| 3 | uidx_qcbd_inspectionitems_billno |  | fnumber |
| 4 | idx_t_qcbd_inspectionitems_createorg |  | fcreateorgid |

---

## 检验项目-使用范围位图表 t_qcbd_inspectionitems_m

- **表名称：** 检验项目-使用范围位图表
- **表名：** t_qcbd_inspectionitems_m

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
| 1 | pk_t_qcbd_inspectionitems_m |  | forgid |

---

## 检验项目-多语言表 t_qcbd_inspectionitems_l

- **表名称：** 检验项目-多语言表
- **表名：** t_qcbd_inspectionitems_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 510 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_ispitems_fid |  | fid,flocaleid |
| 2 | t_qcbd_inspectionitems_l_pkey |  | fpkid |

---

## 检验项目-使用范围表 t_qcbd_inspectionitems_u

- **表名称：** 检验项目-使用范围表
- **表名：** t_qcbd_inspectionitems_u

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
| 1 | t_qcbd_inspectionitems_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_inspectionitems_u_uo |  | fuseorgid |

---

## 单据体-子表 t_qcbd_inspecitems_entry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_inspecitems_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckmethod | 检验方法 | int8 | 64 |  | √ | 0 | 检验方法 qcbd_inspectionmethod |
| 3 | fcheckbasis | 检验依据 | int8 | 64 |  | √ | 0 | 检验依据 qcbd_inspectioncrit |
| 4 | funitld | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fdownvalue | fdownvalue | int8 | 64 |  | √ | 0 |  |
| 6 | fcheckcontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 7 | fnormtype | fnormtype | varchar | 50 |  | √ | ' ' |  |
| 8 | fspecvalue | fspecvalue | varchar | 50 |  | √ | ' ' |  |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | ftopvalue | ftopvalue | int8 | 64 |  | √ | 0 |  |
| 11 | fcheckinstruct | 检验仪器 | int8 | 64 |  | √ | 0 | 检验仪器 qcbd_inspectioninstru |
| 12 | fkeyquality | 关键特性 | varchar | 50 |  | √ | ' ' | 关键特性,枚举: A :是 B :否 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcheckstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :合格 B :不合格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcbd_inspecitems_entry_pkey |  | fentryid |
| 2 | idx_qcbd_ispitemsent_fnumber |  | fid |
