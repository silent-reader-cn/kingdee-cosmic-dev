# 零成本批量维护-cal_batchprice

## 成本要素明细-子表 t_cal_batchpricesubentry

- **表名称：** 成本要素明细-子表
- **表名：** t_cal_batchpricesubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funitactualcost | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 2 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_batchpricesubentry |  | fdetailid |

---

## 零成本批量维护-多语言表 t_cal_batchprice_l

- **表名称：** 零成本批量维护-多语言表
- **表名：** t_cal_batchprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_batchprice_l |  | fpkid |
| 2 | idx_cal_batchprice_l_id |  | fid,flocaleid |

---

## 零成本批量维护-主表 t_cal_batchprice

- **表名称：** 零成本批量维护-主表
- **表名：** t_cal_batchprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fapprovetime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fisfitbycaldimension | 按核算维度设置 | bpchar | 1 |  | √ | '0' | 按核算维度设置 |
| 9 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fisfitbycalrange | 按核算范围设置 | bpchar | 1 |  | √ | '0' | 按核算范围设置 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsetdimension | 设置维度 | varchar | 255 |  | √ | ' ' | 设置维度,枚举: x :物料 owner :货主 storageorgunit :库存组织 warehouse :仓库 location :仓位 assist :辅助属性 lot :批号 mversion :物料版本 invtype :库存类型 invstatus :库存状态 project :项目编码 configuredcode :配置号 tracknumber :跟踪号 |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_batchprice |  | fid |
| 2 | idx_cal_batchprice_number |  | fnumber |

---

## 单据体-子表 t_cal_batchpriceentry

- **表名称：** 单据体-子表
- **表名：** t_cal_batchpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fassist | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | funitactualcost | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 |
| 12 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 13 | flot | 批号 | varchar | 510 |  | √ | ' ' | 批号 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_batchpriceentry_fmaterialid |  | fmaterialid |
| 2 | pk_cal_batchpriceentry |  | fentryid |
| 3 | idx_cal_batchpricesubentry_fentryid |  | fentryid |
| 4 | idx_cal_batchpriceentry_fid |  | fid |
