# 尾盘销售税源信息（废弃）-tdm_tdzzs_wpxssw

## 尾盘销售税源信息（废弃）-主表 t_tdm_tdzzs_wpxssw

- **表名称：** 尾盘销售税源信息（废弃）-主表
- **表名：** t_tdm_tdzzs_wpxssw

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqssysmj | 清算时已售面积 | numeric | 23 | 10 | √ | 0 | 清算时已售面积 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsbbbillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fsblimit | 税源期限 | varchar | 50 |  | √ | ' ' | 税源期限,枚举: month :月 season :季 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 9 | fqshsyksmj | 清算后剩余可售面积 | numeric | 23 | 10 | √ | 0 | 清算后剩余可售面积 |
| 10 | ftdzzsxm | 项目名称 | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 11 | fzksmj | 总可售面积 | numeric | 23 | 10 | √ | 0 | 总可售面积 |
| 12 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fenddate | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 16 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 17 | fssbsylx | 申报表适用类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 18 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fstartdate | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fsbbbillno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 24 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_wpxssw_fnum1 |  | fnumber |
| 2 | pk_tdm_tdzzs_wpxssw |  | fid |

---

## 减免信息-子表 t_tdm_tdzzs_wpx_jm

- **表名称：** 减免信息-子表
- **表名：** t_tdm_tdzzs_wpx_jm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhoutype | 房屋类型 | varchar | 50 |  | √ | ' ' | 房屋类型,枚举: ptzz :普通住宅 fptzz :非普通住宅 qtlxfc :其他类型房地产 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tdzzs_wpx_jm |  | fentryid |
| 2 | idx_tdm_tdzzs_wpx_jm_fk |  | fid |

---

## 单据体-子表 t_tdm_tdzzs_wpx_en

- **表名称：** 单据体-子表
- **表名：** t_tdm_tdzzs_wpx_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fupdaco | 触发更新字段 | varchar | 50 |  | √ | ' ' | 触发更新字段 |
| 4 | ffptzz | 非普通住宅 | numeric | 23 | 10 | √ | 0 | 非普通住宅 |
| 5 | fqtlxfc | 其他类型房地产 | numeric | 23 | 10 | √ | 0 | 其他类型房地产 |
| 6 | fptzz | 普通住宅 | numeric | 23 | 10 | √ | 0 | 普通住宅 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fhj | 合计 | varchar | 50 |  | √ | ' ' | 合计 |
| 9 | fproject | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tdzzs_wpx_en_fk |  | fid |
| 2 | pk_tdm_tdzzs_wpx_en |  | fentryid |

---

## 尾盘销售税源信息（废弃）-多语言表 t_tdm_tdzzs_wpxssw_l

- **表名称：** 尾盘销售税源信息（废弃）-多语言表
- **表名：** t_tdm_tdzzs_wpxssw_l

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
| 1 | pk_tdm_tdzzs_wpxssw_l |  | fpkid |
| 2 | idx_tdm_tdzzs_wpxssw_l_0 |  | fid,flocaleid |
