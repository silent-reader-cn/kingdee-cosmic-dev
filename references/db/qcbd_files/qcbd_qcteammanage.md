# QC小组-qcbd_qcteammanage

## QC小组-使用范围位图表 t_qcbd_qcteam_m

- **表名称：** QC小组-使用范围位图表
- **表名：** t_qcbd_qcteam_m

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
| 1 | pk_t_qcbd_qcteam_m |  | forgid |

---

## QC小组-多语言表 t_qcbd_qcteam_l

- **表名称：** QC小组-多语言表
- **表名：** t_qcbd_qcteam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_qcteam_l |  | fpkid |
| 2 | idx_qcbd_qcteaml_fid |  | fid,flocaleid |
| 3 | idx_qcbd_qcteaml_fname |  | fname |

---

## QC小组-使用范围表 t_qcbd_qcteam_u

- **表名称：** QC小组-使用范围表
- **表名：** t_qcbd_qcteam_u

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
| 1 | pk_t_qcbd_qcteam_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_qcteam_u_uo |  | fuseorgid |

---

## QC小组-主表 t_qcbd_qcteam

- **表名称：** QC小组-主表
- **表名：** t_qcbd_qcteam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fregistdate | 注册日期 | timestamp | 0 |  |  | null | 注册日期 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcuturalcontent | 小组文化 | varchar | 2000 |  | √ | ' ' | 小组文化 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fteambadge | 小组徽章 | varchar | 255 |  | √ | ' ' | 小组徽章 |
| 11 | fgrpdesc | 小组描述 | varchar | 512 |  | √ | ' ' | 小组描述 |
| 12 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 15 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_qcteam |  | fid |
| 2 | idx_t_qcbd_qcteam_master |  | fmasterid |
| 3 | idx_qcbd_qcteam_fcreatetime |  | fcreatetime |
| 4 | idx_qcbd_qcteam_fnumber |  | fnumber |
| 5 | idx_t_qcbd_qcteam_createorg |  | fcreateorgid |

---

## 小组成员-子表 t_qcbd_qcteamuser

- **表名称：** 小组成员-子表
- **表名：** t_qcbd_qcteamuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fperfduty | 履行职责 | varchar | 1000 |  | √ | ' ' | 履行职责 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fuserid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fispersonfail | 人员失效 | bpchar | 1 |  | √ | '0' | 人员失效 |
| 7 | froleval | 角色 | varchar | 255 |  | √ | ' ' | 角色 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_qcteamuser |  | fentryid |
| 2 | idx_qcbd_qcteer_fseq |  | fseq |
| 3 | idx_qcbd_qcteer_fid |  | fid |
