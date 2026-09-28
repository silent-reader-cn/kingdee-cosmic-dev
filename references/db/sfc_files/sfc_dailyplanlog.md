# 工作日志单(废弃)-sfc_dailyplanlog

## 交接信息-子表 t_sfc_handentry

- **表名称：** 交接信息-子表
- **表名：** t_sfc_handentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhanddate | 交接时间 | timestamp | 0 |  |  | null | 交接时间 |
| 3 | fhandprofesid | 交接人行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 4 | fdailyplanid | 日计划（工作清单）id | int8 | 64 |  | √ | 0 | 日计划（工作清单）id |
| 5 | fhandstatus | 交接状态 | varchar | 5 |  | √ | ' ' | 交接状态,枚举: A :已确认 B :已拒绝 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdeliverid | 转交人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 8 | freciveprofesid | 接收人行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 9 | fhandoverorderid | 个人交接单据id | int8 | 64 |  | √ | 0 | 个人交接单据id |
| 10 | fhandmodel | 方式 | varchar | 5 |  | √ | ' ' | 方式,枚举: A :交接 B :转交 |
| 11 | fhandcontent | 内容 | varchar | 999 |  | √ | ' ' | 内容 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fhanderid | 交接人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 14 | frevicerid | 接收人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_handentry |  | fentryid |
| 2 | idx_sfc_handry_fseq |  | fseq |
| 3 | idx_sfc_handry_fid |  | fid |
| 4 | idx_sfc_handry_dailyid |  | fdailyplanid |

---

## 附件-附件表 t_sfc_fnisattach

- **表名称：** 附件-附件表
- **表名：** t_sfc_fnisattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_fnisch_fentryid |  | fentryid,fbasedataid |
| 2 | pk_t_sfc_fnisattach |  | fpkid |

---

## 工作日志单(废弃)-主表 t_sfc_dailyplanlog

- **表名称：** 工作日志单(废弃)-主表
- **表名：** t_sfc_dailyplanlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmroorderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 8 | fmroorderid | 检修工单id | int8 | 64 |  | √ | 0 | 检修工单id |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dailog_createtime |  | fcreatetime |
| 2 | idx_sfc_dailog_mroorder |  | fmroorderno,fmroorderid |
| 3 | pk_t_sfc_dailyplanlog |  | fid |
| 4 | idx_sfc_dailog_fbillno |  | fbillno |

---

## 关联子实体-子表 t_sfc_dailyplanlog_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_dailyplanlog_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dailyplanlog_lk |  | fpkid |
| 2 | idx_sfc_dailyplanlog_lk_fk |  | fid |

---

## 附件-附件表 t_sfc_excepattach

- **表名称：** 附件-附件表
- **表名：** t_sfc_excepattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_excech_fentryid |  | fentryid,fbasedataid |
| 2 | pk_t_sfc_excepattach |  | fpkid |

---

## 异常信息-子表 t_sfc_exceptentry

- **表名称：** 异常信息-子表
- **表名：** t_sfc_exceptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcepresonid | 异常原因 | int8 | 64 |  | √ | 0 | 异常原因 fmm_abnormalreason |
| 3 | fexcepcontent | 异常内容 | varchar | 500 |  | √ | ' ' | 异常内容 |
| 4 | fexcepprofesid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fexceptiondate | 异常时间 | timestamp | 0 |  |  | null | 异常时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexceptionerid | 异常记录人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_excery_fseq |  | fseq |
| 2 | idx_sfc_excery_fid |  | fid |
| 3 | pk_t_sfc_exceptentry |  | fentryid |

---

## 工作日志单(废弃)-关联追踪表 t_sfc_dailyplanlog_tc

- **表名称：** 工作日志单(废弃)-关联追踪表
- **表名：** t_sfc_dailyplanlog_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dailyplanlog_tc |  | fid |
| 2 | idx_sfc_dailyplanlog_tc_tbill |  | ftbillid |
| 3 | idx_sfc_dailyplanlog_tc_tid |  | ftid |

---

## 收工记录-子表 t_sfc_fnishentry

- **表名称：** 收工记录-子表
- **表名：** t_sfc_fnishentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 3 | frecorddate | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |
| 4 | fresponserid | 责任人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 5 | fmodel | 方式 | varchar | 5 |  | √ | ' ' | 方式,枚举: A :收工 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcontent | 内容 | varchar | 999 |  | √ | ' ' | 内容 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_fnisry_fid |  | fid |
| 2 | pk_t_sfc_fnishentry |  | fentryid |
| 3 | idx_sfc_fnisry_fseq |  | fseq |

---

## 附件-附件表 t_sfc_handattach

- **表名称：** 附件-附件表
- **表名：** t_sfc_handattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_handch_fentryid |  | fentryid,fbasedataid |
| 2 | pk_t_sfc_handattach |  | fpkid |

---

## 工作日志单(废弃)-反写记录表 t_sfc_dailyplanlog_wb

- **表名称：** 工作日志单(废弃)-反写记录表
- **表名：** t_sfc_dailyplanlog_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dailyplanlog_wb |  | fentryid |
| 2 | idx_sfc_dailyplanlog_wb_fk |  | fid |
