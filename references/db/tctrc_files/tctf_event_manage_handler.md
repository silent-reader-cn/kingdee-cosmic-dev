# 事件处理-tctf_event_manage_handler

## 事件处理-反写记录表 t_tctf_event_manag_handle_wb

- **表名称：** 事件处理-反写记录表
- **表名：** t_tctf_event_manag_handle_wb

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
| 1 | idx_tctf_event_manag_handle_wb_fk |  | fid |
| 2 | pk_tctf_event_manag_handle_wb |  | fentryid |

---

## 单据体1-子表 t_tctf_event_handler_djt

- **表名称：** 单据体1-子表
- **表名：** t_tctf_event_handler_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffinishdatedjt | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fhandlersituation | 处理情况 | varchar | 2000 |  | √ | ' ' | 处理情况 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctf_event_handler_djt |  | fentryid |
| 2 | idx_tctf_event_handler_djt_fk |  | fid |

---

## 事件处理-主表 t_tctf_event_manag_handle

- **表名称：** 事件处理-主表
- **表名：** t_tctf_event_manag_handle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxoffices | 下发检查税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finvaliddate | 检查期间止 | timestamp | 0 |  |  | null | 检查期间止 |
| 5 | freseventcode | 事件编码 | varchar | 200 |  | √ | ' ' | 事件编码 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | feventclass | 事件分类 | int8 | 64 |  | √ | 0 | [事件分类 tctf_event_class](../tctrc_files/tctf_event_class.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 检查税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | feventbackground | 事件背景 | varchar | 2000 |  | √ | ' ' | 事件背景 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | feffectdate | 检查期间起 | timestamp | 0 |  |  | null | 检查期间起 |
| 13 | ffinishdate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fhandlestatus | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: 0 :未处理 1 :已处理 |
| 17 | ftaxprocessingplan | 税务处理方案 | varchar | 2000 |  | √ | ' ' | 税务处理方案 |
| 18 | fselfisituation | 自查情况 | varchar | 2000 |  | √ | ' ' | 自查情况 |
| 19 | fjbr | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcheckdate | 检查日期 | timestamp | 0 |  |  | null | 检查日期 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fimportlevel | 重要级别 | varchar | 50 |  | √ | ' ' | 重要级别,枚举: 0 :高 1 :中 2 :低 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctf_event_manag_handle |  | fid |
| 2 | idx_tctf_managhan_org |  | forgid |

---

## 附件-附件表 t_tctf_event_attachment

- **表名称：** 附件-附件表
- **表名：** t_tctf_event_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctf_event_attachment |  | fpkid |
| 2 | idx_tctf_event_att_pkid |  | fbasedataid |

---

## 单据体-子表 t_tctf_event_details_djt

- **表名称：** 单据体-子表
- **表名：** t_tctf_event_details_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fbjskje | 补缴税款金额 | numeric | 23 | 10 | √ | 0 | 补缴税款金额 |
| 4 | feventdes | 事件简述 | varchar | 500 |  | √ | ' ' | 事件简述 |
| 5 | fclje | 滞纳金 | numeric | 23 | 10 | √ | 0 | 滞纳金 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftaxpayername | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 9 | ffkje | 罚款 | numeric | 23 | 10 | √ | 0 | 罚款 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ftaxtype | 涉及税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 12 | fdjtjbr | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctf_event_details_djt |  | fentryid |
| 2 | idx_tctf_event_details_djt_fk |  | fid |

---

## 事件处理-关联追踪表 t_tctf_event_manag_handle_tc

- **表名称：** 事件处理-关联追踪表
- **表名：** t_tctf_event_manag_handle_tc

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
| 1 | idx_tctf_event_manag_handle_tc_tid |  | ftid |
| 2 | pk_tctf_event_manag_handle_tc |  | fid |
| 3 | idx_tctf_event_manag_handle_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_tctf_event_details_djt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_tctf_event_details_djt_lk

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
| 1 | pk_tctf_event_details_djt_lk |  | fpkid |
| 2 | idx_tctf_event_details_djt_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_tctf_event_manag_handle_lk

- **表名称：** 关联子实体-子表
- **表名：** t_tctf_event_manag_handle_lk

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
| 1 | idx_tctf_event_manag_handle_lk_fk |  | fid |
| 2 | pk_tctf_event_manag_handle_lk |  | fpkid |
