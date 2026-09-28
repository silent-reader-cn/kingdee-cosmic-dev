# 内协发出单-sfc_internaloutsend

## 关联子实体-子表 t_sfc_internaloutsend_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_internaloutsend_lk

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
| 1 | idx_sfc_internaloutsend_lk_fk |  | fid |
| 2 | pk_sfc_internaloutsend_lk |  | fpkid |

---

## 内协发出单-多语言表 t_sfc_internaloutsend_l

- **表名称：** 内协发出单-多语言表
- **表名：** t_sfc_internaloutsend_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_internaloutsend_l |  | fpkid |
| 2 | idx_sfc_internal_l |  | fid,flocaleid |

---

## 内协发出单-主表 t_sfc_internaloutsend

- **表名称：** 内协发出单-主表
- **表名：** t_sfc_internaloutsend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fprocessorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fdate | 发出日期 | timestamp | 0 |  |  | null | 发出日期 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_internal_billno |  | fbillno |
| 2 | pk_sfc_internaloutsend |  | fid |

---

## 单据体-多语言表 t_sfc_intoutsendentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_sfc_intoutsendentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_intoutsendentry_l |  | fpkid |
| 2 | idx_sfc_intoutsendentry_l |  | fentryid,flocaleid |

---

## 内协发出单-关联追踪表 t_sfc_internaloutsend_tc

- **表名称：** 内协发出单-关联追踪表
- **表名：** t_sfc_internaloutsend_tc

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
| 1 | idx_sfc_internaloutsend_tc_tid |  | ftid |
| 2 | idx_sfc_internaloutsend_tc_tbill |  | ftbillid |
| 3 | pk_sfc_internaloutsend_tc |  | fid |

---

## 关联子实体-子表 t_sfc_intoutsendentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_intoutsendentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_intoutsendentry_lk |  | fpkid |
| 2 | idx_sfc_intoutsendentry_lk_fk |  | fentryid |

---

## 内协发出单-反写记录表 t_sfc_internaloutsend_wb

- **表名称：** 内协发出单-反写记录表
- **表名：** t_sfc_internaloutsend_wb

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
| 1 | pk_sfc_internaloutsend_wb |  | fentryid |
| 2 | idx_sfc_internaloutsend_wb_fk |  | fid |

---

## 单据体-子表 t_sfc_intoutsendentry

- **表名称：** 单据体-子表
- **表名：** t_sfc_intoutsendentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 3 | fprocessqty | 委托加工数量 | numeric | 23 | 10 | √ | 0 | 委托加工数量 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 9 | fworkid | 生产工单 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 10 | frevoveryqty | 关联接收数量 | numeric | 23 | 10 | √ | 0 | 关联接收数量 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |
| 13 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 14 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 15 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 16 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 17 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | freturnreworkqty | 退回返工数量 | numeric | 23 | 10 | √ | 0 | 退回返工数量 |
| 19 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 20 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 21 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fyetrerevoveryqty | 已接收数量 | numeric | 23 | 10 | √ | 0 | 已接收数量 |
| 23 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 24 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 25 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 26 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 27 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 28 | fplanendtime | 计划接收日期 | timestamp | 0 |  |  | null | 计划接收日期 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 31 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_intoutsendentry |  | fentryid |
| 2 | idx_sfc_intoutsendentry_fid |  | fid |
