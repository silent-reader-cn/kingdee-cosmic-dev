# 工作量维护-fa_workload

## 本期工作量维护(弃用)-子表 t_fa_workloadentry

- **表名称：** 本期工作量维护(弃用)-子表
- **表名：** t_fa_workloadentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepreworkload | 本期工作量(弃用) | numeric | 23 | 10 | √ | 0.0000000000 | 本期工作量(弃用) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsumworkload | 累计工作量(弃用) | numeric | 23 | 10 | √ | 0.0000000000 | 累计工作量(弃用) |
| 5 | ffincardid | 财务卡片(弃用) | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frealcardid | 卡片编号(弃用) | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_workloadentry_pkey |  | fentryid |
| 2 | idx_fa_workloadentry |  | fid |

---

## 工作量维护-主表 t_fa_workload

- **表名称：** 工作量维护-主表
- **表名：** t_fa_workload

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 10 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 11 | fassetbookid | 资产账簿(弃用) | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 12 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 18 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 22 | fworkload | 本期工作量 | numeric | 19 | 6 | √ | 0.000000 | 本期工作量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_workload_pkey |  | fid |
| 2 | idx_fa_workload |  | forgid |
| 3 | idx_t_fa_workload_createorg |  | fcreateorgid |
