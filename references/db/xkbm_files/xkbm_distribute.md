# 预算方案分发明细-xkbm_distribute

## 预算方案分发明细-多语言表 t_xkbm_distribute_l

- **表名称：** 预算方案分发明细-多语言表
- **表名：** t_xkbm_distribute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
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
| 1 | idx_xkbm_distribute_l_fid |  | fentryid,flocaleid |
| 2 | pk_xkbm_distribute_l |  | fpkid |

---

## 预算方案分发明细-主表 t_xkbm_distribute

- **表名称：** 预算方案分发明细-主表
- **表名：** t_xkbm_distribute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdeptorgid | 部门组织ID | int8 | 64 |  | √ | 0 | 部门组织ID |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnewsampleid | 分发预算复制模板ID | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 8 | forgtype | 预算组织类型 | varchar | 30 |  | √ | ' ' | 预算组织类型,枚举: DEPT :部门 ORG :组织 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsampleid | 分发源预算模板ID | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fallowedit | 允许编辑 | bpchar | 1 |  | √ | '0' | 允许编辑 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fdetailid | 分发ID | varchar | 50 |  | √ | ' ' | 分发ID |
| 18 | frpttype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型,枚举: 60 :预算报表模板 61 :预算报表 62 :预算实际数模板 63 :预算实际数报表 64 :预算汇总报表（周期性） 65 :预算汇总表 66 :预算调整表 |
| 19 | freportbegindate | 报表起始日期 | timestamp | 0 |  |  | null | 报表起始日期 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | freportenddate | 报表结束日期 | timestamp | 0 |  |  | null | 报表结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_distribute_detail |  | fdetailid |
| 2 | pk_xkbm_distribute |  | fentryid |
