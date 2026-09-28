# 可销量分配结果反写表-ococic_allotresult_wb

## 可销量分配结果反写表-主表 t_ococic_allotresult_wb

- **表名称：** 可销量分配结果反写表-主表
- **表名：** t_ococic_allotresult_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbillid | 单据主键 | int8 | 64 |  | √ | 0 | 单据主键 |
| 5 | fsubentryid | 子分录主键 | int8 | 64 |  | √ | 0 | 子分录主键 |
| 6 | fbillentity | 单据 | varchar | 80 |  | √ | ' ' | 单据 |
| 7 | fsumreservebaseqty | 总占用量(基本单位) | numeric | 23 | 10 | √ | 0 | 总占用量(基本单位) |
| 8 | fentryid | 分录主键 | int8 | 64 |  | √ | 0 | 分录主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_allotresultwb_bill |  | fbillentity,fbillid,fentryid,fsubentryid |
| 2 | pk_ococic_allotresult_wb |  | fid |

---

## 占用明细-子表 t_ococic_allotresult_wbe

- **表名称：** 占用明细-子表
- **表名：** t_ococic_allotresult_wbe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freservebaseqty | 占用量(基本单位) | numeric | 23 | 10 | √ | 0 | 占用量(基本单位) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fallotresultid | 可销量分配结果主键 | int8 | 64 |  | √ | 0 | 可销量分配结果主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotresult_wbe |  | fentryid |
| 2 | idx_ococic_allotresultwbe_fid |  | fid |
