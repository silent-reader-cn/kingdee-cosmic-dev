# 宽严度转换方案-qcbd_widstrict_rule

## 宽严度转换方案-使用范围位图表 t_qcbd_wdstct_rule_m

- **表名称：** 宽严度转换方案-使用范围位图表
- **表名：** t_qcbd_wdstct_rule_m

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
| 1 | pk_t_qcbd_wdstct_rule_m |  | forgid |

---

## 宽严度转换方案-多语言表 t_qcbd_wdstct_rule_l

- **表名称：** 宽严度转换方案-多语言表
- **表名：** t_qcbd_wdstct_rule_l

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
| 1 | idx_qcbd_wsl_rule_fname |  | fname |
| 2 | pk_qcbd_wdstct_rule_l |  | fpkid |
| 3 | idx_qcbd_wsl_rule_fid |  | fid,flocaleid |

---

## 宽严度转换方案-使用范围表 t_qcbd_wdstct_rule_u

- **表名称：** 宽严度转换方案-使用范围表
- **表名：** t_qcbd_wdstct_rule_u

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
| 1 | idx_t_qcbd_wdstct_rule_u_uo |  | fuseorgid |
| 2 | pk_t_qcbd_wdstct_rule_u |  | fdataid,fuseorgid |

---

## 转换规则-子表 t_qcbd_wdstct_rle

- **表名称：** 转换规则-子表
- **表名：** t_qcbd_wdstct_rle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstarttage | 起始检验阶段 | bpchar | 1 |  | √ | '0' | 起始检验阶段 |
| 3 | fcontacceptnum | 连续检验批数 | int4 | 32 |  | √ | 0 | 连续检验批数 |
| 4 | frejectvaliddt | frejectvaliddt | int4 | 32 |  | √ | 0 |  |
| 5 | fcontinspectnum | 连续检验批数 | int4 | 32 |  | √ | 0 | 连续检验批数 |
| 6 | fnextstageid | 下批检验阶段 | int8 | 64 |  | √ | 0 | 宽严度阶段 qcbd_widstrict_stage |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frstartcondition | 启动“下批检验阶段”的条件 | varchar | 255 |  | √ | ' ' | 启动“下批检验阶段”的条件 |
| 9 | frejectnum | 不接受批数 | int4 | 32 |  | √ | 0 | 不接受批数 |
| 10 | frnextstageid | 下批检验阶段 | int8 | 64 |  | √ | 0 | 宽严度阶段 qcbd_widstrict_stage |
| 11 | fsapplanid | 抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 12 | fcurrentstageid | 当前检验阶段 | int8 | 64 |  | √ | 0 | 宽严度阶段 qcbd_widstrict_stage |
| 13 | fstartcondition | 启动“下批检验阶段”的条件 | varchar | 255 |  | √ | ' ' | 启动“下批检验阶段”的条件 |
| 14 | facceptvaliddt | 批数有效期(天) | int4 | 32 |  | √ | 0 | 批数有效期(天) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_wdstct_fid |  | fid |
| 2 | pk_qcbd_wdstct_rle |  | fentryid |
| 3 | idx_qcbd_wdstct_fseq |  | fseq |

---

## 宽严度转换方案-主表 t_qcbd_wdstct_rule

- **表名称：** 宽严度转换方案-主表
- **表名：** t_qcbd_wdstct_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 12 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fresetprd | 重置周期(天) | int4 | 32 |  | √ | 0 | 重置周期(天) |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_wdstct_rule |  | fid |
| 2 | idx_qcbd_ws_rule_fcreatetime |  | fcreatetime |
| 3 | uidx_qcbd_wdstct_rule_billno |  | fnumber |
| 4 | idx_t_qcbd_wdstct_rule_createorg |  | fcreateorgid |
| 5 | idx_t_qcbd_wdstct_rule_master |  | fmasterid |
