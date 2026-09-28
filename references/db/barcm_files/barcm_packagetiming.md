# 包装时机-barcm_packagetiming

## 混装校验条件-多语言表 t_barcm_packagetentry_l

- **表名称：** 混装校验条件-多语言表
- **表名：** t_barcm_packagetentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulfieldentryname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 2 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packagetentry_l |  | fpkid |
| 2 | idx_barcm_packtimee_fidflcid |  | fentryid,flocaleid |

---

## 包装时机-主表 t_barcm_packagetiming

- **表名称：** 包装时机-主表
- **表名：** t_barcm_packagetiming

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fbillqtyfieldcode | 计划数量字段编码 | varchar | 255 |  | √ | ' ' | 计划数量字段编码 |
| 9 | fsourcedataid | 原资料ID | int8 | 64 |  | √ | 0 | 原资料ID |
| 10 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 11 | fbillqtyfieldentry | fbillqtyfieldentry | varchar | 255 |  | √ | ' ' |  |
| 12 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fmainbizentitymark | 主业务实体标识 | varchar | 255 |  | √ | ' ' | 主业务实体标识 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fsrcbizbillld | 来源业务单据 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fmulbillqtyfieldname | 计划数量字段名称 | varchar | 255 |  | √ | ' ' | 计划数量字段名称 |
| 22 | fsyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fbizobjwhiteid | 条码业务对象 | int8 | 64 |  | √ | 0 | 条码业务对象白名单 barcm_bizobjwhitelist |
| 25 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_barcm_packagetiming_createorg |  | fcreateorgid |
| 2 | idx_t_barcm_packagetiming_master |  | fmasterid |
| 3 | pk_barcm_packtime |  | fid |
| 4 | idx_barcm_packtime_number |  | fnumber |

---

## 混装校验条件-子表 t_barcm_packagetentry

- **表名称：** 混装校验条件-子表
- **表名：** t_barcm_packagetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldcode | 匹配字段 | varchar | 255 |  | √ | ' ' | 匹配字段 |
| 3 | fentrysyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 4 | fmulfieldentryname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 6 | ffieldentryname | 字段实体名 | varchar | 255 |  | √ | ' ' | 字段实体名 |
| 7 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packtimeentry |  | fentryid |
| 2 | idx_barcm_packtimeentry_fid |  | fid |

---

## 包装时机-多语言表 t_barcm_packagetiming_l

- **表名称：** 包装时机-多语言表
- **表名：** t_barcm_packagetiming_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmulbillqtyfieldname | 计划数量字段名称 | varchar | 255 |  | √ | ' ' | 计划数量字段名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packtime_l |  | fpkid |
| 2 | idx_barcm_packtime_l_fidfld |  | fid,flocaleid |

---

## 包装时机-使用范围表 t_barcm_packagetiming_u

- **表名称：** 包装时机-使用范围表
- **表名：** t_barcm_packagetiming_u

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
| 1 | idx_t_barcm_packagetiming_u_uo |  | fuseorgid |
| 2 | pk_t_barcm_packagetiming_u |  | fdataid,fuseorgid |
