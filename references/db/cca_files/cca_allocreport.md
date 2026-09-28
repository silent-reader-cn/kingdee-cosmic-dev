# 分配报告-cca_allocreport

## 接收方成本中心-多选基础资料表 t_cca_allocreportesc

- **表名称：** 接收方成本中心-多选基础资料表
- **表名：** t_cca_allocreportesc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_allocreportesc_fk |  | fentryid |
| 2 | pk_cca_allocreportesc |  | fpkid |

---

## 分配规则-多选基础资料表 t_cca_allocreportrule

- **表名称：** 分配规则-多选基础资料表
- **表名：** t_cca_allocreportrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [费用分配规则 cca_feeallocrule](../cca_files/cca_feeallocrule.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_allocreportrule_fk |  | fid |
| 2 | pk_cca_allocreportrule |  | fpkid |

---

## 步骤明细-子表 t_cca_allocreportdtl

- **表名称：** 步骤明细-子表
- **表名：** t_cca_allocreportdtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 详细步骤 | varchar | 50 |  | √ | ' ' | 详细步骤 |
| 3 | ftip | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresult | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :不通过 7 :提醒 |
| 6 | fcostime | 耗时（毫秒） | varchar | 50 |  | √ | ' ' | 耗时（毫秒） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftip_tag | 提示_详情 | text | 0 |  |  | null | 提示_详情 |
| 9 | fcheckdesc | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_allocreportdtl |  | fentryid |
| 2 | idx_cca_allocreportdtl_fk |  | fid |

---

## 分配报告-主表 t_cca_allocreport

- **表名称：** 分配报告-主表
- **表名：** t_cca_allocreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalcost | 总耗时（毫秒） | varchar | 50 |  | √ | ' ' | 总耗时（毫秒） |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :警告 |
| 10 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | falloctime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 12 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_allocreport |  | fid |
| 2 | idx_cca_allocreport_m0 |  | fbillno |

---

## 发送方成本中心-多选基础资料表 t_cca_allocreporterc

- **表名称：** 发送方成本中心-多选基础资料表
- **表名：** t_cca_allocreporterc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_allocreporterc_fk |  | fentryid |
| 2 | pk_cca_allocreporterc |  | fpkid |

---

## 单据体-子表 t_cca_allocreportentry

- **表名称：** 单据体-子表
- **表名：** t_cca_allocreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fruleentrynum | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fallocrule | 费用分配规则 | int8 | 64 |  | √ | 0 | [费用分配规则 cca_feeallocrule](../cca_files/cca_feeallocrule.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fruleentryname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_allocreportentry |  | fentryid |
| 2 | idx_cca_allocreportentry_fk |  | fid |
