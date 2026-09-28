# 个人工作交接(废弃)-sfc_personhandover

## 关联子实体-子表 t_sfc_persho_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_persho_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_persho_entry_lk |  | fpkid |
| 2 | idx_t_sfc_persho_entry_lk |  | fentryid |

---

## 个人工作交接(废弃)-反写记录表 t_sfc_persho_wb

- **表名称：** 个人工作交接(废弃)-反写记录表
- **表名：** t_sfc_persho_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_persho_wb |  | fid |
| 2 | pk_t_sfc_persho_wb |  | fentryid |

---

## 工作内容-子表 t_sfc_persho_entry

- **表名称：** 工作内容-子表
- **表名：** t_sfc_persho_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscheduletime | 排班时间 | timestamp | 0 |  |  | null | 排班时间 |
| 3 | fdailyplanid | 日计划单据ID | int8 | 64 |  | √ | 0 | 日计划单据ID |
| 4 | ftaskno | 任务编号 | varchar | 50 |  | √ | ' ' | 任务编号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftaskname | 任务内容 | varchar | 50 |  | √ | ' ' | 任务内容 |
| 7 | fendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fnotice | 注意事项 | varchar | 255 |  | √ | ' ' | 注意事项 |
| 10 | fdailyplanbillno | 日计划单据编码 | varchar | 50 |  | √ | ' ' | 日计划单据编码 |
| 11 | fbegintime | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 12 | fdailyplanentryid | 日计划单据分录ID | int8 | 64 |  | √ | 0 | 日计划单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_persho_entry |  | fentryid |
| 2 | idx_t_sfc_persho_entry |  | fid,fseq |

---

## 工作内容-多语言表 t_sfc_persho_entry_l

- **表名称：** 工作内容-多语言表
- **表名：** t_sfc_persho_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fnotice | 注意事项 | varchar | 255 |  | √ | ' ' | 注意事项 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_persho_entry_l |  | fentryid,flocaleid |
| 2 | pk_t_sfc_persho_entry_l |  | fpkid |

---

## 个人工作交接(废弃)-关联追踪表 t_sfc_persho_tc

- **表名称：** 个人工作交接(废弃)-关联追踪表
- **表名：** t_sfc_persho_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_persho_tc_tbill |  | ftbillid |
| 2 | idx_sfc_persho_tc_tid |  | ftid |
| 3 | idx_t_sfc_persho_tc |  | fsbillid |
| 4 | pk_t_sfc_persho_tc |  | fid |

---

## 个人工作交接(废弃)-主表 t_sfc_persho

- **表名称：** 个人工作交接(废弃)-主表
- **表名：** t_sfc_persho

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fhopersmobile | 交接人联系方式 | varchar | 50 |  | √ | ' ' | 交接人联系方式 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fhandoverpersonid | 交接人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | freceivedbyid | 接收人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fforwardtoid | 转交人 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fhandoverstatus | 交接状态 | varchar | 50 |  | √ | ' ' | 交接状态,枚举: A :接收 B :拒绝 C :转交 |
| 16 | fhandovertime | 交接日期 | timestamp | 0 |  |  | null | 交接日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_persho |  | fid |
| 2 | idx_t_sfc_persho |  | fbillno,fcreatorid |
