# 采购计划协议配额-ssm_allocation

## 配额区间-子表 t_ssm_allocationinfo

- **表名称：** 配额区间-子表
- **表名：** t_ssm_allocationinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_allocationinfo_fk |  | fid |
| 2 | pk_ssm_allocationinfo |  | fentryid |

---

## 配额明细-子表 t_ssm_allocationdetail

- **表名称：** 配额明细-子表
- **表名：** t_ssm_allocationdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsupplier | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 2 | ffullfillsupplier | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 8 | fallocationpercent | 配额比例（%） | numeric | 23 | 10 | √ | 0 | 配额比例（%） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsupplyschedule | 采购计划协议 | int8 | 64 |  | √ | 0 | 采购计划协议 ssm_purschdorder |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_allocationdetail_fk |  | fentryid |
| 2 | pk_ssm_allocationdetail |  | fdetailid |

---

## 采购计划协议配额-主表 t_ssm_allocation

- **表名称：** 采购计划协议配额-主表
- **表名：** t_ssm_allocation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fauxptyid | 辅助属性 | varchar | 50 |  | √ | ' ' | 辅助属性 |
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdetail | 查看详情 | varchar | 50 |  | √ | ' ' | 查看详情 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisaffectplan | 辅助属性影响计划 | bpchar | 1 |  | √ | '0' | 辅助属性影响计划 |
| 11 | fmastermaterial | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 13 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | freceiveorg | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_allocation |  | fid |
| 2 | idx_t_ssm_allocation |  | forgid,fmaterial,freceiveorg |
