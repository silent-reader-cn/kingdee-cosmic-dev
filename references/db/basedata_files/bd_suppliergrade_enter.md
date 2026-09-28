# 分级录入-bd_suppliergrade_enter

## 分级录入-主表 t_bd_supgradeenter

- **表名称：** 分级录入-主表
- **表名：** t_bd_supgradeenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fnote | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbdsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supgrade_enter_fbillno |  | fbillno |
| 2 | pk_t_bd_supgradeenter |  | fid |

---

## 单据体-子表 t_bd_supgradeentry

- **表名称：** 单据体-子表
- **表名：** t_bd_supgradeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fcategory | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 4 | ftimeto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 5 | ftimefrom | 有效期从 | timestamp | 0 |  |  | null | 有效期从 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fevagrade | 核准等级 | int8 | 64 |  | √ | 0 | 评估等级 bd_evagrade |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supgradeentry_fid |  | fid |
| 2 | pk_t_bd_supgradeentry |  | fentryid |
