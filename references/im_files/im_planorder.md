# 外购计划建议-im_planorder

## 外购计划建议-关联追踪表 t_im_planorder_tc

- **表名称：** 外购计划建议-关联追踪表
- **表名：** t_im_planorder_tc

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
| 1 | idx_im_planorder_tc_tbill |  | ftbillid |
| 2 | pk_im_planorder_tc |  | fid |
| 3 | idx_im_planorder_tc_tid |  | ftid |

---

## 外购计划建议-反写记录表 t_im_planorder_wb

- **表名称：** 外购计划建议-反写记录表
- **表名：** t_im_planorder_wb

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
| 1 | idx_im_planorder_wb_fk |  | fid |
| 2 | pk_im_planorder_wb |  | fentryid |

---

## 关联子实体-子表 t_im_planorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_planorder_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fdropqty | 已投放数量_确认携带值 | numeric | 23 | 10 |  | null | 已投放数量_确认携带值 |
| 3 | fdropqty_old | 已投放数量_原始携带值 | numeric | 23 | 10 |  | null | 已投放数量_原始携带值 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_planorder_lk_fk |  | fid |
| 2 | pk_im_planorder_lk |  | fpkid |

---

## 外购计划建议-主表 t_im_planorder

- **表名称：** 外购计划建议-主表
- **表名：** t_im_planorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdropqty | 已投放数量 | numeric | 23 | 10 | √ | 0 | 已投放数量 |
| 3 | fproorpurorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fplanprogram | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案定义(作废) mrp_planprogram |
| 5 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fdemandseq | 需求单据行号 | int4 | 32 |  | √ | 0 | 需求单据行号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | forderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 14 | fplanoperatenum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | fcomment | varchar | 512 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsurplusdropqty | 未投放数量 | numeric | 23 | 10 | √ | 0 | 未投放数量 |
| 21 | fdemandbill | 需求单据编号 | varchar | 50 |  | √ | ' ' | 需求单据编号 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 24 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 25 | fdatasource | 数据来源 | bpchar | 1 |  | √ | 'A' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 26 | funit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_planorder_fbillno |  | fbillno |
| 2 | idx_t_im_planorder_timeorg |  | fcreatetime,fproorpurorg |
| 3 | pk_t_im_planorder |  | fid |
| 4 | idx_t_im_planorder_fplannum |  | fplanoperatenum |
| 5 | idx_t_im_planorder_fmaterial |  | fmaterial |

---

## 外购计划建议-多语言表 t_im_planorder_l

- **表名称：** 外购计划建议-多语言表
- **表名：** t_im_planorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 原因描述 | varchar | 512 |  | √ | ' ' | 原因描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_planorder_l |  | fpkid |
| 2 | idx_t_im_planorder_l_flid |  | fid,flocaleid |
