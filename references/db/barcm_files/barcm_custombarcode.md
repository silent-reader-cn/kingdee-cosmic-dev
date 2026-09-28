# 自定义条码-barcm_custombarcode

## 自定义条码-主表 t_barcm_custbc

- **表名称：** 自定义条码-主表
- **表名：** t_barcm_custbc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_custbc_fbillno |  | fbillno |
| 2 | pk_barcm_custbc |  | fid |

---

## 条码数据-子表 t_barcm_custbcentry

- **表名称：** 条码数据-子表
- **表名：** t_barcm_custbcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 3 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fbarcode | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 10 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | fwarelocarelation | 仓库仓位关系 | int8 | 64 |  | √ | 0 | 仓库仓位关系 bd_warelocareference |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_custbcentry |  | fentryid |
| 2 | idx_barcm_custbcentry_fid |  | fid |
