# 关联项-plm_ipdsm_itemrealtion

## 关联项-多语言表 t_plm_ipdsm_itemrealtion_l

- **表名称：** 关联项-多语言表
- **表名：** t_plm_ipdsm_itemrealtion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdsm_itemrealtion_l_0 |  | fid,flocaleid |
| 2 | pk_plm_ipdsm_itemrealtion_l |  | fpkid |

---

## 关联项-多语言表 t_plm_ipdsm_itemr_entry_l

- **表名称：** 关联项-多语言表
- **表名：** t_plm_ipdsm_itemr_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fext_field49 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 2 | fext_field1 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 3 | fext_field48 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 4 | fext_field47 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 5 | fext_field46 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 6 | fext_field4 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 7 | fext_field5 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 8 | fext_field2 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 9 | fext_field3 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 10 | fext_field41 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 11 | fext_field40 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 12 | fext_field45 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 13 | fext_field44 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 14 | fext_field43 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 15 | fext_field42 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 16 | fext_field38 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 17 | fext_field37 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 18 | fext_field36 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 19 | fext_field35 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 20 | fext_field39 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 21 | fext_field30 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 22 | fext_field | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 23 | fext_field34 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fext_field33 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 26 | fext_field32 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 27 | fext_field31 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 28 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 29 | fext_field27 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 30 | fext_field26 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 31 | fext_field25 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 32 | fext_field24 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 33 | fext_field29 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 34 | fext_field28 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 35 | fext_field23 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 36 | fext_field22 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 37 | fext_field21 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 38 | fext_field20 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 39 | fext_field8 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 40 | fext_field9 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 41 | fext_field6 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 42 | fext_field7 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 43 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 44 | fext_field16 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 45 | fext_field15 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 46 | fext_field14 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 47 | fext_field13 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 48 | fext_field19 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 49 | fext_field18 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 50 | fext_field17 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 51 | fext_field50 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 52 | fext_field12 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 53 | fext_field11 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 54 | fext_field10 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_itemr_entry_l |  | fpkid |
| 2 | idx_plm_ipdsm_itemr_entry_l_0 |  | fentryid,flocaleid |

---

## 关联项-子表 t_plm_ipdsm_itemr_entry

- **表名称：** 关联项-子表
- **表名：** t_plm_ipdsm_itemr_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fresultsubmitter | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fext_field49 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 5 | fext_field48 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 6 | fext_field1 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 7 | fext_field47 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 8 | fext_field46 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 9 | fext_field4 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 10 | fext_field5 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 11 | fext_field2 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 12 | flcstatus | 状态 | int8 | 64 |  | √ | 0 | 状态 plm_ipd_lc_status |
| 13 | fext_field3 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 14 | fext_field41 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 15 | fext_field40 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 16 | fpicturefield | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 17 | fext_field45 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 18 | fext_field44 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 19 | fext_field43 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 20 | fext_field42 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 21 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 22 | fext_field38 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 23 | fext_field37 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 24 | fext_field36 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 25 | fext_field35 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 26 | fitemgroup | 工作项类型 | int8 | 64 |  | √ | 0 | 工作项类型配置 plm_ipditemgroup |
| 27 | fext_field39 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 28 | fext_field30 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 29 | fext_field | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 30 | fext_field34 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 31 | fext_field33 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fext_field32 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 34 | fext_field31 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 35 | fext_field27 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 36 | fext_field26 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 37 | fext_field25 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 38 | fext_field24 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 39 | fext_field29 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 40 | fext_field28 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 41 | fext_field23 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 42 | fext_field22 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 43 | fext_field21 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 44 | fext_field20 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 45 | fdeliverable | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 46 | fext_field8 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 47 | fext_field9 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 48 | fext_field6 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 49 | fext_field7 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 50 | fachievementmodel | 类型 | int8 | 64 |  | √ | 0 | 关联项类型配置 plm_ipdsm_fc_model |
| 51 | fext_field16 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 52 | fext_field15 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 53 | fext_field14 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 54 | fext_field13 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 55 | fdeliverablenumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 56 | fext_field19 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 57 | fext_field18 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 58 | fresultcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 59 | fext_field17 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 60 | fdeliverableid | 数据ID | varchar | 50 |  | √ | ' ' | 数据ID |
| 61 | fext_field50 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 62 | fext_field12 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 63 | fext_field11 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 64 | fext_field10 | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdsm_itemr_entry_fk |  | fid |
| 2 | pk_plm_ipdsm_itemr_entry |  | fentryid |

---

## 关联项-主表 t_plm_ipdsm_itemrealtion

- **表名称：** 关联项-主表
- **表名：** t_plm_ipdsm_itemrealtion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fseten_enbale | 控制单据体字段锁定 | varchar | 50 |  | √ | ' ' | 控制单据体字段锁定,枚举: A :A B :B |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | ftype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: A :工作项 B :交付物 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbelongitem | 所属关联对象 | varchar | 50 |  | √ | ' ' | 所属关联对象 |
| 12 | fbelongtype | 关联项类型编码 | varchar | 50 |  | √ | ' ' | 关联项类型编码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdsm_itemrealtion_m0 |  | fmasterid |
| 2 | pk_plm_ipdsm_itemrealtion |  | fid |
